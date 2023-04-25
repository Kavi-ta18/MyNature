from msilib.schema import SelfReg
import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
from camera import Cam
from tools import Tools
from about import About
from profilepage import Profile

class LoginPage:
    def __init__(self, root):
        self.root=root
        self.root.title("Home")
        self.root.geometry("400x600+0+0")

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        # Create and place the widgets
        label_username = Label(self.root, text="Username:")
        label_password = Label(self.root, text="Password:")
        self.entry_username = ttk.Entry(self.root)
        self.entry_password = ttk.Entry(self.root, show="*")
        button_admin = Button(self.root, text="Admin", command=self.login_admin)
        button_volunteer = Button(self.root, text="Volunteer", command=self.login_volunteer)
        button_student = Button(self.root, text="Student", command=self.login_student)
        button_login = Button(self.root, text="Login", command=self.val)

        label_signup = Label(self.root, text="Dont have an account? SIGNUP!!")

        button_signup = Button(self.root, text="Sign Up", command=self.signup)


        label_username.place(x=50, y=120)
        label_password.place(x=50, y=160)
        self.entry_username.place(x=50, y=140)
        self.entry_password.place(x=50, y=180)
        button_admin.place(x=10, y=220)
        button_volunteer.place(x=100, y=220)
        button_student.place(x=200, y=220)
        button_login.place(x=100, y=260)

        button_signup.place(x=100, y=300)
        label_signup.place(x=50, y=340)



    def signup(self):
        # Add signup logic here
        self.new_window=Toplevel(self.root)
        self.app=SignupPage(self.new_window)
       

    def val(self):
        # TODO: Implement admin login logic
        if self.entry_username.get()=="" or self.entry_password.get()=="":
            messagebox.showerror("Error","All fields are compulsory")
        
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password='#lilu@5%',database="nature")
            my_cursor=conn.cursor()
            my_cursor.execute("Select *from adminsignup where Username=%s and pwd=%s",(
                                                                           self.entry_username.get(),
                                                                           self.entry_password.get()
                                                                                      ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or password")
            else:
                    self.new_window=Toplevel(self.root)
                    self.app=MainPage(self.new_window)
    
            conn.commit()
            conn.close()
        

        
    def login_admin(self):
        # TODO: Implement admin login logic
        self.new_window=Toplevel(self.root)
        self.app=CommonLogin(self.new_window)
        # Hide the login page
        
        
    def login_volunteer(self):
        # TODO: Implement volunteer login logic
        self.new_window=Toplevel(self.root)
        self.app=CommonLogin(self.new_window)

    def login_student(self):
        # TODO: Implement volunteer login logic
        self.new_window=Toplevel(self.root)
        self.app=CommonLogin(self.new_window)

class SignupPage:
    def __init__(self, root):
        self.root=root
        self.root.title("Signup")
        self.root.geometry("400x600+0+0")

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
     
        
        # Create and place the widgets with padding
        label_name = Label(self.root, text="Name:")
        label_phone = Label(self.root, text="Phone No:")
        label_username = Label(self.root, text="Username:")
        label_password = Label(self.root, text="Password:")
        self.entry_name = ttk.Entry(self.root)
        self.entry_phone = ttk.Entry(self.root)
        self.entry_username = ttk.Entry(self.root)
        self.entry_password = ttk.Entry(self.root, show="*")
        button_signup = Button(self.root, text="Sign Up", command=self.enter)



        label_name.grid(row=0, column=0, padx=10, pady=20)
        label_phone.grid(row=1, column=0, padx=10, pady=20)

        label_username.grid(row=2, column=0, padx=10, pady=20)
        label_password.grid(row=3, column=0, padx=10, pady=20)
        self.entry_name.grid(row=0, column=1, padx=10, pady=20)
        self.entry_phone.grid(row=1, column=1, padx=10, pady=20)

        self.entry_username.grid(row=2, column=1, padx=10, pady=20)
        self.entry_password.grid(row=3, column=1, padx=10, pady=20)
        button_signup.grid(row=4, column=0, columnspan=2, padx=10, pady=30)
        
        
    def enter(self):
        # Add signup logic here
        conn=mysql.connector.connect(host="127.0.0.1",username="root",password='#lilu@5%',database="nature")
        my_cursor=conn.cursor()
        query=("Select * from adminsignup where username=%s")
        value=(self.entry_username.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()
        if row!=None:
                messagebox.showerror("Error","User already exists,please try again using another Username")
        else:
                my_cursor.execute("insert into adminsignup values(%s,%s,%s,%s)",(
                                                                    self.entry_username.get(),
                                                                    self.entry_name.get(),
                                                                    self.entry_phone.get(),
                                                                    self.entry_password.get()                                                                   
                                                                                 ))
        conn.commit()
        conn.close()
        messagebox.showinfo("SUCCESS","Registered Successfully")
        
        

    def mainpage(self):
        self.new_window=Toplevel(self.root)
        self.app=MainPage(self.new_window)

class CommonLogin:
    def __init__(self, root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("400x600+0+0")
    
        label_username = Label(self.root, text="Username:")
        label_password = Label(self.root, text="Password:")
        self.entry_username = ttk.Entry(self.root)
        self.entry_password = ttk.Entry(self.root, show="*")

        button_login = Button(self.root, text="Login", command=self.val)

        label_username.grid(row=0, column=0,padx=10, pady=30)
        label_password.grid(row=1, column=0,padx=10, pady=30)
        self.entry_username.grid(row=0, column=1,padx=20, pady=30)
        self.entry_password.grid(row=1, column=1,padx=20, pady=30)

        button_login.grid(row=2, column=1, padx=10, pady=30)
        
    def val(self):
        # TODO: Implement admin login logic
        if self.entry_username.get()=="" or self.entry_password.get()=="":
            messagebox.showerror("Error","All fields are compulsory")
        
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password='#lilu@5%',database="nature")
            my_cursor=conn.cursor()
            my_cursor.execute("Select *from adminsignup where Username=%s and pwd=%s",(
                                                                           self.entry_username.get(),
                                                                           self.entry_password.get()
                                                                                      ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or password")
            else:
                    self.new_window=Toplevel(self.root)
                    self.app=MainPage(self.new_window)
    
            conn.commit()
            conn.close()

    

class MainPage:
    def __init__(self, root):
        self.root=root
        self.root.title("Main Page")
        self.root.geometry("1600x900")
        
        #self.login_page = login_page

        nav_frame = Frame(root, bg="white")
        nav_frame.place(x=610,y=170,width=340,height=450)

# Add buttons to the navigation bar
        button1 = Button(self.root, text="Back", command=self.back_func)
        button2 = Button(self.root, text="About", command=self.abt)
        button3 = Button(self.root, text="Camera", command=self.camera)
        button4 = Button(self.root, text="Profile", command=self.profile)
        button5 = Button(self.root, text="Setting", command=self.tool)

        button1.grid(row=0, column=0, padx=20, pady=450)
        button2.grid(row=0, column=1, padx=20, pady=450)
        button3.grid(row=0, column=2, padx=20, pady=450)
        button4.grid(row=0, column=3, padx=20, pady=450)
        button5.grid(row=0, column=4, padx=20, pady=450)

# Create a frame for the cards
        cards_frame = Frame(root,width=400,height=600)
        #cards_frame.place(x=610,y=170,width=340,height=450)
        #cards_frame.pack(side=TOP)
        self.root.geometry("405x500+610+170")

# Create a canvas and scrollbar for the cards
        canvas = Canvas(cards_frame)
        canvas.place(x=610,y=170,width=340,height=450)
        scrollbar = Scrollbar(cards_frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.place(x=340,y=170)

# Set canvas scroll region and bind scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a frame for the cards in the canvas
        frame = Frame(canvas)
        canvas.create_window((0,25), window=frame, anchor=tk.NW)
        
        

# Add cards to the frame
        for i in range(20):
            card_frame = Frame(frame, width=300, height=500, bg="white", bd=2, relief=SOLID)
            card_frame.pack(padx=20, pady=20)

    
    def camera(self):
         self.new_window=Toplevel(self.root)
         self.app=Cam(self.new_window)

    def back_func(self):
         self.root.destroy()

    def tool(Self):
         Self.new_window=Toplevel(Self.root)
         Self.app=Tools(Self.new_window)

    def abt(self):
         self.new_window=Toplevel(self.root)
         self.app=About(self.new_window)

    def profile(self):
         self.new_window=Toplevel(self.root)
         self.app=Profile(self.new_window)
# Create the main window and the login page

# Start the event loop


if __name__ =="__main__":
    root=Tk()
    app=LoginPage(root)
    root.mainloop()

