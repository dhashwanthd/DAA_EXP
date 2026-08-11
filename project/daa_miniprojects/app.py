"""
DAA Mini Projects - single Flask web app unifying 10 algorithm experiments.
Run with: python app.py
Then open http://127.0.0.1:5000 in a browser.
"""
from flask import Flask, render_template, request

from experiments import exp1_interpolation_search as exp1
from experiments import exp2_string_matching as exp2
from experiments import exp3_mst as exp3
from experiments import exp4_dijkstra as exp4
from experiments import exp5_minmax as exp5
from experiments import exp6_matrix_chain as exp6
from experiments import exp7_n_queens as exp7
from experiments import exp8_tsp as exp8
from experiments import exp9_bin_packing as exp9
from experiments import exp10_quicksort as exp10

app = Flask(__name__)

EXPERIMENTS = [
    {'number': 1, 'endpoint': 'interpolation_search', 'short': 'Interpolation Search',
     'title': 'Interpolation Search vs Binary Search',
     'aim': 'Search a sorted array and compare comparison counts against Binary Search.'},
    {'number': 2, 'endpoint': 'string_matching', 'short': 'String Matching',
     'title': 'Naive, Rabin-Karp & KMP String Matching',
     'aim': 'Find pattern occurrences in text using three matching algorithms.'},
    {'number': 3, 'endpoint': 'mst', 'short': 'MST (Kruskal/Prim)',
     'title': "Kruskal's & Prim's Minimum Spanning Tree",
     'aim': 'Build the minimum spanning tree of a weighted graph two ways.'},
    {'number': 4, 'endpoint': 'dijkstra', 'short': "Dijkstra's SSSP",
     'title': "Dijkstra's Shortest Path",
     'aim': 'Compute shortest paths from a source vertex to all others.'},
    {'number': 5, 'endpoint': 'minmax', 'short': 'Min-Max D&C',
     'title': 'Min-Max via Divide and Conquer',
     'aim': 'Find min and max together, minimizing total comparisons.'},
    {'number': 6, 'endpoint': 'matrix_chain', 'short': 'Matrix Chain Mult.',
     'title': 'Matrix Chain Multiplication (DP)',
     'aim': 'Find the cheapest way to parenthesize a chain of matrix multiplications.'},
    {'number': 7, 'endpoint': 'n_queens', 'short': 'N-Queens',
     'title': 'N-Queens using Backtracking',
     'aim': 'Place N queens on an NxN board with no two attacking each other.'},
    {'number': 8, 'endpoint': 'tsp', 'short': 'TSP (Branch & Bound)',
     'title': 'Travelling Salesman Problem',
     'aim': 'Find the minimum-cost tour that visits every city once.'},
    {'number': 9, 'endpoint': 'bin_packing', 'short': 'Bin Packing',
     'title': 'Bin Packing Approximation Algorithms',
     'aim': 'Pack items into the fewest bins using FF, FFD and BFD heuristics.'},
    {'number': 10, 'endpoint': 'quicksort', 'short': 'Quick Sort',
     'title': 'Deterministic vs Randomized Quick Sort',
     'aim': 'Compare Quick Sort variants across different input distributions.'},
]


@app.context_processor
def inject_experiments():
    return {'experiments': EXPERIMENTS}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/interpolation-search', methods=['GET', 'POST'])
def interpolation_search():
    result, error, form = None, None, {}
    if request.method == 'POST':
        form = request.form
        try:
            result = exp1.solve(form['array'], form['target'])
        except Exception as e:
            error = str(e)
    return render_template('interpolation_search.html', result=result, error=error,
                            form=form, active='interpolation_search')


@app.route('/string-matching', methods=['GET', 'POST'])
def string_matching():
    result, error, form = None, None, {}
    if request.method == 'POST':
        form = request.form
        try:
            result = exp2.solve(form['text'], form['pattern'])
        except Exception as e:
            error = str(e)
    return render_template('string_matching.html', result=result, error=error,
                            form=form, active='string_matching')


@app.route('/mst', methods=['GET', 'POST'])
def mst():
    result, error, form = None, None, {}
    if request.method == 'POST':
        form = request.form
        try:
            result = exp3.solve(form['n'], form['edges'])
        except Exception as e:
            error = str(e)
    return render_template('mst.html', result=result, error=error, form=form, active='mst')


@app.route('/dijkstra', methods=['GET', 'POST'])
def dijkstra():
    result, error, form = None, None, {}
    if request.method == 'POST':
        form = request.form
        try:
            result = exp4.solve(form['n'], form['edges'], form['source'])
        except Exception as e:
            error = str(e)
    return render_template('dijkstra.html', result=result, error=error, form=form, active='dijkstra')


@app.route('/minmax', methods=['GET', 'POST'])
def minmax():
    result, error, form = None, None, {}
    if request.method == 'POST':
        form = request.form
        try:
            result = exp5.solve(form['array'])
        except Exception as e:
            error = str(e)
    return render_template('minmax.html', result=result, error=error, form=form, active='minmax')


@app.route('/matrix-chain', methods=['GET', 'POST'])
def matrix_chain():
    result, error, form = None, None, {}
    if request.method == 'POST':
        form = request.form
        try:
            result = exp6.solve(form['dims'])
        except Exception as e:
            error = str(e)
    return render_template('matrix_chain.html', result=result, error=error, form=form, active='matrix_chain')


@app.route('/n-queens', methods=['GET', 'POST'])
def n_queens():
    result, error, form = None, None, {}
    if request.method == 'POST':
        form = request.form
        try:
            result = exp7.solve(form['n'], form.get('max_display', '10'))
        except Exception as e:
            error = str(e)
    return render_template('n_queens.html', result=result, error=error, form=form, active='n_queens')


@app.route('/tsp', methods=['GET', 'POST'])
def tsp():
    result, error, form = None, None, {}
    if request.method == 'POST':
        form = request.form
        try:
            result = exp8.solve(form['matrix'], form.get('cities', ''))
        except Exception as e:
            error = str(e)
    return render_template('tsp.html', result=result, error=error, form=form, active='tsp')


@app.route('/bin-packing', methods=['GET', 'POST'])
def bin_packing():
    result, error, form = None, None, {}
    if request.method == 'POST':
        form = request.form
        try:
            result = exp9.solve(form['items'], form['capacity'])
        except Exception as e:
            error = str(e)
    return render_template('bin_packing.html', result=result, error=error, form=form, active='bin_packing')


@app.route('/quicksort', methods=['GET', 'POST'])
def quicksort():
    result, error, form = None, None, {}
    if request.method == 'POST':
        form = request.form
        try:
            result = exp10.solve(form['n'], form.get('kind', 'random'))
        except Exception as e:
            error = str(e)
    return render_template('quicksort.html', result=result, error=error, form=form, active='quicksort')


if __name__ == '__main__':
    app.run(debug=True)