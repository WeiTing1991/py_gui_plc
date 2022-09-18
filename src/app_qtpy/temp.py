import sys
from qtpy import (
    QtCore, QtGui, QtWidgets
    )
from qtpy.QtGui import QIcon

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
        self.window = QtWidgets()
        self.layout = QtWidgets.QVBoxLayout()
        
        self.app = app
        self.button = QtWidgets.QRadioButton("1")
        self.button2 = QtWidgets.QPushButton("push")
        
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)


        self.app.
    def show(self):
        """ Show the window viewer
        """

        self.window.resize(self.width, self.height)
        self.window.show()
        sys.exit(self.app.exec())

    def toggle(self, text:str):
        self.button = QtWidgets.QPushButton(text)
        self.layout.addWidget(self.button)
        self.button.setCheckable(True)



if __name__ == "__main__":
    
    dcs_app = App()
    dcs_app.show()