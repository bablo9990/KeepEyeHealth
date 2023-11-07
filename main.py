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
finish_time = 1


class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = "1"
        self.progress_bar = MDProgressBar(max=finish_time, value=finish_time)
        self.btn = MDRaisedButton(text='Начать', on_press=self.start_timer)
        self.label1 = MDLabel(text='Упражнение', halign='center', bold=True, font_style='H6', size_hint=(1, .3))
        self.label2 = MDLabel(text='Выполняйте упражнения как показано на видео', halign='center')
        self.video_player = Video(source='Ex1.avi')
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
            self.btn.text = 'Перейти к следующему упражнению'
            self.btn.on_press = self.go_next
            Clock.unschedule(self.update_progress_bar)
    def go_next(self):
        self.manager.current = self.next_screen

class TxtTemplate(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.txt='Поставить палец левой руки по средней линии на расстоянии 25-30 см.,' \
            ' прикрыть ладонью правой руки правый глаз на 3-5 сек., убрать ладонь,' \
            ' смотреть обои глазами на конец пальца 3-5 сек. Повторить 5-6 раз. ' \
            'Упражнение укрепляет мышцы обоих глаз (бинокулярное зрение).'
        self.next_screen = "1"
        self.progress_bar = MDProgressBar(max=finish_time, value=finish_time)
        self.btn = MDRaisedButton(text='Начать', on_press=self.start_timer)
        self.label1 = MDLabel(text='Упражнение', halign='center', bold=True, font_style='H6', size_hint=(1, .3))
        self.label2 = MDLabel(text=self.txt, halign='center')
        self.main_screen = MDBoxLayout(orientation='vertical', spacing=10, padding=10,
                                       pos_hint={'center_x': .5, 'center_y': .5}, )
        self.main_screen.add_widget(self.label1)
        self.main_screen.add_widget(self.label2)
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
            self.btn.text = 'Перейти к следующему упражнению'
            self.btn.on_press = self.go_next
            Clock.unschedule(self.update_progress_bar)

    def go_next(self):
        self.manager.current = self.next_screen

class Ex1Screen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = '2'
        self.label1.text = 'Упражнение 1'

class Ex2Screen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = '3'
        self.label1.text = 'Упражнение 2'
        self.video_player.source = 'Ex2.mp4'

class Ex3Screen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = '4'
        self.label1.text = 'Упражнение 3'
        self.video_player.source = 'Ex3.mp4'

class Ex4Screen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = '5'
        self.label1.text = 'Упражнение 4'
        self.video_player.source = 'Ex4.mp4'

class Ex5Screen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = '6'
        self.label1.text = 'Упражнение 5'
        self.video_player.source = 'Ex5.mp4'

class Ex6Screen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = '7'
        self.label1.text = 'Упражнение 6'
        self.video_player.source = 'Ex6.mp4'


class Ex7Screen(TxtTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = '8'
        self.label1.text = 'Упражнение 7'


class Ex8Screen(TxtTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = '9'
        self.label1.text = 'Упражнение 8'
        self.txt = '«Змейка». Проведите взглядом волнистую линию от нижнего правого угла к нижнему левому, после чего поморгайте и повторите упражнение в другую сторону. Выполните «змейку» несколько раз.'
        self.label2.text = self.txt

class Ex9Screen(TxtTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = '10'
        self.label1.text = 'Упражнение 9'
        self.txt = 'Упражнение №1 “Большие глаза” — сидя. Крепко зажмурить глаза на 3-5 сек., а затем открыть глаза 3-5 сек., повторить 6-8 раз. Данное упражнение укрепляет мышцы век. Способствует кровообращению и расслаблению мышц глаз.'
        self.label2.text = self.txt

class Ex10Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.progress_bar = MDProgressBar(max=60, value=60)
        self.btn = MDRaisedButton(text='Начать', on_press=self.start_timer)
        self.label1 = MDLabel(text='Упражнение 10', halign='center', bold=True, font_style='H6', size_hint=(1, .3))
        self.label2 = MDLabel(text='Сконцентрируйтесь на центре стерео картинки и не отводите взгляд пока не увидите 3D объект'
                                   ' или закончиться время', halign='center')
        self.main_screen = MDBoxLayout(orientation='vertical', spacing=10, padding=10,
                                       pos_hint={'center_x': .5, 'center_y': .5}, )
        self.main_screen.add_widget(self.label1)
        self.main_screen.add_widget(self.label2)
        self.main_screen.add_widget(self.progress_bar)
        self.main_screen.add_widget(self.btn)

        self.add_widget(self.main_screen)

    def start_timer(self, *args):
        self.btn.disabled = True
        self.show_image()
        Clock.schedule_interval(self.update_progress_bar, 1)

    def update_progress_bar(self, dt):
        self.progress_bar.value -= 1
        if self.progress_bar.value <= timer_time:
            self.progress_bar.value = 0
            self.btn.on_press = None
            self.popup.dismiss()
            Clock.unschedule(self.update_progress_bar)

    def show_image(self):
        from kivy.uix.popup import Popup
        self.popup = Popup(title='Image Popup', size_hint=(None, None), size=(400, 400))
        image = FitImage(source=['st1.png', 'st2.png', 'st3.png', 'st4.png', 'st5.png', 'st6.png',
                                    'st7.png', 'st8.png', 'st9.png', 'st10.png'][randint(0, 9)])
        self.popup.content = image
        self.popup.open()

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
        sm.add_widget(Ex1Screen(name='1'))
        sm.add_widget(Ex2Screen(name='2'))
        sm.add_widget(Ex3Screen(name='3'))
        sm.add_widget(Ex4Screen(name='4'))
        sm.add_widget(Ex5Screen(name='5'))
        sm.add_widget(Ex6Screen(name='6'))
        sm.add_widget(Ex7Screen(name='7'))
        sm.add_widget(Ex8Screen(name='8'))
        sm.add_widget(Ex9Screen(name='9'))
        sm.add_widget(Ex10Screen(name='10'))

        return sm


if __name__ == '__main__':

    MyApp().run()

