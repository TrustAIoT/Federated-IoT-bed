#GST_DEBUG=v4l2*:7 \
     gst-launch-1.0 -vvv libcamerasrc ! \
     video/x-raw,colorimetry=bt709,format=NV12,interlace-mode=progressive,width=1280,height=720,framerate=47/1 ! queue !\
     v4l2h264enc ! video/x-h264,level="(string)3.2" ! \
     rtph264pay config-interval=1 pt=96 ! \
     udpsink host=192.168.0.40 port=5000
