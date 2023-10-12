# 전처리
/*
  데이터베이스 생성 및 지정
*/
create database IF NOT EXISTS university;
use university;

set foreign_key_checks = 0;   -- 외래키 체크하지 않는 것으로 설정
drop table IF EXISTS student cascade;   -- 기존 student 테이블 제거  
drop table IF EXISTS course cascade;   -- 기존 course 테이블 제거  
drop table IF EXISTS enroll cascade;   -- 기존 enroll 테이블 제거  
set foreign_key_checks = 1;   -- 외래키 체크하는 것으로 설정


/*
  student 테이블 생성
*/
create table student (
   sno char(7) NOT NULL, 
   sname varchar(20) NOT NULL, 
	grade int DEFAULT 1, 
	dept varchar(20),
	primary key (sno));

/*
  course 테이블 생성
*/
create table course(
	cno char(4),
	cname varchar(30) not null,
	credit int,
	profname varchar(20),
	dept varchar(20),
	primary key (cno)
);

/*
  enroll 테이블 생성
*/
create table enroll(
	sno char(15),
	cno char(4),
	lettergrade char(2),
	midterm int,
	final int,
	FOREIGN KEY (sno) REFERENCES student (sno) on delete cascade,
	FOREIGN KEY (cno) REFERENCES course (cno) on delete cascade,
    	primary key (sno, cno)
);

/*
  student 테이블에 샘플 레코드 삽입
*/
insert into student 
values('C090309', '홍길동', 4,'컴퓨터공');
insert into student 
values('C090515', '이순신', 3, '전기공');
insert into student 
values('B990801', '김세종', 3, '전기공');
insert into student 
values('B710628', '김철수', 2, '디자인');
insert into student 
values('B870805', '김영희', 3, '기계공');
insert into student 
values('C170805', '김제주', 2, '산업공');


/*
  course 테이블에 샘플 레코드 삽입
*/
insert into course 
values('C101', 'C프로그래밍', 3, '김대구', '컴퓨터공');
insert into course 
values('C102', 'OS', 3, '이부산', '컴퓨터공');
insert into course 
values('C103', '자료구조', 2, '박광주', '컴퓨터공');
insert into course 
values('C104', '산공개론', NULL, '홍전주', '산업공');


/*
  enroll 테이블에 샘플 레코드 삽입
*/
insert into enroll 
values('C090309', 'C101', 'B', 80 ,80);
insert into enroll 
values('B990801', 'C103', 'C', 80, 75);
insert into enroll 
values('B870805', 'C102', 'A', 100, 85);
insert into enroll 
values('B870805', 'C103', 'A', 90, 90);
insert into enroll 
values('C170805', 'C102', 'B', 95, 80);
insert into enroll 
values('C090515', 'C103', 'B', 80, 95);

# select (8)

SELECT s.sno as 학번, s.sname as 학생이름
FROM enroll e, student s
WHERE e.sno=s.sno AND e.cno='C102';

# select (9)
SELECT c.cname as 과목이름
FROM course c, enroll e, student s
WHERE e.sno=s.sno AND e.cno=c.cno AND s.sname='김영희';

# select (10)
SELECT grade as 학년, COUNT(*) as '학년별 학생수'
FROM student s, enroll e, course c
WHERE s.sno=e.sno AND e.cno=c.cno AND c.cname='OS'
GROUP BY grade;

# select (11)
SELECT cname as 과목이름, dept as 개설학과
FROM course
WHERE cno in (
	SELECT cno
    FROM enroll
    WHERE sno='B870805'
);

# select (12)
SELECT cname as 과목이름, dept as 개설학과
FROM course
WHERE cno not in (
	SELECT cno
    FROM enroll
    WHERE sno='B870805'
);
