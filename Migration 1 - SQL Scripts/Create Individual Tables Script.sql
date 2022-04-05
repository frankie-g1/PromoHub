CREATE TABLE Creator_Table
(
	Creator_Id		int NOT NULL,
    Creator_Name    varchar(30)

);

CREATE TABLE PromoCode_Table
(
    PromoCode_Id    int NOT NULL,
    PromoCode		varchar(30),
    Creator_Id		int NOT NULL

);

CREATE TABLE Product_Table
(
    Product_Id		int NOT NULL,
    PromoCode_Id    int NOT NULL,
    Product         varchar(30)

);

CREATE TABLE WebsiteLink_Table
(            
    WebsiteLink		varchar(255),
    Product_Id      int NOT NULL

);

CREATE TABLE YouTubeLink_Table
(
    YoutubeLink		varchar(255),
    ReleaseDate     date,
    Creator_Id      int NOT NULL

);
