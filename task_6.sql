-- task_6.sql

-- Use the alx_book_store database
USE alx_book_store;

-- Insert multiple rows into the customers table
INSERT INTO customers (customer_id, customer_name, email, address)
VALUES
    (2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness Ave.'),
    (3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness Ave.'),
    (4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness Ave.');

-- Check for the insertion of the customer with customer_id = 2
SELECT * FROM customers WHERE customer_id = 2;

-- Check for the insertion of the customer with customer_id = 3
SELECT * FROM customers WHERE customer_id = 3;

-- Check for the insertion of the customer with customer_id = 4
SELECT * FROM customers WHERE customer_id = 4;

