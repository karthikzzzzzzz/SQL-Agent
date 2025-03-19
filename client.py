from fastapi import HTTPException,FastAPI
from starlette import status
from schema import Request
from services import chat

app= FastAPI()

@app.post("/chat")
async def chat_with_ai(request: Request):
    try:
        result = await chat.run_query(request.text)
        return result  
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error processing query: {str(e)}")
