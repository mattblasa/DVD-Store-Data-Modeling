
CREATE TABLE store_staff
(staff_id serial PRIMARY KEY, 
 first_name varchar(128),
 last_name varchar(128),
 address_id int,
 email varchar(128),
 active varchar(45),
 username varchar(128),
 staff_password varchar(128),
last_update date
);

COPY store_staff
FROM 'C:\Users\blasa\Documents\Data Science\Projects - Portfolio\Data Modeling\DVD_Rental\store_staff.csv'
DELIMITER ','
CSV HEADER