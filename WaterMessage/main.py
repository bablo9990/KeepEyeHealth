from random import randint
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.progressbar import MDProgressBar
from kivy.clock import Clock
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import Screen
from kivy.uix.video import Video
sm = MDScreenManager()
timer_time = 0
finish_time = 20


class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = "1"
        self.progress_bar = MDProgressBar(max=finish_time, value=finish_time)
        self.btn = MDRaisedButton(text='Начать', on_press=self.start_timer)
        self.label1 = MDLabel(text='Упражнение', halign='center', bold=True, font_style='H6', size_hint=(1, .3))
        self.label2 = MDLabel(text='Выполняйте упражнения как показано на видео', halign='center')
        self.video_player = Video(source='Water.mp4')
        self.video_player.options = {'eos': 'loop'}
        self.video_player.state = 'play'
        self.main_screen = MDBoxLayout(orientation='vertical', spacing=10, padding=10,
                                  pos_hint={'center_x': .5, 'center_y': .5}, )
        self.main_screen.add_widget(self.label1)
        self.main_screen.add_widget(self.label2)
        self.main_screen.add_widget(self.video_player)
        self.main_screen.add_widget(self.progress_bar)
        self.main_screen.add_widget(self.btn)

        self.add_widget(self.main_screen)


    def start_timer(self, *args):
        self.btn.disabled = True
        Clock.schedule_interval(self.update_progress_bar, 1)
    def update_progress_bar(self, dt):
        self.progress_bar.value -= 1
        if self.progress_bar.value <= timer_time:
            self.progress_bar.value = 0
            self.btn.disabled = False
            self.btn.text = 'Завершить'
            self.btn.on_press = self.go_next
            Clock.unschedule(self.update_progress_bar)
    def go_next(self):
        self.manager.current = self.next_screen

class MyApp(MDApp):
    def build(self):
        global sm
        from kivy.config import Config
        Config.set('graphics', 'resizable', False)
        Config.write()
        from kivy.core.window import Window
        from kivy.config import Config
        Config.set('kivy', 'window_icon', 'ico.ico')
        self.icon = 'ico.png'
        self.title = 'Eye Health Keep'
        Window.size = (350, 600)
        sm.add_widget(BaseScreen(name='1'))
        return sm


if __name__ == '__main__':

    MyApp().run()

