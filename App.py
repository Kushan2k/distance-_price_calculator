
# imprting relavent modules 
import tkinter
from tkinter import ttk
import psycopg2 as sql
from tkinter import messagebox

from DetailsWindow import DetailWindow
from PIL import Image,ImageTk
from tkinter.font import Font



class App(tkinter.Tk):

  

  def __init__(self, screenName: str | None):
      super().__init__(screenName)

      # window confugurations 
      self.title(screenName)
      self.resizable(False,False)
      self.conn=sql.connect(
        database='places',
        user='postgres',
        port='5432',
        password='root'
      )
      
      self.style=ttk.Style()
      self.__DESTINATIONS={}
      self.__PROVINCE=[]
      self.__fetchDestications()
      self.__fetchProvince()
      self.__distination=tkinter.StringVar(value=list(self.__DESTINATIONS.keys())[0])
      self.__province=tkinter.StringVar(value=self.__PROVINCE[0])

      # calling the init function to initalize the ui 
      self.__initUI()
      

      
      

  
  def __initUI(self):

    # creaate the frame for holding element 
    font_2 = Font(family='Times New Roman',
      size=16,
      weight='normal',
      slant='roman',
      underline=0,
      overstrike=0
    )
    select_font=Font(
      family='Helvetica',
      size=10,
      weight='normal',
      slant='roman'
    )

    frame=ttk.Frame(master=self,relief='ridge')
    frame.pack(expand=True,fill=tkinter.BOTH,padx=20,pady=20)
    LOGO='./assets/logo.jpg'
    logo=ImageTk.PhotoImage(Image.open(fp=LOGO))
    title_label=ttk.Label(master=frame,image=logo)
    title_label.image=logo
    title_label.grid(row=0,columnspan=2,padx=10,pady=10)
    discription=ttk.Label(master=frame,text='Welcome to katunayaka bandaranaika international airport, Sri lanka',font=font_2)
    discription.grid(row=1,columnspan=2,padx=20,pady=20)

    input_label=ttk.Label(master=frame,text='ENTER YOUR DESTINATION HERE',font=font_2)
    input_label.grid(row=2,pady=25,padx=20,columnspan=2)

    

    ttk.Label(master=frame,text='Select Province:- ',font=font_2).grid(row=3,column=0,sticky=tkinter.W,padx=20)
    provice_box=ttk.Combobox(master=frame,values=self.__PROVINCE,justify='center',width=55,textvariable=self.__province,state='readonly',font=select_font)
    provice_box.grid(row=3,column=1,padx=10)

    ttk.Label(master=frame,text='Select destination:- ',font=font_2).grid(row=4,column=0,sticky=tkinter.W,padx=20)
    select_menu=ttk.Combobox(master=frame,width=55,font=select_font,
    justify='center',values=list(self.__DESTINATIONS.keys()),textvariable=self.__distination,state='readonly')
    select_menu.grid(row=4,column=1,pady=10,padx=10)

    

    FILE='./assets/search32.png'
    img=tkinter.PhotoImage(file=FILE)

    search_btn=ttk.Button(master=frame,image=img,width=50,padding=5)
    search_btn.image=img
    search_btn.grid(row=5,columnspan=2,pady=10,ipadx=40)

    # listen for the click event
    search_btn.bind('<Button-1>',self.__openDetailWindow)


  # function for geting the data from the database 
  def __fetchDestications(self):
    
    try:
      curser=self.conn.cursor()
      curser.execute("SELECT id,name FROM place")

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
    
    
      



  # function for opening the new window with the details 
  def __openDetailWindow(self,event):
    value=self.__distination.get()

    DetailWindow(self,value,self.conn,self.__DESTINATIONS.get(value))



      

  