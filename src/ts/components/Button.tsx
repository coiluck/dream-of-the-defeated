import React from 'react';
import './Button.css';

// プロパティの型定義
type ButtonProps = {
  text: string;
  onClick: () => void;
  minWidth?: string;
  fontSize?: string;
  className?: string;
};

export const Button: React.FC<ButtonProps> = ({
  text,
  onClick,
  minWidth = 'clamp(10rem, 7.5rem + 6.6667vw, 15rem)',
  fontSize = '1rem',
  className = ''
}) => {
  return (
    <div className={`button-component-container ${className}`}>
      <button
        className="button-component"
        style={{ minWidth: minWidth, fontSize: fontSize }}
        onClick={onClick}
      >
        {text}
      </button>
    </div>
  );
};