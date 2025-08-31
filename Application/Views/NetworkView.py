from PyQt5.QtWidgets import QWidget, QVBoxLayout

class NetworkView(QWidget):
    def __init__(self, model, controller):
        super().__init__()
        self.model = model
        self.controller = controller
        self.initUI()
        
    def initUI(self):
        # Create a central widget to handle the QGraphViz object
        self.setLayout(QVBoxLayout())
        # Add the QGraphViz object to the layout
        self.layout().addWidget(self.model.graph)