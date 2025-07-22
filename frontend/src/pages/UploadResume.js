import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "./uploadResume.css";

axios.defaults.withCredentials = true;

const UploadResume = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [resumeId, setResumeId] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        const savedId = sessionStorage.getItem("resume_id");
        if (savedId) {
            setResumeId(savedId);
        }
    }, []);

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        if (!selectedFile) {
            alert("Please select a file first.");
            return;
        }

        const formData = new FormData();
        formData.append("resume", selectedFile);

        try {
            const response = await axios.post(
                "http://localhost:8000/api/resumes/upload/",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                }
            );

            const { resume_id } = response.data;
            setResumeId(resume_id);
            sessionStorage.setItem("resume_id", resume_id);
            alert("Resume uploaded successfully. ID: " + resume_id);
        } catch (error) {
            console.error("Upload error:", error);
            alert("Error uploading resume.");
        }
    };

    return (
        <div className="upload-container">
            <header className="upload-header">Upload Your Resume</header>

            <form onSubmit={handleSubmit} className="upload-form">
                <label htmlFor="resume-upload" className="upload-label">
                    Select a PDF or DOCX file
                </label>
                <input
                    id="resume-upload"
                    type="file"
                    accept=".pdf,.doc,.docx"
                    onChange={handleFileChange}
                />

                <button type="submit" className="upload-button">
                    Submit
                </button>
            </form>

            {resumeId && (
                <div className="resume-options">
                    <p className="resume-id-info">
                        Resume uploaded with ID: <strong>{resumeId}</strong>
                    </p>

                    <button
                        className="resume-button"
                        onClick={() => navigate(`/resume/${resumeId}`)}
                    >
                        View Resume Details
                    </button>

                    <button
                        className="resume-button"
                        onClick={() => navigate(`/recommendations/${resumeId}`)}
                    >
                        View Recommendations
                    </button>
                </div>
            )}
        </div>
    );
};

export default UploadResume;
