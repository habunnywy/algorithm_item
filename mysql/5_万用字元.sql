-- wildcards 万用字元  % 代表多个字元， _ 代表一个字元

-- 1. 取得手机尾数是335的客户
SELECT *
FROM `client`
WHERE `phone` LIKE '%335';

-- 2. 取得手机开头是254的客户
SELECT *
FROM `client`
WHERE `phone` LIKE '254%';

-- 3. 取得手机号中间是354的客户
SELECT *
FROM `client`
WHERE `phone` LIKE '%354%';

-- 4. 取得姓艾的客户
SELECT *
FROM `client`
WHERE `client_name` LIKE '艾%';

-- 5. 取得生日在12月的员工
SELECT *
FROM `employee`
WHERE `birth_data` LIKE '____-12%';