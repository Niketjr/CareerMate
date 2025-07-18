import React from "react";
import { Link } from "react-router-dom";
import "./Dashboard.css";

const Dashboard = () => {
    return (
        <div className="dashboard-container">
            <header className="dashboard-header">Welcome to Your Dashboard</header>

            <div className="dashboard-cards">
                <Link to="/upload" className="dashboard-card-link">
                    <div className="dashboard-card">
                        <h2>Uploaded Resumes</h2>
                        <p>Manage the resumes you’ve uploaded.</p>
                    </div>
                </Link>

                <Link to="/recommendations" className="dashboard-card-link">
                    <div className="dashboard-card">
                        <h2>Job Matches</h2>
                        <p>See recommendations based on your resume.</p>
                    </div>
                </Link>
            </div>
        </div>
    );
};

export default Dashboard;
