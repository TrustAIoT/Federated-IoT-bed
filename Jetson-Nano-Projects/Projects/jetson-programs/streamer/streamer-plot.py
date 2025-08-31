import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

import sys

# Get the Figure
#fig = plt.figure()
#ax = fig.add_subplot(1,1,1)
#ax.set_facecolor((1,1,1)) # Set the background to black

print("Location,Mean,Variance", file=open('plots/streamer-location-data.csv','w'))

def plot_data(filename):
	# Create a canvas window
	fig = plt.figure(filename)
	ax = fig.add_subplot(1, 1, 1)
	ax.set_facecolor((1, 1, 1))
	# Read the csv file
	record_df = pd.read_csv(filename + ".csv", sep=',', names=['Time', 'FPS'])
	record_df = record_df.iloc[50:]
	time = pd.to_numeric(record_df['Time'], downcast="integer")
	fps = pd.to_numeric(record_df['FPS'], downcast="float")
	# Plot the data
	ax.clear()
	ax.plot(time, fps, '-o', color = 'b')
	ax.set_xlabel("Frame Samples")
	ax.set_ylabel("Frame Rate")
	ax.set_title("Plot of Camera Frame Rate")
	fig.tight_layout() # To remove outside borders
	ax.yaxis.grid(True)
	# Calculate mean and variance
	print(filename)
	print("Mean = " +  str(fps.mean()))
	print("Variance = " + str(fps.var()))
	print(filename + ',' + str(fps.mean()) + ',' + str(fps.var()), file=open('plots/streamer-location-data.csv', 'a'))
	# Save the plot
	plt.savefig("./plots/" + filename + ".png")

# Show the plot
for index in range(1, len(sys.argv)):
	plot_data(sys.argv[index][:-4])
plt.show(block=False)
