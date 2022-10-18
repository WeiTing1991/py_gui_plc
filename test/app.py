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
        self.layout = QtWidgets.QHBoxLayout()
        
        
        self.button = QtWidgets.QPushButton("True")
        self.button_2 = QtWidgets.QPushButton("False")

        self.button_text = QtWidgets.QLineEdit()
        self.button.clicked.connect(lambda: self.toogle())
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button_2)
        self.layout.addWidget(self.button_tg)
        self.layout.addStretch(1)
        
        self.layout_v= QtWidgets.QVBoxLayout()
        self.layout_v.addLayout(self.layout)


        self.window.setLayout(self.layout_v)
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

