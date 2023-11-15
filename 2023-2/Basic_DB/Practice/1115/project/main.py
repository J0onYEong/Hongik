import pymysql

conn = pymysql.connect(host='localhost', user='root',
                       password='wnsdudmysql0921', db='university', charset='utf8mb4')

cursor = conn.cursor()

sql = "set foreign_key_checks = 0"
cursor.execute(sql)
sql = "drop table IF EXISTS student cascade"
cursor.execute(sql)
sql = "drop table IF EXISTS course cascade"
cursor.execute(sql)
sql = "set foreign_key_checks = 1"
cursor.execute(sql)

try:
    cursor.execute(sql)
except Exception as err:
    print(err)

sql = """
    create table student (
        sno char(7) NOT NULL, 
        sname varchar(20) NOT NULL, 
	    grade int DEFAULT 1, 
	    dept varchar(20),
	    primary key (sno)
	)
"""
try:
    cursor.execute(sql)
except Exception as err:
    print(err)

sql = """
    create table course(
	    cno char(4),
	    cname varchar(30) not null,
	    credit int,
	    profname varchar(20),
	    dept varchar(20),
       	primary key (cno)
    )
"""
try:
    cursor.execute(sql)
except Exception as err:
    print(err)

def insert_studnet():
    sno = input("학번: ")
    if sno == "":
        print("학번입력은 필수입니다.")
        return
    sname = input("이름: ")
    grade = input("학년: ")
    dept = input("학과: ")
    sql = """insert into student values ('{}', '{}', {}, '{}')""".format(sno, sname, grade, dept)
    try:
        cursor.execute(sql)
    except Exception as err:
        print(err)

def insert_course():
    cno = input("과목번호: ")
    if cno == "":
        print("과목번호입력은 필수입니다.")
        return
    cname = input("과목이름: ")
    credit = input("점수: ")
    profname = input("지도교수: ")
    dept = input("부서: ")
    sql = """insert into course values ('{}', '{}', {}, '{}', '{}')""".format(cno, cname, credit, profname, dept)
    try:
        cursor.execute(sql)
    except Exception as err:
        print(err)

def show_student():
    sql = "select * from student"
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except Exception as err:
        print(err)

def show_coruse():
    sql = "select * from course"

    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except Exception as err:
        print(err)

order_input = -1
while order_input != 0:
    order_input = int(input(">> "))
    sql = ""

    if order_input == 1:
        insert_studnet()

    if order_input == 2:
        insert_course()

    if order_input == 3:
        show_student()

    if order_input == 4:
        show_coruse()


sql = """
    drop table IF EXISTS student cascade
    drop table IF EXISTS course cascade
"""
cursor.execute(sql)

conn.close()


