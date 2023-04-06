import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

kivy.require('1.11.1')

class CoworkerPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'
        self.spacing = 20
        self.padding = 50

        self.title = Label(text='Co-worker Login', font_size=30, halign='center')
        self.add_widget(self.title)

        self.username = TextInput(hint_text='Username', font_size=20, size_hint=(None, None), size=(400, 50), pos_hint={'center_x': 0.5})
        self.add_widget(self.username)

        self.password = TextInput(hint_text='Password', password=True, font_size=20, size_hint=(None, None), size=(400, 50), pos_hint={'center_x': 0.5})
        self.add_widget(self.password)

        self.error_label = Label(text='', font_size=20, color=(1, 0, 0, 1), halign='center')
        self.add_widget(self.error_label)

        self.login_button = Button(text='Login', font_size=20, size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5})
        self.login_button.bind(on_press=self.check_credentials)
        self.add_widget(self.login_button)

    def check_credentials(self, instance):
        username = self.username.text
        password = self.password.text

        # Check if the username and password are valid
        if username == 'coworker' and password == 'password':
            # Successful login
            self.error_label.text = ''
            # TODO: Add code to switch to coworker dashboard
        else:
            # Invalid login
            self.error_label.text = 'Invalid username or password'

class MyApp(App):
    def build(self):
        return CoworkerPage()

if __name__ == '__main__':
    MyApp().run()
