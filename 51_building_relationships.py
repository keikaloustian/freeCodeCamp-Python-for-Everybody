# In SQLite, the use of quotation marks or double quotes around column or table names is optional, except when using spaecs or special characters.

'''
DROP TABLE Users

CREATE TABLE "Artist" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
  "name" TEXT
)

CREATE TABLE "Album" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
  "artist_id" INTEGER,
  "title" TEXT
)

CREATE TABLE "Genre" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
  "name" TEXT
)

CREATE TABLE "Track" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
  album_id INTEGER,
  genre_id INTEGER,
  len INTEGER,
  rating INTEGER, 
  "title" TEXT,
  "count" INTEGER
)

INSERT INTO Artist (name) VALUES ('Led Zepplin');
INSERT INTO Artist (name) VALUES ('AC/DC');

INSERT INTO Genre (name) VALUES ('Rock') ;
INSERT INTO Genre (name) VALUES ('Metal');


INSERT INTO Album (title, artist_id) VALUES ('Who Made Who', 2);
INSERT INTO Album (title, artist_id) VALUES ('IV', 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Black Dog', 5, 297, 0, 2, 1) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Stairway', 5, 482, 0, 2, 1) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('About to Rock', 5, 313, 0, 1, 2) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Who Made Who', 5, 207, 0, 1, 2) ;
'''