import sqlite3 as slite
import psycopg2 as psql

sconn=slite.connect('./db.sqlite')

pconn=psql.connect(
  database='places',
  user='postgres',
  port='5432',
  password='root'
)

sc=sconn.cursor()
pc=pconn.cursor()
sc.execute("SELECT * FROM place")
data=sc.fetchall()

for row in data:

    pl=row[1].strip()
    km=row[2]
    dis=row[3].strip()
    ci=row[6].strip()
    pr=row[7].strip()

    pc.execute('INSERT INTO place (name, discription, district, province, distance) VALUES (%s,%s,%s,%s,%s)',(pl,dis,ci,pr,km))
    pconn.commit()
