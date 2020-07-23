#Install SQLAlchemy using pip install sqlalchemy in the Windows cmd
#More information: https://docs.sqlalchemy.org/en/latest/core/engines.html
from sqlalchemy import create_engine
import pandas


#Loading the TXT file for writing to a new table in the database
dtxt = pandas.read_csv("E:\\new\\frnds.txt")



#Loading the JSON file for writing to a new table in the database
djson = pandas.read_json("E:\\new\\FRNDS.json")

#Loading the Excel file for writing to a new table in the database
dxlsx = pandas.read_excel("E:\\new\\FRNDS.xlsx", sheet_name = 0)

#Loading an existing SQL table as a DataFrame for writing to a new table in the database
#Creating an SQLAlchemy engine (Dialect object + Pool object) 
#More information: https://docs.sqlalchemy.org/en/latest/core/engines.html#engine-configuration
engine = create_engine('postgresql+psycopg2://USERNAME:PASSWORD@127.0.0.1:5432/staff')
dsql = pandas.read_sql_table('employees', engine, schema = 'mystaff')

dsql.rename({"id": "ID", "first_name": "FirstName", "last_name": "LastName", "Age": "Age", "College": "College", "Place": "Place"}, axis = 'columns', inplace = True)


#Writing the scattered data (DataFrames) to a new table in the PostgreSQL database
dtxt.to_sql('allstaff', engine, schema = 'mystaff', index = False,)


djson.to_sql('allstaff', engine, schema = 'mystaff', index = False, if_exists = 'append')

dxlsx.to_sql('allstaff', engine, schema = 'mystaff', index = False, if_exists = 'append')

dsql.to_sql('allstaff', engine, schema = 'mystaff', index = False, if_exists = 'append')


#End of program