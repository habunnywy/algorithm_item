SET SQL_SAFE_UPDATES = 0;
DROP TABLE `student`;
CREATE TABLE IF NOT EXISTS `student`(
	`student_id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(20),
    `major` VARCHAR(20) DEFAULT '历史',
    `score` INT
);

SELECT * FROM `student`; 
/*
SELECT {所需属性列表} 
FROM `表格名` 
<WHERE> <{条件列表}> 
<ORDER BY> <{`排序属性列表`}>  默认从小到大ASC
<LIMIT> <{需要的数量}>;
*/

DESCRIBE `student`;
INSERT INTO `student` (`name`,`major`,`score`) VALUES('小白','英语',50);
INSERT INTO `student` (`name`,`major`,`score`) VALUES('小黄','生物',90);
INSERT INTO `student` (`name`,`major`,`score`) VALUES('小绿','历史',70);
INSERT INTO `student` (`name`,`major`,`score`) VALUES('小蓝','英语',80);
INSERT INTO `student` (`name`,`major`,`score`) VALUES('小黑','化学',20);
SELECT * FROM `student` WHERE `student_id` < 6 AND `score` <> 70 ORDER BY `SCORE` DESC LIMIT 3;

/*
更新major中的英语为英语文学
*/
UPDATE `student`
SET `major`='英语文学'
WHERE `major`='英语'; 

UPDATE `student`
SET `major`='物理'; -- 不加条件


UPDATE `student`
SET `major` = '生化'
WHERE `major` = '生物' OR `major` = '化学'; 

DELETE FROM `student`
WHERE `name`='小惠' AND `major`='生化';

DELETE FROM `student`
WHERE `score` < 60; -- > < >= <= = <>

SELECT *
FROM `student`
WHERE `major` in('历史','英语'); -- 使用in来进行范围搜索