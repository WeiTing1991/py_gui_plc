from qtpy import QtWidgets

class Button:
    """ This class represnts a button
    
    app:
    parent:
    text: str
    action:
    
    """

    def __init__(self, app, parent, text, action):

        box = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        box.setLayout(layout)
        button = QtWidgets.QPushButton(text)
        layout.addWidget(button)
        parent.addWidget(box)
        
        # connect
        button.clicked.connect(action)
        button.clicked.connect(app.view.update)

        # attributes
        self.action = action
        self.button = button

    def __call__(self, *args, **kwargs):
        return self.action()
