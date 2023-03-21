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
curs.execute("CREATE DATABASE runoob_db")
curs.execute("SHOW DATABASES")
curs.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")