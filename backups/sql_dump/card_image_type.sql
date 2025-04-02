BEGIN TRANSACTION;
--CREATE TABLE IF NOT EXISTS `card_image_type` (
--	`id`	INT,
--	`descriptor`	VARCHAR ( 50 ),
--	PRIMARY KEY(`id`)
--);
INSERT INTO `cardImageType` (Id,Descriptor) VALUES
 (0, 'xs'),
 (1,'sm'),
 (2,'rg'),
 (3,'lg')
COMMIT;
