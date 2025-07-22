import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

// Import your pages
import Home from './pages/Home';
import UploadResume from './pages/UploadResume';
import ResumeDetail from './pages/ResumeDetail';
import Recommendations from './pages/Recommendations';
import Chatbot from './pages/Chatbot';
import Dashboard from './pages/Dashboard';


function App() {
  return (
    <Router>
      {/* <Navbar /> */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/upload" element={<UploadResume />} />
        <Route path="/resume/:id" element={<ResumeDetail />} />
        <Route path="/recommendations/:id" element={<Recommendations />} />
        <Route path="/chat" element={<Chatbot />} />
      </Routes>
    </Router>
  );
}

export default App;
