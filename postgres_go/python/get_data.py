from sqlalchemy import create_engine

url = 'postgresql+psycopg2://user:pwd@database:5432/mydb'

engine = create_engine(url)

sql = 'SELECT * FROM people;'
rows = engine.execute(sql)

for r in rows : print(r)
