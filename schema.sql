DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS chats;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE chats (

);
// varbinary(max)
// work on later
// need message, time sent, chat, who,  