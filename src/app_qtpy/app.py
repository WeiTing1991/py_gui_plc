import sys
from qtpy import (
    QtCore, QtGui, QtWidgets
    )
from qtpy.QtGui import QIcon
from qtpy.QtCore import Slot

from button import Button
from slider import Slider

class App:
    def __init__(self, 
                 title: str = 'dcs',
                 width: int = 1200,
                 height: int = 800,
                ):
        
        # create the window
        app = QtWidgets.QApplication(sys.argv)
        #app.references = set()
        app.setApplicationName(title)

        self.width = width
        self.height = height
        self.app = app
        self.window = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout()
        
        self.button = QtWidgets.QPushButton("Click me")
        self.button_tg = QtWidgets.QDialog()
        self.button.clicked.connect(lambda: self.toogle())
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button_tg)
        self.window.setLayout(self.layout)
        self.a =[]

    def show(self):
        """ Show the window viewer
        """
        self.window.resize(self.width, self.height)
        self.window.show()
        self.app.exec()
    
    def toogle(self):
        x = True
        print(x)
        self.a.append(x)
        return x

if __name__ == "__main__":
    
    dcs_app = App()
    dcs_app.show()
    print(dcs_app.a)

