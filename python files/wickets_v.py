def wickets():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import mysql.connector

    # MySQL connection and data fetch
    mydb = mysql.connector.connect(user='root', host='localhost', password='Yashwanth@7', database='ipl_data')
    cursor = mydb.cursor()

    # Fetch team_wickets data
    cursor.execute('SELECT * FROM team_wickets')
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    df = pd.DataFrame(data=data, columns=columns)

    # Create 2x2 subplot grid
    fig, axs = plt.subplots(2, 2, figsize=(10, 9))
    plt.suptitle("Comprehensive IPL Team Bowling Performance", fontsize=18, fontfamily='Times New Roman', color='darkblue')

    cmap = plt.get_cmap('tab20')
    colors = [cmap(i) for i in range(len(df))]

    # Plot 1 - Total Wickets
    sorted_df1 = df.sort_values(by='Wickets', ascending=False)
    teams = sorted_df1['Team'].apply(lambda x: ''.join([word[0] for word in x.split()]))
    wickets = sorted_df1['Wickets']

    bars1 = axs[0, 0].bar(teams, wickets, color=colors, width=0.5)
    axs[0, 0].set_title('Total Wickets', fontsize=12, fontfamily='Times New Roman', color='navy')
    axs[0, 0].set_xlabel('Teams', fontsize=10, color='maroon', fontfamily='Times New Roman')
    axs[0, 0].set_ylabel('Wickets', fontsize=10, color='maroon', fontfamily='Times New Roman')
    axs[0, 0].grid(True, linestyle='--', alpha=0.3)
    for bar in bars1:
        axs[0, 0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, int(bar.get_height()),
                    ha='center', va='bottom', fontsize=8, color='black')
    axs[0, 0].spines['top'].set_visible(False)
    axs[0, 0].spines['right'].set_visible(False)

    # Plot 2 - Runs Conceded
    sorted_df2 = df.sort_values(by='Runs', ascending=False)
    teams2 = sorted_df2['Team'].apply(lambda x: ''.join([word[0] for word in x.split()]))
    runs = sorted_df2['Runs']

    bars2 = axs[0, 1].bar(teams2, runs, color=colors, width=0.5)
    axs[0, 1].set_title('Runs Conceded', fontsize=12, fontfamily='Times New Roman', color='navy')
    axs[0, 1].set_xlabel('Teams', fontsize=10, color='maroon', fontfamily='Times New Roman')
    axs[0, 1].set_ylabel('Runs', fontsize=10, color='maroon', fontfamily='Times New Roman')
    axs[0, 1].grid(True, linestyle='--', alpha=0.3)
    for bar in bars2:
        axs[0, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, int(bar.get_height()),
                    ha='center', va='bottom', fontsize=8, color='black')
    axs[0, 1].spines['top'].set_visible(False)
    axs[0, 1].spines['right'].set_visible(False)

    # Plot 3 - Overs Bowled
    sorted_df3 = df.sort_values(by='Overs', ascending=False)
    teams3 = sorted_df3['Team'].apply(lambda x: ''.join([word[0] for word in x.split()]))
    overs = sorted_df3['Overs']

    bars3 = axs[1, 0].bar(teams3, overs, color=colors, width=0.5)
    axs[1, 0].set_title('Overs Bowled', fontsize=12, fontfamily='Times New Roman', color='navy')
    axs[1, 0].set_xlabel('Teams', fontsize=10, color='maroon', fontfamily='Times New Roman')
    axs[1, 0].set_ylabel('Overs', fontsize=10, color='maroon', fontfamily='Times New Roman')
    axs[1, 0].grid(True, linestyle='--', alpha=0.3)
    for bar in bars3:
        axs[1, 0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, round(bar.get_height(), 1),
                    ha='center', va='bottom', fontsize=8, color='black')
    axs[1, 0].spines['top'].set_visible(False)
    axs[1, 0].spines['right'].set_visible(False)

    # Plot 4 - 4W vs 5W Hauls
    sorted_df4 = df.copy()
    sorted_df4['Total_Hauls'] = sorted_df4['4W'] + sorted_df4['5W']
    sorted_df4 = sorted_df4.sort_values(by='Total_Hauls', ascending=False)

    teams4 = sorted_df4['Team'].apply(lambda x: ''.join([word[0] for word in x.split()]))
    fours = sorted_df4['4W']
    fives = sorted_df4['5W']
    index = np.arange(len(teams4))
    width = 0.3

    bars4 = axs[1, 1].bar(index - width/2, fours, width=width, color='skyblue', label='4W')
    bars5 = axs[1, 1].bar(index + width/2, fives, width=width, color='orange', label='5W')
    axs[1, 1].set_title('4W vs 5W Hauls', fontsize=12, fontfamily='Times New Roman', color='navy')
    axs[1, 1].set_xlabel('Teams', fontsize=10, color='maroon', fontfamily='Times New Roman')
    axs[1, 1].set_ylabel('Hauls', fontsize=10, color='maroon', fontfamily='Times New Roman')
    axs[1, 1].set_xticks(index)
    axs[1, 1].set_xticklabels(teams4, rotation=45)
    axs[1, 1].grid(True, linestyle='--', alpha=0.3)
    axs[1, 1].legend()
    for bar in bars4:
        axs[1, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, int(bar.get_height()),
                    ha='center', va='bottom', fontsize=8, color='black')
    for bar in bars5:
        axs[1, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, int(bar.get_height()),
                    ha='center', va='bottom', fontsize=8, color='black')
    axs[1, 1].spines['top'].set_visible(False)
    axs[1, 1].spines['right'].set_visible(False)

    # Final layout
    plt.tight_layout(rect=[0, 0.03, 0.95, 0.95])
    plt.subplots_adjust(hspace=0.4)
    plt.show()
