# Databricks notebook source
# MAGIC %run /Users/blasa.matthew_yahoo.com#ext#@blasamatthewyahoo.onmicrosoft.com/utils/mount 

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT fc.film_id
# MAGIC       , fc.category_id
# MAGIC       , c.name
# MAGIC FROM dvd_objects.film_category fc
# MAGIC LEFT JOIN dvd_objects.category c
# MAGIC ON fc.category_id = c.category_id

# COMMAND ----------

# DBTITLE 1,Add Category and Language Name
# MAGIC %sql 
# MAGIC WITH category as(
# MAGIC SELECT fc.film_id
# MAGIC       , fc.category_id
# MAGIC       , c.name
# MAGIC FROM dvd_objects.film_category fc
# MAGIC LEFT JOIN dvd_objects.category c
# MAGIC ON fc.category_id = c.category_id
# MAGIC )
# MAGIC 
# MAGIC SELECT f.film_id
# MAGIC       , f.title
# MAGIC       , f.description as film_descrip
# MAGIC       , f.release_year
# MAGIC       , f.language_id
# MAGIC       , f.length as film_length
# MAGIC       , f.rating
# MAGIC       , c.name as genre
# MAGIC       , l.name as orignal_language
# MAGIC FROM dvd_objects.film f
# MAGIC LEFT JOIN category c
# MAGIC   ON f.film_id = c.film_id
# MAGIC LEFT JOIN dvd_objects.language l 
# MAGIC   ON f.language_id = l.language_id

# COMMAND ----------

rental_movies = spark.sql('''
WITH category as(
SELECT fc.film_id
      , fc.category_id
      , c.name
FROM dvd_objects.film_category fc
LEFT JOIN dvd_objects.category c
ON fc.category_id = c.category_id
)

SELECT f.film_id
      , f.title
      , f.description as film_descrip
      , f.release_year
      , f.language_id
      , f.length as film_length
      , f.rating
      , c.name as genre
      , l.name as original_language
FROM dvd_objects.film f
LEFT JOIN category c
  ON f.film_id = c.film_id
LEFT JOIN dvd_objects.language l 
  ON f.language_id = l.language_id
''')
rental_movies.createOrReplaceTempView('rental_movies')

# COMMAND ----------

# MAGIC %sql 
# MAGIC SELECT * 
# MAGIC FROM rental_movies

# COMMAND ----------

rental_movies.write.mode("overwrite").saveAsTable("test_db.rental_movies")

# COMMAND ----------


