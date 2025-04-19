def three_wickets():
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

    # Load the table containing Wickets, 3W, and Name (assume it's 'most_wickets')
    cursor.execute('SELECT Name, Wickets,3W FROM 3w_haul')
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    df = pd.DataFrame(data=data, columns=columns)

    # Convert 3W and Wickets to integer
    df['3W'] = df['3W'].astype(int)

    # Filter players with at least one 3W haul
    df_filtered = df[df['3W'] > 0]

    labels = [
        f"{row['Name']} ({row['3W']}x3W, {row['Wickets']} Wkts)"
        for _, row in df_filtered.iterrows()
    ]

    # Plotting the pie chart
    plt.figure(figsize=(10, 8))
    plt.pie(
        df_filtered['3W'],
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        textprops={'fontsize': 10, 'color': 'black', 'fontname': 'Times New Roman'}
    )
    plt.suptitle('Distribution of 3-Wicket Hauls Among Bowlers - IPL 2024', fontsize=16, color='darkblue', fontname='Times New Roman')
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    plt.tight_layout(rect=[0, 0, 0.2, 0])
    plt.show()
