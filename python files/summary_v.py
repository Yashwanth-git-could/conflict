def summary():
    # Import necessary libraries
    import pandas as pd  # For data manipulation
    import matplotlib.pyplot as plt  # For creating plots
    import numpy as np  # For numerical operations (e.g., array manipulation)
    import mysql.connector
    mydb=mysql.connector.connect(user='root',host='localhost',password='Yashwanth@7',database='ipl_data')
    cursor=mydb.cursor()
    cursor.execute('select * from team_summary')
    columns = [col[0] for col in cursor.description]
    data=cursor.fetchall()
    df=pd.DataFrame(data=data,columns=columns)
    # Read the data from the CSV file containing IPL team toss and match statistics

    # Create a new column 'intials' by extracting the first letter of each word in the 'Team' column
    df['intials'] = df['Team'].apply(lambda x: ''.join([word[0] for word in x.split()]))

    # Sort the DataFrame by the 'Mat' column (matches played) in descending order
    df = df.sort_values(by='Mat', ascending=False)

    # Assign 'intials', 'Mat', 'Won', and 'Lost' columns to variables for ease of use
    x = df['intials']  # Team initials for the x-axis
    y = df['Mat']      # Total matches played for the y-axis
    z = df['Won']      # Matches won for the z-axis
    w = df['Lost']     # Matches lost for the w-axis

    # Create a subplot for the bar chart
    fig, axs = plt.subplots()

    # Hide the top and right spines of the plot for a cleaner look
    axs.spines['top'].set_visible(False)
    axs.spines['right'].set_visible(False)

    # Set the width of each bar in the grouped bar chart
    barwidth = 0.2

    # Generate an array of positions for each team on the x-axis
    index = np.arange(len(x))

    # Plot the bars for 'Matches', 'Won', and 'Lost' with different colors
    plt.bar(index, y, barwidth, label='Matches', color='skyblue')  # Total matches
    plt.bar(index + barwidth, z, barwidth, label='Won', color='green')  # Matches won
    plt.bar(index + 2 * barwidth, w, barwidth, label='Lost', color='tomato')  # Matches lost

    # Add text annotations above each 'Matches' bar to display the count of matches
    for i, value in enumerate(y):
        plt.text(i, value + 0.5, str(y.iloc[i]), ha='center')

    # Add text annotations above each 'Won' bar to display the count of wins
    for i, value in enumerate(z):
        plt.text(i + barwidth, value + 0.5, str(z.iloc[i]), ha='center',rotation=45)

    # Add text annotations above each 'Lost' bar to display the count of losses
    for i, value in enumerate(w):
        plt.text(i + 2 * barwidth, value + 0.5, str(w.iloc[i]), ha='center',rotation=45)

    # Set the x-axis label
    plt.xlabel('Teams',fontdict={'color':'darkblue','family':'Times New Roman','size':'15'})

    # Set the y-axis label
    plt.ylabel('Games Played',fontdict={'color':'darkblue','family':'Times New Roman','size':'15'})

    # Set the x-axis tick labels (team initials) and rotate them for better visibility
    plt.xticks(index + barwidth, x, rotation=45)

    # Set the title of the plot
    plt.title('IPL Team Journey: Matches, Wins & Losses',fontdict={'color':'navy','family':'Times New Roman','size':'20'})

    # Adjust the layout of the plot for better spacing
    plt.subplots_adjust(left=0.12, right=0.9, top=0.85, bottom=0.15)
    axs.grid(axis='y', linestyle='--', alpha=0.3,color='skyblue')


    # Display the legend to label each bar
    plt.legend()

    # Show the plot
    plt.show()
