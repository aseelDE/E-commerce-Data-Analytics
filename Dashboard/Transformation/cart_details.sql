CREATE OR REPLACE TABLE `e-commerce-de-project.ecommerce_analytics.cart_details` AS
(
  SELECT 
    c.id AS cart_id,
    c.userId,
    c.date,
    product.productId,
    p.title,
    p.category,
    p.price,
    product.quantity,
    p.price * product.quantity AS total_price
  FROM `ecommerce_raw.ecommercerawcarts` AS c
  CROSS JOIN UNNEST(c.products) AS product
  LEFT JOIN `ecommerce_raw.ecommercerawproducts` AS p 
    ON product.productId = p.id
)