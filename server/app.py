from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
from werkzeug.exceptions import BadRequest

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from model.semantic import semantic_check
from model.statistics import statistics_check
from model.syntax import syntax_check  

app = Flask(__name__)

CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000"],
        "methods": ["POST", "OPTIONS"],
        "allow_headers": ["Content-Type"],
        "max_age": 3600
    }
})

@app.route('/api/analyze', methods=['POST', 'OPTIONS'])
def analyze():
    # Handle preflight requests
    if request.method == 'OPTIONS':
        return '', 204

    try:
        # Verify content type
        if not request.is_json:
            raise BadRequest("Content-Type must be application/json")

        data = request.get_json()
        
        # Input validation
        if not isinstance(data, dict):
            raise BadRequest("Invalid JSON format")
            
        prompt = data.get('prompt', '')
        essay = data.get('essay', '')
        
        if not essay:
            raise BadRequest("Essay is required")

        suggestions = []

        print("Analysis starting...")
        
        # Perform each analysis in try-except blocks
        try:
            statistic_score = statistics_check(essay, suggestions)
        except Exception as e:
            print(f"Statistics check failed: {str(e)}")
            statistic_score = 0

        try:
            syntax_results = syntax_check(essay)
            syntax_score = (syntax_results['final_score']) 
            
            # Add spelling and grammar suggestions
            suggestions.extend(syntax_results['spelling_errors'])
            suggestions.extend(syntax_results['grammar_errors'])
        except Exception as e:
            print(f"Language analysis failed: {str(e)}")
            syntax_score = 0
            syntax_results = {
                'spelling_score': 0,
                'grammar_score': 0
            }

        try:
            semantic_score = semantic_check(prompt, essay, suggestions)
        except Exception as e:
            print(f"Semantic check failed: {str(e)}")
            semantic_score = 0

        total_score = (statistic_score + 2 * syntax_score + 2 * semantic_score) / 5

        analysis_results = {
            'total_score': round(total_score, 1),
            'statistic_score': round(statistic_score, 1),
            'syntax_score': round(syntax_score, 1),
            'semantic_score': round(semantic_score, 1),
            'suggestions': suggestions
        }

        print("Analysis complete...")
        return jsonify(analysis_results)

    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        return jsonify({'error': 'Internal server error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)