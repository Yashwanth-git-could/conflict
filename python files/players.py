import mysql.connector
import pandas as pd

# Resolve full team name from short code
def resolve_team_name(short_code):
    short_code = short_code.upper().strip()
    team_names = {
        "CSK": "Chennai Super Kings",
        "MI": "Mumbai Indians",
        "RCB": "Royal Challengers Bangalore",
        "RR": "Rajasthan Royals",
        "KKR": "Kolkata Knight Riders",
        "SH": "Sunrisers Hyderabad",
        "PK": "Punjab Kings",  # use PBKS as per new official abbreviation
        "DC": "Delhi Capitals",
        "GT": "Gujarat Titans",
        "LSG": "Lucknow Super Giants"
    }
    return team_names.get(short_code)

# Fetch and display top batters and bowlers by team
def get_top_players_by_team():
    team_code = input("Enter team short code (e.g., CSK, MI, RCB): ")
    full_team_name = resolve_team_name(team_code)

    if not full_team_name:
        print("Invalid team code. Please try again.")
        return

    try:
        # Database connection
        conn = mysql.connector.connect(
            host="localhost",
            user="root",         
            password="Yashwanth@7",
            database="ipl_data"
        )
        cursor = conn.cursor(dictionary=True)

        # Top Batters
        print(f"\n Top 5 Batters for {full_team_name}:")
        cursor.execute("SELECT * FROM batters WHERE Team = %s LIMIT 5", (full_team_name,))
        batters = cursor.fetchall()
        columns=[des[0] for des in cursor.description]
        if batters:
            df=pd.DataFrame(data=batters,columns=columns)
            print(df.to_string(index=False))
        else:
            print("No batting data found.")

        # Top Bowlers
        print(f"\n Top 5 Bowlers for {full_team_name}:")
        cursor.execute("SELECT * FROM bowlers WHERE Team = %s LIMIT 5", (full_team_name,))
        bowlers = cursor.fetchall()
        columns=[des[0] for des in cursor.description]
        if batters:
            df=pd.DataFrame(data=bowlers,columns=columns)
            print(df.to_string(index=False))
        else:
            print("No bowlers data found.")

        # Close connection
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    except Exception as e:
        print(f"Error: {e}")
