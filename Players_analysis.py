import pandas as pd
import matplotlib.pyplot as plt


# Load deliveries dataset 

deliveries = pd.read_csv("Dataset/deliveries.csv.zip")
print(deliveries.head())
print(deliveries.info())

# Top batsman by runs

batsman_run = deliveries.groupby('batter')['batsman_runs'].sum()
top_batsman = batsman_run.sort_values(ascending=False).head(10)
print("Top 10 run scorers: ")
print(top_batsman)

# graphs

top_batsman.plot(kind='bar')
plt.title("Top 10 run scorers")
plt.xlabel("players")
plt.ylabel("Runs")
plt.xticks(rotation=45)

plt.savefig("Output/Top_run_scorer.png")

plt.show()

# Top wickets taker

wickets = deliveries[deliveries['is_wicket']==1]
bowler_wickets = wickets.groupby('bowler').size()

top_bowlers = bowler_wickets.sort_values(ascending=False).head(10)

print("Top 10 wickets Taker: ")
print(top_bowlers)

# graph

top_bowlers.plot(kind='bar')
plt.title("Top 10 IPL wickets taker")
plt.xlabel("Bowlers")
plt.ylabel("wickets")
plt.xticks(rotation=45)

plt.savefig("Output/Top_wicket_taker.png")

plt.show()
