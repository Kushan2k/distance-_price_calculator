
# imprting relavent modules 
import tkinter
from tkinter import ttk
import sqlite3 as sql
from tkinter import messagebox

from DetailsWindow import DetailWindow




class App(tkinter.Tk):

  

  def __init__(self, screenName: str | None):
      super().__init__(screenName)

      # window confugurations 
      self.title(screenName)
      self.resizable(False,False)
      self.conn=sql.connect('db.sqlite')
      
      self.style=ttk.Style()
      self.__DESTINATIONS={}
      self.__fetchDestications()
      self.__distination=tkinter.StringVar(value=list(self.__DESTINATIONS.keys())[0])

      # calling the init function to initalize the ui 
      self.__initUI()
      

      
      

  
  def __initUI(self):

    # creaate the frame for holding element 
    frame=ttk.Frame(master=self)
    frame.pack(expand=True,fill=tkinter.BOTH)
    title_label=ttk.Label(master=frame,text='Guid SpArk',style='TLabel',font=('monospace',30,'normal'),underline=0)
    title_label.grid(row=0,column=0,padx=10,pady=10,sticky=tkinter.W)
    discription=ttk.Label(master=frame,text='Welcome to katunayaka bandaranaika international airport, Sri lanka',font=('serif',17))
    discription.grid(row=1,column=0,padx=20,pady=20)

    input_label=ttk.Label(master=frame,text='ENTER YOUR DESTINATION HERE',font=('sans-serif',16))
    input_label.grid(row=2,column=0,pady=25,padx=20,columnspan=2)

    select_menu=ttk.Combobox(master=frame,width=55,
    justify='center',values=list(self.__DESTINATIONS.keys()),textvariable=self.__distination,state='readonly')
    select_menu.grid(row=3,columnspan=2,padx=10,pady=10)

    FILE='./assets/search32.png'
    img=tkinter.PhotoImage(file=FILE)

    search_btn=ttk.Button(master=frame,text='Search',image=img,padding=15,compound='top')
    search_btn.image=img
    search_btn.grid(row=4,columnspan=2,pady=10)

    # listen for the click event
    search_btn.bind('<Button-1>',self.__openDetailWindow)


  # function for geting the data from the database 
  def __fetchDestications(self):
    
    try:
      curser=self.conn.cursor()
      data=curser.execute("SELECT id,name FROM place")

      for i in data.fetchall():
        if i != None:
          self.__DESTINATIONS[i[1].strip()]=i[0]
    except Exception as e:
      messagebox.showerror(title="Error",message="fetching data failed!")
      



  # function for opening the new window with the details 
  def __openDetailWindow(self,event):
    value=self.__distination.get()

    DetailWindow(self,value,self.conn,self.__DESTINATIONS.get(value))



      

  