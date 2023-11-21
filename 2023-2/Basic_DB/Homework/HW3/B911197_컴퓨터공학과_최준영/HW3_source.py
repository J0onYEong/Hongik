import datetime
import pymysql

# 함수 이름 : make_string_from
# 기능 : 전달받은 튜플의 요소들을 하나의 문자열로 만들어준다.
# 반환값 : 없음
# 전달인자 :
#   - tuple : 문자열로 변환하고자 하는 파이썬 튜플이다.
def make_string_from(tuple):
    result_string = ""

    for element in tuple:

        if type(element) == str:
            result_string += element
        elif type(element) == datetime.date:
            # 요소의 타입이 datetime.date일 경우 요구형식으로 변환 ex) '2000/02/23'
            result_string += element.strftime('%Y/%m/%d')
        else:
            result_string += str(element)

        result_string += " "

    return result_string.strip()





# 함수 이름 : insert_row_to
# 기능 : 테이블 명과 열값을 입력받아 특정 테이블에 삽입하는 함수입니다.
# 반환값 : 없음
# 전달인자 :
#   - table_name : 열을 삽입할 테이블명
#   - *values : 테이블에 삽이할 열값들로 가변 매개변수 형태로 전달받음
def insert_row_to(table_name, *values):
    global cursor

    # ('값1', '값2', '값3' ... ) 현태로 sql문에 삽입할 값들의 문자열형태입니다.
    values_string = ""
    num_of_values = len(values)

    for index in range(num_of_values): # 가변매개변수들로 부터 값 문자열을 만든다.
        value = values[index]
        if type(value) == str:
            value = "'{}'".format(value)
        if type(value) == int:
            value = str(value)

        values_string+=value

        if index != num_of_values-1:
            values_string+=', '

    # 완성된 문자열을 가지고 sql문을 완성한다.
    sql = "insert into {} values ({})".format(table_name, values_string)

    try:
        cursor.execute(sql)
    except Exception as err:
        print(err)





# 함수 이름 : write_line_to_file
# 기능 : output.txt파일에 전달한 라인을 입력한다.
# 반환값 : 없음
# 전달인자 :
#   - line : output.txt에 기록할 문자열
def write_line_to_file(line):
    global w_file

    w_file.write(line+"\n")





# 함수 이름 : register
# 기능 : 입력파일의 라인을 읽어들여 테이블에 튜플을 등록합니다.
# 반환값 : 없음
# 전달인자 :
#   - table_name : 튜블입 삽입하려는 테이블의 이름
#   - message : 메뉴텍스트
def register(table_name, message):
    write_line_to_file(message)
    stripped_line = r_file.readline().strip()

    # 라인에 입력된 값들을 ouput.txt에 기록합니다.
    write_line_to_file("> " + stripped_line)

    # 공백으로 구분되는 값들(str)을 list로 변환합니다.
    values = stripped_line.split()

    # 값들(list)을 테이블에 삽입합니다.
    insert_row_to(table_name, *values)





# 함수 이름 : exit
# 기능 : 프로그램이 종료됬음을 파일에 기록합니다.
# 반환값 : 없음
# 전달인자 : 없음
def exit() :
     write_line_to_file("1.2. 종료\n")





# 함수 이름 : login
# 기능 : customer테이블에서 입력받은 cid를 보유한 열을 찾음, cid를 output.txt에 기록
# 반환값 : 없음
# 전달인자 :
#   - isAdmin : True일 경우 관린자 로그인을 의미한다, 기본값은 False로 고객 로그인을 의미한다.
def login(isAdmin=False):
    # 전역변수은 login_user_id를 명시적으로 불러옵니다.
    global login_user_id, cursor

    write_line_to_file("3.1. 로그인" if isAdmin else "2.1. 로그인")

    input_line = r_file.readline()
    cid = input_line.strip()
    # login_user_id를 cid값으로 가지는 튜프을 customer테이블에서 조회하는 sql문입니다.
    sql = """
        select CID
        from customer
        where CID='{}'
    """.format(cid)
    try:
        cursor.execute(sql)

        # 검색에 성공한 cid를 output파일에 기록한다.
        cid_from_table = cursor.fetchall()[0][0]

        # login_user전역 변수에 현재 로그인한 유저의 cid를 기록
        login_user_id = cid_from_table

        # customer테이블에서 조회한 고객의 cid를 output.txt에 기록합니다.
        write_line_to_file("> " + cid_from_table)
    except Exception as err:
        print(err)





