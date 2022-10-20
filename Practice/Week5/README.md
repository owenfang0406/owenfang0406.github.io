#Week5 HW
>需求3 新增資料
---
![需求2](https://github.com/owenfang0406/owenfang0406.github.io/blob/main/Practice/Week5/1.png)
---
insert into member(id, name, username, password, follow_count)values (0, 'tester', 'test', 'test', 5);

insert into member(id, name, username, password, follow_count)values (2, 'adminr', 'admint', '12345t', 55);

insert into member(id, name, username, password, follow_count)values (3, 'Owen', 'Owen0406t', '67890zt', 53);

insert into member(id, name, username, password, follow_count)values (4, 'User_Will', 'willt', '1qaz2wsxt', 455);

insert into member(id, name, username, password, follow_count)values (5, 'User_Tom"', 'Tom', 'aaabbb', 4455);

---
>需求3 查詢資料
---
![需求3](https://github.com/owenfang0406/owenfang0406.github.io/blob/main/Practice/Week5/2.png)
---
select * from member;

select * from member order by time desc;

select * from member order by time desc limit 2,4;

select * from member where username = 'test';

select * from member where username = 'test' and password = 'test';

select * from member where username = 'test';

update member set name = 'tes2' where username = 'test';

---
![需求3 update語法](https://github.com/owenfang0406/owenfang0406.github.io/blob/main/Practice/Week5/2.1.png)
---
>需求4 計算資料
---
![需求4](https://github.com/owenfang0406/owenfang0406.github.io/blob/main/Practice/Week5/3.png)
---
select COUNT(*) id from member;

select SUM(follow_count) from member;

select AVG(follow_count) from member;
---

>需求5 Join 兩張 Table 查詢
---
![需求5](https://github.com/owenfang0406/owenfang0406.github.io/blob/main/Practice/Week5/4.png)
---
>建立表格 schema

create table message (

id bigint primary key auto_increment,

member_id bigint not null,

content varchar(255) not null,

like_count int not null default 0,

time datetime not null default current_timestamp

);

>新增表格資料

insert into message(id, member_id, content, like_count)values (1, '2', '好讚喔', 50);

insert into message(id, member_id, content, like_count)values (2, '5', '問世堅情是何物', 509);

insert into message(id, member_id, content, like_count)values (3, '2', '南北菜蟲一起串連', 550);

insert into message(id, member_id, content, like_count)values (4, '3', '就是這麼簡單，八個字', 590);

insert into message(id, member_id, content, like_count)values (5, '1', '你進土城看守所得時候，記得先吞曲棍球', 5220);

insert into message(id, member_id, content, like_count)values (6, '4', '小兒科啦', 70);

insert into message(id, member_id, content, like_count)values (7, '1', 'Over my dead body', 960);

insert into message(id, member_id, content, like_count)values (8, '3', '愚人的問題，智者無法回答', 790);

insert into message(id, member_id, content, like_count)values (9, '5', '沒錢用不等於缺錢，停工不等於缺工，沒電不等於缺電', 9990);

insert into message(id, member_id, content, like_count)values (10, '2', '我沒有去汽車旅館拉', 10002);

>配合 join 查詢所有留言並顯示username

select member.id, member.name, member.username, message.member_id, message.content from message

inner join member

on message.member_id = member.id;

---
![需求5](https://github.com/owenfang0406/owenfang0406.github.io/blob/main/Practice/Week5/5.png)
---
>配合 join 顯示 username = 'test'

select member.id, member.username, message.member_id, message.content from message

inner join member

on message.member_id = member.id

where member.username = 'test';

>配合 join 查詢出 username = test 且 按讚數平均值

select member.username, message.member_id, avg(message.like_count) from message

inner join member

on message.member_id = member.id

where username = 'test'

group by member_id;
