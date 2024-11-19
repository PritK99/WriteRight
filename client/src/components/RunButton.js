import React from 'react';

const RunButton = ({ onClick, disabled }) => {
  return (
    <button 
      className="run-button"
      onClick={onClick}
      disabled={disabled}
    >
      {disabled && <span className="loading">Processing...</span>}
      {!disabled && (
        <>
          <span>Analyze Essay</span>
          <svg 
            xmlns="http://www.w3.org/2000/svg" 
            width="20" 
            height="20" 
            viewBox="0 0 24 24" 
            fill="none" 
            stroke="currentColor" 
            strokeWidth="2" 
            strokeLinecap="round" 
            strokeLinejoin="round"
          >
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
          </svg>
        </>
      )}
    </button>
  );
};

export default RunButton;
