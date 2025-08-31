import sys
import argparse
import os
import _thread

from jetson.utils import videoSource, videoOutput

# parse command line
parser = argparse.ArgumentParser(description="View various types of video streams", 
                                 formatter_class=argparse.RawTextHelpFormatter, 
                                 epilog=videoSource.Usage() + videoOutput.Usage())

parser.add_argument("input", type=str, help="URI of the input stream")
parser.add_argument("output", type=str, default="", nargs='?', help="URI of the output stream")

try:
	args = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)

# create video sources & outputs
input = videoSource(args.input, argv=sys.argv)    # default:  options={'width': 1280, 'height': 720, 'framerate': 30}
output = videoOutput(args.output, argv=sys.argv)  # default:  options={'width': 1280, 'height': 720, 'framerate': 30}

# prepare a csv file for storage
print("Time, FPS", file=open("streamer-record.csv", "w"))

def start():
	# capture frames until EOS or user exits
	numFrames = 0

	while True:
	    # capture the next image
	    img = input.Capture()

	    if img is None: # timeout
	        continue

	    numFrames += 1

	    # render the image
	    output.Render(img)

	    # update the title bar
	    output.SetStatus("Video Viewer | {:d}x{:d} | {:.1f} FPS".format(img.width, img.height, output.GetFrameRate()))

	    # print the fps to csv
	    print(str(numFrames) + "," + str(output.GetFrameRate()), file=open("streamer-record.csv", "a"))

	    # exit on input/output EOS
	    if not input.IsStreaming() or not output.IsStreaming() or numFrames > 1000:
	        break

def plot():
	os.system("python3 streamer-plot.py")

#_thread.start_new_thread(plot, ())
start()


