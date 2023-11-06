-- 데이터베이스 생성 및 지정
create database IF NOT EXISTS hotel_booking;
use hotel_booking;
alter database hotel_booking default character set utf8mb4;

set foreign_key_checks = 0;    			-- 외래키 체크하지 않는 것으로 설정
drop table IF EXISTS hotel cascade;   				-- 기존 hotel 테이블 제거
drop table IF EXISTS hotelier cascade;   			-- 기존 hotelier 테이블 제거
drop table IF EXISTS hotel_room cascade;   			-- 기존 hotel_room 테이블 제거
drop table IF EXISTS customer cascade;   			-- 기존 customer 테이블 제거
drop table IF EXISTS booking cascade;   			-- 기존 booking 테이블 제거 
drop table IF EXISTS stay_information cascade; 		-- 기존 stay_information 테이블 제거 
drop view IF EXISTS hongik_hotel_customers cascade; -- 기존 hongik_hotel_customers 뷰 제거
set foreign_key_checks = 1;   			-- 외래키 체크하는 것으로 설정

-- (1)  테이블 생성 
# 호텔
CREATE TABLE hotel (
	HID varchar(20) NOT NULL,
    이름 varchar(20),
    주소 varchar(30),
    전화번호 varchar(20),
    PRIMARY KEY(HID)
);

# 호텔리어
CREATE TABLE hotelier (
	HLID varchar(20) NOT NULL,
    이름 varchar(20),
    HID varchar(20),
    PRIMARY KEY(HLID),
    FOREIGN KEY(HID) REFERENCES hotel(HID)
);
# 호텔방
CREATE TABLE hotel_room (
	HID varchar(20) NOT NULL,
	호실 VARCHAR(10) NOT NULL,
    가격 INT,
    PRIMARY KEY(HID, 호실),
    FOREIGN KEY(HID) REFERENCES hotel(HID)
);
# 고객
CREATE TABLE customer (
	CID VARCHAR(20) NOT NULL,
    이름 VARCHAR(20),
    전화번호 VARCHAR(20),
    PRIMARY KEY(CID)
);
# 예약
CREATE TABLE booking (
    CID varchar(20) NOT NULL,
    HID varchar(20) NOT NULL,
    호실 varchar(10) NOT NULL,
    `체크인 날짜` DATE,
    `체크아웃 날짜` DATE,
    PRIMARY KEY(호실, HID, CID),
    FOREIGN KEY(CID) REFERENCES customer(CID),
    FOREIGN KEY(HID, 호실) REFERENCES hotel_room(HID, 호실)
);
# 투숙정보
CREATE TABLE stay_information (
	CID varchar(20) NOT NULL,
    HID varchar(20) NOT NULL,
	호실 varchar(10) NOT NULL,
	`체크인 날짜` DATE NOT NULL,
    `체크아웃 날짜` DATE,
    PRIMARY KEY(호실, HID, CID, `체크인 날짜`),
    FOREIGN KEY(CID) REFERENCES customer(CID),
	FOREIGN KEY(HID, 호실) REFERENCES hotel_room(HID, 호실)
);

-- (2)  데이터 삽입
INSERT 
INTO hotel(HID, 이름, 주소, 전화번호)
VALUES 
	('H001', '홍익호텔', '마포구 상수동', '02-320-1234'),
    ('H002', '중앙호텔', '동작구 흑석동', '02-850-1234'),
    ('H003', '건국호텔', '광진구 자양동', '02-415-1234');

SELECT * FROM hotel;

INSERT 
INTO hotelier(HLID, 이름, HID)
VALUES 
	('HL001', 'KMS', 'H001'),
	('HL002', 'LED', 'H001'),
	('HL003', 'YHD', 'H002'),
	('HL004', 'KKT', 'H002'),
	('HL005', 'CPC', 'H003'),
	('HL006', 'LSY', 'H003');
    
SELECT * FROM hotelier;
    
INSERT
INTO hotel_room(HID, 호실, 가격)
VALUES
	('H001', '01', 1400),
	('H001', '02', 1200),
	('H001', '03', 700),
	('H002', '01', 1900),
	('H002', '02', 1000),
	('H002', '03', 1300),
	('H002', '04', 1600),
	('H003', '01', 900),
	('H003', '02', 1100);
    
SELECT * FROM hotel_room;
    
INSERT 
INTO customer(CID, 이름, 전화번호)
VALUES
	('C001', 'PDN', '010-3304-6302'),
	('C002', 'KYS', '010-7323-3789'),
	('C003', 'YDJ', '010-2628-7436'),
	('C004', 'KSM', '010-2299-7827'),
	('C005', 'PJH', '010-3157-2501'),
	('C006', 'HBC', '010-2936-5427'),
	('C007', 'KCY', '010-7119-6732'),
	('C008', 'PYS', '010-2523-9738');

SELECT * FROM customer;

INSERT
INTO booking(CID, HID, 호실, `체크인 날짜`, `체크아웃 날짜`)
VALUES
	('C001', 'H001', '01', '2023-07-16', '2023-07-28'),
	('C002', 'H001', '02', '2023-07-21', '2023-07-22'),
	('C001', 'H002', '01', '2023-08-16', '2023-08-18'),
	('C005', 'H002', '01', '2023-09-06', '2023-09-09'),
	('C005', 'H002', '02', '2023-09-10', '2023-09-18'),
	('C003', 'H002', '02', '2023-09-14', '2023-10-17'),
	('C002', 'H002', '03', '2023-10-16', '2023-10-18'),
	('C008', 'H003', '01', '2023-10-22', '2023-10-26'),
	('C004', 'H003', '01', '2023-10-28', '2023-11-02'),
	('C003', 'H003', '02', '2023-10-29', '2023-11-03');
    
