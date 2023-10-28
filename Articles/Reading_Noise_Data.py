# graphing library
import matplotlib.pyplot as plt

# reading in my data
import pandas as pd

# read in the document
df = pd.read_excel("Articles/readingData.xlsx")

#grab the headers
headers = df.columns

sounds = set()

for i in df['Sound Type']:
    sounds.add(i)
    
# create a dictionary of avg reading speeds (pgs/min)
avg_speeds = {}

for sound in sounds:
    timesForThisSound = df.loc[df["Sound Type"] == sound, 'Total time in minutes']
    pgsForThisSound = df.loc[df["Sound Type"] == sound, 'Pages Read']
    speedsForThisSound = [pgs / time for pgs, time in zip(pgsForThisSound,timesForThisSound)]
    avg_speeds[sound] = round(sum(speedsForThisSound) / len(speedsForThisSound), 2)

# get the x axis labels and the heights for each one
x_labels = list(sounds)
heights = [avg_speeds.get(x,0) for x in x_labels]

# colors for the bars
colors = ['chocolate', 'mediumseagreen', 'mediumpurple', 
          'lightsteelblue', 'lightyellow', 'lightcyan'
          , 'snow']

# background color
plt.figure(facecolor='black')

# plot the values
plt.bar(x_labels, heights, color=colors)

# background color
plt.gca().set_facecolor('black')

# Customize the color of the axes
ax = plt.gca()
ax.spines['bottom'].set_color('white')  # X-axis
ax.spines['top'].set_color('white')     # X-axis
ax.spines['left'].set_color('white')     # Y-axis
ax.spines['right'].set_color('white')    # Y-axis
ax.tick_params(colors="white")

# put the values of each bar on top
for x, y in zip(x_labels, heights):
    plt.text(x, y, str(y), ha='center', va='bottom', color='white')

# label the axis's
plt.xlabel("Sounds", fontweight='bold', color='white')
plt.ylabel("Average Reading Speed (page/minute)", fontweight='bold', color='white')
plt.title("Sounds vs. Reading Speed", color='white')
plt.show()
