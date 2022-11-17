import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget


class ControllerApp():
    def __init__(self,
                title: str='ControllerApp_v1',
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


    def run(self):
        """ Show the window viewer
        """
        self.window.resize(self.width, self.height)
        self.window.show()

        try:
            sys.exit(self.app.exec())
        except SystemExit:
            print("Closing the app...")


if __name__ == "__main__":
    app = ControllerApp()
    app.run()