SELECT * FROM booking;

INSERT
INTO stay_information(CID, HID, 호실, `체크인 날짜`, `체크아웃 날짜`)
VALUE 
	('C002', 'H002', '01', '2021-07-16', '2021-07-20'),
	('C001', 'H003', '02', '2021-07-21', '2021-07-25'),
	('C001', 'H001', '01', '2021-08-16', '2021-08-28'),
	('C004', 'H002', '02', '2021-09-06', '2021-09-18'),
	('C001', 'H002', '02', '2021-09-10', '2021-09-17'),
	('C003', 'H002', '02', '2021-09-14', '2021-09-21'),
	('C002', 'H001', '03', '2022-10-15', '2022-10-24'),
	('C005', 'H003', '01', '2022-10-19', '2022-10-26'),
	('C004', 'H002', '01', '2022-10-22', '2022-10-26'),
	('C005', 'H003', '02', '2022-10-29', '2022-11-01');

SELECT * FROM stay_information;

-- (3) 1)
SELECT "1)";       -- 문제 번호 출력하기
SELECT * FROM hotel;
SELECT * FROM hotelier;
SELECT * FROM hotel_room;
SELECT * FROM customer;
SELECT * FROM booking;
SELECT * FROM stay_information;

-- (3) 2)
SELECT "2)";
SELECT HLID, 이름
FROM hotelier
WHERE HID = 'H001';

-- (3) 3)
SELECT "3)";
SELECT CID, SUM(datediff(`체크아웃 날짜`, `체크인 날짜`)) as '총 투숙일'
FROM stay_information
GROUP BY CID;

-- (3) 4)
SELECT "4)";
SELECT c.이름 as 고객이름, h.이름 as 호텔이름
FROM booking b, customer c, hotel h
WHERE b.CID = c.CID and b.HID = h.HID and datediff(b.`체크아웃 날짜`, b.`체크인 날짜`) < 4;

-- (3) 5)
SELECT "5)";
SELECT CID, datediff(`체크아웃 날짜`, `체크인 날짜`) as 투숙일수
FROM stay_information
WHERE CID = 'C001';

-- (3) 6)
SELECT "6)";
SELECT *
FROM hotel_room
WHERE 가격 >= 1300
order by HID DESC, 호실 ASC;

-- (3) 7)
SELECT "7)";
SELECT h.이름 as 호텔이름, h.전화번호 as 전화번호
FROM stay_information si, hotel h
WHERE si.HID = h.HID
order by si.`체크인 날짜` ASC limit 1;

-- (3) 8)
SELECT "8)";
SELECT c.이름 as 고객이름
FROM booking b, customer c
WHERE b.CID = c.CID and b.HID = 'H003';

-- (3) 9)
SELECT "9)";
SELECT h.이름 as 호텔이름
FROM stay_information si, hotel h
WHERE si.HID = h.HID and year(si.`체크인 날짜`) = '2021' 
GROUP BY si.HID
HAVING count(*) >= 2;

-- (3) 10)
SELECT "10)";
SELECT distinct c.이름 as 고객이름, c.전화번호 as 전화번호
FROM booking b, customer c, hotel h
WHERE b.CID=c.CID and b.HID=h.HID and b.CID in (
	SELECT CID
    FROM stay_information
    WHERE `체크인 날짜` < '2022-08-30'
) and h.주소 like '%흑석동';

-- (3) 11)
SELECT "11)";
SELECT c.이름 as 고객이름
FROM booking b, customer c
WHERE b.CID = c.CID and b.CID in (
	SELECT CID
    FROM booking
    WHERE HID='H001'
) and b.CID in (
	SELECT CID
    FROM booking
    WHERE HID='H002'
)
GROUP BY b.CID;

-- (3) 12)
SELECT "12)";
SELECT HID, (
	SELECT count(*)
    FROM booking
    WHERE HID = h.HID
) as '예약 수', (
	SELECT count(*)
    FROM stay_information
	WHERE HID = h.HID
) as '투숙 수'
FROM hotel h;

-- (3) 13)
UPDATE hotel_room
SET 가격 = 가격+100
WHERE (HID, 호실) in (
	SELECT HID, 호실
    FROM booking
    WHERE CID = "C002"
);

SELECT *
FROM hotel_Room;

-- (3) 14)
SELECT "14)";
DELETE 
FROM hotelier
WHERE HID in (
	SELECT HID
    FROM hotel
    WHERE 이름 = '중앙호텔'
);

SELECT * FROM hotelier;

-- (3)  15)
SELECT "15";
CREATE VIEW hongik_hotel_customers
AS SELECT *
	FROM customer
	WHERE CID in (
		SELECT CID
        FROM stay_information si, hotel h
        WHERE si.HID = h.HID and h.이름 = '홍익호텔'
    );

SELECT * FROM hongik_hotel_customers;

set foreign_key_checks = 0;    			-- 외래키 체크하지 않는 것으로 설정
drop table IF EXISTS hotel cascade;   				-- 기존 hotel 테이블 제거
drop table IF EXISTS hotelier cascade;   			-- 기존 hotelier 테이블 제거
drop table IF EXISTS hotel_room cascade;   			-- 기존 hotel_room 테이블 제거
drop table IF EXISTS customer cascade;   			-- 기존 customer 테이블 제거
drop table IF EXISTS booking cascade;   			-- 기존 booking 테이블 제거 
drop table IF EXISTS stay_information cascade; 		-- 기존 stay_information 테이블 제거 
drop view IF EXISTS hongik_hotel_customers cascade; -- 기존 hongik_hotel_customers 뷰 제거
set foreign_key_checks = 1;   			-- 외래키 체크하는 것으로 설정