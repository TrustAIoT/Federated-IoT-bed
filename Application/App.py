from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QStyleFactory, QDesktopWidget, QDockWidget
from PyQt5.QtGui import QFont

from Models.NetworkModel import NetworkModel

from Views.NetworkView import NetworkView
from Views.NodeView import NodeView

from Controllers.NetworkController import NetworkController
from Controllers.NodeController import NodeController

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()     
        font = QFont()
        font.setPointSize(16)
        
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.center()
        self.setWindowTitle("Graph Application")

        self.network_model = NetworkModel()
        self.network_controller = NetworkController(self.network_model)
        self.network_view = NetworkView(self.network_model, self.network_controller)   
        
        self.node_controller = NodeController(self.network_model)
        self.node_view = NodeView(self.network_model, self.node_controller)
        
        self.setCentralWidget(self.network_view)  
        node_dock = QDockWidget("Selection Attributes")
        node_dock.setWidget(self.node_view)
        self.addDockWidget(Qt.RightDockWidgetArea, node_dock)

    # Create a ghost rectangle to center the window on the screen
    def center(self):
        windowRect = self.frameGeometry()
        screenCenter = QDesktopWidget().availableGeometry().center()
        windowRect.moveCenter(screenCenter)
        self.move(windowRect.topLeft())

if __name__ == '__main__':
    import sys  
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    app.setStyle(QStyleFactory.create("gtk"))
    screen = MainWindow() 
    screen.showMaximized()   
    sys.exit(app.exec_())