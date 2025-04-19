def runouts():
    import pandas as pd
    import seaborn as sns
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

    # Load most_runouts table
    cursor.execute('SELECT * FROM most_runs_outs')
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    df = pd.DataFrame(data=data, columns=columns)

    # Convert RunOuts to integer
    df['RunOuts'] = df['Run Out'].astype(int)

    # Sort by RunOuts descending
    df = df.sort_values(by='RunOuts', ascending=False)  # Ascending for horizontal bar plot

    # Plot using seaborn
    plt.figure(figsize=(10, 6))
    sns.set(style="whitegrid")

    barplot = sns.barplot(
        x='RunOuts',
        y='Name',
        data=df,
        palette='viridis'
    )

    # Add value labels
    for index, value in enumerate(df['RunOuts']):
        plt.text(value + 0.1, index, str(value), color='black', va='center', fontsize=9)

    plt.title('Top Fielders by Run Outs (IPL 2024)', fontsize=16, color='darkgreen', fontname='Times New Roman')
    plt.xlabel('Run Outs', fontsize=12, color='purple', fontname='Times New Roman')
    plt.ylabel('Player', fontsize=12, color='purple', fontname='Times New Roman')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.show()
