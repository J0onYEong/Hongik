import pymysql

conn = pymysql.connect(host='localhost', user='root',
                       password='root', db='university', charset='utf8mb4')

cursor = conn.cursor()

cursor.execute("set foreign_key_checks = 0")
cursor.execute("drop table IF EXISTS student cascade")
cursor.execute("drop table IF EXISTS course cascade")
cursor.execute("drop table IF EXISTS enroll cascade")
cursor.execute("set foreign_key_checks = 1")

enroll_sql = """
    create table enroll(
        sno char(7),
        cno char(4),
        final int,
        lettergrade char(2),
        primary key (sno, cno)
    )
"""
student_sql = """
    create table student(
        sno char(7) not null,
        sname   varchar(20),
        grade   int,
        dept    varchar(20),
        primary key (sno)
    )
"""
course_sql = """
    create table course(
	    cno char(4) not null,
	    cname varchar(30),
	    credit int,
	    profname varchar(20),
	    dept varchar(20),
       	primary key (cno)
    )
"""
try:
    # 테이블들을 생성한다.
    cursor.execute(enroll_sql)
    cursor.execute(course_sql)
    cursor.execute(student_sql)
except Exception as err:
    print(err)


# 함수 이름 : insert_row_to
# 기능 : 테이블 명과 열값을 입력받아 특정 테이블에 삽입하는 함수입니다.
# 반환값 : 없음
# 전달인자 : table_name(테이블명), *values(열값들)
def insert_row_to(table_name, *values):
    total = ""
    count = len(values)
    for index in range(count): # 가변매개변수들로 부터 값 문자열을 만든다.
        value = values[index]
        if type(value) == str:
            value = "'{}'".format(value)
        if type(value) == int:
            value = str(value)
        total+=value
        if index != count-1:
            total+=', '
    sql = "insert into {} values ({})".format(table_name, total) # 완성된 문자열을 가지고 sql문을 완성한다.
    try:
        cursor.execute(sql)
    except Exception as err:
        print(err)

# 함수 이름 : show_table
# 기능 : 테이블을 조회하고 파일에 입력한다.
# 반환값 : 없음
# 전달인자 : table_name(테이블명)
def show_table(table_name):
    sql = "select * from {}".format(table_name)
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            total = ""
            count = len(row)
            for index in range(count): # 열의 값들을 하나의 문자열로 만든다.
                item = row[index]
                if type(item) == int: # 타입이 int면 string으로 변환해 total변수에 합쳐준다.
                    item = str(item)
                total += item
                if index != count-1:
                    total += " "
            write_line_to_file(total) # 완성된 문자열을 파일에 write
    except Exception as err:
        print(err)

# 함수 이름 : read_file
# 기능 : input.txt파일을 라인별로 읽어들여 파이썬 배열에 저장하는 함수입니다.
# 반환값 : inputLines(라인배열)
# 전달인자 : 없음
def read_file():
    inputLines = []

    while True:
        line = input_file.readline() # 파일을 한줄씩 읽음
        if not line:
            break;
        inputLines.append(line.strip())
    return inputLines

# 함수 이름 : write_line_to_file
# 기능 : output.txt파일에 전달한 라인을 입력한다.
# 반환값 : 없음
# 전달인자 : line(입력하고자하는 라인 문자열)
def write_line_to_file(line):
    output_file.write(line+"\n")

# student, course 하드코딩
hardcoding_data = [
    ['student', 'B922019', '김영희', 4, '기계'],
    ['student', 'B990617', '홍철수', 3, '컴퓨터'],
    ['course', 'C101', '동역학', 3, '김공과', '기계'],
    ['course', 'C102', '데이터베이스', 4, '유대학', '컴퓨터']
]
for data in hardcoding_data:
    table_name = data[0];
    insert_row_to(table_name, *data[1:])

input_file = open("./input.txt", "r")
output_file = open("./output.txt", "w")

lines = read_file()

# 전달받은 라인배열을 읽어들여 요구사항을 수행합니다.
for index in range(len(lines)):
    now_input = lines[index]
    if now_input == '0':
        break

    if now_input == '1':
        write_line_to_file("1. student 레코드 검색")
        show_table(table_name="student")

    if now_input == '2':
        write_line_to_file("2. course 레코드 검색")
        show_table(table_name="course")

    if now_input == '3':
        write_line_to_file("3. enroll 레코드 검색")
        show_table(table_name="enroll")

    if now_input == '4':
        write_line_to_file("4. enroll 레코드 삽입")
        index += 1
        next_line = lines[index]
        write_line_to_file(next_line)
        values = next_line.split()
        insert_row_to("enroll", *values)

write_line_to_file("0. 종료")

try:
    cursor.execute("set foreign_key_checks = 0")
    cursor.execute("drop table IF EXISTS student cascade")
    cursor.execute("drop table IF EXISTS course cascade")
    cursor.execute("set foreign_key_checks = 1")
except Exception as err:
    print(err)

input_file.close()
output_file.close()
conn.close()
