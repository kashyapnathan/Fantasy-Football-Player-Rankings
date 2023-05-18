import pandas as pd
from sklearn.linear_model import LinearRegression
import json

# Load the JSON file
with open('PlayerSeasonStats.json') as f:
    data = json.load(f)

# Create a DataFrame from the JSON data
df = pd.DataFrame(data)

# Define a dictionary to hold the equations for each position
equations = {
    "WR": lambda x: x["ReceivingYards"]*0.1 + x["ReceivingTouchdowns"]*6 - x["Fumbles"]*2 + x["RushingYards"]*0.1 + x["RushingTouchdowns"]*6 + x["TwoPointConversionRuns"]*2 + x["TwoPointConversionReceptions"]*2 + x["TwoPointConversionPasses"]*2,
    "QB": lambda x: x["PassingYards"]*0.04 - x["Interceptions"]*2 + x["PassingTouchdowns"]*4 - x["Fumbles"]*2,
    "RB": lambda x: x["RushingYards"]*0.1 + x["RushingTouchdowns"]*6 + x["ReceivingYards"]*0.1 + x["ReceivingTouchdowns"]*6 - x["Fumbles"]*2 + x["TwoPointConversionRuns"]*2 + x["TwoPointConversionReceptions"]*2 + x["TwoPointConversionPasses"]*2 + x["PassingYards"]*0.04 + x["PassingTouchdowns"]*4,
    "TE": lambda x: x["ReceivingYards"]*0.1 + x["ReceivingTouchdowns"]*6 - x["Fumbles"]*2 + x["RushingYards"]*0.1 + x["RushingTouchdowns"]*6,
    "K": lambda x: x["FieldGoalsMade"]*3 + x["ExtraPointsMade"],
    "DT": lambda x: x["Tackles"] + x["Sacks"]*2,
    "DE": lambda x: x["Tackles"] + x["Sacks"]*2,
    "CB": lambda x: x["Tackles"] + x["Interceptions"]*2 + x["Sacks"]*2,
    "S": lambda x: x["Tackles"] + x["Interceptions"]*2 + x["Sacks"]*2,
}

# Define a dictionary to hold the rankings for each position
rankings = {}

# For each position and equation in the equations dictionary, filter the DataFrame to only include players in the current position, calculate the score for each player, sort the DataFrame by the score, and add the DataFrame to the rankings dictionary. 
for position, equation in equations.items():
    # Filter the DataFrame to only include players in the current position
    position_df = df[df["Position"] == position].copy()

    # Check if the DataFrame is empty
    if position_df.empty:
        print(f"No players found for position {position}")
        continue

    # Calculate the score for each player
    scores = position_df.apply(equation, axis=1)
    position_df.loc[:, "Score"] = scores

    # Sort the DataFrame by the score
    position_df = position_df.sort_values(by="Score", ascending=False)
    rankings[position] = position_df



# Print the rankings for each position
for position, df in rankings.items():
    print(f"{position} Rankings:")
    top35 = df[["Name", "Score"]].head(35)
    top35.columns = [f"{column}," for column in top35.columns]
    print(top35.to_string(index=False))
    print()
    bottom5 = df[["Name", "Score"]].tail(5)
    bottom5.columns = [f"{column}," for column in bottom5.columns]
    print("Last 5 Scores:")
    print(bottom5.to_string(index=False))
    print("\n")

# Get the list of teams
teams = df['Team'].unique()

# Store the team scores
team_scores = {}

# For each team in the list, using the scores from the DT, DE, CB, and S positions, add the scores together and store them in the team_scores dictionary
for team in teams:
    team_df = df[df['Team'] == team]
    team_score = team_df.loc[team_df['Position'].isin(['DT', 'DE', 'CB', 'S']), 'Score'].sum()
    team_scores[team] = team_score

# Convert the dictionary to a DataFrame
team_scores_df = pd.DataFrame.from_dict(team_scores, orient='index', columns=['Score'])

# Sort the DataFrame by score
team_scores_df = team_scores_df.sort_values(by='Score', ascending=False)

# Print the team scores
print("Defense Scores:")
print(team_scores_df.to_string())
