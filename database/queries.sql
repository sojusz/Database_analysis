best selling products:

SELECT products.productName, products.buyPrice, SUM(orderdetails.quantityOrdered) AS
sold_product's_quantity, COUNT(orderdetails.quantityOrdered)*products.buyPrice AS
product's_revenue FROM orderdetails JOIN products ON
orderdetails.productCode=products.productCode GROUP BY products.productName ORDER BY
SUM(orderdetails.quantityOrdered) DESC;


products with the biggest revenue:

SELECT products.productName, products.buyPrice, SUM(orderdetails.quantityOrdered) AS
sold_product's_quantity, SUM(orderdetails.quantityOrdered)*products.buyPrice AS
product's_revenue FROM orderdetails JOIN products ON
orderdetails.productCode=products.productCode GROUP BY products.productName ORDER BY
SUM(orderdetails.quantityOrdered)*products.buyPrice DESC;


total revenue:

SELECT SUM(quantityOrdered*priceEach) AS "total revenue" FROM orderdetails;


average order value:

SELECT AVG(total_order_value) AS average_order_value
FROM (
    SELECT orderNumber, SUM(quantityOrdered * priceEach) AS total_order_value
    FROM orderdetails GROUP BY orderNumber
) AS order_totals;


month's revenue:

SELECT 
    YEAR(orders.orderDate) AS year_num,
    MONTHNAME(orders.orderDate) AS month_name, 
    SUM(orderdetails.quantityOrdered * orderdetails.priceEach) AS month_revenue
FROM orderdetails
JOIN orders ON orderdetails.orderNumber = orders.orderNumber 
GROUP BY YEAR(orders.orderDate), MONTH(orders.orderDate), MONTHNAME(orders.orderDate)
ORDER BY year_num, MONTH(orders.orderDate);


top 10 customers:

SELECT customers.customerName, SUM(orderdetails.quantityOrdered*orderdetails.priceEach) AS
money_spent FROM customers JOIN orders ON customers.customerNumber=orders.customerNumber JOIN
orderdetails ON orders.orderNumber=orderdetails.orderNumber GROUP BY customerName ORDER BY
SUM(orderdetails.quantityOrdered*orderdetails.priceEach) DESC LIMIT 10;
