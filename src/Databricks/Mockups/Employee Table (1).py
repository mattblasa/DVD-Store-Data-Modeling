# Databricks notebook source
# MAGIC %run /Users/blasa.matthew_yahoo.com#ext#@blasamatthewyahoo.onmicrosoft.com/utils/mount 

# COMMAND ----------

# MAGIC %sql 
# MAGIC SELECT * 
# MAGIC FROM dvd_objects.staff

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT sf.staff_id
# MAGIC       , sf.store_id
# MAGIC       , sf.first_name 
# MAGIC       , sf.last_name
# MAGIC       , sf.address_id 
# MAGIC       , sf.email
# MAGIC       , sf.active as Is_Active 
# MAGIC       , st.manager_staff_id as manager_id
# MAGIC       , CASE 
# MAGIC           WHEN st.manager_staff_id = sf.staff_id THEN True
# MAGIC           ELSE False 
# MAGIC           END AS Is_Manager
# MAGIC       , sf.last_update
# MAGIC FROM dvd_objects.staff sf
# MAGIC LEFT JOIN dvd_objects.store st
# MAGIC ON sf.store_id = st.store_id

# COMMAND ----------

employee_table = spark.sql('''
WITH staff_info AS (
SELECT sf.staff_id
      , sf.store_id
      , sf.first_name 
      , sf.last_name
      , sf.address_id 
      , sf.email
      , sf.active as Is_Active 
      , st.manager_staff_id as manager_id
      , CASE 
          WHEN st.manager_staff_id = sf.staff_id THEN True
          ELSE False 
          END AS Is_Manager
      , sf.last_update
FROM dvd_objects.staff sf
LEFT JOIN dvd_objects.store st
ON sf.store_id = st.store_id
)

SELECT  sf.staff_id
      , sf.store_id
      , sf.first_name 
      , sf.last_name
      , sf.address_id 
      , sf.email
      , sf.Is_Active 
       , sf.manager_id
       , sf.Is_Manager
       , ad.address
       , ad.address2
       , ct.city
       , ad.district
       , co.country
       , ad.postal_code
       , ad.phone
       , sf.last_update
       
FROM staff_info as sf
LEFT JOIN dvd_objects.address AS ad
ON ad.address_id = sf.address_id
LEFT JOIN dvd_objects.city AS ct
ON ct.city_id = ad.city_id
LEFT JOIN dvd_objects.country AS co
ON ct.country_id = co.country_id;
''')
employee_table.createOrReplaceTempView('employee')


# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM employee

# COMMAND ----------

employee_table.write.mode("overwrite").saveAsTable("test_db.employee")

# COMMAND ----------


