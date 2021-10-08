# Databricks notebook source
# MAGIC %run /Users/blasa.matthew_yahoo.com#ext#@blasamatthewyahoo.onmicrosoft.com/utils/mount 

# COMMAND ----------

# DBTITLE 1,Customer_Info 
customer_info = spark.sql('''
WITH customer_info AS (
SELECT cus.customer_id
       , cus.store_id
       , cus.address_id
       , cus.first_name
       , cus.last_name
       , cus.email
       , case 
           when cus.active = 1 then True 
           else False 
           end as is_active_customer
       , cus.create_date 
       , cus.last_update
FROM dvd_objects.customer AS cus
)

SELECT customer_info.*
      , ad.address
      , ad.address2
      , ct.city
      , ad.district
      , cou.country
      , ad.postal_code
      , ad.phone
      , ad.city_id
      , ct.country_id
FROM customer_info
LEFT JOIN dvd_objects.address AS ad 
  ON customer_info.address_id = ad.address_id
LEFT JOIN dvd_objects.city AS ct
  ON ad.city_id = ct.city_id
LEFT JOIN dvd_objects.country AS cou
  ON ct.country_id = cou.country_id
''')
customer_info.createOrReplaceTempView('customer_info')

# COMMAND ----------

customer_final = spark.sql('''
SELECT DISTINCT customer_id
      , store_id
      , address_id
      , first_name
      , last_name
      , is_active_customer
      , create_date as customer_create_date
      , last_update as last_customer_info_update
      , address
      , address2
      , city
      , district
      , country
      , postal_code
      , phone
FROM customer_info ci 
ORDER BY customer_id ASC
''')

# COMMAND ----------

customer_final.write.mode("overwrite").saveAsTable("test_db.customer")
