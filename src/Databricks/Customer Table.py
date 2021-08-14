# Databricks notebook source
# MAGIC %run /Users/blasa.matthew_yahoo.com#ext#@blasamatthewyahoo.onmicrosoft.com/utils/mount 

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM dvd_objects.customer

# COMMAND ----------

# DBTITLE 1,Build from Customer 
# MAGIC %sql
# MAGIC SELECT cus.customer_id
# MAGIC        , cus.store_id
# MAGIC        , cus.address_id
# MAGIC        , cus.first_name
# MAGIC        , cus.last_name
# MAGIC        , cus.email
# MAGIC        , case 
# MAGIC            when cus.active = 1 then True 
# MAGIC            else False 
# MAGIC            end as is_active_customer
# MAGIC        , cus.create_date 
# MAGIC        , cus.last_update
# MAGIC 
# MAGIC FROM dvd_objects.customer AS cus

# COMMAND ----------

# DBTITLE 1,test CTE
# MAGIC %sql
# MAGIC WITH customer_info AS (
# MAGIC SELECT cus.customer_id
# MAGIC        , cus.store_id
# MAGIC        , cus.address_id
# MAGIC        , cus.first_name
# MAGIC        , cus.last_name
# MAGIC        , cus.email
# MAGIC        , case 
# MAGIC            when cus.active = 1 then True 
# MAGIC            else False 
# MAGIC            end as is_active_customer
# MAGIC        , cus.create_date 
# MAGIC        , cus.last_update
# MAGIC FROM dvd_objects.customer AS cus
# MAGIC )
# MAGIC 
# MAGIC SELECT *
# MAGIC FROM customer_info

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT ad.address
# MAGIC       , ad.address2
# MAGIC       , ad.district
# MAGIC       , ad.postal_code
# MAGIC       , ad.phone
# MAGIC FROM dvd_objects.address AS ad

# COMMAND ----------

# MAGIC %sql
# MAGIC WITH customer_info AS (
# MAGIC SELECT cus.customer_id
# MAGIC        , cus.store_id
# MAGIC        , cus.address_id
# MAGIC        , cus.first_name
# MAGIC        , cus.last_name
# MAGIC        , cus.email
# MAGIC        , case 
# MAGIC            when cus.active = 1 then True 
# MAGIC            else False 
# MAGIC            end as is_active_customer
# MAGIC        , cus.create_date 
# MAGIC        , cus.last_update
# MAGIC FROM dvd_objects.customer AS cus
# MAGIC )
# MAGIC 
# MAGIC SELECT customer_info.*
# MAGIC       , ad.address
# MAGIC       , ad.address2
# MAGIC       , ct.city
# MAGIC       , ad.district
# MAGIC       , cou.country
# MAGIC       , ad.postal_code
# MAGIC       , ad.phone
# MAGIC       , ad.city_id
# MAGIC       , ct.country_id
# MAGIC FROM customer_info
# MAGIC LEFT JOIN dvd_objects.address AS ad 
# MAGIC   ON customer_info.address_id = ad.address_id
# MAGIC LEFT JOIN dvd_objects.city AS ct
# MAGIC   ON ad.city_id = ct.city_id
# MAGIC LEFT JOIN dvd_objects.country AS cou
# MAGIC   ON ct.country_id = cou.country_id

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

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM customer_info

# COMMAND ----------

# MAGIC %sql 
# MAGIC SELECT DISTINCT customer_id
# MAGIC       , store_id
# MAGIC       , address_id
# MAGIC       , first_name
# MAGIC       , last_name
# MAGIC       , is_active_customer
# MAGIC       , create_date as customer_create_date
# MAGIC       , last_update as last_customer_info_update
# MAGIC       , address
# MAGIC       , address2
# MAGIC       , city
# MAGIC       , district
# MAGIC       , country
# MAGIC       , postal_code
# MAGIC       , phone
# MAGIC FROM customer_info ci 
# MAGIC ORDER BY customer_id ASC

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

# COMMAND ----------


