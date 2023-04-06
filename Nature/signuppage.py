
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class SignupPage(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.padding = 40
        self.spacing = 30

        
        self.add_widget(Label(text="Username:"))
        self.username_input = TextInput(multiline=False)
        self.add_widget(self.username_input)

        
        self.add_widget(Label(text="Email:"))
        self.email_input = TextInput(multiline=False)
        self.add_widget(self.email_input)

        
        self.add_widget(Label(text="Contact Number:"))
        self.contact_input = TextInput(multiline=False)
        self.add_widget(self.contact_input)

        
        self.add_widget(Label(text="Area:"))
        self.area_input = TextInput(multiline=False)
        self.add_widget(self.area_input)

    
        self.add_widget(Label(text="Password:"))
        self.password_input = TextInput(multiline=False, password=True)
        self.add_widget(self.password_input)

        
        self.add_widget(Label(text="Confirm Password:"))
        self.confirm_password_input = TextInput(multiline=False, password=True)
        self.add_widget(self.confirm_password_input)

        
        self.signup_button = Button(text="Signup")
        self.signup_button.bind(on_press=self.signup)
        self.add_widget(self.signup_button)

    def signup(self, instance):
        
        username = self.username_input.text
        email = self.email_input.text
        contact = self.contact_input.text
        area = self.area_input.text
        password = self.password_input.text
        confirm_password = self.confirm_password_input.text

        if password != confirm_password:
            print("Passwords do not match")
            return

        
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Contact Number: {contact}")
        print(f"Area: {area}")
        print(f"Password: {password}")


class MyApp(App):

    def build(self):
        return SignupPage()


if __name__ == '__main__':
    MyApp().run()
