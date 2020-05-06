from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
import webbrowser

class TestApp(App):

    title = 'Title'

    def hello(self, obj):
        webbrowser.open('http://python.org')

    def world(self, obj):
        webbrowser.open('http://youtube.com')

    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn1 = Button(text="Button1", on_press=self.hello)
        layout.add_widget(btn1)
        btn2 = Button(text="Button2", on_press=self.world)
        layout.add_widget(btn2)
        # return a Button() as a root widget
        popup = Popup(content=layout,title='Test popup')

        return popup


if __name__ == '__main__':
    TestApp().run()