import React, { useState } from 'react';
import './styles/App.css';

const EssayAnalyzer = () => {
  const [prompt, setPrompt] = useState('');
  const [essay, setEssay] = useState('');
  const [showRunButton, setShowRunButton] = useState(false);

  const [analysisResults, setAnalysisResults] = useState({
    totalScore: 0,
    statisticScore: 0,
    semanticScore: 0,
    syntaxScore: 0,
    suggestions: [],
  });

  const handlePromptChange = (e) => {
    setPrompt(e.target.value);
    checkRunButtonVisibility(e.target.value, essay);
  };

  const handleEssayChange = (e) => {
    setEssay(e.target.value);
    checkRunButtonVisibility(prompt, e.target.value);
  };

  // Run Button is only made visible when user inputs both prompt and essay
  const checkRunButtonVisibility = (promptValue, essayValue) => {
    setShowRunButton(promptValue.trim() !== '' && essayValue.trim() !== '');
  };

  const handleRunButtonClick = () => {
    // Temporary for testing purposes
    const mockAnalysisResults = {
      totalScore: 80,
      statisticScore: 90,
      semanticScore: 85,
      syntaxScore: 75,
      suggestions: ['Improve vocabulary', 'Check grammar'],
    };

    setAnalysisResults(mockAnalysisResults);
  };

  return (
    <div className="container">
      <div className="left-section">
        <textarea
          placeholder={`Enter the topic sentence.\n\nExample: Many of the world's lesser-known languages are being lost as fewer and fewer people speak them. The governments of countries in which these languages are spoken should act to prevent such languages from becoming extinct. Present your perspective on the given issue.`}
          value={prompt}
          onChange={handlePromptChange}
        />
        <textarea
          placeholder={`Enter the essay.\n\nExample: The speaker asserts that governments of countries where lesser-known languages are spoken should intervene to prevent these languages from becoming extinct. I agree in so far as a country's indigenous and distinct languages should not be abandoned and forgotten altogether. At some point, however, I think cultural identity should yield to the more practical considerations of day-to-day life in a global society...`}
          value={essay}
          onChange={handleEssayChange}
        />
        <button onClick={handleRunButtonClick} disabled={!showRunButton}>
          Run
        </button>
      </div>

      <div className="right-section">
        {/* Score Bars */}
        <div className="score-bars">
          <div className="score-bar" style={{ width: `${analysisResults.totalScore}%` }}>
            Total Score
          </div>
          <div className="score-bar" style={{ width: `${analysisResults.statisticScore}%` }}>
            Statistic Score
          </div>
          <div className="score-bar" style={{ width: `${analysisResults.semanticScore}%` }}>
            Semantic Score
          </div>
          <div className="score-bar" style={{ width: `${analysisResults.syntaxScore}%` }}>
            Syntax Score
          </div>
        </div>

        {/* Suggestions */}
        <div className="suggestions">
          <h3>Suggestions:</h3>
          <ul>
            {analysisResults.suggestions.map((suggestion, index) => (
              <li key={index}>{suggestion}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default EssayAnalyzer;