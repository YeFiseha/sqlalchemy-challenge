# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List of all available routes."""
    return (
        f"Available Routes:<br/>"
        f"Precipitation:/api/v1.0/precipitation<br/>"
        f"Stations:/api/v1.0/stations<br/>"
        f"Temperature observations:/api/v1.0/tobs<br/>"
        f"Temperature from start date:/api/v1.0/yyyy-mm-dd<br/>"
        f"Temperature from start to end dates:/api/v1.0/yyyy-mm-dd/yyyy-mm-dd<br/>"
    )

# Query results from the precipitation analysis
# Query for the dates and precipitation values

@app.route("/api/v1.0/precipitation")
def precipitation():
     
    # session (link) from Python to the DB
     session = Session(engine)

     # Query for the dates and precipitation values
     results =   session.query(Measurement.date, Measurement.prcp).\
            order_by(Measurement.date).all()
     session.close()

     # Convert to list of dictionaries to jsonify
     prcp_date = []

     for date, prcp in results:
        dict = {}
        dict[date] = prcp
        prcp_date.append(dict)

     session.close()

     return jsonify (prcp_date)


# JSON list of stations from the dataset
@app.route("/api/v1.0/stations")
def stations():

    # session (link) from Python to the DB
    session = Session(engine)

    # Query all stations
    stations = {}

    results = session.query(Station.station, Station.name).all()
    
    for St,name in results:
        stations[St] = name

    session.close()

    return jsonify(stations)

#the dates and temperature observations of the most-active station for the previous year of data
@app.route("/api/v1.0/tobs")
def tobs():

    # session (link) from Python to the DB
    session = Session(engine)
   
    #the dates and temperature values
    results = session.query(Measurement.date,  Measurement.tobs,Measurement.prcp).\
                filter(Measurement.date >= '2016-08-23').\
                filter(Measurement.station=='USC00519281').\
                order_by(Measurement.date).all()

    session.close()

    #create dictionary from the data and apped to the list of temp observations at themost active station for the one year
    tobs_active_station = []

    for prcp, date,tobs in results:
        tob_dict = {}
        tob_dict["prcp"] = prcp
        tob_dict["date"] = date
        tob_dict["tobs"] = tobs
        
        tobs_active_station.append(tob_dict)

    return jsonify(tobs_active_station)

#JSON list of the minimum, the average, and the maximum temperature for a specified start or start-end range

#For a specified start TMin, TMax, TAvg for all the dates greater than or equal to the start date
@app.route("/api/v1.0/<start_date>")
def Start_date(start_date):
    
    # Temp_Min, Temp_Max, Temp_Avg for all the dates greater than or equal to the start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start_date).all()

    session.close()

    # start date tobs
    startdate_tobs = []

    for min, avg, max in results:
        startdate_dict = {}
        startdate_dict["min_temp"] = min
        startdate_dict["avg_temp"] = avg
        startdate_dict["max_temp"] = max
        startdate_tobs.append(startdate_dict) 
    return jsonify(startdate_tobs)

# Temp_Min, Temp_Max, Temp_Avg for specified start-end time range
@app.route("/api/v1.0/<start_date>/<end_date>")
def Start_end_date(start_date, end_date):
     
     results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

     session.close()

     #  list of start_end_date_tobs
     startend_tobs = []

     for min, avg, max in results:
        startend_dict = {}
        startend_dict["min_temp"] = min
        startend_dict["avg_temp"] = avg
        startend_dict["max_temp"] = max
        startend_tobs.append(startend_tobs) 
    

     return jsonify(startend_tobs)

if __name__ == "__main__":
    app.run(debug=True)
