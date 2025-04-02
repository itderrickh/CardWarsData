BEGIN TRANSACTION;
--CREATE TABLE IF NOT EXISTS `landscape` (
--	`id`	INT,
--	`value`	VARCHAR ( 50 ),
--	`description`	VARCHAR ( 50 ),
--	PRIMARY KEY(`id`)
--);
INSERT INTO `landscape` (Id,Value,Description) VALUES (0,'BluePlains','Blue Plains'),
 (1,'Cornfield','Cornfield'),
 (2,'UselessSwamp','Useless Swamp'),
 (3,'SandyLands','SandyLands'),
 (4,'NiceLands','NiceLands'),
 (5,'IcyLands','IcyLands'),
 (6,'Rainbow','Rainbow'),
 (7,'LavaFlats','LavaFlats');
COMMIT;
