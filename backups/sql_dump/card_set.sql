BEGIN TRANSACTION;
--CREATE TABLE IF NOT EXISTS `card_set` (
--	`id`	INT,
--	`value`	VARCHAR ( 50 ),
--	`description`	VARCHAR ( 50 ),
--	`code`	VARCHAR ( 10 ),
--	PRIMARY KEY(`id`)
--);
INSERT INTO `set` (Id,Value,Description,Code) VALUES (0,'FinnVSJake','Finn Vs Jake','cp1'),
 (1,'BMOVSLadyRainicorn','BMO Vs Lady Rainicorn','cp2'),
 (2,'PrincessBubblegumVSLumpySpacePrincess','Princess Bubblegum Vs Lumpy Space Princess','cp3'),
 (3,'IceKingVSMarceline','Ice King Vs Marceline','cp4'),
 (4,'LemonGrabVSGunter','Lemon Grab Vs Gunter','cp5'),
 (5,'FionnaVSCake','Fionna Vs Cake','cp6'),
 (6,'DoublesTournament','Doubles Tournament','2v2'),
 (7,'HeroPack','Hero Pack','hp1'),
 (8,'ForTheGlory','For The Glory','ftg'),
 (9,'Promo','Promo','promo'),
 (10,'Kickstarter1','Kickstarter #1','ks1'),
 (11,'FlamePrincessVSFern','Flame Princess Vs Fern','cp7'),
 (12,'PrismoVSTheLich','Prismo Vs The Lich','cp8'),
 (13,'PeppermintButlerVSMagicMan','Peppermint Butler Vs Magic Man','cp9'),
 (14,'Kickstarter2','Kickstarter #2','ks2'),
 (15,'DarklandsExpansion','Darklands Expansion','dl1');
COMMIT;
