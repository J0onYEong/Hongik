
create database if not exists university;
use university;
drop table if exists student;

create table student (
sno varchar(7) not null,
sname varchar(20) not null,
grade int default 1,
dept varchar(20),
primary key(sno)
);

show tables;

desc student;

-- address속성 추가
alter table student add address varchar(30);

desc student;

-- address속성 삭제
alter table student drop column address;

desc student;

drop table student;

show tables;