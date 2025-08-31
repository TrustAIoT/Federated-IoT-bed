import cv2
import signal
import sys

print(cv2.getBuildInformation())

host_address = '192.168.0.40'
host_port = 5000


# Receieve from UDP Protocol
camSettings = 'udpsrc'
# Set the listener on address and port
camSettings+= ' port=' + str(host_port) + ' multicast-group=' + host_address
camSettings+= ' auto-multicast=true'
# Set the cap for the data received
camSettings+= ' caps="application/x-rtp,media=video,clock-rate=90000,encoding-name=H264,payload=96"'
# Remove the RTP payload
camSettings+= ' ! rtph264depay'
#camSettings+= ' ! h264parse ! v4l2h264dec ! videoconvert ! appsink '
# Parse to h264 encoding
camSettings+= ' ! h264parse'
camSettings+= ' ! nvv4l2decoder ! nvvidconv ! video/x-raw, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink drop=1'
'''
# Decode the h264 with hardware decoding
camSettings+= ' ! omxh264dec'
#camSettings+= ' ! avdec_h264'
# Set the format to raw video
#camSettings+= ' ! video/x-raw ! nvvidconv ! video/x-raw, format=NV12 '
camSettings+= ' ! video/x-raw '
# Set the sink to application-based
camSettings+= ' ! appsink drop=1'
'''
print(camSettings)

# Capture the video
cam=cv2.VideoCapture(camSettings, cv2.CAP_GSTREAMER)
#cam = cv2.VideoCapture("rtp://192.168.0.40:5000")

if not cam.isOpened():
	print('Failed to open camera')
	sys.exit(0)


def sigterm_handler(signal, frame):
	terminate()
	sys.exit(0)
def terminate():
	cam.release()
	cv2.destroyAllWindows()

signal.signal(signal.SIGTERM, sigterm_handler)

while True:
	# Capture the next frame
	ret, frame = cam.read()
	cv2.imshow("Camera", frame)
	cv2.moveWindow("Camera", 0, 0)
	if cv2.waitKey(1)==ord('q'):
		terminate()
