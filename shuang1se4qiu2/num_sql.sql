PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE kai1_jiang3_hao4(
ID TEXT NOT NULL,
LEI4_XING2 TEXT NOT NULL,
H1 TEXT NOT NULL,
H2 TEXT NOT NULL,
H3 TEXT NOT NULL,
H4 TEXT NOT NULL,
H5 TEXT NOT NULL,
L1 TEXT NOT NULL,
L2 TEXT NOT NULL
);
INSERT INTO kai1_jiang3_hao4 VALUES('2019','kai1_jiang3_hao4','1','2','3','4','5','a','b');
INSERT INTO kai1_jiang3_hao4 VALUES('2018','kai1_jiang3_hao4','1','2','3','4','5','a','b');
INSERT INTO kai1_jiang3_hao4 VALUES('2017','kai1_jiang3_hao4','1','2','3','4','5','a','b');
INSERT INTO kai1_jiang3_hao4 VALUES('2016','kai1_jiang3_hao4','3','4','5','6','7','f','g');
INSERT INTO kai1_jiang3_hao4 VALUES('2015','hehe','2','5','8','12','21','i','m');
COMMIT;
