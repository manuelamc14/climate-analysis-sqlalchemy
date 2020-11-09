# Dependencies

import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
print(Base.classes.keys())

Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome(): 
    """List all availabe api routes"""
    return (
        f"Welcome!<br?>"
        f" What are you looking for? These are all availabe API routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/2017-08-23<br/>"
        f"/api/v1.0/2010-01-01/2017-08-23"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    # Create the session (link) from Python to the DB
    session = Session(engine)

    precipitation_inf = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >='2016-08-23')

    session.close()

    # Create a dictionary from the row data and append to a list of precipitation_list
    precipitation_list = []
    for date, prcp in precipitation_inf:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"]= prcp  
        precipitation_list.append(precipitation_dict)

    return jsonify(precipitation_list)

@app.route("/api/v1.0/stations")
def stations():
    # Create the session (link) from Python to the DB
    session = Session(engine)

    stations_query = session.query(Station.station).distinct().all()

    session.close

    # Convert list of tuples into normal list

    stations_list = list(np.ravel(stations_query))

    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create the session (link) from Python to the DB
    session = Session(engine)

    tobs_query = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >='2016-08-23').filter(Measurement.station == 'USC00519281').all()

    session.close
    
    # Create at list for the temperatures of last year
    
    tobs_list = [tob[1] for tob in tobs_query]

    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def start_date(start):

    # Create the session (link) from Python to the DB
    session = Session(engine)
    
    sel_sd = [func.max(Measurement.tobs), func.min(Measurement.tobs), func.avg(Measurement.tobs)]
    
    start_date_query = session.query(*sel_sd).filter(Measurement.date >=start).all()

    session.close

    # Create a dictionary from the row data and append to a list of precipitation_list
    
    start_date_list = []
    for max_temp, min_temp, avg_temp in start_date_query:
        start_date_dict = {}
        start_date_dict["max_temp"]= max_temp
        start_date_dict["min_temp"]= min_temp
        start_date_dict["avg_temp"]= avg_temp  
        start_date_list.append(start_date_dict)


    return jsonify(start_date_list)

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    
    # Create the session (link) from Python to the DB
    session = Session(engine)
    
    sel_sd = [func.max(Measurement.tobs), func.min(Measurement.tobs), func.avg(Measurement.tobs)]
    
    start_date_query = session.query(*sel_sd).filter(Measurement.date >=start).filter(Measurement.date <= end).all()

    session.close

    # Create a dictionary from the row data and append to a list of precipitation_list
    
    start_date_list = []
    for max_temp, min_temp, avg_temp in start_date_query:
        start_date_dict = {}
        start_date_dict["max_temp"]= max_temp
        start_date_dict["min_temp"]= min_temp
        start_date_dict["avg_temp"]= avg_temp  
        start_date_list.append(start_date_dict)


    return jsonify(start_date_list)
        
if __name__ == '__main__':
    app.run(debug=True)



