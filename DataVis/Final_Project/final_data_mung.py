import pandas as pd
import numpy as np


goals_df = pd.read_csv("PremierLeague24_25(Goals).csv", encoding="latin-1")

goals_df["Goals"] = 1
teams_goals = goals_df.groupby("Team")["Goals"].sum().reset_index()
player_goals = goals_df.groupby(["Team", "Scorer"])["Goals"].sum().reset_index()


teams_goals.to_csv("PremierLeague24_25(Teams_Goals).csv", index=False)
player_goals.to_csv("PremierLeague24_25(Player_Goals).csv", index=False)