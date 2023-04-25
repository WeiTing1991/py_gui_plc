# !/user/bin/python
import os
import sys
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QToolBar, QMenu, QStatusBar, QLineEdit
#from PySide6.QtUiTools import QUiLoader
#from interface import Ui_Main

#from PyQt6 import uic
from PySide6.QtGui import QAction
import threading

class ControllerApp():
    def __init__(self,
                title: str='ControllerApp_v0.1',
                width: int = 1200,
                height: int = 800,
                ):
        super().__init__()
        app = QApplication(sys.argv)
        app.setApplicationName(title)

        self.app = app
        self.width = width
        self.height = height
        self.window = QMainWindow()
        self.window.resize(self.width, self.height)
        
        ######
        toolbar = QToolBar("My main toolbar")
        self.window.addToolBar(toolbar)
        button_action = QAction("Your button", self.window)
        
        button_action.setStatusTip("This is your button")
        toolbar.addAction(button_action)
        #####
        
        self.main_win = MainWindow()
        self.window.setCentralWidget(self.main_win.Widget)  
        self.main_win.pb_connect.clicked.connect(self.is_connect_to_plc)
        
    #@Slot(str)
    def is_connect_to_plc(self):
        print(True)
        c = 0
        for i in range(10):
            i+=1  
            c = i   
        self.main_win.textbox.setText(f"{c}")
        
    def run(self):
        """ Show the window viewer
        
        """
        self.window.show()

        try:
            self.app.exec()
        except SystemExit:
            print("Closing the app...")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.Widget = QWidget()
        self.Widget.setStyleSheet("background-color:grey;")
        #self.ui = Ui_Main()
        #self.ui.setupUi(self.Widget)
        
        # set the meun 
        self.container_left = QWidget(self.Widget)
        self.container_left.setGeometry(10,10,250,750)
        self.container_left.setAutoFillBackground(True)
        self.container_left.setStyleSheet("background-color:white;"
                                            )        

        self.button_wd= QWidget(self.container_left)
        self.v_layout = QVBoxLayout(self.button_wd)

        # push_buttton = pb
        self.pb_connect = QPushButton("ON")
        self.textbox = QLineEdit()
        pb_turn_motor_On = QPushButton("ON_Motor")

        
        self.v_layout.addWidget(self.pb_connect)
        self.v_layout.addWidget(self.textbox)
        
        self.v_layout.addWidget(pb_turn_motor_On)
        
        #self.v_layout.addWidget(self.container_left)
    
    # TBC
    @classmethod
    def add_button(self, button_name:str, parent): 
        push_buttton = QPushButton(text=button_name, parent=parent)
        # set alien
        #push_buttton.setGeometry(30,10,200,60)

if __name__ == "__main__":
    app = ControllerApp()
    app.run()
