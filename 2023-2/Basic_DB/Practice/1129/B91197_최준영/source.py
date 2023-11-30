import pymysql

conn = pymysql.connect(host='localhost', user='root', password='wnsdudmysql0921', db='school', charset='utf8mb4')
cursor = conn.cursor()

cursor.execute("set foreign_key_checks = 0")
cursor.execute("drop table if exists teacher cascade")
cursor.execute("set foreign_key_checks = 1")


record_count = int(input("생성할 teacher 테이블의 레코드 수를 입력하시오: "))

sql = """
    create table teacher(
        t_id varchar(10) not null,
        t_no varchar(30),
        primary key (t_id)
    )
"""

try:
    cursor.execute(sql)
except Exception as err:
    print(err)


def create_records():
    global cursor, record_count

    for index in range(record_count):
        number = index+1
        label = "T{}".format(number)
        t_id_value = label
        t_no_value = label*2

        sql = "insert into teacher values ('{}', '{}')".format(t_id_value, t_no_value)

        try:
            cursor.execute(sql)
        except Exception as err:
            print(err)


create_records()

conn.commit()