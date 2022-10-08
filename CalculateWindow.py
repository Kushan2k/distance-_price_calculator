from tkinter import Toplevel
from tkinter import ttk
import tkinter as tk



class CalculateWindow(Toplevel):

  def __init__(self,master,cost:int,place,mode):
    self.master=master
    super().__init__(master)
    self.cost=cost
    self.place:str=place
    self.mode:str=mode
    self.title('Estimated Price')
    self.resizable(False,False)
    

    self.__BuildUI()


  def __BuildUI(self):
    frame=ttk.Frame(master=self)
    frame.pack(expand=True,fill=tk.BOTH)

    ttk.Label(master=frame,text='Cost calculator  ',font=('monospace',25)).grid(row=0,column=0,sticky=tk.W,pady=20,padx=20)
    ttk.Label(master=frame,text=f'Katunayaka to {self.place.capitalize()} ',font=('serif',17)).grid(row=1,column=0,sticky=tk.W,padx=20)
    ttk.Label(master=frame,text=f'Mode - By {self.mode.capitalize()} ',font=('serif',17)).grid(row=2,column=0,padx=20,sticky=tk.W)


    ttk.Label(master=frame,padding=10,text=f'Your Cost is- Rs. {self.cost} ',font=('serif',17)).grid(row=3,column=0,sticky=tk.W,pady=20,padx=20)
