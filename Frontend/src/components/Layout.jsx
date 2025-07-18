import React from 'react'
import { Outlet, useNavigate } from 'react-router-dom'
import './LandingPage.css' // or move common styles to a shared CSS

const Layout = () => {
  const navigate = useNavigate()

  return (
    <>
      <nav className="navbar">
        <div className="logo" onClick={() => navigate('/')}>
          <div className="circle-icon"></div>
          <span className="brand">Demeter</span>
        </div>
        <ul className="nav-links">
          <li onClick={() => navigate('/')}>Home</li>
          <li onClick={() => navigate('/dashboard')}>Analyzer</li>
          <li>About</li>
        </ul>
        <button className="sign-in">Sign in</button>
      </nav>
      <Outlet />
    </>
  )
}

export default Layout
