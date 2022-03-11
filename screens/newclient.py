from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition


class NewClient(Screen):
   def chektel(self):
        sometel = '+79536510450'
        a = sometel.find('+')
        if sometel.find('+') == -1:
            sometel = '+' + sometel
        if len(sometel) == 12:
            print('Введен верный номер: ', sometel)
        self.sometel = sometel
