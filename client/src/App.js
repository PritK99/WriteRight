import React, { useState, useEffect } from 'react';
import './styles/App.css';
import TextInput from './components/TextInput';
import RunButton from './components/RunButton';
import ScoreReport from './components/ScoreReport';

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

  const checkRunButtonVisibility = (promptValue, essayValue) => {
    setShowRunButton(promptValue.trim() !== '' && essayValue.trim() !== '');
  };

  const handleRunButtonClick = async () => {
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

      try {
        const analysisResults = await response.json();
        console.log(analysisResults);
        setAnalysisResults(analysisResults);
      } catch (error) {
        console.error('Failed to parse response JSON', error);
        // Handle error, show a message, etc.
      }
    } catch (error) {
      console.error(error);
      // Handle error, show a message, etc.
    }
  };

  return (
    <div className="container">
      <div className="left-section">
        <TextInput
          placeholder={`Enter the topic sentence...\n\nExample: Many of the world's lesser-known languages are being lost...`}
          value={prompt}
          onChange={handlePromptChange}
        />
        <TextInput
          placeholder={`Enter the essay...\n\nExample: The speaker asserts that governments of countries...`}
          value={essay}
          onChange={handleEssayChange}
          isLarge={true}
        />
        <RunButton onClick={handleRunButtonClick} disabled={!showRunButton} />
      </div>

      <div className="right-section">
        <ScoreReport analysisResults={analysisResults} />

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
