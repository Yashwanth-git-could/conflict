def runs_wickets():
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

    # Load most_runs table into DataFrame
    cursor.execute('SELECT * FROM most_runs')
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    df1 = pd.DataFrame(data=data, columns=columns)

    # Load most_wickets table into DataFrame
    cursor.execute('SELECT * FROM most_wickets')
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    df2 = pd.DataFrame(data=data, columns=columns)

    # Ensure "Runs" is treated as an integer
    df1['Runs'] = df1['Runs'].astype(int)
    df2['Wickets'] = df2['Wickets'].astype(int)

    # Sort by Runs and Wickets
    sorted_df1 = df1.sort_values(by='Runs', ascending=True)
    sorted_df2 = df2.sort_values(by='Wickets', ascending=True)

    # Plotting
    fig, axs = plt.subplots(1, 2, figsize=(16, 7))
    plt.suptitle("Comprehensive IPL Team Bowling Performance", fontsize=18, fontfamily='Times New Roman', color='darkblue')

    # Plot 1 - Runs Conceded
    axs[0].bar(sorted_df1['Name'], sorted_df1['Runs'], color='coral')
    axs[0].set_title('Total Runs Scored', fontsize=14, fontname='Times New Roman', color='green')
    axs[0].set_ylabel('Runs', fontsize=12, fontname='Times New Roman', color='purple')
    axs[0].set_xlabel('Player', fontsize=12, fontname='Times New Roman', color='purple')
    axs[0].set_xticks(range(len(sorted_df1['Name'])))
    axs[0].set_xticklabels(sorted_df1['Name'], rotation=45, ha='right', fontsize=9)

    # Plot 2 - Total Wickets
    axs[1].bar(sorted_df2['Name'], sorted_df2['Wickets'], color='skyblue')
    axs[1].set_title('Total Wickets Taken', fontsize=14, fontname='Times New Roman', color='green')
    axs[1].set_ylabel('Wickets', fontsize=12, fontname='Times New Roman', color='purple')
    axs[1].set_xlabel('Player', fontsize=12, fontname='Times New Roman', color='purple')
    axs[1].set_xticks(range(len(sorted_df2['Name'])))
    axs[1].set_xticklabels(sorted_df2['Name'], rotation=45, ha='right', fontsize=9)

    plt.tight_layout(rect=[0, 0.03, 0.95, 0.95])
    plt.subplots_adjust(wspace=0.2)
    plt.show()
