import React from 'react';

const TextInput = ({ placeholder, value, onChange, isLarge, label }) => {
  return (
    <div className={`text-input ${isLarge ? 'large' : ''}`}>
      {label && <label className="input-label">{label}</label>}
      <textarea
        placeholder={placeholder}
        value={value}
        onChange={onChange}
        className="input-textarea"
      />
    </div>
  );
};

export default TextInput;
