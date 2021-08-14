# Databricks notebook source
# MAGIC %run /Users/blasa.matthew_yahoo.com#ext#@blasamatthewyahoo.onmicrosoft.com/utils/mount 

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM dvd_objects.rental

# COMMAND ----------

# DBTITLE 1,Rental and Payment
# MAGIC %sql 
# MAGIC SELECT r.rental_id
# MAGIC       , r.rental_date
# MAGIC       , r.return_date
# MAGIC       , r.inventory_id
# MAGIC       , p.staff_id
# MAGIC       , p.customer_id
# MAGIC       , p.payment_id
# MAGIC       , p.payment_date
# MAGIC       , p.amount
# MAGIC FROM dvd_objects.payment p
# MAGIC LEFT JOIN dvd_objects.rental r
# MAGIC   ON p.rental_id = r.rental_id
# MAGIC /*LEFT JOIN dvd_objects.inventory i
# MAGIC   ON r.inventory_id = i.inventory_id */

# COMMAND ----------

rental_transactions = spark.sql('''
SELECT  DISTINCT r.rental_id
      , r.rental_date
      , r.return_date
      , r.inventory_id
      , p.staff_id
      , p.customer_id
      , p.payment_id
      , p.payment_date
      , p.amount
FROM dvd_objects.payment p
LEFT JOIN dvd_objects.rental r
ON p.rental_id = r.rental_id
''')
rental_transactions.createOrReplaceTempView('rental_transactions')

# COMMAND ----------

# MAGIC %sql 
# MAGIC SELECT  DISTINCT r.rental_id
# MAGIC       , r.rental_date
# MAGIC       , r.return_date
# MAGIC       , r.inventory_id
# MAGIC       , p.staff_id
# MAGIC       , p.customer_id
# MAGIC       , p.payment_id
# MAGIC       , p.payment_date
# MAGIC       , p.amount
# MAGIC FROM dvd_objects.payment p
# MAGIC LEFT JOIN dvd_objects.rental r
# MAGIC ON p.rental_id = r.rental_id

# COMMAND ----------

rental_transactions.write.mode("overwrite").saveAsTable("test_db.rental_transactions")

# COMMAND ----------


