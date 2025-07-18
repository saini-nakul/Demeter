import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import './LandingPage.css'
import { BeatLoader } from "react-spinners"

const LandingPage = () => {
  const [topic, setTopic] = useState("")
  const [loading, setLoading] = useState(false)


  const handleAnalyze = async () => {
    if (!topic.trim()) return alert("Please enter a topic.")

    setLoading(true)

    try {
      const res = await fetch('http://localhost:5000/api/scrape', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic })
      })

      const data = await res.json()
      console.log('Scraped Data:', data)

    

      // Pass data via navigation state
      navigate('/dashboard', { state: { scrapedPosts: data, topic } })
    } catch (err) {
      console.error('Error scraping:', err)
      alert("Something went wrong while Scraping :(")
    } finally {
      setLoading(false)
    }
  }

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
            {loading ? (
              <div className="spinner-container">
                <BeatLoader color="#2563EB" size={20} />
              </div>
            ) : (
              <>
                <input
                  type="text"
                  placeholder="Search anything..."
                  value={topic}
                  onChange={(e) => setTopic(e.target.value)}
                />
                <button className="analyze-btn" onClick={handleAnalyze}>
                  Analyze Now
                </button>
              </>
            )}
          </div>
        </main>
      </div>
    </div>
  )
}

export default LandingPage
