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
SELECT * from member;

SELECT * from member ORDER BY time desc;

SELECT * from member WHERE username = 'test';

SELECT * from member WHERE username = 'test' and password = 'test';

SELECT * from member WHERE username = 'test2';

UPDATE member SET username = 'test2' WHERE id = 1;

---
>需求4 計算資料
---
![需求4](https://github.com/owenfang0406/owenfang0406.github.io/blob/main/Practice/Week5/3.png)
---
SELECT COUNT(*) id from member;

SELECT SUM(follow_count) from member;

SELECT AVG(follow_count) from member;

