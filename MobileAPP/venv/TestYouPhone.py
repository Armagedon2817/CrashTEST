
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu



class TestYourPhone(MDApp):
    
    

    def build(self):
        return Builder.load_string()


    def on_start(self):
        self.fps_monitor_start()

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_string(
            '''
BoxLayout:
    orientation:'vertical'

    MDToolbar:
        title: 'Тест От Никитоса'
        md_bg_color: .2, .2, .2, 1
        specific_text_color: 1, 1, 1, 1
        

    MDBottomNavigation:
        panel_color: .2, .2, .2, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'О проекте'
            icon: 'book-account'

            MDLabel:
                text: 'Добро пожаловать на стресс тест!!! На данный момент он может казаться ванильным. В скором времени будут выходить обновления, так и интерфейс станет более приятный для глаз! Прошу вас сразу реагировать на ошибки и баги приложения! Я всегда буду проверять отзывы!! Буду ждать отзывы)) Связь со мной: https://vk.com/programmernew , Так же можно поддержать проект небольшой суммой на киви: 89990032244'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'СТРЕСС тест'
            icon: 'album'

            MDLabel:
                text: ''
                halign: 'center'


'''
        )

KV = '''
MDScreen:

    MDRaisedButton:
        id: button
        text: "PRESS ME"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.menu.open()
'''







TestYourPhone().run()