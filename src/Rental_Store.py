# Databricks notebook source
# MAGIC %run /Users/blasa.matthew_yahoo.com#ext#@blasamatthewyahoo.onmicrosoft.com/utils/mount 

# COMMAND ----------

# MAGIC %sql 
# MAGIC SELECT * 
# MAGIC FROM dvd_objects.store

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM dvd_objects.store 

# COMMAND ----------

# MAGIC %sql 
# MAGIC WITH store_add AS (
# MAGIC SELECT s.store_id
# MAGIC 	, s.manager_staff_id
# MAGIC 	, s.address_id 
# MAGIC 	, a.city_id
# MAGIC 	, a.address
# MAGIC 	, a.address2
# MAGIC 	, a.district
# MAGIC 	, a.postal_code
# MAGIC 	, a.phone
# MAGIC FROM dvd_objects.store as s
# MAGIC LEFT JOIN dvd_objects.address as a
# MAGIC ON s.address_id = a.address_id
# MAGIC )
# MAGIC 
# MAGIC 
# MAGIC SELECT sa.store_id
# MAGIC 	,sa.manager_staff_id  
# MAGIC 	,sa.address
# MAGIC 	,c.city
# MAGIC 	,sa.address2
# MAGIC 	,sa.district
# MAGIC 	,sa.postal_code
# MAGIC 	,sa.phone
# MAGIC 	,cc.country
# MAGIC FROM store_add as sa
# MAGIC LEFT JOIN dvd_objects.city as c
# MAGIC ON c.city_id = sa.city_id
# MAGIC LEFT JOIN dvd_objects.country as cc 
# MAGIC ON c.country_id = cc.country_id;

# COMMAND ----------

# MAGIC %sql 
# MAGIC WITH store_add AS (
# MAGIC SELECT s.store_id
# MAGIC 	, s.manager_staff_id
# MAGIC 	, s.address_id 
# MAGIC 	, a.city_id
# MAGIC 	, a.address
# MAGIC 	, a.address2
# MAGIC 	, a.district
# MAGIC 	, a.postal_code
# MAGIC 	, a.phone
# MAGIC FROM dvd_objects.store as s
# MAGIC LEFT JOIN dvd_objects.address as a
# MAGIC ON s.address_id = a.address_id
# MAGIC )
# MAGIC 
# MAGIC SELECT *
# MAGIC FROM store_add as sa
# MAGIC LEFT JOIN dvd_objects.staff sf
# MAGIC ON sa.store_id = sf.store_id

# COMMAND ----------

# DBTITLE 1,Count Number of Employees Per Store
# MAGIC %sql 
# MAGIC WITH store_add AS (
# MAGIC SELECT s.store_id
# MAGIC 	, s.manager_staff_id
# MAGIC 	, s.address_id 
# MAGIC 	, a.city_id
# MAGIC 	, a.address
# MAGIC 	, a.address2
# MAGIC 	, a.district
# MAGIC 	, a.postal_code
# MAGIC 	, a.phone
# MAGIC FROM dvd_objects.store as s
# MAGIC LEFT JOIN dvd_objects.address as a
# MAGIC ON s.address_id = a.address_id
# MAGIC )
# MAGIC 
# MAGIC SELECT sa.store_id as store_id
# MAGIC   ,COUNT(sf.staff_id) as total_staff
# MAGIC   ,COUNT( DISTINCT sa.manager_staff_id) as total_supervisors
# MAGIC FROM store_add as sa
# MAGIC LEFT JOIN dvd_objects.staff sf
# MAGIC ON sa.store_id = sf.store_id
# MAGIC GROUP BY sa.store_id
# MAGIC ORDER BY COUNT(sf.staff_id);

# COMMAND ----------

# MAGIC %sql 
# MAGIC WITH store_add AS (
# MAGIC SELECT s.store_id
# MAGIC 	, s.manager_staff_id
# MAGIC 	, s.address_id 
# MAGIC 	, a.city_id
# MAGIC 	, a.address
# MAGIC 	, a.address2
# MAGIC 	, a.district
# MAGIC 	, a.postal_code
# MAGIC 	, a.phone
# MAGIC FROM dvd_objects.store as s
# MAGIC LEFT JOIN dvd_objects.address as a
# MAGIC ON s.address_id = a.address_id
# MAGIC )
# MAGIC 
# MAGIC SELECT DISTINCT sa.store_id
# MAGIC 	,sa.manager_staff_id  
# MAGIC 	,sa.address
# MAGIC 	,c.city
# MAGIC 	,sa.address2
# MAGIC 	,sa.district
# MAGIC 	,sa.postal_code
# MAGIC 	,sa.phone
# MAGIC 	,cc.country
# MAGIC     --,sf.staff_id
# MAGIC FROM store_add as sa
# MAGIC LEFT JOIN dvd_objects.city as c
# MAGIC   ON c.city_id = sa.city_id
# MAGIC LEFT JOIN dvd_objects.country as cc 
# MAGIC   ON c.country_id = cc.country_id
# MAGIC LEFT JOIN dvd_objects.staff sf
# MAGIC   ON sa.store_id = sf.store_id

# COMMAND ----------

# DBTITLE 1,Store and Address
rental_store = spark.sql('''
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
''')
rental_store.createOrReplaceTempView('store_address')

# COMMAND ----------

# DBTITLE 1,Rental_Store
rental_store2 = spark.sql('''
SELECT sa.store_id
	,sa.manager_staff_id  
	,sa.address
	,c.city
	,sa.address2
	,sa.district
	,sa.postal_code
	,sa.phone
	,cc.country
FROM store_address as sa
LEFT JOIN dvd_objects.city as c
ON c.city_id = sa.city_id
LEFT JOIN dvd_objects.country as cc 
ON c.country_id = cc.country_id;
''')
rental_store2.createOrReplaceTempView('rental_store')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM rental_store

# COMMAND ----------

rental_store.write.mode("overwrite").saveAsTable("test_db.rental_store")

# COMMAND ----------


