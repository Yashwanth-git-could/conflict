def teams_followers():
    import pandas as pd
    import mysql.connector
    import matplotlib.pyplot as plt

    # Connect to the MySQL database
    mydb = mysql.connector.connect(
        user='root', 
        host='localhost', 
        password='Yashwanth@7',  # For security, use environment variables
        database='ipl_data'
    )
    cursor = mydb.cursor()

    # Query the team_followers table
    cursor.execute("SELECT Team, `Facebook Followers (m)`, `Instagram Followers (m)`, `Twitter Followers (m)`, `Overall Follwers (m)` FROM team_followers")
    data = cursor.fetchall()
    columns = ['Team', 'Facebook', 'Instagram', 'Twitter', 'Overall']
    df = pd.DataFrame(data, columns=columns)

    df['Team']=df['Team'].apply(lambda x:''.join([word[0] for word in x.split()]))
    # Melt the DataFrame for bar plotting
    melted_df = df.melt(id_vars='Team', 
                        value_vars=['Facebook', 'Instagram', 'Twitter', 'Overall'], 
                        var_name='Platform', 
                        value_name='Followers (m)')

    # Set up the plot
    fig, ax = plt.subplots(figsize=(12, 6))

    # Hide top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Define platform colors
    platform_colors = {
        'Facebook': 'blue',
        'Instagram': 'deeppink',
        'Twitter': 'skyblue',
        'Overall': 'darkgreen'
    }

    # Set bar width and position for each platform group
    bar_width = 0.2
    bar_positions = range(len(df))

    # Plot data for each platform as bars
    for i, platform in enumerate(melted_df['Platform'].unique()):
        temp = melted_df[melted_df['Platform'] == platform]
        ax.bar([pos + i * bar_width for pos in bar_positions], 
            temp['Followers (m)'], 
            width=bar_width, 
            label=platform, 
            color=platform_colors[platform])

        # Annotate each bar with the value
        for j in range(len(temp)):
            ax.text(bar_positions[j] + i * bar_width, 
                    temp['Followers (m)'].iloc[j] + 0.1, 
                    str(temp['Followers (m)'].iloc[j]), 
                    ha='center', va='bottom', fontsize=8, color='black')

    # Titles and labels
    plt.title('IPL Teams Social Media Followers (in Millions)', fontsize=15, color='darkcyan', pad=40)
    plt.xlabel('Team', fontsize=12, color='navy', labelpad=10)
    plt.ylabel('Followers (in millions)', fontsize=12, color='navy', labelpad=10)

    # Customize x-ticks to show team names
    ax.set_xticks([pos + bar_width * 1.5 for pos in bar_positions])
    ax.set_xticklabels(df['Team'])

    # Add gridlines, legend, and layout
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.legend(title='Platform')
    plt.tight_layout()

    # Show plot
    plt.show()

    # Close the database connection
    mydb.close()
