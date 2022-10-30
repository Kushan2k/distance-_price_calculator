from tkinter import Toplevel
from tkinter import ttk
import tkinter as tk
from tkinter.font import Font
from PIL import Image,ImageTk


# calculator window for show calculation 
class CalculateWindow(Toplevel):

  def __init__(self,master,cost:int,place,mode):
    self.master=master
    super().__init__(master)
    self.cost=cost
    self.place:str=place
    self.mode:str=mode
    self.title('Estimated Price')
    self.resizable(False,False)
    

    # calling the function for building the ui 
    self.__BuildUI()


  def __BuildUI(self):

    font_2 = Font(family='Times New Roman',
              size=16,
              weight='normal',
              slant='roman',
              underline=0,
              overstrike=0)
              
    #  frame for holding the ui elements (labels,buttons etc )         
    frame=ttk.Frame(master=self,relief='ridge')
    frame.pack(expand=True,fill=tk.BOTH,padx=20,pady=20)

    LOGO='./assets/logo.jpg'
    logo=ImageTk.PhotoImage(Image.open(fp=LOGO))
    title_label=ttk.Label(master=frame,image=logo)
    title_label.image=logo
    title_label.grid(row=0,columnspan=2,padx=10,pady=10)

    ttk.Label(master=frame,text='Cost calculator  ',font=('Times',25)).grid(row=1,columnspan=2,pady=20,padx=20)
    ttk.Label(master=frame,text=f'Katunayaka to {self.place.capitalize()} ',font=font_2).grid(row=2,column=0,sticky=tk.W,padx=20)
    ttk.Label(master=frame,text=f'Mode - By {self.mode.capitalize()} ',font=font_2).grid(row=3,column=0,padx=20,sticky=tk.W)


    ttk.Label(master=frame,padding=10,text=f'Your Cost is- Rs. {self.cost} ',font=font_2,background='lightgreen').grid(row=4,column=0,sticky=tk.W,pady=20,padx=20)
