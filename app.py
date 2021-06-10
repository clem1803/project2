from flask import Flask, jsonify, request
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import os

from db import session, WWI_aircraft_data

# Flask Setup
app = Flask(__name__)

# Flask Route
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/aircraft_data<br/>"
        f"/api/v1.0/passengers"
    )

@app.route("/api/v1.0/aircraft_data")
def names():
    # Create our session (link) from Python to the DB


    # Query all passengers
    results = session.query(WWI_aircraft_data).all()
    print(len(results))


    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
