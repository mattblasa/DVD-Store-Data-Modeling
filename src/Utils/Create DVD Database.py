# Databricks notebook source
# MAGIC %run /Users/blasa.matthew_yahoo.com#ext#@blasamatthewyahoo.onmicrosoft.com/utils/mount 

# COMMAND ----------

# DBTITLE 1,Create Database 
# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS dvd_objects

# COMMAND ----------

import pyspark
from pyspark.sql.functions import to_date, col

#LOAD CSV FILE - INCLUDES 5M ROWS
actor = (spark.read.format('csv')
           .option('header', 'True')
           .option("inferSchema", "true")
           .load('/mnt/dvd/actor.csv'))
display(actor)

# COMMAND ----------

# DBTITLE 1,Create Actors Table 
# MAGIC %sql
# MAGIC create table if not exists
# MAGIC dvd_objects.actor
# MAGIC (
# MAGIC       actor_id INT,
# MAGIC       first_name STRING,
# MAGIC       last_name STRING,
# MAGIC       last_update TIMESTAMP
# MAGIC )
# MAGIC using csv
# MAGIC options (
# MAGIC path '/mnt/dvd/actor.csv',
# MAGIC sep ',',
# MAGIC header true
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Create Address Table
# MAGIC %sql
# MAGIC create table if not exists
# MAGIC dvd_objects.address
# MAGIC (
# MAGIC       address_id INT,
# MAGIC       address STRING,
# MAGIC       address2 STRING,
# MAGIC       district STRING,
# MAGIC       city_id INT,
# MAGIC       postal_code INT,
# MAGIC       phone INT, 
# MAGIC       last_update TIMESTAMP
# MAGIC )
# MAGIC using csv
# MAGIC options (
# MAGIC path '/mnt/dvd/address.csv',
# MAGIC sep ',',
# MAGIC header true
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Create Category Table
# MAGIC %sql
# MAGIC create table if not exists
# MAGIC dvd_objects.category
# MAGIC (
# MAGIC       category_id INT
# MAGIC       , name STRING
# MAGIC       , last_update STRING
# MAGIC )
# MAGIC using csv
# MAGIC options (
# MAGIC path '/mnt/dvd/category.csv',
# MAGIC sep ',',
# MAGIC header true
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Create City Table
# MAGIC %sql
# MAGIC create table if not exists
# MAGIC dvd_objects.city
# MAGIC (
# MAGIC       city_id INT
# MAGIC       , city STRING
# MAGIC       , country_id INT
# MAGIC       , last_update STRING
# MAGIC )
# MAGIC using csv
# MAGIC options (
# MAGIC path '/mnt/dvd/city.csv',
# MAGIC sep ',',
# MAGIC header true
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Create County Table
# MAGIC %sql
# MAGIC create table if not exists
# MAGIC dvd_objects.country
# MAGIC (
# MAGIC       country_id INT
# MAGIC       , country STRING
# MAGIC       , last_update STRING
# MAGIC )
# MAGIC using csv
# MAGIC options (
# MAGIC path '/mnt/dvd/country.csv',
# MAGIC sep ',',
# MAGIC header true
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Create Customer Table
# MAGIC %sql
# MAGIC create table if not exists
# MAGIC dvd_objects.customer
# MAGIC (
# MAGIC       customer_id INT
# MAGIC       , store_id INT
# MAGIC       , first_name STRING
# MAGIC       , last_name STRING
# MAGIC       , email STRING
# MAGIC       , address_id INT
# MAGIC       , activebool STRING
# MAGIC       , create_date STRING
# MAGIC       , last_update STRING
# MAGIC       , active INT
# MAGIC )
# MAGIC using csv
# MAGIC options (
# MAGIC path '/mnt/dvd/customer.csv',
# MAGIC sep ',',
# MAGIC header true
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Create Film Table
# MAGIC %sql
# MAGIC create table if not exists
# MAGIC dvd_objects.film
# MAGIC (
# MAGIC       film_id INT
# MAGIC       , title STRING
# MAGIC       , description STRING
# MAGIC       , release_year INT
# MAGIC       , language_id INT
# MAGIC       , rental_duration INT
# MAGIC       , rental_rate FLOAT
# MAGIC       , length INT
# MAGIC       , replacement_cost FLOAT
# MAGIC       , rating STRING
# MAGIC       , last_update STRING
# MAGIC       , special_features STRING
# MAGIC       , fulltext STRING
# MAGIC )
# MAGIC using csv
# MAGIC options (
# MAGIC path '/mnt/dvd/film.csv',
# MAGIC sep ',',
# MAGIC header true
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Create Film_actor Table
# MAGIC %sql
# MAGIC create table if not exists
# MAGIC dvd_objects.film_actor
# MAGIC (
# MAGIC       actor_id INT
# MAGIC       , film_id INT
# MAGIC       , last_update STRING
# MAGIC )
# MAGIC using csv
# MAGIC options (
# MAGIC path '/mnt/dvd/film_actor.csv',
# MAGIC sep ',',
# MAGIC header true
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Create Film_category Table
# MAGIC %sql
# MAGIC create table if not exists
# MAGIC dvd_objects.film_category
# MAGIC (
# MAGIC       film_id INT
# MAGIC       , category_id INT
# MAGIC       , last_update STRING
# MAGIC )
# MAGIC using csv
# MAGIC options (
# MAGIC path '/mnt/dvd/film_category.csv',
# MAGIC sep ',',
# MAGIC header true
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Create Inventory Table
# MAGIC %sql
# MAGIC create table if not exists
# MAGIC dvd_objects.inventory
# MAGIC (
# MAGIC       inventory_id INT
# MAGIC       , film_id INT
# MAGIC       , store_id INT
# MAGIC       , last_update STRING
# MAGIC )
# MAGIC using csv
# MAGIC options (
# MAGIC path '/mnt/dvd/inventory.csv',
# MAGIC sep ',',
# MAGIC header true
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Create Language Table
# MAGIC %sql
# MAGIC create table if not exists
# MAGIC dvd_objects.language
# MAGIC (
# MAGIC       language_id INT
# MAGIC       , name STRING
# MAGIC       , last_update STRING
# MAGIC )
# MAGIC using csv
# MAGIC options (
# MAGIC path '/mnt/dvd/language.csv',
# MAGIC sep ',',
# MAGIC header true
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Create Payment Table
# MAGIC %sql
# MAGIC create table if not exists
# MAGIC dvd_objects.payment
# MAGIC (
# MAGIC       payment_id INT
# MAGIC       , customer_id INT
# MAGIC       , staff_id INT
# MAGIC       , rental_id INT
# MAGIC       , amount FLOAT
# MAGIC       , payment_date STRING
# MAGIC 
# MAGIC )
# MAGIC using csv
# MAGIC options (
# MAGIC path '/mnt/dvd/payment.csv',
# MAGIC sep ',',
# MAGIC header true
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Create Rental Table
# MAGIC %sql
# MAGIC create table if not exists
# MAGIC dvd_objects.rental
# MAGIC (
# MAGIC       rental_id INT
# MAGIC       , rental_date STRING
# MAGIC       , inventory_id INT
# MAGIC       , customer_id INT
# MAGIC       , return_date STRING
# MAGIC       , staff_id INT
# MAGIC       , last_update STRING
# MAGIC 
# MAGIC )
# MAGIC using csv
# MAGIC options (
# MAGIC path '/mnt/dvd/rental.csv',
# MAGIC sep ',',
# MAGIC header true
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Create Staff Table
# MAGIC %sql
# MAGIC create table if not exists
# MAGIC dvd_objects.staff
# MAGIC (
# MAGIC       staff_id INT
# MAGIC       , first_name STRING
# MAGIC       , last_name STRING
# MAGIC       , address_id INT
# MAGIC       , email STRING
# MAGIC       , store_id INT
# MAGIC       , active STRING
# MAGIC       , username STRING
# MAGIC       , password STRING
# MAGIC       , last_update STRING
# MAGIC 
# MAGIC )
# MAGIC using csv
# MAGIC options (
# MAGIC path '/mnt/dvd/staff.csv',
# MAGIC sep ',',
# MAGIC header true
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Create Store Table
# MAGIC %sql
# MAGIC create table if not exists
# MAGIC dvd_objects.store
# MAGIC (
# MAGIC       store_id INT
# MAGIC       , manager_staff_id INT
# MAGIC       , address_id INT
# MAGIC       , last_update STRING
# MAGIC 
# MAGIC )
# MAGIC using csv
# MAGIC options (
# MAGIC path '/mnt/dvd/store.csv',
# MAGIC sep ',',
# MAGIC header true
# MAGIC )

# COMMAND ----------


