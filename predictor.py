import pandas as pd

# Load match data from CSV file
def load_data(csv_path):
    try:
        df = pd.read_csv(csv_path)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        exit(1)

# Calculate total matches played, won, and winning percentage for each team
def calculate_team_stats(df):
    teams = set(df['Team1']).union(set(df['Team2']))
    stats = {}
    for team in teams:
        played = df[(df['Team1'] == team) | (df['Team2'] == team)].shape[0]
        won = df[df['Winner'] == team].shape[0]
        win_pct = (won / played * 100) if played > 0 else 0
        stats[team] = {'played': played, 'won': won, 'win_pct': win_pct}
    return stats

def print_team_stats(team_stats):
    print("\nTeam Statistics (2020-2024):")
    print(f"{'Team':30} {'Played':>6} {'Won':>6} {'Win %':>7}")
    print("-" * 52)
    for team, stats in sorted(team_stats.items()):
        print(f"{team:30} {stats['played']:6} {stats['won']:6} {stats['win_pct']:7.2f}")

# Main predictor logic
def main():
    csv_path = 'ipl_results_2020_2024.csv'
    df = load_data(csv_path)
    team_stats = calculate_team_stats(df)

    print("\nWelcome to the IPL Winner Predictor!")
    print("This tool predicts the winner between two IPL teams based on overall winning percentage from the last 5 seasons (2020-2024).\n")
    print("Available teams:")
    for team in sorted(team_stats.keys()):
        print(f"- {team}")

    print("\nType the team names exactly as shown above.")
    team1 = input("Enter the name of Team 1: ").strip()
    team2 = input("Enter the name of Team 2: ").strip()

    # Handle case-insensitive matching
    team_lookup = {t.lower(): t for t in team_stats}
    t1_key = team1.lower()
    t2_key = team2.lower()
    if t1_key in team_lookup and t2_key in team_lookup:
        t1 = team_lookup[t1_key]
        t2 = team_lookup[t2_key]
        t1_pct = team_stats[t1]['win_pct']
        t2_pct = team_stats[t2]['win_pct']
        print(f"\n{t1}'s 5-year winning percentage: {t1_pct:.2f}%")
        print(f"{t2}'s 5-year winning percentage: {t2_pct:.2f}%")
        if t1_pct > t2_pct:
            print(f"\nPrediction: Based on winning percentage, {t1} is predicted to win.")
        elif t2_pct > t1_pct:
            print(f"\nPrediction: Based on winning percentage, {t2} is predicted to win.")
        else:
            print("\nPrediction: The teams have equal winning percentages over the last 5 years.")
    else:
        print("\nError: Could not find data for one or both teams. Please check the spelling and try again.\n")
        print_team_stats(team_stats)
        print("\nTip: Copy and paste the team names from the list above.")

if __name__ == "__main__":
    main()
