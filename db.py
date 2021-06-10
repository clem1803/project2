import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, MetaData, Table, inspect



connection_string = "postgres:mavourneen18@localhost:5432/project2"
engine = create_engine(f'postgresql://{connection_string}')

metadata = MetaData()
metadata.reflect(bind=engine)
print(metadata.tables)

insp = inspect(engine)
print(insp.get_table_names())

# reflect an existing database into a new model
Base = automap_base(metadata=metadata)
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
# wwi_aircraft_data = Base.classes.wwi_aircraft_data
print(Base.classes.__tablenames__)

# messages = Table('wwi_aircraft_data', metadata, autoload_with=engine)

# session = Session(engine)
# results = session.query(wwi_aircraft_data).all()
# print(len(results))


# print (engine.table_names())