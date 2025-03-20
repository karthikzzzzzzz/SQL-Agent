import ChatBotIcon from "./ChatBotIcon";
import UserIcon from "./UserIcon";
const ChatMessage = ({ chat }) => {
    return (
        <div className={`message ${chat.role === "chatbot" ? 'bot' : 'user'}-message`}>
            {chat.role === 'chatbot' ? <ChatBotIcon /> : <UserIcon />}
            <p className="message-text">{chat.text}</p>
        </div>
    );
};

export default ChatMessage;
