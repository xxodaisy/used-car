# Database for Used Car Sales Website
SQL Relational Database implementation of Used Car Sales Website

# Backgroud Project
The project I worked on came from Pacmann's BI Engineer course. This project was created to learn how to build a database for a project 
application and understand the data retrieval process is one of the tasks of Software & Data Engineering.

In this project, I was given the task of building a relational database for a website that offers used car sales. 

An overview of this project is that anyone can offer their products (used cars) in the form of advertisements and
potential buyers can search by several categories.

# Designing the Database
- Mission Statement
- Create Table Structure
- Determine Table Relationship
- Business Rules
- Determine Views
- ER Diagram
- Querying of create table


## Mission Statement
Mission statement is an explanation of the purpose of the database and the problems it aims to solve

Database for Used Car Sales Website aims to:
- Manage the data of used car sellers and buyers by facilitating a secure and efficient online platform
- Manage the advertising feature for used cars
- Manage the bidding feature for buyers who are interested in a car by ensuring user data and product information can be managed properly

## Create Table Structure
- Create the required table and fields
- Determine the key
- Create a description of the function of each table
  
All that is required:
- Sellers can sell used cars and advertise them on the website
- Sellers can advertise their used car more than once
- Buyers can buy used cars
- Buyers can make used car price offers to sellers through advertisement posted on the website

So, all that is required is seller, buyer, ads and also bid data

Here are the details of creating a table for Database Used Car Sales Website

| tabel Sellers | tabel Buyers |
| --- | --- |
| to store car seller information | to store car buyer information |
| seller_id: VARCHAR(255) NOT NULL PRIMARY KEY,  Auto Increment | buyer_id: VARCHAR(255) NOT NULL PRIMARY KEY, Auto Increment |
|name: VARCHAR(100), full name of seller |name: VARCHAR(100), full name of buyer
|email: VARCHAR(100), email of seller (unique) |email: VARCHAR(100), email of buyer (unique)
|password: VARCHAR(255), password of seller |password: VARCHAR(255), password of buyer
|contact_number: VARCHAR(20), contact number of seller |contact_number: VARCHAR(20), contact number of buyer
|location: VARCHAR(100), location of seller |location: VARCHAR(100), location of buyer
|registration_date: TIMESTAMP, time of seller registration  |registration_date: TIMESTAMP, time of buyer registration
|status: ENUM(’Active’, ‘Inactive’), account status of seller |status: ENUM(’Active’, ‘Inactive’), account status of buyer
|rating: DECIMAL(10, 2), average rating from buyers |purchase_history: TEXT, purchase history record |
|number_of_sales: INTEGER, total number of sales | 

| tabel Ads | tabel Bids |
| --- | --- |
| to store ads information | to store bids information |
| ad_id: VARCHAR(255) NOT NULL PRIMARY KEY, Auto Increment | bid_id: VARCHAR(255) NOT NULL PRIMARY KEY Auto Increment |
| seller_id: VARCHAR(255), Foreign Key, referes to the Sellers table |  ad_id: VARCHAR(255), FOREIGN KEY, refers to the Ads table |
| title: VARCHAR(200), ad title | buyer_id: VARCHAR(255), Foreign Key, referes to the Buyers table |
| description: TEXT, description of the car |  bid_amount: DECIMAL (12,2), the number of bids submitted by buyers |
| car_brand: ENUM, car brands | status: ENUM(’Pending’, ‘Accepted’, ‘Rejected’), status of bid |
| models:  VARCHAR(100), car models | bid_date: TIMESTAMP, offer time |
| body_car_type: ENUM(’MPV’, ‘SUV’, ‘Van’, ‘Sedan’, ‘Hatcback’), type of car body | interaction_type: ENUM(’View’, ‘Bid’, Contract’), type of interaction |
| transmission: ENUM(’Manual’, ‘Automatic’) type of car transmission | bid_detail: TEXT, detail of bid |
| year_of_manufacture: YEAR, year of car manufacture  |
| color: VARCHAR(30), color of car |
| mileage: INTEGER, the distance traveled in kilometers |
| engine: ENUM, machine spesification |
| price: DECIMAL(12,2), offered price |
| is_negotiable: BOOLEAN, is the price negotiable |
| created_at: TIMESTAMP, time the ad was created |
| updated_at: TIMESTAMP, time the ad was last updated |
| status: ENUM(’Active’, ‘Sold’, ‘Expired’), status of ad |
| image: TEXT, store the url or path to the car image |  

