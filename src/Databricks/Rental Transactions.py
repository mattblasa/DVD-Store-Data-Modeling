# Databricks notebook source
# MAGIC %run /Users/blasa.matthew_yahoo.com#ext#@blasamatthewyahoo.onmicrosoft.com/utils/mount 

# COMMAND ----------

# MAGIC %run /Users/blasa.matthew_yahoo.com#ext#@blasamatthewyahoo.onmicrosoft.com/utils/database_utils

# COMMAND ----------

spark.sql('''
CREATE DATABASE IF NOT EXISTS dvd_objects
''')

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

rental_transactions.write.mode("overwrite").saveAsTable("test_db.rental_transactions")
