import pandas as pd
import matplotlib.pyplot as plt 

# Load Dataset

matches = pd.read_csv("Dataset/Cleaned_matches.csv")
print(matches)

# Total played matches count

total_matches = matches['team1'].value_counts() + matches['team2'].value_counts()

# Total wins count

wins = matches['winner'].value_counts()

# logic win percentage

win_percentage = (wins/total_matches)*100

# Graph

win_percentage.sort_values(ascending=False).head(10).plot(kind='bar')
plt.title("Top 10 IPL teams win percentage")
plt.xlabel("teams")
plt.ylabel("Win percentage")
plt.xticks(rotation=45)

plt.savefig("Output/Win_percentage.png")

plt.show()