# 함수 이름 : logout
# 기능 : login_user전역변수에 빈 문자열을 할당하여 로그아웃합니다.
# 반환값 : 없음
# 전달인자 : 없음
#   - isAdmin : True일 경우 관린자 로그아웃을 의미한다, 기본값은 False로 고객 로그아웃을 의미한다.
def logout(isAdmin=False):
    # 전역변수은 login_user_id를 명시적으로 불러옵니다.
    global login_user_id

    write_line_to_file("3.5. 로그아웃" if isAdmin else "2.5. 로그아웃")
    write_line_to_file("> " + login_user_id)

    # login_user_id젼역변수 값에 빈문자열을 집어넣음으로써 로그아웃합니다.
    login_user_id = ""






# 함수 이름 : book_hotel_room
# 기능 : 특정 고객 예약정보를 booking테이블에 기록한다.
# 반환값 : 없음
# 전달인자 : 없음
def book_hotel_room():
    # 전역변수은 login_user_id를 명시적으로 불러옵니다.
    global login_user_id, cursor

    write_line_to_file("2.2. 호텔방 예약")

    # 예약 정보를 읽어들임
    input_line = r_file.readline()
    stripped_line = input_line.strip()

    write_line_to_file("> " + stripped_line)

    values = stripped_line.split()

    # 예약하는 고객의 CID를 값 list의 마지막 값으로 삽입합니다.
    values.append(login_user_id)

    # 완성된 값 list를 booking테이블에 삽입합니다.
    insert_row_to("booking", *values)






# 함수 이름 : show_booking_information_for_user
# 기능 : 특정 고객의 모든 예약정보를 조회한다.
# 반환값 : 없음
# 전달인자 : 없음
def show_booking_information_for_user():
    # 전역변수은 login_user_id를 명시적으로 불러옵니다.
    global login_user_id, cursor

    write_line_to_file("2.3. 호텔방 예약 조회")

    # 로그인한 유저의 호텔방 예약점보를 조회하는 sql문입니다.
    sql = """
        select HID, 호실, `체크인 날짜`, `체크아웃 날짜`
        from booking
        where cid = '{}'
    """.format(login_user_id)

    try:
        cursor.execute(sql)

        rows = cursor.fetchall()

        # 조회한 예약정보들을 output.txt에 기록합니다.
        for row in rows:
            write_line_to_file("> " + make_string_from(row))

    except Exception as err:
        print(err)





# 함수 이름 : show_booking_information
# 기능 : 모든 호텔에 예약된 모든 정보를 조회한다.
# 반환값 : 없음
# 전달인자 : 없음
def show_all_booking_information():
    global cursor

    write_line_to_file("3.4. 예약 내역 조회")

    # 모든 호텔에 예약된 모든 예약정보를 조회합니다.
    # 예약자정보, 호텔방정보, 호텔정보, 예약정보를 모두 조회하는 sql문 입니다.
    sql = """
        select c.cid, c.이름, b.hid, h.이름, h.주소, b.호실, hr.가격, b.`체크인 날짜`, b.`체크아웃 날짜`
        from booking b, customer c, hotel_room hr, hotel h
        where b.cid = c.cid and b.hid = hr.hid and b.호실 = hr.호실 and hr.hid = h.hid
        order by c.cid
    """

    try:
        cursor.execute(sql)

        rows = cursor.fetchall()

        # 조회한 튜플을 output.txt에 기록합니다.
        for row in rows:
            write_line_to_file("> " + make_string_from(row))

    except Exception as err:
        print(err)





