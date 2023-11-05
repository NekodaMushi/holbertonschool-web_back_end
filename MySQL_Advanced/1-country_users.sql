-- create users table
-- attributes are id email & name
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users
(
  id serial NOT NULL PRIMARY KEY AUTO_INCREMENT,
  email character varying(255) NOT NULL,
  name character varying(255),
  country ENUM('US','CO','TN') NOT NULL,
  UNIQUE (email)
)
