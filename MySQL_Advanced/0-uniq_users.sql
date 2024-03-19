
CREATE TABLE IF NOT EXISTS users (
	id int NOT NULL AUTO_INCREMENT,PRIMARY KEY(id),
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255),
)