# 함수 이름 : unbook_hotel_room
# 기능 : HID, 호실 정보를 가지고 호텔방 예약정보를 삭제한다.
# 반환값 : 없음
# 전달인자 : 없음
def unbook_hotel_room():
    # 전역변수은 login_user_id를 명시적으로 불러옵니다.
    global login_user_id

    write_line_to_file("2.4 호텔방 예약 취소")

    input_line = r_file.readline()
    stripped_line = input_line.strip()

    write_line_to_file("> " + stripped_line)

    hid, room_number = stripped_line.split()

    # 로그인한 유저의 특정 예약정보를 삭제하는 sql문 입니다.
    sql = """
        delete from booking
        where HID = '{}' and 호실 = '{}' and cid = '{}'
    """.format(hid, room_number, login_user_id)

    try:
        cursor.execute(sql)

    except Exception as err:
        print(err)





# 함수 이름 : doTask
# 기능 : 메뉴를 입력받아 특정 함수를 호출하는 함수이다.
# 반환값 : 없음
# 전달인자 : 없음
def doTask() :
    # 전역변수은 login_user_id를 명시적으로 불러옵니다.
    global login_user_id

    # 종료 메뉴(1 2)가 입력되기 전까지 반복함
    while True :
        # 입력파일에서 메뉴 숫자 2개 읽기
        line = r_file.readline()
        line = line.strip()
        menu_levels = line.split()

        # 메뉴 파싱을 위한 level 구분
        menu_level_1 = int(menu_levels[0])
        menu_level_2 = int(menu_levels[1])

        # 메뉴 구분 및 해당 연산 수행
        if menu_level_1 == 1 :

            if menu_level_2 == 1 :
                register("customer", "1.1. 회원가입")

            elif menu_level_2 == 2 :
                exit()
                break

        elif menu_level_1 == 2 :

            if menu_level_2 == 1 :
                login()

            elif menu_level_2 == 2 :
                book_hotel_room()

            elif menu_level_2 == 3 :
                show_booking_information_for_user()

            elif menu_level_2 == 4 :
                unbook_hotel_room()

            elif menu_level_2 == 5 :
                logout()

        elif menu_level_1 == 3:

            if menu_level_2 == 1:
                login(isAdmin=True)

            elif menu_level_2 == 2:
                register("hotel", "3.2. 호텔 정보 등록")

            elif menu_level_2 == 3:
                register("hotel_room", "3.3. 호텔방 정보 등록")

            elif menu_level_2 == 4:
                show_all_booking_information()

            elif menu_level_2 == 5:
                logout(isAdmin=True)

##############
#  메인 코드  #
##############

conn = pymysql.connect(host='localhost', user='root', password='root', db='hotel_booking', charset='utf8mb4')
cursor = conn.cursor()

cursor.execute("set foreign_key_checks = 0")
cursor.execute("drop table if exists hotel cascade")
cursor.execute("drop table if exists hotel_room cascade")
cursor.execute("drop table if exists customer cascade")
cursor.execute("drop table if exists booking cascade")
cursor.execute("set foreign_key_checks = 1")

# 테이블을 생성하는 sql문 입니다.
create_table_sqls = [
    """
        create table hotel(
            HID varchar(30) not null,
            이름 varchar(30),
            주소 varchar(30),
            primary key (HID)
        )
    """,
    """
        create table hotel_room(
            HID varchar(30) not null,
            호실 varchar(30) not null,            
            가격 int,
            foreign key(HID) references hotel(HID),
            primary key(HID, 호실)
        )
    """,
    """
        create table customer(
            CID varchar(30) not null,
            이름 varchar(30),
            전화번호 varchar(30),
            primary key(CID)
        )
    """,
    """
        create table booking(
            HID varchar(30) not null,
            호실 varchar(30) not null,
            `체크인 날짜` date,
            `체크아웃 날짜` date,
            CID varchar(30) not null,
            foreign key(HID, 호실) references hotel_room(HID, 호실),
            foreign key(CID) references customer(CID),
            primary key(HID, 호실, CID)
        )
    """
]
# 배열에 저장된 sql문들을 실행해 테이블을 생성합니다.
for sql in create_table_sqls:
    try:
        cursor.execute(sql)
    except Exception as err:
        print(err)


r_file = open("input.txt", "r")
w_file = open("output.txt", "w")

# 현재 로그인한 유저의 CID를 저장하는 전역변수 입니다.
login_user_id = ""

doTask()

r_file.close()
w_file.close()
