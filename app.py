from flask import Flask, jsonify, request
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import os
import pandas as pd
import json

from db import engine

# Flask Setup
app = Flask(__name__)

# Flask Route
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/aircraft_data<br/>"
        f"/api/v1.0/aerial_attack<br/>"
        f"/api/v1.0/weapon_data<br/>"
    )

@app.route("/api/v1.0/aircraft_data")
def aircraft_data():
    aircraft_query = "select * from wwi_aircraft_data"
    aircraft_data = pd.read_sql(aircraft_query, engine)
    return aircraft_data.to_json(orient="records")
#with open('aircraft_data.json', 'w') as f:
    #json.dump(data, f)

@app.route("/api/v1.0/aerial_attack")
def aircraft_attack():
    aerial_attack_query = "select * from wwi_aerial_attack"
    aerial_attack_data = pd.read_sql(aerial_attack_query, engine)
    return aerial_attack_data.to_json(orient="records")
#with open('aerial_attack.json', 'w') as f:
    #json.dump(data, f)

@app.route("/api/v1.0/weapon_data")
def waepon_data():
    weapon_query = "select * from wwi_weapon_data"
    weapon_data = pd.read_sql(weapon_query, engine)
    return weapon_data.to_json(orient="records")
#with open('weapon_data.json', 'w') as f:
    #json.dump(data, f)

if __name__ == '__main__':
    app.run(debug=True)
