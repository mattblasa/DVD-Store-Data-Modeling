# DVD Store Data Modeling
 
# Introduction

In this project, we have queried the DVD Rental database. The database was originally contained within a file  called xxxx.gz. The database holds information about a company with stores that rent movie DVDs. There are 15 total tables in the database, which are related to each other.  For this project, we created data models to: 
- Cut costs and achieve faster time to value for business analysts
- Understand and improve business processes that are commonly used
- Reduce complexity and risk for reporting. 

ETL (Extract Transform Load) processes will be addressed in the next phase of the project. 

# Business Scenario

The DVD rental database exists without a business context. For this project, we will assume the following objectives: 
- DVD Rental Business would like to migrate their data to the cloud 
- Tables and data infrastructure must be recreated in the cloud 
- Business must be able to access models from the cloud

We will also assume the following issues:
- Need to walk through multiple to tables to get business insights. 
- Business processes are slowed down to get insights
- Business needs objects that address its use cases 


# Use Cases
I also assumed we would be interviewing stakeholders for use cases. Use cases will address their common business needs and answers to their questions. 

-  As a sales analyst, I would like to know the address, country and phone number associated to each store. 
-  As a HR representative, I would like to have an easy access to employees' basic information. 
-  As a Customer Retention Representative, I would like to know the address, region, city, and country of a customer. 
-  As a store manager, I would like to know the transactions by store, and the number of items we have in inventory. 
-  As a store manager, I would like to know about movies in our current inventory, replacement costs, duration of rental, and rental rate.

# Data Governance and Data Management Notes

# Tools Used 
### _Testing Queries:_
- PgAdmin (Postgres SQL) 

### _Modeling and Transformation:_ 
- Azure Databricks (Production Environment)
- PySpark (Database Creation, Table Ingestion, Schema Creation)
- SparkSQL (Model Creation) 

### _Data Ingestion_
- Scala, Accessing data from Azure storage accounts (Mounting a storage account) 
- Azure Data Factory, batching and creating ids for batches uploaded to my Azure SQL Server 
