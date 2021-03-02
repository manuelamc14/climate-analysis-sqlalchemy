## Dependencies

* SQL Alchemy
* Pandas
* Flask 

## Description

This project aims to use Python and SQLAlchemy to do fundamental climate analysis and data exploration of the climate database. All of the following analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

The project has two sessions:

 1. Analysis and Exploration
 
SQLAlchemy was used to “create_engine” to connect the SQLite database to the Jupyter notebook. Then SQLAlchemy “automap_base()” was used to reflect the tables into classes and save a reference to those classes called Station and Measurement.
 
A query was designed to retrieve the last 12 months of precipitation data and select only the date and precipitation values to analyze the precipitation. The results were loaded to Pandas DataFrame, and the date column was set as the index. The results were plotted. 

![ScreenShot](https://github.com/manuelamc14/climate-analysis-sqlalchemy/blob/main/Images/pcr_august_2017.png)

For the station analysis, a query was designed to calculate the total number of stations, followed by another query that intended to find the most activated station to plot the last 12 months of temperature observation data (TOBS) for this station.
 
 ![ScreenShot](https://github.com/manuelamc14/climate-analysis-sqlalchemy/blob/main/Images/temperature_frequency.png)
 
 2. Flask APP
A Flask API was designed to retrieve the following information:

Routes:
 - /
Home page.
List all routes that are available.

- /api/v1.0/precipitation
Return a JSON list of dates and the precipitation information.

- /api/v1.0/stations
Return a JSON list of stations from the dataset.

- /api/v1.0/tobs

Return a JSON list of temperature observations (TOBS) for the previous year of the most activate station. 

- /api/v1.0/<start> and /api/v1.0/<start>/<end>

Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
When given the start only,  the app calculates TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

## Instructions

* To access to the app, run "app.py" and open your local browser. 

![ScreenShot](https://github.com/manuelamc14/climate-analysis-sqlalchemy/blob/main/Images/flask_app.png)

![ScreenShot](https://github.com/manuelamc14/climate-analysis-sqlalchemy/blob/main/Images/flask_nutrition_route.png)



