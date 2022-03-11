
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition


class NewClient(Screen):

  def id_client(self):
    gs = gspread.service_account(filename='fileapi.json')
    sht = gs.open_by_key('1a-dZsSTf4umMqdZJd3zax-9btQEcR1k1rDS7-4MGGoE')
    self.worksheet = sht.sheet1
    list_of_lists = self.worksheet.get_all_values()
    self.id_client = len(list_of_lists)

  def fio(self):
    self.someName = input("Введите ваше имя: ")
    self.someS = input("Введите вашу фамилию: ")
    self.somefather = input("Введите ваше отчество:")
    self.sometel = input("Введите ваш телефон:")
    def check_phone(self):

  def chektel(self):
        sometel = '+79536510450'
        a = sometel.find('+')
        if sometel.find('+') == -1:
            sometel = '+' + sometel
        if len(sometel) == 12:
            print('Введен верный номер: ', sometel)
        self.sometel = sometel

