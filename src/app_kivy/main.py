import kivy

#print(kivy.__version__)
#kivy.require("2.0.1")
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout  # one of many layout structures
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label



class MainPage(GridLayout):
    # runs on initialization
    def __init__(self, **kwargs):
        # we want to run __init__ of both ConnectPage AAAAND GridLayout (understanding_super.py)
        super().__init__(**kwargs)

        self.cols = 2  # used for our grid

        # widgets added in order, so mind the order.
        # self.add_widget(Label(text='IP:'))  # widget #1, top left
        # self.ip = TextInput(multiline=False)  # defining self.ip...
        # self.add_widget(self.ip) # widget #2, top right
        # 
        # 
        btn = Button(text="Connect", font_size=14)
        self.add_widget(btn)
        self.add_widget(Label(text=""))  

        btn.bind(on_press=self.callback)
        
    def callback(self,event):
        print("True")
        
        
        
        
        # self.add_widget(Label(text='Username:'))
        # self.username = TextInput(multiline=False)
        # self.add_widget(self.username)
        
        
        
        
        
class MainApp(App):
    def build(self):
        return MainPage()
    







if __name__ == '__main__':
    MainApp().run()
    