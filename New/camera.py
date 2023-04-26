import tkinter as tk
import cv2
from PIL import Image, ImageTk

class Cam(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Click Picture")
        
        
        # Open device camera
        self.cap = cv2.VideoCapture(0)
        
        # Create canvas to display image
        self.canvas = tk.Canvas(master, width=self.cap.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()
        
        # Add capture button
        self.btn_capture = tk.Button(master, text="Capture", command=self.capture)
        self.btn_capture.pack(anchor=tk.CENTER, expand=True)
        
        # Start video streaming
        self.delay = 15  # milliseconds
        self.update()
        
        self.master.mainloop()

    def update(self):
        # Read frame from camera
        ret, frame = self.cap.read()
        
        if ret:
            # Convert frame to PIL ImageTk format
            self.img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            self.imgtk = ImageTk.PhotoImage(image=self.img)
            
            # Update canvas with new image
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.imgtk)
            
        # Call update function again after delay
        self.master.after(self.delay, self.update)
        
    def capture(self):
        # Save current frame to file
        cv2.imwrite("capture.jpg", self.cap.read()[1])
        
        # Show message box with image
        img = Image.open("capture.jpg")
        img.show()

if __name__ == '__main__':
    root = tk.Tk()
    app = Cam(master=root)
    root.mainloop()
