CREATE TABLE IF NOT EXISTS users
(
  id serial NOT NULL PRIMARY KEY AUTO_INCREMENT,
  email character varying(255) NOT NULL UNIQUE,
  name character varying(255)
)
