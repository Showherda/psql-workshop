CREATE TABLE "Customer" (
  "CustomerID" serial,
  "CustomerName" varchar,
  "CustomerContact" varchar,
  "CustomerEmail" varchar,
  PRIMARY KEY ("CustomerID")
);

CREATE TABLE "Product" (
  "ProductID" serial,
  "ProductName" varchar,
  "ProductDescription" varchar,
  "ProductQuantity" int,
  "ProductPrice" decimal,
  PRIMARY KEY ("ProductID")
);

CREATE TABLE "Transaction" (
  "TransactionID" serial,
  "CustomerID" int,
  "ProductID" int,
  "DiscountRate" decimal,
  PRIMARY KEY ("TransactionID")
);

INSERT INTO "Customer" ("CustomerName", "CustomerContact", "CustomerEmail")
VALUES ('John Doe', '123-456-7890', 'john@example.com'),
       ('Jane Smith', '987-654-3210', 'jane@example.com'),
       ('David Lee', '456-789-0123', 'david@example.com');

INSERT INTO "Product" ("ProductName", "ProductDescription", "ProductQuantity", "ProductPrice")
VALUES ('Laptop', 'High-performance laptop', 10, 999.99),
       ('Smartphone', 'Latest smartphone model', 20, 599.99),
       ('Tablet', 'Lightweight tablet', 15, 299.99);

INSERT INTO "Transaction" ("CustomerID", "ProductID", "DiscountRate")
VALUES (1, 1, 0.1),  -- John Doe purchases Laptop with 10% discount
       (2, 2, 0.05), -- Jane Smith purchases Smartphone with 5% discount
       (3, 3, 0.0);  -- David Lee purchases Tablet with no discount

INSERT INTO "Customer" ("CustomerName", "CustomerContact", "CustomerEmail")
VALUES ('Harry Maguire', '123-456-7890', 'harry@example.com');

UPDATE "Product"
SET "ProductQuantity" = 15
WHERE "ProductID" = 1;