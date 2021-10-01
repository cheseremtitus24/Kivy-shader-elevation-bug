from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

#Design Our .kv design file
design= Builder.load_file('design_md_elevationbug.kv')

class MyLayout(MDBoxLayout): #this bug occurs when inheriting from a kivymd class e.g. we have just inherited from MDBoxLayout class
    pass # in the kivy definition file when we set an elevation to any element tree class we hit this bug
# I believe the but lies within the way inheritance of the elevation property is passed down to the children.
# to Fix this I commented out all the elevation properties within MyLayout child class
class MdElevationBugApp(MDApp):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MdElevationBugApp().run()

