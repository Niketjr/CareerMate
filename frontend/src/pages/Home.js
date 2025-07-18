import React from "react";
import { Link } from "react-router-dom";
import "./Home.css";

const Home = () => {
    return (
        <div className="home-container">
            <header className="top-bar">
                <span>CareerMate</span>
                <div className="top-right">
                    <Link to="/dashboard">Dashboard</Link>
                    <Link to="/chat">Chatbot</Link>
                </div>
            </header>

            <main className="main-content">
                <h1>
                    Your Smart Career <br /> Companion Starts Here.
                </h1>
                <p className="sub">
                    <Link to="/upload">Upload your resume</Link> and get personalized insights.
                </p>
            </main>

            <footer className="footer">
                <Link to="/recommendations">Recommendations</Link>
                <Link to="/resume/123">Sample Resume</Link>
            </footer>
        </div>
    );
};

export default Home;
