from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject, QTimer
from Processes.Worker import Worker
import subprocess
import time

class NetworkQuery(QObject):
    #############################################
    # Signal Definitions
    #############################################
    batadv_vis_query_finished = pyqtSignal(str)
    alfred_ipcomm_query_finished = pyqtSignal(str)
    alfred_comp_query_finished = pyqtSignal(str)
    alfred_link_query_finished = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.batadv_vis_query_worker = None
        self.batadv_vis_query_stop_flag = False
        self.alfred_ipcomm_query_worker = None
        self.alfred_ipcomm_query_stop_flag = False
    
    def batadv_vis_query(self):
        queryResult = subprocess.run(['batadv-vis', '-f', 'jsondoc'], 
                            stdout=subprocess.PIPE).stdout.decode('utf-8')
        print(queryResult)

        query = '''{
    "timestamp" : ''' + str(time.time()) + ''',
    "source_version" : "debian-2020.3-1+b1",
    "algorithm" : 4,
    "vis" : [
        {
            "primary" : "d8:3a:dd:21:c1:92",
            "neighbors" : [
                {
                    "router" : "d8:3a:dd:21:c1:92",
                    "neighbor" : "d8:3a:dd:22:59:60",
                    "metric" : ''' + str((int(time.time()) % 2000) / 1000.0) + '''
                }
            ]
        },
        {
            "primary" : "d8:3a:dd:22:59:60",
            "neighbors" : [
                {
                    "router" : "d8:3a:dd:22:59:60",
                    "neighbor" : "d8:3a:dd:21:c1:92",
                    "metric" : "1.054"
                }
            ]
        },
        {
            "primary" : "d8:3a:dd:22:59:61",
            "neighbors" : [
                {
                    "router" : "d8:3a:dd:22:59:61",
                    "neighbor" : "d8:3a:dd:21:c1:92",
                    "metric" : "1.001"
                }
            ]
        }
    ]
}'''
        self.batadv_vis_query_finished.emit(queryResult)
    
    def stop_batadv_vis_query(self):
        self.batadv_vis_query_stop_flag = True
    
    def start_batadv_vis_query(self, interval_ms=10000):
        self.batadv_vis_query_stop_flag = False
        self.batadv_vis_query_interval = interval_ms
        self.batadv_vis_query_continue()
    
    def batadv_vis_query_continue(self):
        if self.batadv_vis_query_stop_flag:
            return
        self.batadv_vis_query_worker = Worker(self.batadv_vis_query, ())
        self.batadv_vis_query_worker.start()
        QTimer.singleShot(self.batadv_vis_query_interval, self.batadv_vis_query_continue)
    
    def alfred_ipcomm_query(self):
        queryResult = subprocess.run(['alfred', '-r', '65'], 
                            stdout=subprocess.PIPE).decode('utf-8')
        self.alfred_ipcomm_query_finished.emit(queryResult)
    
    def stop_alfred_ipcomm_query(self):
        self.alfred_ipcomm_query_stop_flag = True
    
    def start_alfred_ipcomm_query(self, interval_ms=10000):
        self.alfred_ipcomm_query_stop_flag = False
        self.alfred_ipcomm_query_interval = interval_ms
        self.alfred_ipcomm_query_continue()
    
    def alfred_ipcomm_query_continue(self):
        if self.alfred_ipcomm_query_stop_flag:
            return
        self.alfred_ipcomm_query_worker = Worker(self.alfred_ipcomm_query, ())
        self.alfred_ipcomm_query_worker.start()
        QTimer.singleShot(self.alfred_ipcomm_query_interval, self.alfred_ipcomm_query_continue)
        
    def alfred_comp_query(self):
        queryResult = subprocess.run(['alfred', '-r', '66'], 
                            stdout=subprocess.PIPE).decode('utf-8')
        self.alfred_comp_query_finished.emit(queryResult)
    
    def stop_alfred_comp_query(self):
        self.alfred_comp_query_stop_flag = True
    
    def start_alfred_comp_query(self, interval_ms=10000):
        self.alfred_comp_query_stop_flag = False
        self.alfred_comp_query_interval = interval_ms
        self.alfred_comp_query_continue()
    
    def alfred_comp_query_continue(self):
        if self.alfred_comp_query_stop_flag:
            return
        self.alfred_comp_query_worker = Worker(self.alfred_comp_query, ())
        self.alfred_comp_query_worker.start()
        QTimer.singleShot(self.alfred_comp_query_interval, self.alfred_comp_query_continue)
    
    def alfred_link_query(self):
        queryResult = subprocess.run(['alfred', '-r', '67'], 
                            stdout=subprocess.PIPE).decode('utf-8')
        self.alfred_link_query_finished.emit(queryResult)
    
    def stop_alfred_link_query(self):
        self.alfred_link_query_stop_flag = True
        
    def start_alfred_link_query(self, interval_ms=10000):
        self.alfred_link_query_stop_flag = False
        self.alfred_link_query_interval = interval_ms
        self.alfred_link_query_continue()
    
    def alfred_link_query_continue(self):
        if self.alfred_link_query_stop_flag:
            return
        self.alfred_link_query_worker = Worker(self.alfred_link_query, ())
        self.alfred_link_query_worker.start()
        QTimer.singleShot(self.alfred_link_query_interval, self.alfred_link_query_continue)
    
    

        
        
            
    
