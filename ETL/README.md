# Assignment 9 - ETL Project

## Background

This week the focus was on the process of extracting, transforming, and loading data. Each of these individual skills we have learned, and now the task was to set up a pipeline flow which handled the data starting from extraction/gathering, all the way to loading the data into a database.

This was a two person group project, and my group decided to focus on oil metrics (supply, demand, reserves, crude/brent prices etc.) This project was meant to collect a wide range of oil metrics in a single database which could produce some actionable insight into future oil trends with further analysis.

### Extract

* The brent and crude oil historical prices were retreived as csvs from the eia.gov website, dating back to as early as 1987

* OPEC reports were used to extract oil rig counts, storage, and demand for 2017-2020

* Tables for consumption, production, and proven oil reserves were web scraped from wikepedia, each of these tables from varying years

### Transform

* The brent and crude oil csvs were straightforward and required no cleaning, following the formatting of data and oil price for that date

* The OPEC reports were in excel sheets that were not formatted correctly for database loading, and had to be transformed by loading these sheets into pandas and isolating specific columns needed using iloc, dropping columns and null values, and resetting the indexes appropriately

* The webscraped data was loaded into pandas using the .to_html functionality which takes the url given and transforms any tables on the page into pandas dataframes
 * The tables contained many null values which needed to formatted with drop_na
 * Many entries in the tables had extra tags that were irrelevant to the oil information needed and had to removed with string splitting 

### Load

* Loading the data into a database was performed using a python script and SQLalchemy which would create a new database named "oil" if this database did not exist previously. 

* Using the os.listdir() method to extract all the full file names from our transformed data csvs, the script will check for the file extension to make sure they are csvs and not corrupt. These csvs will then be loaded into pandas dataframes

* These loaded dataframes will then be loaded into sql using the .to_sql function

### Copyright
Coding Boot Camp © 2018. All Rights Reserved.
 
