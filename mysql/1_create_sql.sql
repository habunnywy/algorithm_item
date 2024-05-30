CREATE DATABASE sql_tutorial;
SHOW DATABASES;
DROP DATABASE sql_tutorial;
USE `sql_tutorial`;

CREATE TABLE `student`(
	`student_id` INT AUTO_INCREMENT ,
    `name` VARCHAR(20),
    `major` VARCHAR(20) DEFAULT '历史',
    PRIMARY KEY(`student_id`)
);

DESCRIBE `student`;
DROP TABLE `student`;
ALTER TABLE `student` ADD `GPA` DECIMAL(3,2);
ALTER TABLE `student` DROP COLUMN `GPA`;

INSERT INTO `student` VALUES(1,'小白','历史');
INSERT INTO `student` VALUES(2,'小黑','生物');
INSERT INTO `student` VALUES(3,'小绿',NULL);
INSERT INTO `student` VALUES(3,'XIAO',NULL); 
INSERT INTO `student` (`name`,`major`,`student_id`) VALUES('小蓝','物理',4);
INSERT INTO `student` (`student_id`,`name`) VALUES(5,'小粉'); 
INSERT INTO `student` (`student_id`,`name`) VALUES(7,'兔子');

SELECT * FROM `student`;





