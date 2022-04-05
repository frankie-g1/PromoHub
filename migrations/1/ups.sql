 CREATE USER 'root'@'%' IDENTIFIED BY '123';
 
 
 
 GRANT ALL PRIVILEGES ON *.* TO 'test'@'%' WITH GRANT OPTION;


 CREATE TABLE PromoHub
(
	Creator_Id		varchar(30),
    PromoCode		varchar(30),
    Product_Id		varchar(30),
    Release_Date	date,
    WebsiteLink		varchar(255),
    YoutubeLink		varchar(255)

);

