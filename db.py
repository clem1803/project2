import sqlalchemy
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, MetaData, Table, inspect



connection_string = "postgres:bluey786@localhost:5432/project2"
engine = create_engine('postgresql://postgres:bluey786@localhost:5432/project2')

# Querying aircraft data
# aircraft_query = "select * from wwi_aircraft_data"
# aircraft_data = pd.read_sql(aircraft_query, engine)
# print(aircraft_data)

# Querying aerial attack data
# aerial_attack_query = "select * from wwi_aerial_attack"
# aerial_attack_data = pd.read_sql(aerial_attack_query, engine)
# print(aerial_attack_data)

# Querying weapon data
# weapon_query = "select * from wwi_weapon_data"
# weapon_data = pd.read_sql(weapon_query, engine)
# print(weapon_data)
