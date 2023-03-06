"""
get topic
"""
import requests
from bs4 import BeautifulSoup
import datetime


def topic(url, day, name):
    requests_name = requests.get(url)
    reslut_name = requests_name.content.decode("utf-8")
    soup_name = BeautifulSoup(reslut_name, 'html.parser')
    topic_url = []
    for link in soup_name.find_all('iframe', limit=4):
        topic_url.append('https://shudu.one' + link.get('src'))
    if len(topic_url) == 0:
        print('未获取题目')
    else:
        for topic_id in topic_url:
            request_topic = requests.get(topic_id)
            reslut_topic = request_topic.content.decode("utf-8")
            soup_topic = BeautifulSoup(reslut_topic, 'html.parser')
            f = open('./' + name + '-' + str(day) + '.csv', 'a')
            for id_num in range(0, 89):
                if id_num in [9, 19, 29, 39, 49, 59, 69, 79]:
                    f.write('\n')
                    continue
                if id_num in range(0, 9):
                    f.write(soup_topic.find('div', id='con' + '%02d' % id_num).text + ',')
                else:
                    f.write(soup_topic.find('div', id='con' + str(id_num)).text + ',')
            f.write('\n' + topic_id[-7:] + '\n')
            f.close()
    print(name + '-' + str(day))


def get_url(days, name):
    if days == '今天':
        day = datetime.date.today()
        url = 'https://shudu.one/sudoku/printable-' + name + '-sudoku.php'
        topic(url, day, name)
    elif days == '昨天':
        day = datetime.date.today() - datetime.timedelta(days=1)
        url = 'https://shudu.one/sudoku/yesterday-printable-' + name + '-sudoku.php'
        topic(url, day, name)


def shudu_name(name):
    # a = 0
    # while a < 3:
    #     a += 1
        namelist = ['easy', 'hard', 'expert', 'extreme']
        if name in namelist:
            return name
        else:
            print("错误级别："+str(namelist))


def shudu_data(days):
    # a=0
    # while a<3:
    #     a+=1
        match days:
            case '今天':
                return days
            case '昨天':
                return days
            case _:
                print('错误日期：今天,昨天')


if __name__ == '__main__':
    days = input('日期:')
    date_shudu = shudu_data(days)
    if date_shudu is None:
        print('未获取日期')
    else:
        name = input("级别['easy', 'hard', 'expert', 'extreme']:")
        name_shudu = shudu_name(name)
        if name_shudu is None:
            print('未获取级别')
        else:
            get_url(date_shudu, name_shudu)
