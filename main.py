from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

#Design Our .kv design file
design= Builder.load_file('design_md_elevationbug.kv')

class MyLayout(MDBoxLayout):
    pass

class MdElevationBugApp(MDApp):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MdElevationBugApp().run()

