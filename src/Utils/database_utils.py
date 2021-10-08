# Databricks notebook source
def overwrite_table(database, table):
  '''
  Method overwrites table attached to cluster 
  
  Parameters: 
  
  database- name of database (string)
  table - name of table (string)
  
  Returns: 
  Overwrites table in databricks cluster
  
  '''
  mode = str(mode)
  try: 
    database.write.mode("overwrite").saveAsTable(test_db + "." + table)
  except: 
    print("Unable to overwrite table, please check for correct path")
