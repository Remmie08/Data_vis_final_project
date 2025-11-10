import pandas as pd
import numpy as np
import os

#GOALS SCORED BY TEAMS
goals_df = pd.read_csv(os.path.join("csv_files", "PremierLeague24_25(Goals).csv"), encoding="latin-1")
goals_df["Goals"] = 1
teams_goals = goals_df.groupby("Team")["Goals"].sum().reset_index()
player_goals = goals_df.groupby(["Team", "Scorer"])["Goals"].sum().reset_index()
teams_goals.to_csv("PremierLeague24_25(Teams_Goals).csv", index=False)
player_goals.to_csv("PremierLeague24_25(Player_Goals).csv", index=False)

#GOALS CONCEDED BY TEAMS
if 'Opponent' in goals_df.columns:
    goals_conceded = goals_df.groupby("Opponent")["Goals"].sum().reset_index()
    goals_conceded.columns = ["Team", "Goals_Conceded"]
    goals_conceded.to_csv("PremierLeague24_25(Goals_Conceded).csv", index=False)

#OPPOSITION SCORES (Head-to-Head)
if 'Opponent' in goals_df.columns:
    opposition_scores = goals_df.groupby(["Team", "Opponent", "Round"])["Goals"].sum().reset_index()
    opposition_scores.columns = ["Team", "Opponent", "Gameweek", "Goals_Scored"]
    opposition_scores = opposition_scores.sort_values(["Team", "Gameweek"])
    opposition_scores.to_csv("csv_files/PremierLeague24_25(Opposition_Scores).csv", index=False)

if 'Gameweek' in goals_df.columns and 'Opponent' in goals_df.columns:
    goals_conceded_gw = goals_df.groupby(["Opponent", "Gameweek"])["Goals"].sum().reset_index()
    goals_conceded_gw.columns = ["Team", "Gameweek", "Goals_Conceded"]
    goals_conceded_gw.to_csv("PremierLeague24_25(Goals_Conceded_By_Gameweek).csv", index=False)