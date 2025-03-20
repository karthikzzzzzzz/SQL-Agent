const getResponse = async (userMessage)=>{
    try {
        const response = await fetch('http://localhost:8000/chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ text: userMessage }),
        });
  
        if (!response.ok) {
          throw new Error('Failed to fetch bot response');
        }
        const data = await response.json();
        const botMessage = data.response;
        return botMessage;
        
      } catch (error) {
        console.error('Error:', error);
      }
    }

export default getResponse;    
