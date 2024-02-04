import React from 'react';

const ScoreReport = ({ analysisResults }) => {
    return (
        <div className="score-report">
            <div className="score-item">
                <strong>Total Score:</strong> {analysisResults.total_score} / 10
            </div>
            <div className="score-item">
                <strong>Statistic Score:</strong> {analysisResults.statistic_score} / 10
            </div>
            <div className="score-item">
                <strong>Syntax Score:</strong> {analysisResults.syntax_score} / 10
            </div>
            <div className="score-item">
                <strong>Semantic Score:</strong> {analysisResults.semantic_score} / 10
            </div>
        </div>
    );
};

export default ScoreReport;
