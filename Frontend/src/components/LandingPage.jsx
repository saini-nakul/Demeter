import React from 'react';
import './LandingPage.css';

const LandingPage = () => {
  return (
    <div className="landing-container">
      <nav className="navbar">
        <div className="logo">
          <div className="circle-icon"></div>
          <span className="brand">Demeter</span>
        </div>
        <ul className="nav-links">
          <li>Home</li>
          <li>Analyzer</li>
          <li>About</li>
        </ul>
        <button className="sign-in">Sign in</button>
      </nav>

      <div className="main-wrapper">
        <main className="main-content">
          <div className="center-circle"></div>
          <h1>
            Understand EMOTIONS
          </h1>
          <p className="subtitle">in every sentence</p>
          <p className="description">
            Analyze any text and discover whether it’s positive, negative, or neutral — powered by AI.
          </p>
          <div className="search-container">
            <input type="text" placeholder="Search anything..." />
            <button className="analyze-btn">Analyze Now</button>
          </div>
        </main>
      </div>
    </div>
  );
};

export default LandingPage;
