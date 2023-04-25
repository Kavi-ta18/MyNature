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
       self.root.geometry("220x150+0+0")

       labelframe=LabelFrame(self.root,bd=4,relief=RIDGE,text="Settings",background="lightblue")
       labelframe.place(x=10,y=10,width=160,height=120)
       
       button_chng = Button(labelframe, command=self.chng, text="Change Password")
       button_chng.grid(row=0, column=0, padx=20, pady=10)

       button_logoff = Button(labelframe, command=self.log_off, text="Log out")
       button_logoff.grid(row=1, column=0, padx=20, pady=20)
       
   def log_off(self):
       self.root.destroy()

   def chng(self):
       self.new_window=Toplevel(self.root)
       self.app=Chng(self.new_window)

class Chng:
       def __init__(self,root):
            self.root=root
            self.root.title("Change Password")
            self.root.geometry("300x300+0+0")

           

            label_username = Label(self.root, text="Username:")
            label_password = Label(self.root, text="Password:")
            self.entry_username = ttk.Entry(self.root)
            self.entry_password = ttk.Entry(self.root, show="*")
            button_updt = Button(self.root, text="Update", command=self.updt)

            label_username.grid(row=2, column=0, padx=10, pady=20)
            label_password.grid(row=3, column=0, padx=10, pady=20)
            self.entry_username.grid(row=2, column=1, padx=10, pady=20)
            self.entry_password.grid(row=3, column=1, padx=10, pady=20)
            button_updt.grid(row=4, column=0, columnspan=2, padx=10, pady=30)


       def updt(self):

            conn=mysql.connector.connect(host="localhost",username="root",password='#lilu@5%',database="nature")
            my_cursor=conn.cursor()
            query=("Select * from adminsignup where username=%s")
            value=(self.entry_username.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                my_cursor.execute("update adminsignup set pwd=%s where Username=%s",(
                                                                                        self.entry_password.get(),
                                                                                        self.entry_username.get()
                                                                                          ))
                messagebox.showinfo("SUCCESS","Updated Successfully") 
            else:  
                messagebox.showerror("Error","User doesn't exist!")
            
                                                                                                
            conn.commit()
            conn.close()
            



if __name__=="__main__":
    root=Tk()
    OBJ=Tools(root)
    root.mainloop()