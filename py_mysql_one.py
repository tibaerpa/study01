import pymysql
def py_mysql():
    conn = pymysql.connect(host='192.168.0.47',
                           user='root',
                           password='123456',
                           database='study_01'
                           )
    return conn
conn = py_mysql()
curs = conn.cursor()
def one_query(var):
    try:
        sql = 'select url from one where id = %s'
        curs.execute(sql,var)
        url = curs.fetchone()
    except TypeError as e:
        print(e)
    else:
        if url is None:
            print('name error')
        else:
            return url[0]
def one_add(one_name,one_url):
    try:
        sql = "insert into one (name,url) values (%s,%s)"
        curs.execute(sql,(one_name,one_url))
        conn.commit()
    except pymysql.Error as e:
        print(e)
def one_update_delete(sql):
    try:
        curs.execute(sql)
        conn.commit()
    except pymysql.Error as e:
        print(e)

curs.close()
conn.close()
