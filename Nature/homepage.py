from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.card import card
import kivy.uix.*

from kivy.graphics import Color, Rectangle

class MyApp(App):
    def build(self):
        # create a vertical box layout to hold the cards
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # create a scrollview to hold the box layout
        scrollview = ScrollView()
        scrollview.add_widget(layout)

        # create five cards
        for i in range(5):
            card = Card()
            card.size_hint = (None, None)
            card.size = (300, 200)
            card.border = (1, 1, 1, 1)
            card.background_color = (1, 1, 1, 1)
            card.add_widget(Label(text=f'Card {i+1}', font_size=20))

            # add the card to the box layout
            layout.add_widget(card)

        return scrollview

if __name__ == '__main__':
    MyApp().run()
