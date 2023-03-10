import pymysql
from faker import Faker
fake = Faker("zh_CN")
# sql1 = """CREATE TABLE two (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT )"""
class py_mysql_conn(object):
   def __init__(self):
      self.conn = pymysql.connect(
         host='192.168.0.38',
         port=3306,
         user='root',
         passwd='123456',
         db='study_01',
         charset='utf8')
      self.curs = self.conn.cursor()
   def __del__(self):
      self.curs.close()
      self.conn.close()
   def two_add(self):
      sql2 = "insert into two values (%s,%s,%s) "
      """
      first_name = fake.first_name()
      last_name = fake.last_name()
      age = fake.pyint(min_value=18, max_value=40)
      """
      last_name = input('输入姓：')
      first_name = input('输入名：')
      age = input('输入年龄：')
      var = (first_name, last_name, age)
      try:
         self.curs.execute(sql2, var)
         self.conn.commit()
      except pymysql.Error as e:
         self.conn.rollback()
         print(e)
   def two_query(self):
      sql3 = "select * from two"
      try:
         self.curs.execute(sql3)
         for row in self.curs.fetchall()[-1:]:
            first = row[0]
            last = row[1]
            age = row[2]
            print(last + first, age)
      except pymysql.Error as e:
         print(e)

if __name__=='__main__':
   db = py_mysql_conn()
   db.two_add()
   db.two_query()
   input('任意键退出')

