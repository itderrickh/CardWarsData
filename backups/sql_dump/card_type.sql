BEGIN TRANSACTION;
--CREATE TABLE IF NOT EXISTS `card_type` (
--	`id`	INT,
--	`value`	VARCHAR ( 50 ),
--	PRIMARY KEY(`id`)
--);
INSERT INTO `cardType` (Id,Value) VALUES (0,'Creature'),
 (1,'Spell'),
 (2,'Building'),
 (3,'Landscape'),
 (4,'Hero'),
 (5,'Teamwork'),
 (6,'Overlord'),
 (7,'Curse'),
 (8,'Barrier');
COMMIT;
