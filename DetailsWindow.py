
# import relavant modules 
from tkinter import Toplevel
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

from CalculateWindow import CalculateWindow



class DetailWindow(Toplevel):

  def __init__(self,master,place,conn,id):
      super().__init__(master)

      # instance variable for holding the data 
      self.id=id
      self.master=master
      self.place:str=place
      self.distrct=''
      self.distance=0
      self.mode=tk.StringVar(value='Car')
      self.price=tk.StringVar(value=0)
      self.discription=''
      self.province=''
      self.style=ttk.Style()
      self.style.configure('TButton',background='blue',foreground='black')


      # top level window confugration
      self.title(self.place)
      self.resizable(False,False)
      self.conn=conn
      self.geometry('700x600+100+100')
      

      self.__getData()
      self.__BuildUI()

  def __BuildUI(self):

    font_head=Font(
      family='Times',
      size=27,
      slant='roman',
      weight='normal'
    )
    font_normal=Font(
      family='Times',
      size=15,
      weight='normal',
      slant='roman'
    )

    mainFrame=ttk.Frame(master=self,padding=20,relief='ridge')
    mainFrame.pack(expand=True,fill=tk.X,padx=20,pady=20)
    city=ttk.Label(master=mainFrame,text=self.place,font=font_head,background='lightgreen',padding=20)
    city.pack(fill=tk.BOTH,expand=True)

    detailFrame=ttk.Frame(master=self,padding=30,relief='ridge')
    detailFrame.pack(fill=tk.BOTH,expand=True,padx=20,pady=20)


    ttk.Label(master=detailFrame,text='Result',foreground='red').grid(row=1,column=0,sticky=tk.W)
    district=ttk.Label(master=detailFrame,text=f'Provinc -',font=font_normal)
    district.grid(row=2,column=0,sticky=tk.W,padx=15,pady=8)
    dis_value=ttk.Label(master=detailFrame,text=f"{self.province}",font=font_normal,foreground='red')
    dis_value.grid(row=2,column=1,sticky=tk.W)

    ttk.Label(master=detailFrame,text=f'Distance to {self.place.capitalize()} -',font=font_normal).grid(row=3,column=0,sticky=tk.W,padx=15,pady=8)
    dist=ttk.Label(master=detailFrame,text=f'{self.distance} Km',font=font_normal,foreground='red')
    dist.grid(row=3,column=1,sticky=tk.W)

    ttk.Label(master=detailFrame,text='Mode of travel -',font=font_normal).grid(row=4,column=0,sticky=tk.W,padx=15,pady=8)
    modes=ttk.Combobox(master=detailFrame,textvariable=self.mode,values=['Car','Van','Bus'],state='readonly',justify='center')
    modes.grid(row=4,column=1,sticky=tk.W)

    ttk.Label(master=detailFrame,text='Description',font=font_normal).grid(row=5,column=0,sticky=tk.W,padx=15,pady=8)
    discription=ttk.Label(master=detailFrame,text=f'{self.discription}',font=font_normal,foreground='red',wraplength=340)
    discription.grid(row=5,column=1,sticky=tk.W)



    # ttk.Label(master=detailFrame,text='Cost per 1 Km').grid(row=6,columnspan=2,pady=5)
    # self.price=ttk.Entry(master=detailFrame,textvariable=self.price)
    # self.price.grid(row=7,columnspan=2,padx=10)
    
    generateBTN=ttk.Button(master=detailFrame,text='Calculate Price',style='TButton',width=30)
    generateBTN.grid(row=8,columnspan=2,pady=20,padx=10)
    generateBTN.bind('<Button-1>',self.__calculate)





  # get the relavent data from the database 
  def __getData(self):

    try:
      cur=self.conn.cursor()
      SQL=f"SELECT * FROM place WHERE id={self.id} "

      data=cur.execute(SQL)

      res=data.fetchone()
      self.distance=res[2]
      self.discription=res[3].strip()
      self.province=res[7].strip()
    except Exception as e:
      messagebox.showerror('Error',"could not fetch data")
      self.destroy()
    

  # calculate the price form the abouve table 
  def __calculate(self,event):
    mode=self.mode.get()
    # price=0
    uniprice=0

    if(mode=='Car'):
      uniprice=50
    elif (mode=='Bus'):
      uniprice=100
    else:
      uniprice=150

    

    if(uniprice<=0):
      messagebox.showinfo('Zero',message='Cost can not be zero or lessthan zero')
    else:
      total=float(self.distance)*uniprice

      self.destroy()
      CalculateWindow(self.master,total,self.place,mode)

    
    





    
    
