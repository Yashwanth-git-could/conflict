def catches_and_dis():
    import pandas as pd
    import matplotlib.pyplot as plt
    import mysql.connector

    # Connect to the MySQL database
    mydb = mysql.connector.connect(
        user='root',
        host='localhost',
        password='Yashwanth@7',
        database='ipl_data'
    )
    cursor = mydb.cursor()

    # Load most_catches table into DataFrame
    cursor.execute('SELECT * FROM most_catches')
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    df1 = pd.DataFrame(data=data, columns=columns)

    # Load most_dis table into DataFrame
    cursor.execute('SELECT * FROM most_dis')
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    df2 = pd.DataFrame(data=data, columns=columns)

    # Convert Catches and Dismissals to integers
    df1['Catches'] = df1['Catches'].astype(int)
    df2['Dismissals'] = df2['Dismissals'].astype(int)

    # Sort the DataFrames
    sorted_df1 = df1.sort_values(by='Catches', ascending=False)
    sorted_df2 = df2.sort_values(by='Dismissals', ascending=True)

    # Plotting
    fig, axs = plt.subplots(1, 2, figsize=(16, 7))
    plt.suptitle("IPL 2024 Fielding Performance Overview", fontsize=18, fontfamily='Times New Roman', color='darkblue')

    cmap=plt.get_cmap('tab20')
    colors=[cmap(i) for i in range(len(sorted_df1))]

    # Plot 1 - Catches
    bars1=axs[0].bar(sorted_df1['Name'], sorted_df1['Catches'], color=colors)
    axs[0].set_title('Top Fielders by Total Catches', fontsize=14, fontname='Times New Roman', color='green')
    axs[0].set_ylabel('Catches', fontsize=12, fontname='Times New Roman', color='purple')
    axs[0].set_xlabel('Player', fontsize=12, fontname='Times New Roman', color='purple')
    axs[0].set_xticks(range(len(sorted_df1['Name'])))
    axs[0].set_xticklabels(sorted_df1['Name'], rotation=45, ha='right', fontsize=9)
    for bar in bars1:
        axs[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2, int(bar.get_height()),
                    ha='center', va='bottom', fontsize=8, color='black')

    cmap=plt.get_cmap('tab20')
    colors1=[cmap(i) for i in range(len(sorted_df1))]
    # Plot 2 - Dismissals (e.g., by Wicketkeepers)
    bars2=axs[1].bar(sorted_df2['Name'], sorted_df2['Dismissals'], color=colors1)
    axs[1].set_title('Top Wicketkeepers by Dismissals', fontsize=14, fontname='Times New Roman', color='green')
    axs[1].set_ylabel('Dismissals', fontsize=12, fontname='Times New Roman', color='purple')
    axs[1].set_xlabel('Player', fontsize=12, fontname='Times New Roman', color='purple')
    axs[1].set_xticks(range(len(sorted_df2['Name'])))
    axs[1].set_xticklabels(sorted_df2['Name'], rotation=45, ha='right', fontsize=9)
    for bar in bars2:
        axs[1].text(bar.get_x() + bar.get_width()/2, bar.get_height()+0.2, int(bar.get_height()),
                    ha='center', va='bottom', fontsize=8, color='black')

    plt.tight_layout(rect=[0, 0.03, 0.95, 0.95])
    plt.subplots_adjust(wspace=0.2)
    plt.show()
