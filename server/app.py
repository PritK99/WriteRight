from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from model.semantic import semantic_check
from model.statistics import statistics_check
from model.syntax import syntax_check

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        essay = data.get('essay', '')
        suggestions = []

        if not essay:
            raise ValueError("Essay is required.")

        print("Analysis starting...")
        statistic_score = statistics_check(essay, suggestions)
        syntax_score = syntax_check(essay, suggestions)
        semantic_score = semantic_check(prompt, essay, suggestions)

        total_score = (statistic_score + 2 * syntax_score + 2 * semantic_score) / 5

        analysis_results = {
            'total_score': round(total_score, 1),
            'statistic_score': round(statistic_score, 1),
            'syntax_score': round(syntax_score, 1),
            'semantic_score': round(semantic_score, 1),
            'suggestions': suggestions  # Assuming suggestions is not a numerical score
        }

        print("Analysis complete...")
        return jsonify(analysis_results)

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return a JSON error response

if __name__ == '__main__':
    app.run(debug=True)