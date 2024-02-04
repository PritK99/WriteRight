import React, { useState, useEffect } from 'react';
import './styles/App.css';
import TextInput from './components/TextInput';
import RunButton from './components/RunButton';
import ScoreReport from './components/ScoreReport';

const EssayAnalyzer = () => {
  // State for prompt, essay, showRunButton, and analysisResults
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

  // Event handlers for prompt and essay changes
  const handlePromptChange = (e) => {
    setPrompt(e.target.value);
    checkRunButtonVisibility(e.target.value, essay);
  };

  const handleEssayChange = (e) => {
    // eslint-disable-next-line
    setEssay(e.target.value);
    checkRunButtonVisibility(prompt, e.target.value);
  };

  // Check the visibility of the RunButton based on prompt and essay values
  const checkRunButtonVisibility = (promptValue, essayValue) => {
    setShowRunButton(promptValue.trim() !== '' && essayValue.trim() !== '');
  };

  // Handle RunButton click
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

  // Render the component
  return (
    <div className="container">
      <div className="left-section">
        {/* TextInput components for prompt and essay */}
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
        {/* RunButton component */}
        <RunButton onClick={handleRunButtonClick} disabled={!showRunButton} />
      </div>

      <div className="right-section">
        {/* ScoreReport component */}
        <ScoreReport analysisResults={analysisResults} />

        {/* Suggestions section */}
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
