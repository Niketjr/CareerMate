import React, { useState } from "react";
import "./Chatbot.css";

const Chatbot = () => {
    const [messages, setMessages] = useState([
        { sender: "bot", text: "Hi there! How can I help you today?" }
    ]);
    const [input, setInput] = useState("");
    const [loading, setLoading] = useState(false);

    const sendMessage = async () => {
        if (input.trim() === "") return;

        const userMessage = { sender: "user", text: input };
        setMessages(prev => [...prev, userMessage]);
        setInput("");
        setLoading(true);

        try {
            const response = await fetch("http://localhost:8000/chatbot/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ message: input })
            });

            const data = await response.json();

            const botReply = {
                sender: "bot",
                text: data.response || "Sorry, I couldn't process that."
            };

            setMessages(prev => [...prev, botReply]);
        } catch (error) {
            setMessages(prev => [
                ...prev,
                { sender: "bot", text: "Error connecting to chatbot backend." }
            ]);
        }

        setLoading(false);
    };

    return (
        <div className="chatbot-container">
            <h1 className="chatbot-title">CareerMate Chatbot</h1>

            <div className="chat-window">
                {messages.map((msg, index) => (
                    <div
                        key={index}
                        className={`message ${msg.sender === "user" ? "user" : "bot"}`}
                    >
                        {msg.text}
                    </div>
                ))}
                {loading && <div className="message bot">Typing...</div>}
            </div>

            <div className="input-section">
                <input
                    type="text"
                    placeholder="Ask me anything..."
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={(e) => e.key === "Enter" && sendMessage()}
                />
                <button onClick={sendMessage}>Send</button>
            </div>
        </div>
    );
};

export default Chatbot;
