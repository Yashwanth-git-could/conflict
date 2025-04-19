def fours_and_sixes():
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

    # Load most_fours table into DataFrame
    cursor.execute('SELECT * FROM most_fours')
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    df1 = pd.DataFrame(data=data, columns=columns)

    # Load most_sixes table into DataFrame
    cursor.execute('SELECT * FROM most_sixes')
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    df2 = pd.DataFrame(data=data, columns=columns)

    # Ensure "Fours" and "Sixes" are treated as integers
    df1['Fours'] = df1['4s'].astype(int)
    df2['Sixes'] = df2['6s'].astype(int)

    # Sort by Fours and Sixes
    sorted_df1 = df1.sort_values(by='Fours', ascending=True)
    sorted_df2 = df2.sort_values(by='Sixes', ascending=True).dropna()
    # Plotting
    fig, axs = plt.subplots(1, 2, figsize=(16, 7))
    plt.suptitle("Comprehensive IPL Player Performance (Fours & Sixes)", fontsize=18, fontfamily='Times New Roman', color='darkblue')

    cmap=plt.get_cmap('tab20')
    colors=[cmap(i) for i in range(len(df1))]
    # Plot 1 - Total Fours
    b1=axs[0].bar(sorted_df1['Name'], sorted_df1['Fours'], color=colors)
    axs[0].set_title('Total Fours Hit', fontsize=14, fontname='Times New Roman', color='darkgreen')
    axs[0].set_ylabel('Fours', fontsize=12, fontname='Times New Roman', color='darkred')
    axs[0].set_xlabel('Player', fontsize=12, fontname='Times New Roman', color='darkred')
    axs[0].set_xticks(range(len(sorted_df1['Name'])))
    axs[0].set_xticklabels(sorted_df1['Name'], rotation=45, ha='right', fontsize=9, color='darkblue')
    for bar in b1:
        axs[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, int(bar.get_height()), 
                    ha='center', va='bottom', fontsize=8, color='black')
    axs[0].spines['top'].set_visible(False)
    axs[0].spines['right'].set_visible(False)

    # Plot 2 - Total Sixes
    b2=axs[1].bar(sorted_df2['Name'], sorted_df2['Sixes'], color=colors)
    axs[1].set_title('Total Sixes Hit', fontsize=14, fontname='Times New Roman', color='darkgreen')
    axs[1].set_ylabel('Sixes', fontsize=12, fontname='Times New Roman', color='darkred')
    axs[1].set_xlabel('Player', fontsize=12, fontname='Times New Roman', color='darkred')
    axs[1].set_xticks(range(len(sorted_df2['Name'])))
    axs[1].set_xticklabels(sorted_df2['Name'], rotation=45, ha='right', fontsize=9, color='darkblue')
    for bar in b2:
        axs[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, int(bar.get_height()), 
                    ha='center', va='bottom', fontsize=8, color='black')
        axs[1].spines['top'].set_visible(False)
    axs[1].spines['right'].set_visible(False)
    # Adjust spacing between columns (subplots)
    plt.subplots_adjust(wspace=0.2)  # Increase the value of wspace for more space

    plt.tight_layout(rect=[0, 0.03, 0.95, 0.95])
    plt.show()
