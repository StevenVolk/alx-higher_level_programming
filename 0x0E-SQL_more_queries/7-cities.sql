-- script that creates the database hbtn_0d_usa and the table cities
CREATE TABLE `hbtn_0d_usa`.cities(id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL FOREIGN KEY REFERENCES states(id),
	name VARCHAR(256) NOT NULL)
