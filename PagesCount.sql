CREATE TABLE pages.temp AS SELECT id, SUM(Home_Page) AS Home_Page, SUM(Product_Page) AS Product_Page, SUM(Warranty_Page) AS Warranty_Page FROM pages.input;

SELECT 'Home_Page' AS PAGE, Home_Page AS counts FROM pages.temp
UNION SELECT 'Product_Page' AS PAGE, Product_Page AS counts FROM pages.temp
UNION SELECT 'Warranty_Page' AS PAGE, Warranty_Page AS counts FROM pages.temp