SET SQL_SAFE_UPDATES = 0;
DROP TABLE `student`;
CREATE TABLE IF NOT EXISTS `student`(
	`student_id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(20),
    `major` VARCHAR(20) DEFAULT '历史',
    `score` INT
);
DESCRIBE `student`;
INSERT INTO `student` (`name`,`major`,`score`) VALUES('小白','英语',50);
INSERT INTO `student` (`name`,`major`,`score`) VALUES('小黄','生物',90);
INSERT INTO `student` (`name`,`major`,`score`) VALUES('小绿','历史',70);
INSERT INTO `student` (`name`,`major`,`score`) VALUES('小蓝','英语',80);
INSERT INTO `student` (`name`,`major`,`score`) VALUES('小黑','化学',20);
SELECT * FROM `student` WHERE `student_id` < 3 ORDER BY `SCORE` DESC ;

UPDATE `student`
SET `major` = '生化啦', `name`='小惠'
WHERE `major` = '生化' OR `major` = '化学'; 

DELETE FROM `student`
WHERE `name`='小惠' AND `major`='生化啦';