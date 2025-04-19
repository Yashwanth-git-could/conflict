def runs():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import mysql.connector

    # MySQL connection and data fetch
    mydb = mysql.connector.connect(user='root', host='localhost', password='Yashwanth@7', database='ipl_data')
    cursor = mydb.cursor()

    # Fetch team_runs data
    cursor.execute('select * from team_runs')
    columns1 = [col[0] for col in cursor.description]
    data1 = cursor.fetchall()
    df1 = pd.DataFrame(data=data1, columns=columns1)

    # Create a 2x2 subplot grid
    fig, axs = plt.subplots(2, 2, figsize=(9, 9))
    plt.suptitle("Comprehensive IPL Teams Batting Performance", fontsize=20, fontfamily='Times New Roman', color='navy')

    cmap = plt.get_cmap('tab20')
    colors = [cmap(i) for i in range(len(df1))]

    # Plot 1 - Total Matches Played (sorted)
    sorted_df1 = df1.sort_values(by='Mat', ascending=False)
    teams1 = sorted_df1['Team'].apply(lambda x: ''.join([word[0] for word in x.split()]))
    matches = sorted_df1['Mat']

    bars1=axs[0, 0].bar(teams1, matches, color=colors, width=0.5)
    axs[0, 0].set_title('Total Matches Played', fontdict={'color':'navy','family':'Times New Roman','size':'12'})
    axs[0, 0].set_xlabel('Teams', fontdict={'color':'maroon','family':'Times New Roman','size':'10'})
    axs[0, 0].set_ylabel('Matches', fontdict={'color':'maroon','family':'Times New Roman','size':'10'})
    axs[0, 0].grid(True, linestyle='--', alpha=0.3)
    for bar in bars1:
        axs[0, 0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, int(bar.get_height()), 
                    ha='center', va='bottom', fontsize=8, color='black')
    axs[0,0].spines['top'].set_visible(False)
    axs[0,0].spines['right'].set_visible(False)


    # Plot 2 - Runs Scored (sorted)
    sorted_df2 = df1.sort_values(by='Runs', ascending=False)
    teams2 = sorted_df2['Team'].apply(lambda x: ''.join([word[0] for word in x.split()]))
    runs = sorted_df2['Runs']

    bars2=axs[0, 1].bar(teams2, runs, color=colors, width=0.5)
    axs[0, 1].set_title('Runs Scored', fontdict={'color':'navy','family':'Times New Roman','size':'12'})
    axs[0, 1].set_xlabel('Teams', fontdict={'color':'maroon','family':'Times New Roman','size':'10'})
    axs[0, 1].set_ylabel('Runs', fontdict={'color':'maroon','family':'Times New Roman','size':'10'})
    axs[0, 1].grid(True, linestyle='--', alpha=0.3)
    for bar in bars2:
        axs[0, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, int(bar.get_height()), ha='center', va='bottom', fontsize=8, color='black')
    axs[0,1].spines['top'].set_visible(False)
    axs[0,1].spines['right'].set_visible(False)

    # Plot 3 - Balls Faced (sorted)
    sorted_df3 = df1.sort_values(by='BF', ascending=False)
    teams3 = sorted_df3['Team'].apply(lambda x: ''.join([word[0] for word in x.split()]))
    balls_faced = sorted_df3['BF']

    bars3=axs[1, 0].bar(teams3, balls_faced, color=colors, width=0.5)
    axs[1, 0].set_title('Balls Faced', fontdict={'color':'navy','family':'Times New Roman','size':'12'})
    axs[1, 0].set_xlabel('Teams', fontdict={'color':'maroon','family':'Times New Roman','size':'10'})
    axs[1, 0].set_ylabel('Balls', fontdict={'color':'maroon','family':'Times New Roman','size':'10'})
    axs[1, 0].grid(True, linestyle='--', alpha=0.3)
    for bar in bars3:
        axs[1, 0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, int(bar.get_height()), ha='center', va='bottom', fontsize=8, color='black')
    axs[1,0].spines['top'].set_visible(False)
    axs[1,0].spines['right'].set_visible(False)

    # Plot 4 - Duck Outs vs Not Outs (sorted by total of both)
    sorted_df4 = df1.copy()
    sorted_df4['Total'] = sorted_df4['Duck Outs'] + sorted_df4['NO']
    sorted_df4 = sorted_df4.sort_values(by='Total', ascending=False)

    teams4 = sorted_df4['Team'].apply(lambda x: ''.join([word[0] for word in x.split()]))
    not_outs = sorted_df4['NO']
    duck_outs = sorted_df4['Duck Outs']
    index = np.arange(len(teams4))
    width = 0.3

    bars4=axs[1, 1].bar(index - width/2, not_outs, width=width, color='limegreen', label='Not Outs')
    bars5=axs[1, 1].bar(index + width/2, duck_outs, width=width, color='darkred', label='Duck Outs')
    axs[1, 1].set_title('Duck Outs vs Not Outs', fontdict={'color':'navy','family':'Times New Roman','size':'12'})
    axs[1, 1].set_xlabel('Teams', fontdict={'color':'maroon','family':'Times New Roman','size':'10'})
    axs[1, 1].set_ylabel('Count', fontdict={'color':'maroon','family':'Times New Roman','size':'10'})
    axs[1, 1].set_xticks(index)
    axs[1, 1].set_xticklabels(teams4, rotation=45)
    axs[1, 1].grid(True, linestyle='--', alpha=0.3)
    axs[1, 1].legend()
    for bar in bars4:
        axs[1, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, int(bar.get_height()), ha='center', va='bottom', fontsize=8, color='black')
    for bar in bars5:
        axs[1, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, int(bar.get_height()), ha='center', va='bottom', fontsize=8, color='black')
    axs[1,1].spines['top'].set_visible(False)
    axs[1,1].spines['right'].set_visible(False)

    # Final layout adjustments
    plt.tight_layout(rect=[0, 0.03, 0.95, 0.95])
    plt.subplots_adjust(hspace=0.4)
    plt.show()
