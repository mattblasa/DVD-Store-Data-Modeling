# Databricks notebook source
# MAGIC %run /Users/blasa.matthew_yahoo.com#ext#@blasamatthewyahoo.onmicrosoft.com/utils/mount 

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM dvd_objects.inventory

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM dvd_objects.film

# COMMAND ----------

# DBTITLE 1,Film Table Complete
# MAGIC %sql
# MAGIC SELECT f.film_id
# MAGIC       , f.title
# MAGIC       , f.description
# MAGIC       , f.release_year
# MAGIC       , l.name as original_lang
# MAGIC       , f.length
# MAGIC       , f.replacement_cost
# MAGIC       , f.rental_duration
# MAGIC       , f.rental_rate
# MAGIC       , f.rating
# MAGIC       , f.last_update
# MAGIC       , REPLACE(TRANSLATE(f.special_features,'{}""',' '),"'","") as special_features
# MAGIC FROM dvd_objects.film f
# MAGIC LEFT JOIN dvd_objects.language l
# MAGIC ON f.language_id = l.language_id

# COMMAND ----------

# DBTITLE 1,CTE Inventory
# MAGIC %sql
# MAGIC WITH film_final AS (
# MAGIC SELECT f.film_id
# MAGIC       , f.title
# MAGIC       , f.description
# MAGIC       , f.release_year
# MAGIC       , l.name as original_lang
# MAGIC       , f.length
# MAGIC       , f.replacement_cost
# MAGIC       , f.rental_duration
# MAGIC       , f.rental_rate
# MAGIC       , f.rating
# MAGIC       , f.last_update
# MAGIC       , REPLACE(TRANSLATE(f.special_features,'{}""',' '),"'","") as special_features
# MAGIC FROM dvd_objects.film f
# MAGIC LEFT JOIN dvd_objects.language l
# MAGIC ON f.language_id = l.language_id
# MAGIC )
# MAGIC 
# MAGIC SELECT DISTINCT i.inventory_id
# MAGIC       , ff.film_id
# MAGIC       , i.store_id
# MAGIC       , ff.title
# MAGIC       , ff.description
# MAGIC       , ff.release_year
# MAGIC       , ff.original_lang
# MAGIC       , ff.length
# MAGIC       , ff.replacement_cost
# MAGIC       , ff.rental_duration
# MAGIC       , ff.rental_rate
# MAGIC       , ff.rating
# MAGIC       , i.last_update
# MAGIC       , ff.special_features
# MAGIC FROM dvd_objects.inventory i 
# MAGIC LEFT JOIN film_final ff
# MAGIC ON i.film_id = ff.film_id
# MAGIC ORDER BY inventory_id ASC

# COMMAND ----------

# DBTITLE 1,Rental Inventory
rental_inventory = spark.sql('''
WITH film_final AS (
SELECT f.film_id
      , f.title
      , f.description
      , f.release_year
      , l.name as original_lang
      , f.length
      , f.replacement_cost
      , f.rental_duration
      , f.rental_rate
      , f.rating
      , f.last_update
      , REPLACE(TRANSLATE(f.special_features,'{}""',' '),"'","") as special_features
FROM dvd_objects.film f
LEFT JOIN dvd_objects.language l
ON f.language_id = l.language_id
)

SELECT DISTINCT i.inventory_id
      , ff.film_id
      , i.store_id
      , ff.title
      , ff.description
      , ff.release_year
      , ff.original_lang
      , ff.length
      , ff.replacement_cost
      , ff.rental_duration
      , ff.rental_rate
      , ff.rating
      , i.last_update
      , ff.special_features
FROM dvd_objects.inventory i 
LEFT JOIN film_final ff
ON i.film_id = ff.film_id
ORDER BY inventory_id ASC
''')
rental_inventory.createOrReplaceTempView('rental_inventory')

# COMMAND ----------

# MAGIC %sql
# MAGIC select *
# MAGIC from rental_inventory

# COMMAND ----------

rental_inventory.write.mode("overwrite").saveAsTable("test_db.rental_inventory_final")

# COMMAND ----------


