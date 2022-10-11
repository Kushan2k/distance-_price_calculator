from App import App
from CalculateWindow import CalculateWindow
from DetailsWindow import DetailWindow
import psycopg2 as sql
def main():
  conn=sql.connect(
    database='places',
    user='postgres',
    port='5432',
    password='root'
  )
  

  app=App("Calculator")

  CalculateWindow(app,2540,'kurunegala','car')
  app.mainloop()


if __name__=='__main__':
  main()
