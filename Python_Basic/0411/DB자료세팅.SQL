show databases;

create database work;

create table work.goods (
code int primary key,
name varchar(20) not null,
su int,
dan int );

use work;
select database();
show tables;
desc goods;

# 냉장고, 세탁기, 전자레인지, HDTV 추가
insert into goods values(1, '냉장고', 2, 850000);
insert into goods values(2, '세탁기', 3, 550000);
insert into goods values(3, '전자레인지', 2, 350000);
insert into goods values(4, 'HDTV', 3, 150000);
select * from goods;

# 사용자 생성
# create user '사용자아이디'@'접속IP 또는 Host' identified by '비밀번호';
# 권한 설정 (모든테이블 모든권한)
# grant all privileges on DB명.* to '사용자ID'@'접속IP';

## 예제
# 사용자 생성 : scott@localhost(remote), 'tiger(pw)'
# 권한 부여 : work DB에 모든 권한 부여

CREATE USER 'scott'@'0.0.0.0' identified by 'tiger';
CREATE USER 'scott'@'localhost' identified by 'tiger';
select * from mysql.user;
GRANT ALL PRIVILEGES ON WORK.* to 'scott'@'0.0.0.0';
GRANT ALL privileges ON work.* to 'scott'@'localhost';
select * from mysql.user where user = 'scott';

# 코드 5, 컴퓨터, 4, 1200000 추가
INSERT INTO goods VALUES(5,'컴퓨터',4,1200000);
UPDATE goods SET dan = 1500000, su = 2 WHERE code = 5;
select * from goods;
DELETE FROM goods WHERE name = '컴퓨터';

# ==== scott 워크벤치(work) 생성 후 접속
