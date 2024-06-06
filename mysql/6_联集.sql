-- union 联集
SHOW TABLES;
SELECT * FROM `works_with`;
-- 1. 员工名字 union 客户名字
SELECT `name`
FROM `employee`
UNION
SELECT `client_name`
FROM `client`;

-- 2. 员工id + 员工名字 union 客户id + 客户名字
SELECT `emp_id` AS `total_id`, `name` AS `total_name`
FROM `employee`
UNION
SELECT `client_id`, `client_name`
FROM `client`;

-- 3. 员工薪水 union 销售金额
SELECT `salary` AS `total_money`
FROM `employee`
UNION
SELECT `total_sales`
FROM `works_with`;