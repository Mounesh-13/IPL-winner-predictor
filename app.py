from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

def load_data(csv_path):
    """
    Load IPL match data from a CSV file.
    Args:
        csv_path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: DataFrame containing IPL match data.
    """
    df = pd.read_csv(csv_path)
    return df

def calculate_team_stats(df):
    """
    Calculate total matches played, matches won, and win percentage for each team.
    Args:
        df (pd.DataFrame): IPL match data.
    Returns:
        dict: Team stats with played, won, win_pct for each team.
    """
    teams = set(df['Team1']).union(set(df['Team2']))
    stats = {}
    for team in teams:
        played = df[(df['Team1'] == team) | (df['Team2'] == team)].shape[0]
        won = df[df['Winner'] == team].shape[0]
        win_pct = (won / played * 100) if played > 0 else 0
        stats[team] = {'played': played, 'won': won, 'win_pct': win_pct}
    return stats




def reload_all():
    """Reload match data and team stats (used on startup and for manual reload)."""
    global df, team_stats, team_list
    df = load_data(CSV_PATH)
    team_stats = calculate_team_stats(df)
    team_list = sorted(team_stats.keys())

CSV_PATH = os.path.join(os.path.dirname(__file__), 'ipl_results_2020_2024.csv')
df = None
team_stats = None
team_list = None
reload_all()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main route for the IPL Winner Predictor web app.
    Handles team selection, prediction logic, and passes data to the template.
    """
    prediction = None
    t1_pct = t2_pct = None
    team1 = team2 = ''
    error = None
    t1_stats = t2_stats = None
    chart_data = None
    if request.method == 'POST':
        team1 = request.form.get('team1', '').strip()
        team2 = request.form.get('team2', '').strip()
        team_lookup = {t.lower(): t for t in team_stats}
        t1_key = team1.lower()
        t2_key = team2.lower()
        if t1_key == t2_key and t1_key in team_lookup:
            error = "Please select two different teams."
        elif t1_key in team_lookup and t2_key in team_lookup:
            t1 = team_lookup[t1_key]
            t2 = team_lookup[t2_key]
            t1_stats = team_stats[t1]
            t2_stats = team_stats[t2]
            t1_pct = t1_stats['win_pct']
            t2_pct = t2_stats['win_pct']
            # Calculate normalized chances
            total = t1_pct + t2_pct
            if total > 0:
                t1_chance = round(t1_pct / total * 100, 2)
                t2_chance = round(t2_pct / total * 100, 2)
            else:
                t1_chance = t2_chance = 50.0
            chart_data = {
                'labels': [t1, t2],
                'percentages': [t1_chance, t2_chance],
            }
            if t1_chance > t2_chance:
                prediction = f"{t1} has a higher chance to win ({t1_chance:.2f}%) vs {t2} ({t2_chance:.2f}%)."
            elif t2_chance > t1_chance:
                prediction = f"{t2} has a higher chance to win ({t2_chance:.2f}%) vs {t1} ({t1_chance:.2f}%)."
            else:
                prediction = f"Both teams have equal chances (50% each)."
        else:
            error = "Could not find data for one or both teams. Please check the names."
    return render_template('index.html',
                           prediction=prediction,
                           team1=team1,
                           team2=team2,
                           t1_pct=t1_pct,
                           t2_pct=t2_pct,
                           error=error,
                           chart_data=chart_data,
                           team_list=team_list)

@app.route('/reload-data', methods=['POST'])
def reload_data():
    reload_all()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
