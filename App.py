# Import Required Librares

import streamlit as st 
import pandas as pd 
import builtins
import matplotlib.pyplot as plt

# Dashboard Title

st.title("🏏 IPL stats dashboard")

# Dataset Load 

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv.zip")

# Season Filter in Sidebar

season = st.sidebar.selectbox(
    "Select Season",
    ["All"]+
    sorted(matches["season"].unique().tolist())
)

# Filter Data according to the selected season

if season != "All":
    match_ids = matches[matches["season"]==season]["id"]
    deliveries[deliveries["match_id"].isin(match_ids)]

# Dashboard Metrices

col1 , col2 , col3 = st.columns(3)

with col1:
    st.metric(
        "🏏Total Matches",
         len(matches)
    )

with col2:
    total_teams = len(
        builtins.set(matches["team1"].unique()).union(builtins.set(matches["team2"].unique())
    ))

    st.metric(
        "🫂Total Teams",
        total_teams
    )

    with col3:
        st.metric("🗓️Total Seasons",matches["season"].nunique())

st.write("Interactive IPL data Analysis")

# Sidebar menu 

option = st.sidebar.selectbox(
    "Selects IPL stats",
    [
        "Top Run Scorer",
        "Top Wicket Taker",
        "Most Sixes",
        "Winning Teams",
        "Most Fours",
        "Most Matches Played",
        "Teams Stats",
        "Player Search",
        "Season Stats",
        "Win Percentage"
    ]
)

# Top run getter table

if option == "Top Run Scorer":
    st.header("🏏 Top Run Scorers")

    runs = deliveries.groupby("batter")['batsman_runs'].sum()
    top_runs = (
        runs.sort_values(ascending=False).head(10).reset_index()
    )

    top_runs.columns = ["Players" , "Runs"]

    st.dataframe(top_runs)

# Top Run Getter Graph

    fig, ax = plt.subplots()
    ax.bar(top_runs["Players"],
    top_runs["Runs"])

    ax.set_xlabel("Players")
    ax.set_ylabel("Runs")
    ax.set_title("Top 10 Run Scorers")

    plt.xticks(rotation = 45)
    st.pyplot(fig)

# Top wicket taker

elif option == "Top Wicket Taker":
    st.header("⚾ Top Wicket Taker")

    wicket = deliveries[deliveries["is_wicket"]==1 & (deliveries["dismissal_kind"] != "run_out")]
    top_wickets = wicket.groupby("bowler").size()
    top_wickets = top_wickets.sort_values(ascending=False).head(10).reset_index()
    top_wickets.columns = ["Bowler" , "Wickets"]
    st.dataframe(top_wickets)

# Top wickets takers Graph

    fig, ax = plt.subplots()
    ax.bar(top_wickets["Bowler"],
    top_wickets["Wickets"])

    ax.set_xlabel("Bowler")
    ax.set_ylabel("Wickets")
    ax.set_title("Top 10 Wickets Takers")

    plt.xticks(rotation = 45)
    st.pyplot(fig)

# Top sixes hitters

elif option == "Most Sixes":
    st.header("🔥 Most Sixes Hitter")

    sixes = deliveries[deliveries['batsman_runs']==6]
    top_six = sixes.groupby("batter").size()
    top_six = top_six.sort_values(ascending=False).head(10).reset_index()
    top_six.columns = ["Players" , "Sixes"]
    st.dataframe(top_six)

# Top sixes Hitters Graph

    fig, ax = plt.subplots()
    ax.bar(top_six["Players"],
    top_six["Sixes"])

    ax.set_xlabel("Players")
    ax.set_ylabel("Sixes")
    ax.set_title("Top 10 Six Hitters")

    plt.xticks(rotation = 45)
    st.pyplot(fig)

# Top winning teams

elif option == "Winning Teams":
    st.header("🏆 Winning Teams")

    teams = matches['winner'].value_counts().reset_index()
    teams.columns = ["Team" , "Wins"]
    st.dataframe(teams)

