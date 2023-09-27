
class MainPage(Widget):
    # runs on initialization
    def __init__(self, **kwargs):
        # we want to run __init__ of both ConnectPage AAAAND GridLayout (understanding_super.py)
        super().__init__(**kwargs)

        #self.cols = 2  # used for our grid

        # widgets added in order, so mind the order.
        # self.add_widget(Label(text='IP:'))  # widget #1, top left
        # self.ip = TextInput(multiline=False)  # defining self.ip...
        # self.add_widget(self.ip) # widget #2, top right
        # 
        # 
        
        # btn = Button(text="Connect", font_size=14)
        # self.add_widget(btn)
        # self.add_widget(Label(text=""))  

        # btn.bind(on_press=self.callback)
        
    def callback(self,event):
        print("True")
        
        
        
class MainApp(App):
    def build(self):
        return MainPage()
    



if __name__ == '__main__':
    MainApp().run()
    