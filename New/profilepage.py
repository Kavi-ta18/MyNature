import tkinter as tk
from tkinter import*
from tkinter import filedialog

class Profile:
    def __init__(self,root):
        self.root = root
        self.root.title("Profile")
# Define some initial data for the user profile
    user_data = {
        'name': 'John Doe',
        'username': '@johndoe',
        'bio': 'A software developer and music lover',
        'profile_picture':r'C:\Users\Kavi\Pictures\Screenshots\Screenshot (55).png'
    }

    # Define a function to update the profile picture
    def update_profile_picture():
        # Open a file dialog to select a new profile picture
        file_path = filedialog.askopenfilename(filetypes=[('Image Files', ('*.png', '*.jpg', '*.jpeg'))])
        if file_path:
            # Update the profile picture in the user data dictionary
            root.user_data['profile_picture'] = file_path
            # Recreate the profile page with the updated data
            root.create_profile_page(root.user_data)

    # Define a function to create a user profile page
    def create_profile_page(data):
        # Create the main window
        root = tk.Tk()
        root.title(f"{data['name']}'s Profile")
        
        # Create the profile picture widget
        profile_picture = tk.PhotoImage(file=data['profile_picture'])
        
        picture_label = tk.Label(root, image=profile_picture,height=300,width=300)
        picture_label.pack(pady=10)
        
        # Create the user information labels
        name_label = tk.Label(root, text=data['name'], font=('Arial', 28, 'bold'))
        name_label.pack()
        
        username_label = tk.Label(root, text=data['username'], font=('Arial', 24, 'italic'))
        username_label.pack()
        
        bio_label = tk.Label(root, text=data['bio'], font=('Arial', 20))
        bio_label.pack(pady=10)
        
        # Create the button to update the profile picture
        update_button = tk.Button(root, text='Change Profile Picture', command=root.update_profile_picture)
        update_button.pack()

        obj=Profile.create_profile_page(root.user_data)
    
if __name__ == "__main__":
    root=Tk()
    app=Profile(root)
    root.mainloop() 

# Call the function to create the initial user profile page

