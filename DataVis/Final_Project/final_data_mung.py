import pandas as pd
import numpy as np

positions_df = pd.read_csv("PremierLeague24_25(Positions).csv")
old_positions_df = pd.read_csv("PremierLeague24_25(Old_Positions).csv")
goals_df = pd.read_csv("PremierLeague24_25(Goals).csv", encoding="latin-1")

print(positions_df.head())
print(old_positions_df.head()) 

print(positions_df.shape)
print(old_positions_df.shape)

def clean_dataframe(df):
    df = df.copy()
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.replace(r"\s+", "_", regex=True)
        .str.replace(r"[^\w_]", "", regex=True)
    )
    for c in df.select_dtypes(include="object").columns:
        df[c] = df[c].astype(str).str.strip()
    return df

positions_df = clean_dataframe(positions_df)
old_positions_df = clean_dataframe(old_positions_df)

print("Cleaned old_positions_df:")
print(old_positions_df.head())
print(old_positions_df.shape)

print("Cleaned positions_df shape:")
print(positions_df.shape)
print("Cleaned old_positions_df shape:")
print(old_positions_df.shape)

for df in (positions_df, old_positions_df):
    if "team" in df.columns:
        df["team"] = df["team"].astype(str).str.replace(r"\s+", " ", regex=True).str.strip()


print("Cleaned Teams in positions_df:")
print(positions_df.head())
print("Cleaned Teams in old_positions_df:")
print(old_positions_df.head()) 


# Rename numeric gameweek columns to have 'GW' prefix
# old_positions_df is already pivoted, so gameweeks are columns, not rows
column_mapping = {}
for col in old_positions_df.columns:
    if col != 'team' and str(col).isdigit():
        column_mapping[col] = 'GW' + str(col)
    else:
        column_mapping[col] = col

GW_old_positions_df = old_positions_df.rename(columns=column_mapping) 

#gameweek (GW) is its own column
print(GW_old_positions_df.head())

#code for data munging the goals csv file
goals_df["Goals"] = 1
teams_goals = goals_df.groupby("Team")["Goals"].sum().reset_index()
player_goals = goals_df.groupby(["Team", "Scorer"])["Goals"].sum().reset_index()



positions_df.to_csv("PremierLeague24_25(Clean_Positions).csv", index=False)
old_positions_df.to_csv("PremierLeague24_25(Clean_Old_Positions).csv", index=False)
GW_old_positions_df.to_csv("PremierLeague24_25(Clean_GW_Old_Positions).csv", index=False)
teams_goals.to_csv("PremierLeague24_25(Teams_Goals).csv", index=False)
player_goals.to_csv("PremierLeague24_25(Player_Goals).csv", index=False)