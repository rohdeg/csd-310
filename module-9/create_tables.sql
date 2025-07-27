CREATE TABLE employee (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50)
);

CREATE TABLE customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone VARCHAR(25),
    address VARCHAR(255)
);

CREATE TABLE trip (
    trip_id INT AUTO_INCREMENT PRIMARY KEY,
    trip_name VARCHAR(50),
    destination VARCHAR(50),
    region VARCHAR(50),
    start_date DATE,
    end_date DATE,
    planned_by INT,
    FOREIGN KEY (planned_by) REFERENCES employee(employee_id)
);

CREATE TABLE booking (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    trip_id INT,
    booking_date DATE,
    health_checklist_reviewed BOOLEAN DEFAULT 0,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (trip_id) REFERENCES trip(trip_id)
);

CREATE TABLE equipment (
    equipment_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    type VARCHAR(50),
    status VARCHAR(50),
    purchase_date DATE
);

CREATE TABLE transaction (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    equipment_id INT,
    transaction_type VARCHAR(50),
    transaction_booking_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id)
);

CREATE TABLE marketing_campaign (
    campaign_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    start_date DATE,
    end_date DATE,
    target_region VARCHAR(50),
    managed_by INT,
    FOREIGN KEY (managed_by) REFERENCES employee(employee_id)
);

CREATE TABLE campaign_recipient (
    campaign_id INT,
    customer_id INT,
    sent_date DATE,
    PRIMARY KEY (campaign_id, customer_id),
    FOREIGN KEY (campaign_id) REFERENCES marketing_campaign(campaign_id),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

-- insert six rows of sample data into tables --
INSERT INTO employee (first_name, last_name, email) VALUES
('Blythe', 'Timmerson', 'blythe@outland.com'),
('Jim', 'Ford', 'jim@outland.com'),
('John', 'MacNell', 'john@outland.com'),
('Duke', 'Marland', 'duke@outland.com'),
('Anita', 'Gallegos', 'anita@outland.com'),
('Dimitrios', 'Stravopolous', 'dimitrios@outland.com'),
('Mei', 'Wong', 'mei@outland.com');


INSERT INTO customer (first_name, last_name, phone, address) VALUES
('Luis', 'Cruz', '555-555-5554', '100 A St'),
('Natasha', 'Foreman', '555-555-5555', '200 B Ln'),
('Breanna', 'Gorham', '555-555-5556', '300 C Ct'),
('Garrett', 'Rohde', '555-555-5557', '400 D Ave'),
('John', 'Smith', '555-555-5558', '500 E Blvd'),
('Jane', 'Doe', '555-555-5559', '600 F Way');

INSERT INTO trip (trip_name, destination, region, start_date, end_date, planned_by) VALUES
('Sahara Adventure', 'Morocco', 'Africa', '2025-08-01', '2025-08-11', 3),
('Himalayan Adventure', 'Nepal', 'Asia', '2025-09-01', '2025-09-11', 4),
('Balkan Adventure', 'Croatia', 'Europe', '2025-10-01', '2025-10-11', 3),
('Savanna Adventure', 'Kenya', 'Africa', '2025-11-01', '2025-11-11', 4),
('Thai Adventure', 'Thailand', 'Asia', '2025-12-01', '2025-12-11', 3),
('Alpine Adventure', 'Greece', 'Europe', '2026-01-01', '2026-01-11', 4);

INSERT INTO booking (customer_id, trip_id, booking_date, health_checklist_reviewed) VALUES
(1, 1, '2025-07-01', TRUE),
(2, 2, '2025-08-01', TRUE),
(3, 3, '2025-09-01', TRUE),
(4, 4, '2025-10-01', TRUE),
(5, 5, '2025-11-01', TRUE),
(6, 6, '2025-12-01', FALSE);

INSERT INTO equipment (name, type, status, purchase_date) VALUES
('Tent', 'Camping', 'Available', '2020-01-01'),
('Sleeping Bag', 'Camping', 'Available', '2021-01-01'),
('Water Filter', 'Tool', 'Available', '2025-02-01'),
('Hiking Boots', 'Shoes', 'Damaged', '2022-01-01'),
('Compass', 'Navigation', 'Lost', '2018-01-01'),
('Backpack', 'Gear', 'Available', '2019-01-01');

INSERT INTO transaction (customer_id, equipment_id, transaction_type, transaction_booking_date, amount) VALUES
(1, 1, 'Rental', '2025-07-01', 20.00),
(2, 2, 'Rental', '2025-08-01', 40.00),
(3, 3, 'Purchase', '2025-09-01', 60.00),
(4, 4, 'Purchase', '2025-10-01', 50.00),
(5, 5, 'Rental', '2024-06-01', 30.00),
(6, 6, 'Purchase', '2024-07-11', 25.00);

INSERT INTO marketing_campaign (name, start_date, end_date, target_region, managed_by) VALUES
('Africa Awaits', '2025-06-01', '2025-06-30', 'Africa', 5),
('Asia Adventure', '2025-07-01', '2025-07-31', 'Asia', 5),
('Explore Europe', '2025-08-01', '2025-08-31', 'Europe', 5),
('Spring Trek Deals', '2024-03-01', '2024-03-31', 'Asia', 5),
('Summer Expedition', '2024-04-01', '2024-04-30', 'Africa', 5),
('Fall Hiking Europe', '2024-05-01', '2024-05-31', 'Europe', 5);

INSERT INTO campaign_recipient (campaign_id, customer_id, sent_date) VALUES
(1, 1, '2025-06-01'),
(2, 2, '2025-07-01'),
(3, 3, '2025-08-01'),
(4, 4, '2025-09-01'),
(5, 5, '2025-10-01'),
(6, 6, '2025-11-01');