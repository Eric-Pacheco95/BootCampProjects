from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Station = Base.classes.station
Measurement = Base.classes.measurement

session = Session(engine)

all_dates = session.query(Measurement.date).all()
most_recent_date = all_dates[-1][0]
year_before_date_datetime = dt.date(2017, 8, 23) - dt.timedelta(days=365)

query_prcps = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date >= year_before_date_datetime).filter\
    (Measurement.date <= most_recent_date).all()
    
dates_prcps = []
prcps = []
for x in query_prcps:
    dates_prcps.append(x[0])
    prcps.append(x[1])

dates_prcps_dict = {}
for x in range(len(dates_prcps)):
    dates_prcps_dict[dates_prcps[x]] = prcps[x]

station_name_query = session.query(Station.name).all()
station_code_query = session.query(Station.station).all()

station_name_code_dict = {}
for x in range(len(station_name_query)):
    station_name_code_dict[station_name_query[x][0]] = station_code_query[x][0]

query_temps = session.query(Measurement.date,Measurement.tobs).filter(Measurement.date >= year_before_date_datetime).filter\
    (Measurement.date <= most_recent_date).all()

dates_temps = []
temps = []
for x in query_temps:
    dates_temps.append(x[0])
    temps.append(x[1])

dates_temps_dict = {}
for x in range(len(dates_temps)):
    dates_temps_dict[dates_temps[x]] = temps[x]

def calc_temps(start_date, end_date):
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

start_temps = calc_temps('2017-07-17',most_recent_date)
start_temps_dict = {}
start_temps_dict['Min'] = start_temps[0][0]
start_temps_dict['Avg'] = start_temps[0][1]
start_temps_dict['Max'] = start_temps[0][2]

start_end_temps = calc_temps('2017-07-17','2017-07-26')
start_end_temps_dict = {}
start_end_temps_dict['Min'] = start_end_temps[0][0]
start_end_temps_dict['Avg'] = start_end_temps[0][1]
start_end_temps_dict['Max'] = start_end_temps[0][2]

app = Flask(__name__)

@app.route("/")
def home():
    return (f"all routes:<br/>\
    /api/v1.0/precipitation<br/>\
    /api/v1.0/stations<br/>\
    /api/v1.0/tobs<br/>\
    /api/v1.0/2017-07-07<br/>\
    /api/v1.0/2017-07-17:2017-07-26")

@app.route("/api/v1.0/precipitation")
def precipitation_query():
    return jsonify(dates_prcps_dict)
   
@app.route("/api/v1.0/stations")
def stations_query():
    return jsonify(station_name_code_dict)
    
@app.route("/api/v1.0/tobs")
def tobs_query():
    return jsonify(dates_temps_dict)

@app.route("/api/v1.0/2017-07-07")
def temp_data_2017_07_07():
    return jsonify(start_temps_dict)
    
@app.route("/api/v1.0/2017-07-17:2017-07-26")
def temp_data_trip():
    return jsonify(start_end_temps_dict)

if __name__ == "__main__":
    app.run(debug=True)