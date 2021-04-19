# -*- coding:UTF-8 -*-
import time
import pymysql
def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def get_conn():
    conn = pymysql.connect(host="192.168.5.216",
                       user="root",
                       password="My-123456",
                       db="video")
    cursor = conn.cursor()
    return conn,cursor
def close_conn(conn,cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def query(sql,*args):
	conn,cursor = get_conn()
	cursor.execute(sql,args)
	res = cursor.fetchall()
	close_conn(conn,cursor)
	return res

def get_c1_data():
    sql = "select sum(confirm)," \
          "(select suspect from history order by ds desc limit 1)," \
          "sum(heal)," \
          "sum(dead)" \
          "from details" \
          " where update_time=(select update_time from details order by update_time desc limit 1)"
    res = query(sql)
    return res[0]

def get_c2_data():
    sql = "select province,sum(confirm) from details " \
          "where update_time=(select update_time from details " \
          "group by update_time desc limit 1) " \
          "group by province"
    res = query(sql)
    return res

def get_l1_data():
    sql = "select ds,confirm,suspect,heal,dead from history"
    res = query(sql)
    return res

def get_l2_data():
    sql = "select ds,confirm_add,suspect_add from history"
    res = query(sql)
    return res

def get_r1_data():
    sql = "SELECT city,confirm FROM(SELECT city,confirm FROM details WHERE update_time=(SELECT update_time FROM details ORDER BY update_time DESC LIMIT 1) AND province NOT IN ('湖北','北京','上海','天津','重庆')  UNION SELECT province AS city,SUM(confirm) AS confirm FROM details WHERE update_time=(SELECT update_time FROM details ORDER BY update_time DESC LIMIT 1) AND province IN ('湖北','北京','上海','天津','重庆')) AS a ORDER BY confirm DESC LIMIT 5"
    res = query(sql)
    return res

def get_r2_data():
    sql = "select content from hotsearch order by id desc limit 20"
    res = query(sql)
    return res

if __name__ == "__main__":
    print(get_r2_data())