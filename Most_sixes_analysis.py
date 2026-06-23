import pandas as pd 
import matplotlib.pyplot as plt

# Dataset load

deliveries = pd.read_csv("Dataset/deliveries.csv.zip")
print(deliveries)

# Analysis sixes balls only

sixes = deliveries[deliveries['batsman_runs']==6]
six_count = sixes.groupby('batter').size().sort_values(ascending=False).head(10)

# graph 

six_count.plot(kind='bar')
plt.title("Top 10 six hitters")
plt.xlabel("players")
plt.ylabel("Number of sixes")
plt.xticks(rotation=45)

plt.savefig("Output/Most_sixes_analysis.png")

plt.show()