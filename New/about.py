import tkinter as tk
from tkinter import*
from PIL import ImageTk, Image

# Create the tkinter window
class About:
    def __init__(self,root):
        self.root = root
        self.root.title("About")

        # Load the image
        img = Image.open(r"C:\Users\Kavi\Pictures\Screenshots\Screenshot (55).png")
        img = img.resize((400, 300))
        img = ImageTk.PhotoImage(img)

        # Create a label to display the image
        img_label = tk.Label(root, image=img)
        img_label.pack()

        # Create a frame for the text
        text_frame = tk.Frame(root)
        text_frame.pack()

        # Add the long text to a scrollbar widge
        text = tk.Text(text_frame, height=20, width=40)
        text_scrollbar = tk.Scrollbar(text_frame)
        text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text.config(yscrollcommand=text_scrollbar.set)
        text.pack(side=tk.LEFT, fill=tk.BOTH)
        text_scrollbar.config(command=text.yview)

        long_text = """My Nature app is design to resolve problem of the surroundings and also to protect our Nature. This app is going to help our volunteers which work under the committee of NSS, works as social servicing. when there is some problem in your surrounding that should be resolve so people who’s having account in the app, they will take a picture and post it on that app with the caption and location than  the volunteers of NSS will go there solve that issue and it will be posted on that app that they have solve the problem. Also, it will help volunteers to get known immediately where the problem is occurs and team of volunteers take an immediate action, also it will help Admin to keep records of the volunteers that are the member of the committee also local people can sign up there account in the app and help to clean our area."""

        text.insert(tk.END, long_text)

# Start the tkinter main loop

if __name__ == "__main__":
    root=Tk()
    app=About(root)
    root.mainloop() 

