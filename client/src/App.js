import React, { useState } from 'react';
import './styles/App.css';
import TextInput from './components/TextInput';
import RunButton from './components/RunButton';
import ScoreReport from './components/ScoreReport';

const EssayAnalyzer = () => {
  // State for prompt, essay, showRunButton, and analysisResults
  const [prompt, setPrompt] = useState('');
  const [essay, setEssay] = useState('');
  const [showRunButton, setShowRunButton] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const [analysisResults, setAnalysisResults] = useState({
    total_score: 0,
    statistic_score: 0,
    semantic_score: 0,
    syntax_score: 0,
    suggestions: [],
  });

   // Event handlers for prompt and essay changes
  const handlePromptChange = (e) => {
    setPrompt(e.target.value);
    checkRunButtonVisibility(e.target.value, essay);
    setError('');
  };

  const handleEssayChange = (e) => {
    // eslint-disable-next-line
    setEssay(e.target.value);
    checkRunButtonVisibility(prompt, e.target.value);
    setError('');
  };

   // Check the visibility of the RunButton based on prompt and essay values
  const checkRunButtonVisibility = (promptValue, essayValue) => {
    setShowRunButton(promptValue.trim() !== '' && essayValue.trim() !== '');
  };

  // Handle RunButton click
  const handleRunButtonClick = async () => {
    setIsLoading(true);
    setError('');

    try {
      const response = await fetch('http://localhost:5000/api/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt, essay }),
      });

      if (!response.ok) {
        throw new Error('Failed to analyze the essay');
      }

      const results = await response.json();
      setAnalysisResults(results);
    } catch (error) {
      console.error('Analysis failed:', error);
      setError('Failed to analyze the essay. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleClear = () => {
    setPrompt('');
    setEssay('');
    setError('');
    setAnalysisResults({
      total_score: 0,
      statistic_score: 0,
      semantic_score: 0,
      syntax_score: 0,
      suggestions: [],
    });
    setShowRunButton(false);
  };

  return (
    <div className="container">
      <div className="left-section">
        <TextInput
          placeholder={`Enter the topic sentence...\n\nExample: Present your views on the below topic. Many of the world's lesser-known languages are being lost as fewer and fewer people speak them. The governments of countries in which these languages are spoken should act to prevent such languages from becoming extinct.`}
          value={prompt}
          onChange={handlePromptChange}
        />
        <TextInput
          placeholder={`Enter the essay...\n\nExample: The speaker asserts that governments of countries...`}
          value={essay}
          onChange={handleEssayChange}
          isLarge={true}
        />
        <div className="button-group">
          <RunButton 
            onClick={handleRunButtonClick} 
            disabled={!showRunButton || isLoading} 
          />
          <button 
            className="clear-button"
            onClick={handleClear}
            disabled={isLoading}
          >
            Clear All
          </button>
        </div>
        {error && <div className="error-message">{error}</div>}
      </div>

      <div className="right-section">
        <ScoreReport analysisResults={analysisResults} />
        <div className="suggestions">
          <h3>Suggestions for Improvement</h3>
          {isLoading ? (
            <div className="loading-message">Analyzing your essay...</div>
          ) : (
            <ul>
              {analysisResults.suggestions.map((suggestion, index) => (
                <li key={index} className="suggestion-item">
                  {suggestion}
                </li>
              ))}
            </ul>
          )}
          {!isLoading && analysisResults.suggestions.length === 0 && (
            <p className="no-suggestions">
              No suggestions yet. Run the analysis to get feedback on your essay.
            </p>
          )}
        </div>
      </div>
    </div>
  );
};

export default EssayAnalyzer;