## Determine Table Relationship
- Sellers to ads → one to many
each seller can create multiple ads

- Ads to bids → one to many
each ad can create multiple bids

- Buyers to bids → one to many
each buyer can create multiple bids

## Business Rules
Business rules are rules that are implemented by the company and must be reflected in the database.

There are several types of business rules:

1. Field-specific business rules → rules for fields in a table
2. Relationship-specific business rules → rules applied between tables (relationships between tables)

How to apply business rules to a database → using constraints

In the project above, determine the business rules as follows:

Each column of each table cannot be empty or not null

1. User Data
    - To sell and buy cars, users (sellers and buyers) must complete their data such as name, contact, and domicile location.
2. Product offerings
    - User sellers can offer their products through advertisements that will be displayed by the website.
    - User sellers can offer more than one used car product.
3. Car search
    - Each buyer can search for cars offered based on the seller's user location, car brand and car body type.
4. Price Offer
    - Prospective buyers can offer product prices if they are interested in a car. this is if the seller allows the bargain feature

## Determine Views

- Create views or virtual tables where we can get information from multiple tables or between views easily.
- Some commands need to be done regularly → views help the commands to be called without having to write the query continuously

In the project above, determine views as follows:

1. Calculate total sales for each month
    - Provide sales report by month for sales trend analysis - calculate sales amount
    - Total revenue from sales each month
2. Buyers who place repeat orders
    - Identify buyers who make purchases more than once
    - Analyze the total revenue generated from repeat buyers.
3. Car brands that sell every month
    - Provide data on car brands that are selling every month
    - Analyze total revenue per car brand to see which brand generates the highest revenue each month
4. Which car body types are popular each month
    - Provides information about the type of car body that is most frequently searched or sold.
    - Analyze revenue by car body type to find out which type generates the highest revenue
5. Total Revenue per month
    - Create a special view to calculate the total monthly revenue from all sales.
  
