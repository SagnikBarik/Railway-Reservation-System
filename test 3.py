from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import AsyncImage
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel

Window.size = (450, 740)

kv = '''
ScreenManager:
    Main:

<main>:
    name: 'main'
    video_list: video_list
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Video downloader'

        ScrollView:
            do_scroll_x: False
            BoxLayout:
                id: video_list
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
     '''

class Main(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Main(name='main'))

class Ytube(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root = Builder.load_string(kv)

        screen_id = self.root.get_screen('main').ids.video_list

        for i in range(5):
            # Make a new image widget for each MDCard
            image = AsyncImage(
                source='https://static.hub.91mobiles.com/wp-content/uploads/2020/05/How-to-download-youtube-videos.jpg', size_hint=(1, .7), )
            card = MDCard(orientation='vertical', pos_hint={
                            'center_x': .5, 'center_y': .7}, size_hint=(.9, None), height=200)
            card.add_widget(image)
            card.add_widget(MDLabel(
                text='Phishing attacks are SCARY easy to do!! (let me show you!)', size_hint=(.6, .2), ))
            screen_id.add_widget(card)

    def build(self):
        return self.root

if __name__ == "__main__":
    Ytube().run()