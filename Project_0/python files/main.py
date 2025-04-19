from wickets_v import wickets
from threew_haul_v import three_wickets
from catches_and_dis_v import catches_and_dis
from fours_and_sixes_v import fours_and_sixes
from records_v import records
from run_out_v import runouts
from runs_v import runs
from runs_and_wickets_v import runs_wickets
from summary_v import summary
from team_followers_v import teams_followers
from team_home_matches_v import team_home_matches
from team_vs_team_v import team_vs_team
from toss_lost_v import team_toss_lost
from toss_won_v import team_won_toss
from players import get_top_players_by_team
from year_wise_points_table import points_table
def display_menu():
    print("\nIPL 2024 Visualization Menu")
    print("1. points_Table")
    print("2. Most Wickets")
    print("3. 3-Wicket Hauls")
    print("4. Catches & Dismissals")
    print("5. Fours and Sixes")
    print("6. Team Records")
    print("7. Run Outs")
    print("8. Most Runs")
    print("9. Runs vs Wickets Comparison")
    print("10. Match Summary")
    print("11. Team Followers")
    print("12. Team Home Matches")
    print("13. Team vs Team")
    print("14. Teams that Lost Toss")
    print("15. Teams that Won Toss")
    print("16. Top 5 Batters and Bowlers by Team")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (0-15): ").strip()
        try:
            if choice == '1':
                points_table()
            elif choice == '2':
                wickets()
            elif choice == '3':
                three_wickets()
            elif choice == '4':
                catches_and_dis()
            elif choice == '5':
                fours_and_sixes()
            elif choice == '6':
                records()
            elif choice == '7':
                runouts()
            elif choice == '8':
                runs()
            elif choice == '9':
                runs_wickets()
            elif choice == '10':
                summary()
            elif choice == '11':
                teams_followers()
            elif choice == '12':
                team_home_matches()
            elif choice == '13':
                team_vs_team()
            elif choice == '14':
                team_toss_lost()
            elif choice == '15':
                team_won_toss()
            elif choice == '16':
                get_top_players_by_team()
            elif choice == '0':
                print("Thank you! Exiting...")
                break
            else:
                print("Invalid input. Please try again.")
        except Exception as e:
            print(f"An error occurred while displaying the chart: {e}")

if __name__ == "__main__":
    main()