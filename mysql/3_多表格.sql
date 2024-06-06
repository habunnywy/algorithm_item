SHOW DATABASES;
DROP DATABASE `sql_tutorial`;
CREATE DATABASE `sql_tutorial`;
USE `sql_tutorial`;
/*创建员工表格*/
CREATE TABLE IF NOT EXISTS `employee`(
	`emp_id` INT PRIMARY KEY,
    `name` VARCHAR(20),
    `birth_data` DATE,
    `sex` VARCHAR(1),
    `salary` INT,
    `branch_id` INT, -- 虽然是外键，但还是先设为普通属性
    `sup_id` INT
    /*
    FOREIGN KEY(`brain_id`) REFERENCES `branch`(`branch_id`),
    FOREIGN KEY(`sup_id`) REFERENCES `employee`(`emp_id`)
    */  -- 这样写错误，因为sql是顺序执行的，此时还没有employee和branch 这两个表格
);
DESCRIBE `employee`;
DROP TABLE `employee`;
SELECT * FROM `employee`;

/*创建部门表格*/
CREATE TABLE IF NOT EXISTS `branch`(	
    `branch_id` INT PRIMARY KEY,
    `branch_name` VARCHAR(20),
    `manager_id` INT,
    FOREIGN KEY(`manager_id`) REFERENCES `employee`(`emp_id`) 
    ON DELETE SET NULL
);
SELECT * FROM `branch`;
DROP TABLE `branch`;

/*有了部门表格，才能补充employee表格的外键*/
ALTER TABLE `employee`
ADD FOREIGN KEY(`branch_id`) REFERENCES `employee`(`emp_id`)
ON DELETE SET NULL;

ALTER TABLE `employee`
ADD FOREIGN KEY(`sup_id`) REFERENCES `branch`(`branch_id`)
ON DELETE SET NULL;



/*创建客户表格*/
CREATE TABLE IF NOT EXISTS `client`(
	`client_id` INT PRIMARY KEY,
    `client_name` VARCHAR(20),
    `phone` VARCHAR(20)    
);
SELECT * FROM `client`;

CREATE TABLE IF NOT EXISTS `works_with`(
	`emp_id` INT,
    `client_id` INT,
    `total_sales` INT,
    PRIMARY KEY(`emp_id`,`client_id`),
    FOREIGN KEY(`emp_id`) REFERENCES `employee`(`emp_id`) ON DELETE CASCADE,
    FOREIGN KEY(`client_id`) REFERENCES `client`(`client_id`) ON DELETE CASCADE
); -- emp_id 和 client_id既是主键又是外键
SELECT * FROM `works_with`;

/*新增资料*/
/*错误写法：因为branch_id是foreign key 此时还没有这一资料
INSERT INTO `employee` VALUES(206, '小黄', '1998-10-08', 'F', 50000, 1, NULL);
INSERT INTO `employee` VALUES(207, '小绿', '1985-09-16', 'M', 29000, 2, 206);
INSERT INTO `employee` VALUES(208, '小黑', '2000-12-19', 'M', 35000, 3, 206);
INSERT INTO `employee` VALUES(209, '小白', '1997-01-22', 'F', 39000, 3, 207);
INSERT INTO `employee` VALUES(210, '小蓝', '1925-11-10', 'F', 84000, 1, 207);
*/

/*新增部门资料*/
INSERT INTO `branch` VALUES(1, '研发', NULL); -- manager_id 因为是外键现在还没有，先设为NULL
INSERT INTO `branch` VALUES(2, '行政', NULL);
INSERT INTO `branch` VALUES(3, '资讯', NULL);

/*部门资料新增后，才能增加雇员资料*/
INSERT INTO `employee` VALUES(206, '小黄', '1998-10-08', 'F', 50000, 1, NULL);
INSERT INTO `employee` VALUES(207, '小绿', '1985-09-16', 'M', 29000, 2, 206);
INSERT INTO `employee` VALUES(208, '小黑', '2000-12-19', 'M', 35000, 3, 206);
INSERT INTO `employee` VALUES(209, '小白', '1997-01-22', 'F', 39000, 3, 207);
INSERT INTO `employee` VALUES(210, '小蓝', '1925-11-10', 'F', 84000, 1, 207);

/*此时再去更新部门资料的主管*/
UPDATE `branch`
SET `manager_id` = 206
WHERE `branch_id` = 1;

UPDATE `branch`
SET `manager_id` = 207
WHERE `branch_id` = 2;

UPDATE `branch`
SET `manager_id` = 208
WHERE `branch_id` = 3;

/*增加客户资料*/
INSERT INTO `client` VALUES(400, '阿狗', '254354335');
INSERT INTO `client` VALUES(401, '阿猫', '25633899');
INSERT INTO `client` VALUES(402, '旺来', '45354345');
INSERT INTO `client` VALUES(403, '露西', '54354365');
INSERT INTO `client` VALUES(404, '艾瑞克', '18783783');

/*增加工作资料*/
INSERT INTO `works_with` VALUES(206, 400, 70000);
INSERT INTO `works_with` VALUES(207, 401, 24000);
INSERT INTO `works_with` VALUES(208, 400, 9800);
INSERT INTO `works_with` VALUES(208, 403, 24000);
INSERT INTO `works_with` VALUES(210, 404, 87940);



-- 练习

-- 1. 取得所有员工资料
SELECT * FROM `employee`;

-- 2. 取得所有客户资料
SELECT * FROM `client`;

-- 3.按薪水高到低取得员工资料
SELECT * FROM `employee` ORDER BY  `salary` DESC;

-- 4.取得薪水前3高的员工
SELECT `name` 
FROM `employee` 
ORDER BY `salary` 
DESC LIMIT 3;

-- 5.取得所有员工的名字
SELECT DISTINCT `sex` FROM `employee`;



















