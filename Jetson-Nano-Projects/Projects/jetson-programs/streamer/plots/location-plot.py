import matplotlib.pyplot as plt
import pandas as pd
# Get the Figure
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

def plot_data():
	ax.clear()
	location_df = pd.read_csv('streamer-location-data.csv', sep=',', header=0)
	location = location_df['Location']
	mean = pd.to_numeric(location_df['Mean'], downcast="float")
	std = pd.to_numeric(location_df['Variance'], downcast="float") ** 0.5
	# Lets add these lists xs, ys to the plot
	ax.clear()
	ax.bar(location, mean, yerr=std, color = (0,1,0.25))
	ax.set_xlabel("Location")
	plt.xticks(rotation=45)
	ax.set_ylabel("Average Frame Rate")
	ax.set_title("Camera Frame Rate at Different Location")
	fig.tight_layout() # To remove outside borders
	ax.yaxis.grid(True)

plot_data()
plt.show()
