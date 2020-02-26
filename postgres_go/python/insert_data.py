from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

names = [("'George'","'Washington'"),
         ("'Andrew'","'Jackson'"),
         ("'Abraham'","'Lincoln'"),
         ("'Ulysses'","'Grant'"),
         ("'Theodore'","'Roosevelt'")]
url = 'postgresql+psycopg2://user:pwd@database:5432/mydb'


engine = create_engine(url)


sql = 'CREATE TABLE IF NOT EXISTS people (first VARCHAR(22), last VARCHAR(22));'
engine.execute(sql)
print('people table crated.')

sql = 'INSERT INTO people VALUES '
for f,l in names : sql += f'({f},{l}),'
sql = sql[:-1] + ';'
engine.execute(sql)
print('data entered into people.')
