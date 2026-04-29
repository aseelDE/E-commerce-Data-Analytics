CREATE OR REPLACE TABLE `e-commerce-de-project.ecommerce_analytics.user_purchase_summary`
AS (
  SELECT
    u.id,
    u.name.firstname,
    u.name.lastname,
    COUNT(DISTINCT c.id) AS total_orders,
    SUM(product.quantity) AS total_items_purchased
  FROM `ecommerce_raw.ecommercerawusers` AS u
  LEFT JOIN `ecommerce_raw.ecommercerawcarts` AS c
    ON u.id = c.userID
  CROSS JOIN UNNEST(c.products) AS product
  GROUP BY u.id, u.name.firstname, u.name.lastname
)
