from flask import Flask, request, jsonify
from flask_cors import CORS
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

        if not essay:
            raise ValueError("Essay is required.")

        statistic_score = statistics_check(essay)
        syntax_score = syntax_check(essay)
        semantic_score = semantic_check(prompt, essay)

        total_score = (statistic_score + 2 * syntax_score + 2 * semantic_score) / 5

        analysis_results = {
            'total_score': total_score,
            'statistic_score': statistic_score,
            'syntax_score': syntax_score,
            'semantic_score': semantic_score,
            'suggestions': []  # Include suggestions if applicable
        }

        return jsonify(analysis_results)

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return a JSON error response

if __name__ == '__main__':
    app.run(debug=True)