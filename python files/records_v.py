def records():
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import mysql.connector

    # Connect to MySQL
    mydb = mysql.connector.connect(
        user='root',
        host='localhost',
        password='Yashwanth@7',
        database='ipl_data'
    )
    cursor = mydb.cursor()

    # Fetch data from the table
    cursor.execute('SELECT * FROM records')
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    df = pd.DataFrame(data=data, columns=columns)

    # Convert team names to short form (e.g., RCB, MI, etc.)
    df['Team'] = df['Team'].apply(lambda x: ''.join([word[0] for word in x.split()]))

    # Melt DataFrames
    melted_mat_wl = df.melt(id_vars="Team", value_vars=["Mat", "Won", "Lost"],
                            var_name="Category", value_name="Count")

    melted_high_low = df.melt(id_vars="Team", value_vars=["High Score", "Low Score"],
                            var_name="Score Type", value_name="Runs")

    melted_misc = df.melt(id_vars="Team", value_vars=["below 100", "highscore in PP"],
                        var_name="Category", value_name="Value")

    # Plotting all in one figure
    fig, axes = plt.subplots(3, 1, figsize=(12, 16), constrained_layout=True)

    # 1. Matches, Wins, Losses
    sns.barplot(data=melted_mat_wl, x="Team", y="Count", hue="Category", ax=axes[0], palette="Set2")
    axes[0].set_title("Matches, Wins, and Losses per Team")
    axes[0].set_xlabel("Team")
    axes[0].set_ylabel("Count")
    axes[0].tick_params(axis='x')
    for bar in axes[0].patches:
        height = bar.get_height()
        if height > 0:
            axes[0].text(bar.get_x() + bar.get_width()/2, height + 1, int(height), 
                        ha='center', va='bottom', fontsize=8, color='black')

    # 2. High Score vs Low Score
    sns.barplot(data=melted_high_low, x="Team", y="Runs", hue="Score Type", ax=axes[1], palette="coolwarm")
    axes[1].set_title("High Score and Low Score per Team")
    axes[1].set_xlabel("Team")
    axes[1].set_ylabel("Runs")
    axes[1].tick_params(axis='x')
    for bar in axes[1].patches:
        height = bar.get_height()
        if height > 0:
            axes[1].text(bar.get_x() + bar.get_width()/2, height + 1, int(height), 
                        ha='center', va='bottom', fontsize=8, color='black')

    # 3. Below 100 and Highscore in PP
    sns.barplot(data=melted_misc, x="Team", y="Value", hue="Category", ax=axes[2], palette="Set1")
    axes[2].set_title("Below 100 Scores & Powerplay High Scores per Team")
    axes[2].set_xlabel("Team")
    axes[2].set_ylabel("Count / Runs")
    axes[2].tick_params(axis='x')
    axes[2].legend(loc='best')
    for bar in axes[2].patches:
        height = bar.get_height()
        if height > 0:
            axes[2].text(bar.get_x() + bar.get_width()/2, height + 1, int(height), 
                        ha='center', va='bottom', fontsize=8, color='black')

    plt.suptitle("IPL Team Stats Summary", fontsize=16, fontfamily='Times New Roman', color='navy')
    plt.show()
