
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table
#introduction to Database
engine = create_engine('sqlite:///census.sqlite')
connection= engine.connect()
# print(engine.table_names())

#connection to database
metadata = MetaData()
census = Table('census',metadata, autoload=True, autoload_with=engine)
print(repr(census))




