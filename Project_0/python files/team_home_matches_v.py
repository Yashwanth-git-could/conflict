def team_home_matches():
    
    import pandas as pd
    import mysql.connector
    import matplotlib.pyplot as plt

    # Connect to the MySQL database
    mydb = mysql.connector.connect(
        user='root', 
        host='localhost', 
        password='Yashwanth@7',  # Use environment variable for security in production
        database='ipl_data'
    )
    cursor = mydb.cursor()

    # Query the team_home_matches table
    cursor.execute("SELECT `Team Name`, Matches, Wins, Losses, Tied, NR FROM team_home_matches")
    data = cursor.fetchall()
    columns = ['Team Name', 'Matches', 'Wins', 'Losses', 'Tied', 'NR']
    df = pd.DataFrame(data, columns=columns)

    # Short team name for aesthetics (e.g., 'Chennai Super Kings' → 'CSK')
    df['Short Name'] = df['Team Name'].apply(lambda x: ''.join(word[0] for word in x.split() if word[0].isupper()))

    # Melt the DataFrame for line plotting
    melted_df = df.melt(id_vars=['Short Name'], 
                        value_vars=['Matches', 'Wins', 'Losses', 'Tied', 'NR'],
                        var_name='Category', value_name='Count')

    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 6))

    # Hide top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Plot line for each category (Matches, Wins, Losses, Tied, NR)
    categories = melted_df['Category'].unique()
    colors = ['navy', 'green', 'red', 'orange', 'gray']

    for cat, color in zip(categories, colors):
        temp = melted_df[melted_df['Category'] == cat]
        line, = ax.plot(temp['Short Name'], temp['Count'], label=cat, marker='o', color=color)

        # Add text annotations
        for i in range(len(temp)):
            ax.text(temp['Short Name'].iloc[i], temp['Count'].iloc[i] + 0.3, 
                    str(temp['Count'].iloc[i]), 
                    fontsize=8, ha='center', va='bottom', color='black')

    # Titles and Labels
    plt.title('IPL Teams Home Match Performance Analysis', fontsize=15, color='darkcyan', pad=40)
    plt.xlabel('Team', fontsize=12, color='navy', labelpad=10)
    plt.ylabel('Count', fontsize=12, color='navy', labelpad=10)

    # Customize ticks and layout
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.legend(title='Match Type')
    plt.tight_layout()

    # Show the plot
    plt.show()

    # Close the database connection
    mydb.close()
