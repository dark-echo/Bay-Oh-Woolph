--
-- File generated with SQLiteStudio v3.1.1 on Fri Feb 24 21:02:26 2017
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: rank
CREATE TABLE rank (
    rankId     INTEGER       PRIMARY KEY AUTOINCREMENT,
    rankName   VARCHAR (250),
    pointValue INTEGER
);

INSERT INTO rank (
                     rankId,
                     rankName,
                     pointValue
                 )
                 VALUES (
                     146724317785358337,
                     'Officer',
                     8
                 );

INSERT INTO rank (
                     rankId,
                     rankName,
                     pointValue
                 )
                 VALUES (
                     146725461727117314,
                     'Cadet',
                     0
                 );

INSERT INTO rank (
                     rankId,
                     rankName,
                     pointValue
                 )
                 VALUES (
                     236544208545120256,
                     'Squadron Lieutenant',
                     90
                 );

INSERT INTO rank (
                     rankId,
                     rankName,
                     pointValue
                 )
                 VALUES (
                     282699878897811466,
                     'Chief Petty Officer',
                     15
                 );

INSERT INTO rank (
                     rankId,
                     rankName,
                     pointValue
                 )
                 VALUES (
                     282699926230532098,
                     'Warrant Officer',
                     25
                 );

INSERT INTO rank (
                     rankId,
                     rankName,
                     pointValue
                 )
                 VALUES (
                     282699976151269376,
                     'Ensign',
                     40
                 );

INSERT INTO rank (
                     rankId,
                     rankName,
                     pointValue
                 )
                 VALUES (
                     282700000629358605,
                     'Lieutenant',
                     65
                 );

INSERT INTO rank (
                     rankId,
                     rankName,
                     pointValue
                 )
                 VALUES (
                     282700054798663691,
                     'Lieutenant Commander',
                     100
                 );

INSERT INTO rank (
                     rankId,
                     rankName,
                     pointValue
                 )
                 VALUES (
                     282700120091262976,
                     'Post Commander',
                     150
                 );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
