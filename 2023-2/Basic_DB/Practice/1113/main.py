import pymysql

conn = pymysql.connect(host = 'localhost', user='root',
                       password='wnsdudmysql0921', db='university', charset='utf8mb4')

cursor = conn.cursor()

sql= "select * from student"

cursor.execute(sql)
rows = cursor.fetchall()
print (rows)

check = True

while check:
    sno = input("학번: ")
    if sno == "":
        break

    sname = input("이름: ")
    grade = input("학년: ")
    dept = input("학과: ")
    sql = """insert into student values ('{}', '{}', {}, '{}')""".format(sno, sname, grade, dept)
    print(sql)
    try:
        cursor.execute(sql)
        check = False
    except Exception as err:
        print(err)

cursor.execute("""
    select *
    from student
""")

rows = cursor.fetchall()

for cur_row in rows :
    sno = cur_row[0]
    sname = cur_row[1]
    grade = cur_row[2]
    dept = cur_row[3]
    print ("%7s %20s %5d %20s" % (sno, sname, grade, dept))


conn.close ()