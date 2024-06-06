CREATE DATABASE `sql_tutorial`; -- 资料库，是许多表格的集合
SHOW DATABASES;
DROP DATABASE sql_tutorial;
USE `sql_tutorial`;

/*
六种资料形态
INT              -- 整数
DECIMAL(m,n)     -- m位浮点数，小数点占n位
VARCHAR(n) 		 -- 最多存放n位的字串
BLOB			 -- 二进制大对象(图片 影片 档案...)
DATE			 -- 日期 'YYYY-MM-DD'
TIMESTAMP		 -- 时间 'YYYY-MM-DD HH:MM:SS'
*/
CREATE TABLE `student`( -- 创建名为student表格
	`student_id` INT AUTO_INCREMENT , -- 属性名 属性类型 <是否主键> <属性特征1> ... <属性特征2>
    -- AUTO_INCREMENT 仅在添加资料时候有用
    `name` VARCHAR(20) NOT NULL,
    `major` VARCHAR(20) DEFAULT '历史', -- ``里面是变量名 ''里面是字串
    PRIMARY KEY(`student_id`) -- 单独设置属性
);

DESCRIBE `student`; -- 展示表格各属性的特征，但不显示内容
DROP TABLE `student`; -- 删除表格
ALTER TABLE `student` ADD `GPA` DECIMAL(3,2); -- ALTER 改变对象 对象名 操作 操作对象 操作属性
ALTER TABLE `student` DROP COLUMN `GPA`;

INSERT INTO `student` VALUES(1,'小白','历史'); -- 插入一笔资料
INSERT INTO `student` VALUES(2,'小黑','生物');
INSERT INTO `student` VALUES(3,'小绿',NULL);
INSERT INTO `student` VALUES(3,'XIAO',NULL); 
INSERT INTO `student` (`name`,`major`,`student_id`) VALUES('小蓝','物理',4);
INSERT INTO `student` (`student_id`,`name`) VALUES(5,'小粉'); 
INSERT INTO `student` (`student_id`,`name`) VALUES(7,'兔子');

SELECT * FROM `student`; -- 搜寻所有student里面的资料


INSERT INTO `student` (`student_id`,`name`,`major`) VALUES(1,NULL,'化工'); -- 因为name设了不为null 故报错




