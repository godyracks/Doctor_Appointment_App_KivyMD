from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from useracc import UserAccountScreen
from appointment import AppointmentScreen
from kivy.core.window import Window
from register import RegisterScreen
from login import LoginScreen


Builder.load_file('loading.kv')
Builder.load_file('login.kv')



class LoadingScreen(Screen):
    def __init__(self, **kwargs):
        super(LoadingScreen, self).__init__(**kwargs)

    def on_enter(self, *args):
        Clock.schedule_once(self.change_screen, 7)

    def change_screen(self, dt):
        self.manager.current = 'login'


class MainApp(MDApp):
    def build(self):
        # Set the window size
        Window.size = (360, 640)
        # Create the screen manager

        sm = ScreenManager()
        sm.id = 'screen_manager'  # assign an id to the screen manager here
        sm.add_widget(LoadingScreen(name='loading'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(AppointmentScreen(name='appointment'))
        sm.add_widget(UserAccountScreen(name='user_account'))
        sm.add_widget(RegisterScreen(name='register'))
        return sm




if __name__ == "__main__":
    MainApp().run()
