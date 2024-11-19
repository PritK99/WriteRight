import React from 'react';

const ScoreReport = ({ analysisResults }) => {
  return (
    <div className="score-report">
      <h3>Analysis Results</h3>
      <div className="score-item">
        <span className="score-label">Total Score</span>
        <span className="score-value">{analysisResults.total_score} / 10</span>
      </div>
      <div className="score-item">
        <span className="score-label">Statistical Analysis</span>
        <span className="score-value">{analysisResults.statistic_score} / 10</span>
      </div>
      <div className="score-item">
        <span className="score-label">Syntax Evaluation</span>
        <span className="score-value">{analysisResults.syntax_score} / 10</span>
      </div>
      <div className="score-item">
        <span className="score-label">Semantic Analysis</span>
        <span className="score-value">{analysisResults.semantic_score} / 10</span>
      </div>
    </div>
  );
};

export default ScoreReport;