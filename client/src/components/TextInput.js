import React from 'react';

const TextInput = ({ placeholder, value, onChange, isLarge }) => {
    const textareaStyle = {
        height: isLarge ? '500px' : '100px',
        width: '99%',
    };

    return (
        <textarea
            placeholder={placeholder}
            value={value}
            onChange={onChange}
            style={textareaStyle}
        />
    );
};

export default TextInput;
