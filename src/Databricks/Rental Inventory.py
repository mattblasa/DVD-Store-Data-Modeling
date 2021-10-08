# Databricks notebook source
# MAGIC %run /Users/blasa.matthew_yahoo.com#ext#@blasamatthewyahoo.onmicrosoft.com/utils/mount 

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

rental_inventory.write.mode("overwrite").saveAsTable("test_db.rental_inventory_final")

# COMMAND ----------


