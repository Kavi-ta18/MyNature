import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

kivy.require('1.11.1')


class LoginPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'
        self.spacing = 20
        self.padding = 50

        self.background = Image(source=r'C:\Users\Akanksha\Downloads\Screenshot_2023-03-27_210932-removebg-preview (1).png', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)

        self.title = Label(text='Welcome to my App', font_size=30)
        self.add_widget(self.title)

        self.username = TextInput(hint_text='Username', font_size=20)
        self.add_widget(self.username)

        self.password = TextInput(hint_text='Password', password=True, font_size=20)
        self.add_widget(self.password)

        self.buttons_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint_y=None, height=50)
        self.add_widget(self.buttons_layout)

        self.admin_button = Button(text='Admin', font_size=20)
        self.admin_button.bind(on_press=self.admin_login)
        self.buttons_layout.add_widget(self.admin_button)

        self.coworkers_button = Button(text='Co-workers', font_size=20)
        self.coworkers_button.bind(on_press=self.coworkers_login)
        self.buttons_layout.add_widget(self.coworkers_button)

        self.locals_button = Button(text='Locals', font_size=20)
        self.locals_button.bind(on_press=self.locals_login)
        self.buttons_layout.add_widget(self.locals_button)

        self.signup_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        self.add_widget(self.signup_layout)

        self.new_here_label = Label(text="New here? Create an account", font_size=20)
        self.signup_layout.add_widget(self.new_here_label)

        self.signup_button = Button(text='SIGN UP', font_size=20)
        self.signup_layout.add_widget(self.signup_button)

    def admin_login(self, instance):
        username = self.username.text
        password = self.password.text

        if username == 'admin' and password == 'password':
            self.title.text = 'Admin Login Successful'
        else:
            self.title.text = 'Invalid Username or Password'

    def coworkers_login(self, instance):
        username = self.username.text
        password = self.password.text

        if username == 'coworker' and password == 'password':
            self.title.text = 'Co-workers Login Successful'
        else:
            self.title.text = 'Invalid Username or Password'

    def locals_login(self, instance):
        username = self.username.text
        password = self.password.text

        if username == 'local' and password == 'password':
            self.title.text = 'Locals Login Successful'
        else:
            self.title.text = 'Invalid Username or Password'


class MyApp(App):
    def build(self):
        return LoginPage()


if __name__ == '__main__':
    MyApp().run()
