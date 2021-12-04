-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2021-11-23 11:54:11.795

-- tables
-- Table: Product_reviews
CREATE TABLE Product_reviews (
    Product_review_id int  NOT NULL,
    Review_id int  NOT NULL,
    Product_id int  NOT NULL,
    CONSTRAINT Product_reviews_pk PRIMARY KEY (Product_review_id)
);

-- Table: Products
CREATE TABLE Products (
    Product_id int  NOT NULL,
    Product_code int  NOT NULL,
    Product_description varchar(50)  NOT NULL,
    Product_status varchar(50)  NOT NULL,
    CONSTRAINT Products_pk PRIMARY KEY (Product_id)
);

-- Table: Rating_systems
CREATE TABLE Rating_systems (
    Rating_id int  NOT NULL,
    No_of_stars int  NOT NULL,
    Rating_description varchar(50)  NOT NULL,
    CONSTRAINT Rating_systems_pk PRIMARY KEY (Rating_id)
);

-- Table: Reviews
CREATE TABLE Reviews (
    Review_id int  NOT NULL,
    Shopper_id int  NOT NULL,
    Rating_id int  NOT NULL,
    Review_date_time  timestamp  NOT NULL,
    Review_comment varchar(50)  NOT NULL,
    CONSTRAINT Reviews_pk PRIMARY KEY (Review_id)
);

-- Table: Seller
CREATE TABLE Seller (
    Seller_id int  NOT NULL,
    Seller_account_ref int  NOT NULL,
    Seller_name varchar(25)  NOT NULL,
    Seller_address_line1 varchar(20)  NOT NULL,
    Seller_address_line2 varchar(30)  NOT NULL,
    Seller_address_line3 varchar(30)  NOT NULL,
    Seller_country varchar(15)  NOT NULL,
    Seller_post_code varchar(15)  NOT NULL,
    Seller_email_address varchar(40)  NOT NULL,
    CONSTRAINT Seller_pk PRIMARY KEY (Seller_id)
);

-- Table: Seller_reviews
CREATE TABLE Seller_reviews (
    Seller_review_id int  NOT NULL,
    Review_id int  NOT NULL,
    Seller_id int  NOT NULL,
    CONSTRAINT Seller_reviews_pk PRIMARY KEY (Seller_review_id)
);

-- Table: Shopper_Contact
CREATE TABLE Shopper_Contact (
    Shopper_id int  NOT NULL,
    Phone int  NOT NULL,
    Shoppers_Shopper_id int  NOT NULL
);

-- Table: Shopper_account
CREATE TABLE Shopper_account (
    Shopper_account_ref int  NOT NULL,
    Date_of_birth date  NOT NULL,
    Date_joined date  NOT NULL,
    Shoppers_Shopper_id int  NOT NULL
);

-- Table: Shoppers
CREATE TABLE Shoppers (
    Shopper_id int  NOT NULL,
    Shopper_first_name varchar(30)  NOT NULL,
    Shopper_surnname varchar(30)  NOT NULL,
    CONSTRAINT Shoppers_pk PRIMARY KEY (Shopper_id)
);

-- Table: productRetailerreviews
CREATE TABLE productRetailerreviews (
    Productreviewid int  NOT NULL,
    name  varchar(46)  NOT NULL,
    Message  varchar(56)  NOT NULL,
    Comments  varchar(96)  NOT NULL,
    Commentdate  varchar(12)  NOT NULL,
    likes int  NOT NULL,
    reply varchar(45)  NOT NULL,
    Products_Product_id int  NOT NULL,
    CONSTRAINT productRetailerreviews_pk PRIMARY KEY (Productreviewid)
);

-- foreign keys
-- Reference: Product_reviews_Products (table: Product_reviews)
ALTER TABLE Product_reviews ADD CONSTRAINT Product_reviews_Products
    FOREIGN KEY (Product_id)
    REFERENCES Products (Product_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Product_reviews_Reviews (table: Product_reviews)
ALTER TABLE Product_reviews ADD CONSTRAINT Product_reviews_Reviews
    FOREIGN KEY (Review_id)
    REFERENCES Reviews (Review_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Rating_systems_Reviews (table: Reviews)
ALTER TABLE Reviews ADD CONSTRAINT Rating_systems_Reviews
    FOREIGN KEY (Rating_id)
    REFERENCES Rating_systems (Rating_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Seller_reviews_Reviews (table: Seller_reviews)
ALTER TABLE Seller_reviews ADD CONSTRAINT Seller_reviews_Reviews
    FOREIGN KEY (Review_id)
    REFERENCES Reviews (Review_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Seller_reviews_Seller (table: Seller_reviews)
ALTER TABLE Seller_reviews ADD CONSTRAINT Seller_reviews_Seller
    FOREIGN KEY (Seller_id)
    REFERENCES Seller (Seller_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Shopper_Contact_Shoppers (table: Shopper_Contact)
ALTER TABLE Shopper_Contact ADD CONSTRAINT Shopper_Contact_Shoppers
    FOREIGN KEY (Shoppers_Shopper_id)
    REFERENCES Shoppers (Shopper_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Shopper_account_Shoppers (table: Shopper_account)
ALTER TABLE Shopper_account ADD CONSTRAINT Shopper_account_Shoppers
    FOREIGN KEY (Shoppers_Shopper_id)
    REFERENCES Shoppers (Shopper_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Shoppers_Reviews (table: Reviews)
ALTER TABLE Reviews ADD CONSTRAINT Shoppers_Reviews
    FOREIGN KEY (Shopper_id)
    REFERENCES Shoppers (Shopper_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: productRetailerreviews_Products (table: productRetailerreviews)
ALTER TABLE productRetailerreviews ADD CONSTRAINT productRetailerreviews_Products
    FOREIGN KEY (Products_Product_id)
    REFERENCES Products (Product_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

