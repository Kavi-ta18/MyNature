from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector        
from tkinter import messagebox

class Tools:
   def __init__(self,root):
       self.root=root
       self.root.title("Settings")
       self.root.geometry("200x450+230+220")

       labelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="Settings")
       labelframe.place(x=5,y=50,width=200,height=450)

       frame=Frame(labelframe)
       frame.place(x=5,y=80,width=200,height=450)
       
       button_chng = Button(frame, text="Change Password", command=self.chng)
       button_chng.grid(row=0, column=0, columnspan=2, padx=10, pady=30)

       button_logoff = Button(frame, command=self.log_off, text="Log out", )
       button_logoff.grid(row=0, column=0, columnspan=2, padx=10, pady=30)
       
   def log_off(self):
       self.root.destroy()

if __name__=="__main__":
    root=Tk()
    OBJ=Tools(root)
    root.mainloop()