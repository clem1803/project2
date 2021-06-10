from flask import Flask, jsonify, request
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import os


connection_string = "postgres:mavourneen18@localhost:5432/project2"
engine = create_engine(f'postgresql://{connection_string}')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
WWI_aircraft_data = Base.classes

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
    session = Session(engine)

    # Query all passengers
    results = session.query(WWI_aircraft_data.AIRCRAFT).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)


if __name__ == '__main__':
    app.run(debug=True)
