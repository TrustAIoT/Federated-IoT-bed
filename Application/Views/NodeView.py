from PyQt5.QtWidgets import QTreeView, QVBoxLayout, QAbstractItemView, QComboBox, QLabel, QLineEdit, QFileDialog, QStackedWidget, QWidget
from PyQt5.QtCore import QEvent, Qt, pyqtSlot
from PyQt5.QtGui import QFont

from Models.NodeModel import NodeModel
from Models.EdgeModel import EdgeModel
from Models.AttributeModel import AttributeModel



class NodeView(QStackedWidget):
    def __init__(self, networkModel, nodeController):
        super(NodeView, self).__init__()
        self.model = networkModel
        self.controller = nodeController
        
        self.initUI()
    
    def initUI(self):
        self.initNodeViewer()
        self.initEdgeViewer()
        self.addWidget(self.nodeViewerContainer)
        self.addWidget(self.edgeViewerContainer)
        self.setCurrentIndex(1)
        
        # Connect user event to controller
        self.typeView.currentTextChanged.connect(self.controller.change_type)
        
        # Connect model event to view change
        self.model.node_selected.connect(self.onNodeSelection)
        self.model.node_added.connect(self.onNodeAdded)      
        self.model.edge_selected.connect(self.onEdgeSelection)
        
    def initNodeViewer(self):   
        self.configView = QTreeView()
        self.configView.setAlternatingRowColors(True)
        self.configView.setSortingEnabled(False)
        self.configView.setHeaderHidden(False)
        self.configView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.configView.setModel(None)
        
        self.overlayLayout = QVBoxLayout(self.configView.viewport())
        self.overlayLayout.setContentsMargins(0, 0, 0, 0)
        self.overlayView = QLabel(text="Please select a node")
        self.overlayView.setFont(QFont("Arial", 20))
        self.overlayView.setWordWrap(True)
        self.overlayView.setStyleSheet("background:rgba(0,0,0,80%); color : white;")
        self.overlayView.setAlignment(Qt.AlignCenter)
        self.overlayView.installEventFilter(self)
        self.overlayLayout.addWidget(self.overlayView)
        
        self.typeView = QComboBox()
        self.typeView.addItems(["Deactivated", "Server", "Client", "Decentralized"])
        self.typeView.setCurrentIndex(-1)
        
        self.sourceView = QLineEdit()
        self.sourceView.setReadOnly(True)
        self.sourceView.installEventFilter(self)
        
        self.entryView = QLineEdit()
        self.entryView.setReadOnly(True)
        self.entryView.installEventFilter(self)
        
        self.nodeViewerContainer = QWidget()
        self.nodeLayout = QVBoxLayout(self.nodeViewerContainer)
        self.nodeLayout.addWidget(self.configView)
        self.nodeLayout.addWidget(QLabel("Type:"))
        self.nodeLayout.addWidget(self.typeView)
        self.nodeLayout.addWidget(QLabel("Source Folder:"))
        self.nodeLayout.addWidget(self.sourceView)
        self.nodeLayout.addWidget(QLabel("Entry File:"))
        self.nodeLayout.addWidget(self.entryView)
    
    def initEdgeViewer(self):
        self.metricView = QTreeView()
        self.metricView.setAlternatingRowColors(True)
        self.metricView.setSortingEnabled(False)
        self.metricView.setHeaderHidden(False)
        self.metricView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.metricView.setModel(None)
        
        self.edgeViewerContainer = QWidget()
        self.edgeLayout = QVBoxLayout(self.edgeViewerContainer)
        self.edgeLayout.addWidget(self.metricView)
        
    def onNodeAdded(self, nodeModel):
        nodeModel.source_path_changed.connect(self.onSourceModified)
        nodeModel.entry_path_changed.connect(self.onEntryModified)
        nodeModel.type_changed.connect(self.onTypeModified)
        nodeModel.attributes_loaded.connect(self.onConfigLoaded)
    
    @pyqtSlot(NodeModel)
    def onNodeSelection(self, nodeModel):
        self.setCurrentIndex(0)
        # Change the Attribute to the selected node
        self.configView.setModel(nodeModel.attributeModel)
        self.configView.expandAll()
        self.checkOverlayStatus()
        # Reset ComboBox
        self.typeView.setCurrentText(nodeModel.type)
        self.sourceView.setText(nodeModel.source_path)
        self.entryView.setText(nodeModel.entry_path)
    
    @pyqtSlot(EdgeModel)
    def onEdgeSelection(self, edgeModel):
        self.setCurrentIndex(1)
        self.metricView.setModel(edgeModel.metricModel)
        self.metricView.expandAll()
        if self.model.oldSelectedEdge != None:
            self.model.oldSelectedEdge.metrics_changed.disconnect(self.onMetricModified)
        edgeModel.metrics_changed.connect(self.onMetricModified)
    
    @pyqtSlot(str)
    def onTypeModified(self, type):
        print(type)
        self.checkOverlayStatus()
    
    @pyqtSlot(str)
    def onSourceModified(self, source_path):
        self.sourceView.setText(source_path)
    
    @pyqtSlot(str)
    def onEntryModified(self, entry_path):
        self.entryView.setText(entry_path)
    
    @pyqtSlot(AttributeModel)
    def onMetricModified(self, metricModel):
        self.metricView.setModel(metricModel)
        self.metricView.expandAll()   

    @pyqtSlot(AttributeModel)
    def onConfigLoaded(self, attributeModel):
        self.configView.setModel(attributeModel)
        self.configView.expandAll()
        self.checkOverlayStatus()
    
    def checkOverlayStatus(self):
        if self.model.selectedNode == None:
            self.turnOnOverlay()
            self.overlayView.setText("Please select a node")
        elif self.model.selectedNode.type == "Deactivated":
            self.turnOnOverlay()
            self.overlayView.setText("This node is deactivated")
        elif self.model.selectedNode.attributeModel.rowCount() == 0:
            self.turnOnOverlay()
            self.overlayView.setText("This node is not configured")
        else:
            self.turnOffOverlay()
    
    def turnOnOverlay(self):
        self.overlayView.show()
        self.configView.horizontalScrollBar().setEnabled(False)
        self.configView.verticalScrollBar().setEnabled(False)
        self.configView.horizontalScrollBar().setStyleSheet("QScrollBar {height:0px;}")
        self.configView.verticalScrollBar().setStyleSheet("QScrollBar {width:0px;}")
    def turnOffOverlay(self):
        self.overlayView.hide()
        self.configView.horizontalScrollBar().setEnabled(True)
        self.configView.verticalScrollBar().setEnabled(True)
        self.configView.horizontalScrollBar().setStyleSheet("QScrollBar {height:20px;}")
        self.configView.verticalScrollBar().setStyleSheet("QScrollBar {width:20px;}") 
    
    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonRelease:
            if source == self.sourceView:
                self.controller.change_source_folder(self.openFolderDialog())
            if source == self.entryView:
                self.controller.change_entry_file(self.openFileDialog())
            if source == self.overlayView:
                self.controller.change_config(self.openConfigDialog())
        return super().eventFilter(source, event)
    
    def openFolderDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        folderPath = QFileDialog.getExistingDirectory(self, "Choose source folder", "", options=options)
        return folderPath
    
    def openFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filePath, _ = QFileDialog.getOpenFileName(self,"Choose entry Python file (.py)", "","All Files (*);;Python Files (*.py)", options=options)
        return filePath
    
    def openConfigDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filePath, _ = QFileDialog.getOpenFileName(self,"Choose configuration file (.yaml)", "","All Files (*);;YAML File (*.yaml)", options=options)
        return filePath
        
        

    