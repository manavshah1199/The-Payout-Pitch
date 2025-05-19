
from flask import Flask, render_template, request

app = Flask(__name__)

MOCK_PLAYERS = [
    {'name': 'Aaron Judge', 'team': 'NYY', 'avg': .402, 'hr': 15, 'rbi': 41},
    {'name': 'Freddie Freeman', 'team': 'LAD', 'avg': .358, 'hr': 9, 'rbi': 34},
    {'name': 'Paul Goldschmidt', 'team': 'NYY', 'avg': .341, 'hr': 5, 'rbi': 24},
    {'name': 'Jacob Wilson', 'team': 'ATH', 'avg': .341, 'hr': 5, 'rbi': 26},
    {'name': 'Manny Machado', 'team': 'SD', 'avg': .331, 'hr': 3, 'rbi': 20},
    {'name': 'Will Smith', 'team': 'LAD', 'avg': .330, 'hr': 3, 'rbi': 21},
    {'name': 'Brendan Donovan', 'team': 'STL', 'avg': .321, 'hr': 3, 'rbi': 21},
    {'name': 'Steven Kwan', 'team': 'CLE', 'avg': .320, 'hr': 4, 'rbi': 17},
    {'name': 'Bobby Witt Jr.', 'team': 'KC', 'avg': .316, 'hr': 5, 'rbi': 25},
    {'name': 'Shohei Ohtani', 'team': 'LAD', 'avg': .316, 'hr': 16, 'rbi': 29},
    {'name': 'Jonathan Aranda', 'team': 'TB', 'avg': .315, 'hr': 6, 'rbi': 20},
    {'name': 'Alex Bregman', 'team': 'BOS', 'avg': .309, 'hr': 11, 'rbi': 33},
    {'name': 'Pete Alonso', 'team': 'NYM', 'avg': .308, 'hr': 9, 'rbi': 37},
    {'name': 'Fernando Tatis Jr.', 'team': 'SD', 'avg': .307, 'hr': 11, 'rbi': 26},
    {'name': 'Jeremy Pena', 'team': 'HOU', 'avg': .306, 'hr': 6, 'rbi': 23},
    {'name': 'CJ Abrams', 'team': 'WSH', 'avg': .305, 'hr': 6, 'rbi': 16},
    {'name': 'Josh Smith', 'team': 'TEX', 'avg': .305, 'hr': 4, 'rbi': 10},
    {'name': 'Josh Naylor', 'team': 'ARI', 'avg': .304, 'hr': 5, 'rbi': 27},
    {'name': 'Trea Turner', 'team': 'PHI', 'avg': .302, 'hr': 2, 'rbi': 15},
    {'name': 'Maikel Garcia', 'team': 'KC', 'avg': .300, 'hr': 5, 'rbi': 19},
    # Add more players as needed...
]

def search_players(query):
    query = query.lower()
    return [p for p in MOCK_PLAYERS if query in p['name'].lower()]

@app.route('/', methods=['GET', 'POST'])
def index():
    players = []
    if request.method == 'POST':
        search_name = request.form.get('player', '')
        if search_name:
            players = search_players(search_name)
    return render_template('index.html', players=players)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
