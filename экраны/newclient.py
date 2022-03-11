from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition


class Clients(Screen):
    def data(self):
        from datetime import datetime

        now = datetime.now()

        print(now.strftime("%m.%d.%Y"))
