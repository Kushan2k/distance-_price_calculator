from tkinter import ttk
import tkinter 
from tkinter.font import Font
from PIL import Image,ImageTk

class Window(tkinter.Tk):

    __DESTINATIONS={}
    __PROVINCE=[]


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

      provice_box.bind('<<ComboboxSelected>>',self.__fetchDestications)

      ttk.Label(master=frame,text='Select destination:- ',font=font_2).grid(row=4,column=0,sticky=tkinter.W,padx=20)

      self.select_menu=ttk.Combobox(master=frame,width=55,font=select_font,
      justify='center',values=list(self.__DESTINATIONS.keys()),textvariable=self.__distination,state='readonly')
      self.select_menu.grid(row=4,column=1,pady=10,padx=10)

      

      

      FILE='./assets/search32.png'
      img=tkinter.PhotoImage(file=FILE)

      search_btn=ttk.Button(master=frame,image=img,width=50,padding=5)
      search_btn.image=img
      search_btn.grid(row=5,columnspan=2,pady=10,ipadx=40)

      # listen for the click event
      search_btn.bind('<Button-1>',self.__openDetailWindow)