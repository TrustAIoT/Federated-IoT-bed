from apscheduler.schedulers.background import BackgroundScheduler
import socket
import subprocess
import psutil
import time
import logging
from datetime import datetime
try:
	import pynvml
	pynvml.nvmlInit()
except:
	no_nvidia_smi = True
else:
	no_nvidia_smi = False

class DeviceInfo(object):
    def __init__(self, args, comp_callback, network_callback):
        self.args = args
        self.destination_MAC = str(self.args.server_mac_address)
        self.comp_callback = comp_callback
        self.network_callback = network_callback
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        self.scheduler.add_job(self.updateAlfredCompInfo, 'interval',  seconds=5)
        self.scheduler.add_job(self.updateAlfredNetworkInfo, 'interval', seconds=30)
        for job in self.scheduler.get_jobs():
            job.modify(next_run_time=datetime.now())
    def __del__(self):
        self.scheduler.shutdown()

    def updateAlfredCompInfo(self):
        #print("Update Computation")
        cpu_percent = psutil.cpu_percent()
        cpu_memory_percent = psutil.virtual_memory().percent
        gpu_memory = {}
        if not no_nvidia_smi:
            gpu_memory["Has Nvidia Driver"] = True
            deviceCount = pynvml.nvmlDeviceGetCount()
            for device in range(deviceCount):
                memory_info = {}
                handle = pynvml.nvmlDeviceGetHandleByIndex(device)
                info = pynvml.nvmlDeviceGetMemoryInfo(handle)
                memory_info["total"] = info.total
                memory_info["free"] = info.free
                memory_info["used"] = info.used
                memory_info["percent"] = info.used / info.total
                gpu_memory["gpu" + str(device)] = memory_info
        else:
            gpu_memory["Has Nvidia Driver"] = False
        message = {"cpu_percent": cpu_percent, "cpu_memory_percent": cpu_memory_percent, "gpu_memory": gpu_memory}
        self.comp_callback(message)
        
    def updateAlfredNetworkInfo(self):
        #print("Update Network")
        pingInfo = self.getNeighborsPing(self.destination_MAC)
        linkInfo = self.getNeighborsLinkQuality()
        throughputInfo = self.getNeighborsThroughput(self.destination_MAC, 5000)
        networkInfo = {"throughput": throughputInfo, 
                         "packetLoss": pingInfo["packetInfo"],
                         "roundTripTime": pingInfo["roundTripTimeInfo"],
                         "linkQuality": linkInfo}
        self.network_callback(networkInfo)
        
    def getNeighborsThroughput(self, destinationMAC, duration=1000):
        #print("Start Throughput")
        throughputInfo = ""
        # Retry if batctl is not ready
        for _ in range(10):
            try :
                sudo_echo = subprocess.Popen(['echo', self.args.sudo_password], stdout=subprocess.PIPE)
                result = subprocess.run(['sudo', '-S', 'batctl', 'tp', '-t', str(int(duration)), destinationMAC],
                                        stdin=sudo_echo.stdout, stdout=subprocess.PIPE).stdout.decode('utf-8')[:-1]
                result = result.split('\n')
                throughputInfo = result[-1].split('(')[1].split(')')[0]
            except:
                time.sleep(2)
                continue
            else:
                break
        else:
            throughputInfo = "batctl is not ready"
        #print(throughputInfo)
        return throughputInfo

    def getNeighborsPing(self, destinationMAC, packetCount=5):
        #print("Start Ping")
        pingInfo = ""
        # Send a packet every 1 seconds (lowest possible)
        sudo_echo = subprocess.Popen(['echo', self.args.sudo_password], stdout=subprocess.PIPE)
        result = subprocess.run(['sudo', '-S', 'batctl', 'ping', destinationMAC, '-c', str(packetCount), '-i', "1"], 
                                stdin=sudo_echo.stdout, stdout=subprocess.PIPE).stdout.decode('utf-8')[:-1]
        #logging.info(result)
        result = result.split('\n')
        # Packet info contain the percent of packet loss
        packetInfo = float(result[-2].split('%')[0].split(' ')[-1])/100
        # Round trip time in ping is in format min/avg/max/mdev
        roundTripTimeInfo = result[-1].split('=')[1].split('/')[1]

        pingInfo = {"packetInfo": packetInfo, "roundTripTimeInfo": roundTripTimeInfo}
        #print(pingInfo)
        return pingInfo

    def getNeighborsLinkQuality(self):
        #print("Start Link")
        linkInfo = ""
        sudo_echo = subprocess.Popen(['echo', self.args.sudo_password], stdout=subprocess.PIPE)
        result = subprocess.run(['sudo', '-S', 'batctl', 'o'], stdin=sudo_echo.stdout, 
                                stdout=subprocess.PIPE).stdout.decode('utf-8')
        result = subprocess.run(['grep', '*'], stdout=subprocess.PIPE,
                                input=result.encode('utf-8')).stdout.decode('utf-8')[:-1]
        originators = result.split('\n')
        for originator in originators:
            originatorMAC = originator.split()[1]
            if originatorMAC == self.destination_MAC:
                linkQuality = originator.split("(")[1].split(")")[0]
                linkInfo = linkQuality
                break
        #print(linkInfo)
        return linkInfo
