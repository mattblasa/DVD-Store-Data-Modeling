# Databricks notebook source
# MAGIC %run /Users/blasa.matthew_yahoo.com#ext#@blasamatthewyahoo.onmicrosoft.com/utils/mount 

# COMMAND ----------


spark.sql('''
CREATE DATABASE IF NOT EXISTS dvd_objects
''')

# COMMAND ----------

rental_store.write.mode("overwrite").saveAsTable("test_db.rental_store")

# COMMAND ----------

spark.sql('''
CREATE OR REPLACE table test_db.rental_store AS 

WITH store_add AS (
SELECT s.store_id
	, s.manager_staff_id
	, s.address_id 
	, a.city_id
	, a.address
	, a.address2
	, a.district
	, a.postal_code
	, a.phone
FROM dvd_objects.store as s
LEFT JOIN dvd_objects.address as a
ON s.address_id = a.address_id
)

SELECT DISTINCT sa.store_id
	,sa.manager_staff_id  
	,sa.address
	,c.city
	,sa.address2
	,sa.district
	,sa.postal_code
	,sa.phone
	,cc.country
    --,sf.staff_id
FROM store_add as sa
LEFT JOIN dvd_objects.city as c
  ON c.city_id = sa.city_id
LEFT JOIN dvd_objects.country as cc 
  ON c.country_id = cc.country_id
LEFT JOIN dvd_objects.staff sf
  ON sa.store_id = sf.store_id
''')
