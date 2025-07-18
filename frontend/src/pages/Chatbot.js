import React, { useState } from "react";
import "./Chatbot.css";

const Chatbot = () => {
    const [messages, setMessages] = useState([
        { sender: "bot", text: "Hi there! How can I help you today?" }
    ]);
    const [input, setInput] = useState("");

    const sendMessage = () => {
        if (input.trim() === "") return;

        const userMessage = { sender: "user", text: input };
        const botReply = {
            sender: "bot",
            text: "Thanks for your message! (Bot logic not implemented yet)"
        };

        setMessages([...messages, userMessage, botReply]);
        setInput("");
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
