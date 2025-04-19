import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

def points_table():
    try:
        # Connect to the MySQL database
        mydb = mysql.connector.connect(
            user='root',
            host='localhost',
            password='Yashwanth@7',
            database='ipl_data'
        )
        cursor = mydb.cursor()

        # Load points_table into DataFrame
        cursor.execute('SELECT * FROM points_table')
        columns = [col[0] for col in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data=data, columns=columns)

        # Ask user for the year
        user_year = input("Enter the IPL year to view the Points Table: ").strip()
        try:
            user_year = int(user_year)
            year_df = df[df['Year'] == user_year].copy()

            if year_df.empty:
                print(f"No data found for the year {user_year}.")
            else:
                print(f"\nPoints Table for IPL {user_year}:\n")
                print(year_df[['Team', 'Macthes', 'Won', 'Lost', 'Tied', 'NR', 'NRR', 'Points']])
                year_df['intials'] = year_df['Team'].apply(lambda x: ''.join([word[0] for word in x.split()]))

                                # Side-by-side bar chart for Matches, Won, Lost, Points
                import numpy as np

                x = np.arange(len(year_df))  # label locations
                width = 0.2  # width of each bar

                plt.figure(figsize=(14, 6))
                b1=plt.bar(x - 1.5*width, year_df['Macthes'], width, label='Matches', color='skyblue')
                b2=plt.bar(x - 0.5*width, year_df['Won'], width, label='Won', color='seagreen')
                b3=plt.bar(x + 0.5*width, year_df['Lost'], width, label='Lost', color='tomato')
                b4=plt.bar(x + 1.5*width, year_df['Points'], width, label='Points', color='goldenrod')
                for bars in [b1,b2,b3,b4]:
                    for bar in bars:
                        height = bar.get_height()
                        plt.text(bar.get_x() + bar.get_width() / 2, height + 0.2, str(int(height)), 
                                ha='center', va='bottom', fontsize=8)

                plt.xlabel("Team", fontsize=12)
                plt.ylabel("Count", fontsize=12)
                plt.title(f"IPL {user_year} - Team Performance Summary", fontsize=14)
                plt.xticks(x, year_df['intials'], rotation=45)
                plt.legend()
                plt.tight_layout()
                plt.show()


        except ValueError:
            print("Invalid year format. Please enter a valid number.")

    except Exception as e:
        print(f"Error: {e}")
