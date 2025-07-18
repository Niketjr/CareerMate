import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import "./Recommendations.css";

const Recommendations = () => {
    const { id } = useParams(); // resume id
    const [loading, setLoading] = useState(true);
    const [recommendations, setRecommendations] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchRecommendations = async () => {
            try {
                const res = await axios.get(`http://localhost:5000/api/recommendations/${id}`);
                setRecommendations(res.data.recommendations || []);
            } catch (err) {
                setError("Failed to fetch job recommendations.");
            } finally {
                setLoading(false);
            }
        };

        fetchRecommendations();
    }, [id]);

    if (loading) return <div className="recommendations-container">Loading recommendations...</div>;
    if (error) return <div className="recommendations-container error">{error}</div>;

    return (
        <div className="recommendations-container">
            <h1 className="recommendations-title">Recommended Jobs Based on Your Resume</h1>
            {recommendations.length === 0 ? (
                <p>No recommendations found. Try uploading a more detailed resume.</p>
            ) : (
                <ul className="recommendations-list">
                    {recommendations.map((job, index) => (
                        <li key={index} className="recommendation-item">
                            <h3>{job.title}</h3>
                            <p>{job.description}</p>
                            <p className="skills-match">Matches your skills: {job.matchingSkills.join(", ")}</p>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default Recommendations;
