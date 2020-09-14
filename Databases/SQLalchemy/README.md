# Assignment 7 -SQLalchemy Challenge

## Background

SQLalchemy was a great intro to ORMs and how python is able to connect with our databases. This was a topic which was a bit more difficult to implement, however I'm happy because I can now confidently use this tool!

![Surf](Images/surfs-up.png)

This assignment required us to look into climate analysis for weather station in Hawaii.

### Step 1 - Climate Analysis and Exploration

First step was define a start and end day for a potential trip and retrieve the corresponding climate information for those days. SQL alchemy was used to connect to the sqlite databases provided and loaded into a jupyter notebook.

Precipitation analysis was conducted on the data starting with a SQLalchemy query to retrieve the last 12 months of precipitation data. The date and prcp values were selected and loaded into a pandas dataframe. This was sorted by date and plotted. 

![Precipitation](Images/precipitation.png)

Station analysis was then conducted through several queries

* Query to calculate total number of station

* Query to find most active stations (highest number of observations)

* query for last 12 months of temperature (TOBS) data was plotted on histogram with 12 bins

![histogram](Images/station-histogram.png)

### Step 2 - Climate App

Created a flask app to return the data of serveral queries 

* / route - homepage that lists all routes of the app

* /api/v1.0/precipitation - returns JSON representation of date and prcp data

* /api/v1.0/stations - return JSON list of temperature observations for the previous year

* /api/v1.0/2017-07-07 - returns JSON temperature data for 2017-07-07

* /api/v1.0/2017-07-17:2017-07-26 - return JSON temperature data for 2017-07-17 to 2017-07-26

### Copyright
Trilogy Education Services © 2019. All Rights Reserved.


