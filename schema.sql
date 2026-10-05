DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS chats;

CREATE TABLE user (
  userid INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE chats (
  chatid INTEGER PRIMARY KEY,
  FOREIGN KEY (userid) REFERENCES user(userid)
);

CREATE TABLE messages (

)
// varbinary(max)
// work on later
// need message, time sent, chat, who,  