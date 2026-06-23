import pandas as pd
import matplotlib.pyplot as plt

# Load cleaning Dataset

matches = pd.read_csv("Dataset/Cleaned_matches.csv")

print(matches.head())
print(matches.info())

# Top winning teams

team_wins = matches['winner'].value_counts()
print("Top winning teams: ")
print(team_wins)

# Top 10 winning teams graph 

team_wins.head(10).plot(kind='bar')

plt.title("Top 10 IPL winning Teams")
plt.xlabel("Teams")
plt.ylabel("Number of Wins")

plt.xticks(rotation=45)

plt.savefig("Output/Analysis.png")

plt.show()