# Top winning teams Graph

    fig, ax = plt.subplots(figsize=(10,8))
    ax.barh(teams["Team"],
    teams["Wins"])

    ax.set_xlabel("Wins")
    ax.set_ylabel("Team")
    ax.set_title("Top Winning Teams")

    
    plt.tight_layout()
    st.pyplot(fig)

# Top fours hitters

elif option == "Most Fours":
    st.header("🏏Most Fours Hitters")

    fours = deliveries[deliveries['batsman_runs']==4]
    top_fours = (
        fours.groupby("batter").size().sort_values(ascending=False).head(10).reset_index()
    )
    top_fours.columns = ["Players" , "Fours"]
    st.dataframe(top_fours)

# Top fours hitters Graph

    fig, ax = plt.subplots()
    ax.bar(top_fours["Players"],
    top_fours["Fours"])

    ax.set_xlabel("Players")
    ax.set_ylabel("Fours")
    ax.set_title("Top 10 Fours Hitters")

    plt.xticks(rotation = 45)
    st.pyplot(fig)

# Most matches played

elif option == "Most Matches Played":
    st.header("🏏Most Matches Played")

    matches_played = deliveries.groupby("batter")["match_id"].nunique()
    top_matches = (
        matches_played.sort_values(ascending=False).head(10).reset_index()
    )

    top_matches.columns = ["Players" , "Matches"]
    st.dataframe(top_matches)

# Teams stats

elif option == "Teams Stats":
    st.header("🏆Team performance")

    team = st.selectbox(
        "Select Team",
        matches['team1'].unique()
    )

    total_matches = matches[
        (matches["team1"]== team) | (matches["team2"]==team)
    ].shape[0]

    wins = matches[
        matches["winner"]== team
    ].shape[0]

    losses = total_matches - wins

    win_percentage = round(
        (wins/total_matches)*100.2
    )

    st.write("Team:",team)
    st.write("Total Matches:",total_matches)
    st.write("Wins:",wins)
    st.write("Losses:",losses)
    st.write("Win Percentage:",win_percentage, "%")

# players searching

elif option == "Player Search":
    st.header("🔍Player Stats")

    player = st.selectbox(
        "Select Player",
        deliveries["batter"].unique()
    )

    player_data = deliveries[deliveries["batter"]==player]
    total_runs = player_data["batsman_runs"].sum()

    total_sixes = player_data[player_data["batsman_runs"]==6].shape[0]
    total_fours = player_data[player_data["batsman_runs"]==4].shape[0]

    

    matches_played = player_data["match_id"].nunique()
    st.write("🏏Player:",player)
    st.write("Runs:",total_runs)
    st.write("Sixes:",total_sixes)
    st.write("Fours:",total_fours)
    st.write("Matches:",matches_played)

# Seasons stats

elif option == "Season Stats":
    st.header("🗓️Season Wise IPL Stats")

    season = st.selectbox(
        "Select Season",
        sorted(matches["season"].unique())
    )

    season_matches = matches[matches["season"]==season]
    st.write("Season:",season)
    st.write("Total Matches:",len(season_matches))

    # Teams
    team = pd.concat([
        season_matches["team1"],
        season_matches["team2"]
    ]).unique()

    st.write(
        "Teams Played:",len(team)
    )

# Win percentage

elif option == "Win Percentage":
    st.header("📊 Win Percentage")

total_matches = matches["winner"].value_counts()
total_played = pd.concat([
    matches["team1"],
    matches["team2"]
]).value_counts()

win_percent = (total_matches/total_played*100).round(2).reset_index()
win_percent.columns = ["Team","Win %"]

st.dataframe(win_percent)

# Top Win percentage Graph

fig, ax = plt.subplots(figsize=(10,6))
ax.bar(win_percent["Team"],
       win_percent["Win %"])

ax.set_xlabel("Team")
ax.set_ylabel("Win %")
ax.set_title("Win Percentage of IPL Teams")

plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)