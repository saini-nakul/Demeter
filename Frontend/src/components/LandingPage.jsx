import React from 'react'
import { useNavigate } from 'react-router-dom'
import './LandingPage.css'

const LandingPage = () => {
  const navigate = useNavigate()

  return (
    <div className="landing-container">
      <div className="main-wrapper">
        <main className="main-content">
          <div className="center-circle"></div>
          <h1>Understand EMOTIONS</h1>
          <p className="subtitle">in every sentence</p>
          <p className="description">
            Analyze any text and discover whether it’s positive, negative, or neutral — powered by AI.
          </p>
          <div className="search-container">
            <input type="text" placeholder="Search anything..." />
            <button className="analyze-btn" onClick={() => navigate('/dashboard')}>
              Analyze Now
            </button>
          </div>
        </main>
      </div>
    </div>
  )
}

export default LandingPage
