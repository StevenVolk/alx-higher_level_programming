-- script that creates the database hbtn_0c_0 in your MySQL server
IF NOT EXISTS (SELECT * FROM master.sys.databases WHERE name = 'hbtn_0c_0')
	CREATE hbtn_0c_0
