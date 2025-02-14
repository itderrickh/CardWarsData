/*
CREATE Card Types
*/
CREATE TABLE IF NOT EXISTS card_type (
    id INT PRIMARY KEY,
    value VARCHAR(50)
);

INSERT INTO card_type (id, value) VALUES
(0, 'Creature'),
(1, 'Spell'),
(2, 'Building'),
(3, 'Landscape'),
(4, 'Hero'),
(5, 'Teamwork');

/*
CREATE Landscape
*/
CREATE TABLE IF NOT EXISTS landscape (
    id INT PRIMARY KEY,
    value VARCHAR(50),
    description VARCHAR(50)
);

INSERT INTO landscape (id, value, description) VALUES
(0, 'BluePlains', 'Blue Plains'),
(1, 'Cornfield', 'Cornfield'),
(2, 'UselessSwamp', 'Useless Swamp'),
(3, 'SandyLands', 'SandyLands'),
(4, 'NiceLands', 'NiceLands'),
(5, 'IcyLands', 'IcyLands'),
(6, 'Rainbow', 'Rainbow');

/*
CREATE Card Sets
*/
CREATE TABLE IF NOT EXISTS card_set (
    id INT PRIMARY KEY,
    value VARCHAR(50),
    description VARCHAR(50),
    code VARCHAR(10)
);

INSERT INTO card_set (id, value, description, code) VALUES
(0, 'FinnVSJake', 'Finn Vs Jake', 'cp1'),
(1, 'BMOVSLadyRainicorn', 'BMO Vs Lady Rainicorn', 'cp2'),
(2, 'PrincessBubblegumVSLumpySpacePrincess', 'Princess Bubblegum Vs Lumpy Space Princess', 'cp3'),
(3, 'IceKingVSMarceline', 'Ice King Vs Marceline', 'cp4'),
(4, 'LemonGrabVSGunter', 'Lemon Grab Vs Gunter', 'cp5'),
(5, 'FionnaVSCake', 'Fionna Vs Cake', 'cp6'),
(6, 'DoublesTournament', 'Doubles Tournament', '2v2'),
(7, 'HeroPack', 'Hero Pack', 'hp1'),
(8, 'ForTheGlory', 'For The Glory', 'ftg'),
(9, 'Promo', 'Promo', 'promo'),
(10, 'Kickstarter1', 'Kickstarter #1', 'ks1'),
(11, 'CommunityCards', 'Community Cards', 'cwe');

/*
CREATE Revisions
*/
CREATE TABLE IF NOT EXISTS card_revision (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    revisionNumber INT,
    cardId INT,
    name varchar(255) NOT NULL,
	typeId INT,
    ability varchar(255),
    setId INT,
    landscapeId INT,
    cost INT,
    attack INT,
    defense INT,
    FOREIGN KEY (setId) REFERENCES card_set(id),
    FOREIGN KEY (typeId) REFERENCES card_type(id),
    FOREIGN KEY (cardId) REFERENCES card(id),
    FOREIGN KEY (landscapeId) REFERENCES landscape(id)
);

/*
CREATE Cards
*/
CREATE TABLE IF NOT EXISTS card (
	id INTEGER PRIMARY KEY
);

/*
CREATE Card Image Type
*/
CREATE TABLE IF NOT EXISTS card_image_type (
    id INT PRIMARY KEY,
    descriptor VARCHAR(50)
);

INSERT INTO card_image_type (id, descriptor) VALUES
(1, 'sm'),
(2, 'rg'),
(3, 'lg');

/*
CREATE Card Images
*/
CREATE TABLE IF NOT EXISTS card_image (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    revisionId INT,
    cardImageTypeId INT,
    imageUrl VARCHAR(255),
    FOREIGN KEY (revisionId) REFERENCES card_revision(id),
    FOREIGN KEY (cardImageTypeId) REFERENCES card_image_type(id)
);