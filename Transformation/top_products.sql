CREATE OR REPLACE TABLE `e-commerce-de-project.ecommerce_analytics.top_products` AS
(
    SELECT id, title, category, price, rating.rate, rating.count FROM `ecommerce_raw.ecommercerawproducts`
ORDER BY rating.rate DESC
)


