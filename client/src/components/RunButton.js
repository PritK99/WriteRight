import React from 'react';

const RunButton = ({ onClick, disabled }) => {
    return <button onClick={onClick} disabled={disabled}>Run</button>;
};

export default RunButton;