## ER Diagram
![image](https://github.com/user-attachments/assets/c0cfdd72-0bc6-4df9-9650-858671e37795)

## Querying of create tables
```sql
-- create enum types for sellers table
CREATE TYPE e_status AS enum('Active', 'Inactive');

--create table sellers 
CREATE TABLE sellers(
	seller_id VARCHAR(255) PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	email VARCHAR(100) NOT NULL,
	password VARCHAR(255) NOT NULL,
	contact_number VARCHAR(20) UNIQUE NOT NULL,
	location VARCHAR(100) NOT NULL,
	registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	status e_status,
	rating DECIMAL(10,2) NOT NULL,
	number_of_sales INTEGER NOT NULL
);

-- rename data type seller_id
ALTER TABLE sellers
ALTER COLUMN seller_id TYPE VARCHAR(255);
```

```sql
-- create enum types for buyers table
CREATE TYPE e_status AS enum('Active', 'Inactive');

CREATE TABLE buyers(
	buyer_id VARCHAR(255) PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	email VARCHAR(100) UNIQUE NOT NULL,
	password VARCHAR(255) NOT NULL,
	contact_number VARCHAR(20) UNIQUE NOT NULL,
	location VARCHAR(100) NOT NULL,
	registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	status e_status,
	purchase_history TEXT NOT NULL
);
```
```sql
--create enum types for table ads
CREATE TYPE e_brand AS enum('Toyota','Honda', 'Daihatsu', 'Suzuki', 'Nissan', 'BMW', 'Mercedes-Benz');
CREATE TYPE e_model AS ENUM('Avanza', 'Yaris', 'Innova', 'Fortuner', 'Brio', 'Jazz', 'Mobilio', 'CR-V', 'HR-V', 'Ertiga', 'Swift' 'Jimny', 'Karimun Wagon R', 'Xenia', 'Ayla', 'Terios', ' Sigra', 'Grand Livina', 'March', 'X-Trail', '3 Series', 'X1', 'C-Class', 'E-Class');
create type e_engine AS ENUM('1.3L 4-Cyl', '1.5L 4-Cyl', '1.0L 3-Cyl', '1.2L 4-Cyl', '2.0L 4-Cyl', '2.5L 4-Cyl', '2.0L 4-Cyl Turbo', '3.0L 6-Cyl Turbo', '1.5L Turbo', '2.0L Turbo');
CREATE TYPE e_body_car AS ENUM('MPV', 'SUV', 'Van', 'Sedan', 'Hatchback');
CREATE TYPE e_transmission AS ENUM('Manual', 'Automatic');
CREATE TYPE e_status_ads AS ENUM('Active', 'Sold', 'Expired');

CREATE TABLE ads(
	ad_id VARCHAR(255) PRIMARY KEY,
	seller_id VARCHAR(255),
	title VARCHAR(200) UNIQUE NOT NULL,
	description TEXT NOT NULL,
	car_brand e_brand,
	models VARCHAR(255),
	body_car_type e_body_car,
	transmission e_transmission,
	year_of_manufacture INTEGER NOT NULL,
	color VARCHAR(30) NOT NULL,
	mileage INTEGER NOT NULL,
	engine VARCHAR(255),
	price DECIMAL(12,2) NOT NULL,
	is_negotiable BOOLEAN NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	status e_status_ads,
	image TEXT NOT NULL,
	
	CONSTRAINT fk_seller_id FOREIGN KEY (seller_id)
	REFERENCES sellers(seller_id)
);

ALTER TABLE ads
ALTER COLUMN description TYPE TEXT;

ALTER TABLE ads
ALTER COLUMN car_brand TYPE e_brand;
```
```sql
-- Create ENUM types for bids table
CREATE TYPE e_statuses AS ENUM('Pending', 'Accepted', 'Rejected');
CREATE TYPE e_interaction AS ENUM('View', 'Bid', 'Contract');

-- Create table bids
CREATE TABLE bids (
    bid_id VARCHAR(255) PRIMARY KEY,
    ad_id VARCHAR(255),
    buyer_id VARCHAR(255),
    bid_amount DECIMAL(10,2) NOT NULL,
    bid_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status_bid e_statuses,
    interaction_type e_interaction,
    bid_detail TEXT NOT NULL,
    CONSTRAINT fk_ad_id FOREIGN KEY (ad_id) REFERENCES ads(ad_id),
    CONSTRAINT fk_buyer_id FOREIGN KEY (buyer_id) REFERENCES buyers(buyer_id)
);

ALTER TABLE bids
ALTER COLUMN bid_amount TYPE DECIMAL(12,2);

ALTER TABLE bids
ALTER COLUMN status_bid TYPE VARCHAR(20);
```

**Now with docker!**

# Installing Dependencies
There are two condition;
## If you already build
1. If you use docker, just `docker-compose up -d --build` in order to re-build the container
## If you haven't
1. Just `docker-compose up -d` since this is the first time we are going to build the container

# How to Docker
1. Make sure docker has been installed in your machine then,
2. go and `docker-compose up -d` and wait untill docker has build and run your container
3. go ahead and do `docker ps` and take a look what ID's is the container
4. execute this `docker exec -it [container_id] sh` and you will be greeted with container's sh
5. do `ls` to make sure there are .pys inside the container
6. all what you have to do just go and play around, have fun!

## How to Access Container sh
1. First of all, check container's id via `docker ps` and take a look `my-python-container` id is
2. then do this `docker exec -it [container_id] sh` to open sh inside container
3. check `ls` what inside, and then
4. have fun!
