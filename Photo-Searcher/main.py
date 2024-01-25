from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):

    def search_image(self):
        query = self.manager.current_screen.ids.user_query.text
        try:
            page = wikipedia.page(title=query)

            wiki_image = page.images[0]

            request = requests.get(wiki_image)

            if request.status_code == 403:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, '
                                  'like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
                request = requests.get(wiki_image, headers=headers)

            content = request.content
            image_path = 'files/result.jpg'

            with open(image_path, 'wb') as output:
                output.write(content)

            self.manager.current_screen.ids.img.source = image_path

        except:

            print('Ambiguous title')


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
