from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.graphics import Color, Rectangle

class ProfilePage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Set orientation to vertical
        self.orientation = 'vertical'
        self.padding = [100, 100]
        with self.canvas:
            Color(1, 1, 1, 1)  # White color
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)
  # Create content with profile image, name, and bio
        content = BoxLayout(orientation='vertical', padding=(10, 20), spacing=10)

          # Create the profile image widget
        self.profile_image = Image(source='logo.png', size_hint=(None, None), size=(250, 190),pos_hint={'center_x': 0.5})
        self.profile_image.allow_stretch = True
        self.profile_image.keep_ratio = False
        self.profile_image.center_x = self.center_x
        self.profile_image.center_y = self.top - 100
      
        self.add_widget(self.profile_image)

         # Create header with title
        header = BoxLayout(size_hint=(1, 0.2))
        header.add_widget(Label(text="""The National Service Scheme (NSS) is a voluntary community
service program that is sponsored by the Indian government and is
implemented by educational institutions throughout the country,
including colleges.The NSS aims to develop a sense of social
responsibility, promote national integration, and encourage students
to engage in community service activities. """, font_size=20, bold=True,color=[0, 0, 0, 1]))
        self.add_widget(header)

                   # Add content to profile page
        self.add_widget(content)
        self.spacing = 20
        self.padding = 20
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class MyApp(App):
    def build(self):
        return ProfilePage()


if __name__ == '__main__':
    MyApp().run()

