import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import psycopg2 as sql



class Window(tk.Tk):

  def __init__(self):
      super().__init__()
      self.__DESTINATIONS={}
      self.__PROVINCE=[]
      self.conn=sql.connect(
        database='places',
        user='postgres',
        port='5432',
        password='root'
      )

  def __fetchDestications(self,evnt):

    pr='North Western'
    self.__DESTINATIONS.clear()
    
    try:
      curser=self.conn.cursor()
      curser.execute(f"SELECT id,name FROM place WHERE province='{pr}'")

      for i in curser.fetchall():
        if i != None:
          self.__DESTINATIONS[i[1].strip()]=i[0]
      

    except Exception as e:

      messagebox.showerror(title="Error",message="fetching data failed!")


  # fetch province data from the database 
  def __fetchProvince(self):

    cur=self.conn.cursor()
    cur.execute("SELECT DISTINCT(province) FROM place ")

    for i in cur.fetchall():
      if i!=None:
        self.__PROVINCE.append(i[0].strip())
  