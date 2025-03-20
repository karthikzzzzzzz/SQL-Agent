import React, { useState } from 'react';
import ChatBotIcon from './components/ChatBotIcon';
import ChatForm from './components/ChatForm';
import getResponse from './api/chat.js';
import ChatMessage from './components/ChatMessage';


function App() {
  const [chatHistory, setChatHistory] = useState([]);
  const [showChatbot, setShowChatbot] = useState(false);

  const generatebotResponse = async (history) => {
    const userMessage = history[history.length - 1].text;
    let botMessage=getResponse(userMessage);
    setChatHistory(prevHistory => [
      ...prevHistory,
      { role: 'chatbot', text: botMessage },
    ]);
  }

  return (
    <div className={`container`}>
      <button 
        onClick={() => setShowChatbot(prev => !prev)} 
        id="chatbot-toggle" 
        className={showChatbot ? 'open' : ''}>
        <span className="icon open-icon material-symbols-rounded">mode_comment</span>
      </button>
      <div className={`chatbot-popup ${showChatbot ? 'show-chatbot' : ''}`}>
        <div className="chat-header">
          <div className="header-info">
            <ChatBotIcon />
            <h2 className="logo-text">Chatbot</h2>
          </div>
          <button 
            className="close-button"
            onClick={() => setShowChatbot(false)}>
            <span className="material-symbols-rounded">close</span>
          </button>
        </div>

        <div className="chat-body">
          <div className="message bot-message">
            <ChatBotIcon />
            <p className="message-text">
              Hello! I'm a SQL-Agent, I can help you to write SQL queries easily. How can I help you today?
            </p>
          </div>

          {chatHistory.map((message, index) => (
            <ChatMessage key={index} chat={message} />
          ))}
        </div>

        <div className="chat-footer">
          <ChatForm chatHistory={chatHistory} setChatHistory={setChatHistory} generatebotResponse={generatebotResponse} />
        </div>
      </div>
    </div>
  );
}

export default App;
