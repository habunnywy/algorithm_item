-- join 连接(多个表格)

INSERT INTO `branch` VALUES(4, '偷懒', NULL);
SELECT * FROM `branch`;

-- 取得所有部门经理的名字
SELECT * 
FROM `employee`
JOIN `branch`
ON `emp_id` = `manager_id`; -- employee中emp_id和branch中manager_id相等的进行配对

SELECT `employee`.`emp_id`, `name`, `branch_name` 
FROM `employee`
JOIN `branch`
ON `employee`.`branch_id` = `branch`.`branch_id`; 

-- LEFT JOIN 左边表格全部返回，右边表格只有符合条件才会返回,不满足的右边资料用NULL代替
SELECT `employee`.`emp_id`, `employee`.`name`, `branch`.`branch_name`
FROM `employee` LEFt JOIN `branch`
ON `employee`.`emp_id` = `branch`.`manager_id`;