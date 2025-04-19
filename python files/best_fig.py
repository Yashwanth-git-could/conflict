import requests
import pandas as pd
from bs4 import BeautifulSoup
from sqlalchemy import create_engine

# MySQL connection using SQLAlchemy
engine = create_engine("mysql+mysqlconnector://root:Yashwanth%407@localhost/ipl_data")

# URL to scrape
url = 'https://www.cricket.com/series/indian-premier-league-2024-4554/stats/t20-bowling-best-figures'
page = requests.get(url=url)
soap = BeautifulSoup(page.text, 'html.parser')

# Extracting column names
thead = soap.find('thead')
trow = thead.find('tr')
columns = [i.text.strip() for i in trow]

# Create empty DataFrame
df = pd.DataFrame(columns=columns)

# Extract table data
tbody = soap.find('tbody')
tr = tbody.find_all('tr')
for i in tr:
    row_data = i.find_all('td')
    data = [i.text.strip() for i in row_data]
    df.loc[len(df)] = data
import re

# Extract Name and Team using Regex
def split_player_info(player_str):
    # Match shortform + Name + Team
    match = re.match(r'^[A-Z]{2}([A-Za-z\s\.]+?)([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)$', player_str)
    if match:
        name, team = match.groups()
        return pd.Series([name.strip(), team.strip()])
    return pd.Series([None, None])  # In case regex fails

# Apply the function
df[['Name', 'Team']] = df['Player'].apply(split_player_info)
df['Opponent'] = df['Opponent'].str.replace('vs ', '', regex=False)

# Drop the old 'Player' column if not needed
df = df.drop(columns=['Player'])
# Insert into MySQL using SQLAlchemy engine
df.to_sql('best_figures', con=engine, index=False, if_exists='replace')
