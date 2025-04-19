def team_vs_team():
        
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import mysql.connector

    # Connect to MySQL
    mydb = mysql.connector.connect(
        user='root',
        host='localhost',
        password='Yashwanth@7',
        database='ipl_data'
    )
    cursor = mydb.cursor()

    # Load team_vs_team table
    cursor.execute('SELECT * FROM team_vs_team')
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=columns)

    # Clean opposition names
    df.rename(columns={'oppisition': 'Opposition'}, inplace=True)
    df['Opposition'] = df['Opposition'].str.replace('vs ', '', regex=False)

    # IPL 2024 teams (you can update this list if there are changes in teams)
    ipl_teams_2024 = [
        'Mumbai Indians', 'Chennai Super Kings', 'Royal Challengers Bangalore', 
        'Delhi Capitals', 'Kolkata Knight Riders', 'Rajasthan Royals', 
        'Punjab Kings', 'Sunrisers Hyderabad', 'Lucknow Super Giants', 'Gujarat Titans'
    ]

    # Filter the data to only include the current IPL 2024 teams
    df_ipl2024 = df[df['Team'].isin(ipl_teams_2024)]

    # Further filter the data to ensure that the opposition is also one of the IPL 2024 teams
    df_ipl2024 = df_ipl2024[df_ipl2024['Opposition'].isin(ipl_teams_2024)]

    # Unique teams for the current IPL season
    teams = df_ipl2024['Team'].unique()

    # Plot setup
    fig, axs = plt.subplots(nrows=2, ncols=5, figsize=(24, 10))
    axs = axs.flatten()

    # Colors for bars
    colors = ['skyblue', 'lightgreen', 'salmon']

    for i, team in enumerate(teams):
        ax = axs[i]
        team_df = df_ipl2024[df_ipl2024['Team'] == team]
        oppositions = team_df['Opposition'].apply(lambda x: ''.join([word[0] for word in x.split()]))

        x = np.arange(len(oppositions))
        width = 0.25

        ax.bar(x - width, team_df['M'], width=width, label='Matches', color=colors[0])
        ax.bar(x, team_df['W'], width=width, label='Wins', color=colors[1])
        ax.bar(x + width, team_df['L'], width=width, label='Losses', color=colors[2])

        ax.set_title(team, fontsize=12, color='navy')
        ax.set_xticks(x)
        ax.set_xticklabels(oppositions, rotation=45, ha='right', fontsize=9)
        ax.grid(axis='y', linestyle='--', alpha=0.6)

    # Add legend to the last subplot only
    axs[-1].legend(loc='upper center', bbox_to_anchor=(0.3, -0.15), ncol=4)

    fig.suptitle("IPL 2024 – Team vs Opposition Performance (Matches / Wins / Losses)", fontsize=18, fontfamily='Times New Roman', color='darkblue')
    plt.tight_layout(rect=[0.01, 0.01, 1, 0.95])
    plt.subplots_adjust(hspace=0.5)
    plt.show()
