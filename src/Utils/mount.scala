// Databricks notebook source
val containerName = "dvd"
val storageAccountName = "kaeshidou"
val sas = <SAS Token> // SAS token for the container - removed for security reasons
val url = "wasbs://" + containerName + "@" + storageAccountName + ".blob.core.windows.net/"
val config = "fs.azure.sas." + containerName + "." + storageAccountName + ".blob.core.windows.net"

// COMMAND ----------

//Prints error message if the directory is not already mounted 
try
{
  dbutils.fs.mount(
  source = url ,
  mountPoint = "/mnt/dvd",
  extraConfigs = Map(config -> sas))
} catch {
  case e: Exception => {
    println("Exception: Directory already mounted.")
  }
}
