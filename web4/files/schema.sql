PRAGMA foreign_keys = ON;

CREATE TABLE skins(
    skinid TEXT PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    price INTEGER NOT NULL DEFAULT 0 CHECK(price >= 0),
    description TEXT NOT NULL,
    image TEXT NOT NULL
);

CREATE TABLE secretskins(
    skinid TEXT PRIMARY KEY,
    description TEXT NOT NULL,
    image TEXT NOT NULL
);

INSERT INTO skins VALUES('333', 'Dumpling', 79, 'Darryl Loves Some Xiao Long Bao', 'https://static.wikia.nocookie.net/brawlstars/images/3/33/Darryl_Skin-Dumpling.png');
INSERT INTO skins VALUES('ee0', 'Cupcake', 149, 'Cupcake CandyLand Darryl!!! Mandyyyyyyyys Candyyyyyyy', 'https://static.wikia.nocookie.net/brawlstars/images/e/e0/Darryl_Skin-Cupcake.png');
INSERT INTO skins VALUES('116', 'Omega Box', 0, '4 BILLION TAKEDOWNS!', 'https://static.wikia.nocookie.net/brawlstars/images/1/16/Darryl_Skin-Omega_Box.png');
INSERT INTO skins VALUES('bb9', 'Mascot', 79, 'Violent soccer mom', 'https://static.wikia.nocookie.net/brawlstars/images/b/b9/Darryl_Skin-Mascot.png');
INSERT INTO skins VALUES('666', 'Default', 0, 'Yo ho ho ho ho!', 'https://static.wikia.nocookie.net/brawlstars/images/6/66/Darryl_Skin-Default.png');
INSERT INTO skins VALUES('aa9', 'Mega Box', 0, 'You got pwned by a pirate.', 'https://static.wikia.nocookie.net/brawlstars/images/a/a9/Darryl_Skin-Mega_Box.png');
INSERT INTO skins VALUES('881', 'Crash Test', 1499, 'Pit Stop Emergency ft Darryl', 'https://static.wikia.nocookie.net/brawlstars/images/8/81/Darryl_Skin-Crash_Test.png');
INSERT INTO skins VALUES('fff', 'True Silver', 1079, 'Im not made of money, goddammit', 'https://static.wikia.nocookie.net/brawlstars/images/f/ff/Darryl_Skin-True_Silver.png');
INSERT INTO skins VALUES('339', 'True Gold', 2689, 'IM GOLD IM GOLD IM GOLDEN WOOOO', 'https://static.wikia.nocookie.net/brawlstars/images/3/39/Darryl_Skin-True_Gold.png');
INSERT INTO skins VALUES('660', 'D4R-RY1', 169, '77687920796F7520776173746520796F75722074696D65206F6E2074686973', 'https://static.wikia.nocookie.net/brawlstars/images/6/60/Darryl_Skin-D4R-RY1.png');
