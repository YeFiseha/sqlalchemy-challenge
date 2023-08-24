# sqlalchemy-challenge
Climate analysis about Honolulu Hawaii 

# Context
As we prepare to treat ourselves to a long holiday vacation in Honolulu, Hawaii – we are doing a climate analysis about the area to help with the trip planning.

For the climate analysis and data exploration, we used -
•	the provided data files [climate_starter.ipynb] and  [hawaii.sqlite]
•	SQLAlchemy [create_engine()] function to connect to the SQLite database
•	SQLAlchemy automap_base() function to reflect our tables into classes and saved the references to the classes named station and measurement
•	SQLAlchemy session to link Python to the database. 

We conducted two analyses:
1.	precipitation analysis
2.	station analysis

# Precipitation Analysis Findings:
	the most recent date in the dataset,
	using the most recent date, the previous 12 months [one year] precipitation data is obtained, organized, and plotted,
	summary statistics of the precipitation data is generated.

# Station Analysis Findings:
1.	total number of stations in the dataset are calculated,

2.	the most-active stations (that is, the stations that have the most rows) are identified,
	stations and their observation counts are listed in descending order.
	station id with the greatest number of observations is identified.

3.	lowest, highest, and average temperatures of the most-active station id are calculated,

4.	previous 12 months of temperature observation (TOBS) data are obtained,
	station with the greatest number of observations is identified.
	the previous 12 months of TOBS data for that station are obtained.
	the results are plotted as a histogram with bins=12.

# Design Climate APP
After the initial analysis was completed, Flask API is designed based on the queries already developed. The following routes are created by using Flask:

Routes
•	/
o	Home page.
o	List of all routes that are available.

•	/api/v1.0/precipitation
o	query results are converted to a dictionary using date as the key and prcp as the value.
o	JSON representation of the dictionary is obtained.

•	/api/v1.0/stations
o	JSON list of all stations from the dataset is obtained.

•	/api/v1.0/tobs
o	dates and the temperature observations of the most active station for the last year of data is obtained.
o	JSON list of temperature observations (TOBS) for the last year is obtained.

•	/api/v1.0/<start> and /api/v1.0/<start>/<end>
o	JSON list of the minimum, average, and maximum temperature are obtained for a given start or start-end range.
o	When provided with the start date only, calculate TMIN, TAVG, and TMAX for all the dates greater than and equal to the start date.
o	When provided with the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

# References
1.	The ‘Resources’ folder includes the provided data files [climate_starter.ipynb] and  [hawaii.sqlite].
2.	The ‘climate_starter.ipynb’ file includes the precipitation analysis and station analysis.
3.	The app.py file includes the Flask API designed based on the precipitation and station analysis queries already developed.
