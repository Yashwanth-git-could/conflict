import requests
import pandas as pd
from bs4 import BeautifulSoup
from sqlalchemy import create_engine

# MySQL connection using SQLAlchemy
engine = create_engine("mysql+mysqlconnector://root:Yashwanth%407@localhost/ipl_data")

import pandas as pd

teams = [
    "Kolkata Knight Riders", "Kolkata Knight Riders",
    "Sunrisers Hyderabad", "Sunrisers Hyderabad",
    "Rajasthan Royals", "Rajasthan Royals",
    "Royal Challengers Bengaluru", "Royal Challengers Bengaluru",
    "Chennai Super Kings", "Chennai Super Kings",
    "Delhi Capitals", "Delhi Capitals",
    "Lucknow Super Giants", "Lucknow Super Giants",
    "Gujarat Titans", "Gujarat Titans",
    "Punjab Kings", "Punjab Kings",
    "Mumbai Indians", "Mumbai Indians"
]

# Take alternate entries (only one per team)
unique_teams = teams[::2]
stats = [
    [14, 9, 3, 2, 20, "+1.428Q"],
    [14, 8, 5, 1, 17, "+0.414Q"],
    [14, 8, 5, 1, 17, "+0.273Q"],
    [14, 7, 7, 0, 14, "+0.459Q"],
    [14, 7, 7, 0, 14, "+0.392"],
    [14, 7, 7, 0, 14, "-0.377"],
    [14, 7, 7, 0, 14, "-0.667"],
    [14, 5, 7, 2, 12, "-1.063"],
    [14, 5, 9, 0, 10, "-0.353"],
    [14, 4, 10, 0, 8, "-0.318"]
]

columns = ["Team", "P", "W", "L", "NR", "PTS", "NRR"]

df = pd.DataFrame(columns=columns)
for i in range(len(unique_teams)):
    df.loc[i] = [unique_teams[i]] + stats[i]

# Optional: remove 'Q' from NRR and add a separate 'Qualified' column
df['Qualified'] = df['NRR'].apply(lambda x: 'Qualified' if 'Q' in x else 'Not Qualified')
df['NRR'] = df['NRR'].str.replace('Q', '')

# Insert into MySQL using SQLAlchemy engine
df.to_sql('points_table', con=engine, index=False, if_exists='replace')
