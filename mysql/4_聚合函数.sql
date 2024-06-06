-- 1. 取得员工人数
SELECT COUNT(*) FROM `employee` WHERE `sex` = 'M';

-- 2. 取得所有出生于1970-01-01之后的女性员工人数
SELECT COUNT(*) 
FROM `employee` 
WHERE `birth_data` > '1970-01-01' AND `sex` = 'F';

-- 3.取得所有员工的平均薪水
SELECT AVG(`salary`) FROM `employee`;

-- 4.取得所有员工薪水的总和
SELECT SUM(`salary`) FROM `employee`;

-- 5.取得最高的薪水
SELECT MAX(`salary`) FROM `employee`;

-- 5.取得最低的薪水
SELECT MIN(`salary`) FROM `employee`;