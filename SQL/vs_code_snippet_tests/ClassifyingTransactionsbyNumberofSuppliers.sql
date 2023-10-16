
SELECT `name`, `param_list`, `comment` 
FROM `mysql`.`proc` WHERE `db`=DATABASE() AND `type` = 'FUNCTION';

