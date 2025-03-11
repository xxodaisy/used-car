DELETE from ads;

DELETE from buyers;

DELETE from sellers;

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

rename data type seller_id
ALTER TABLE sellers
ALTER COLUMN seller_id TYPE VARCHAR(255);

-- select * from sellers

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

-- select * from sellers;

ALTER TABLE ads
ALTER COLUMN description TYPE TEXT;

ALTER TABLE ads
ALTER COLUMN car_brand TYPE e_brand;