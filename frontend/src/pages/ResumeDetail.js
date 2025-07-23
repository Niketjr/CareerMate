import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './ResumeDetail.css';

const ResumeDetail = () => {
    const { id } = useParams();
    const [resume, setResume] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchResume = async () => {
            try {
                const response = await axios.get(`http://localhost:8000/api/resumes/${id}/`);
                setResume(response.data);
                setLoading(false);
            } catch (err) {
                console.error(err);
                setError('Error fetching resume details');
                setLoading(false);
            }
        };

        fetchResume();
    }, [id]);

    if (loading) return <div className="resume-detail-container">Loading...</div>;
    if (error) return <div className="resume-detail-container">{error}</div>;
    if (!resume) return <div className="resume-detail-container">No resume found</div>;

    return (
        <div className="resume-detail-container">
            <h2>Resume Details</h2>

            <div className="resume-field">
                <strong>ID:</strong> <span>{resume.id}</span>
            </div>
            <div className="resume-field">
                <strong>Name:</strong> <span>{resume.name}</span>
            </div>
            <div className="resume-field">
                <strong>Skills:</strong> <span>{resume.skills?.join(', ')}</span>
            </div>
            <div className="resume-field">
                <strong>Education:</strong> <span>{resume.education}</span>
            </div>
            <div className="resume-field">
                <strong>Experience:</strong> <span>{resume.experience}</span>
            </div>
        </div>
    );
};

export default ResumeDetail;
