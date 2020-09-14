# Assignment 14 - Tableau

## Background

After completing project 2 and going through the process of making many visualizations (especially map visualizations), I was relieved to find tableau and anxious to learn how to make dashboards and stories!

The purpose of this assignment was to use Citi Bike Data from https://s3.amazonaws.com/tripdata/index.html to make visualizations and produce dashboards that would hopefully provide some business insight. The final tableau workbook should contain at least two dashboards and a story.

Link to workbook - https://public.tableau.com/profile/eric.pacheco4032#!/vizhome/CitiBike_15941439152520/Story

* The first step was to get all the data from the citibike website, where each month of data was contained in a csv. I decided to only use the past years data from 2019 to represent recent trends. Each monthly file when downloaded came in a zip file, and because of this a python script was created to extract the csv from each zip file and place the csv into the monthly_data folder.

* After compiling all the monthly data, the next step was to load all these csvs into pandas and create one single csv which could be loaded into tableau. A couple formatting techniques were used to make sure the final csv was correctly compiled.

* After loading the compiled csv into tableau, the all the visualizations were made including a maps dashboard showing popularity of stations over the year, an age demographics dashboard showing gender and age statistics

* After completing the individual dashboards a final tableau story was made to include all of the dashboards

### Copyright

Data Boot Camp © 2019. All Rights Reserved.
