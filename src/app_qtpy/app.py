from cgi import test
from qtpy import QtCore
from qtpy import QtGui
from qtpy import QtWidgets
from qtpy.QtGui import QIcon

import sys

app = QtCore.QCoreApplication.instance()
if app is None:
    app = QtWidgets.QApplication(sys.argv)
app.references = set()
app.setApplicationName("App")


window = QtWidgets.QMainWindow()
window.show()

app.exec()