DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS image;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);


CREATE TABLE `recipe` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`author_id`	INTEGER NOT NULL,
	`type`	INTEGER NOT NULL,
	`title`	TEXT,
	`filename`	TEXT,
	`url`	TEXT,
	`description`	TEXT,
	`created`	TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
  FOREIGN KEY (author_id) REFERENCES user (id)
);