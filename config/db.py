from curses import meta
from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:@localhost/fastapi')

meta = MetaData()

conn = engine.connect()
print(conn)
