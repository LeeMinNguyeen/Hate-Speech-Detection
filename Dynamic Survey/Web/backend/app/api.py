from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.tools.redis_client import RedisClient
from app.Data.questions import QUESTIONS
import uuid
from datetime import datetime
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/redis/create_session")
async def create_session():
    session_id = "session_"+str(uuid.uuid4())
    redis_client = RedisClient()
    now = datetime.now().isoformat()
    redis_client.list_set(session_id, {"timestamp": now, "type": "start_interview"})
    redis_client.disconnect()
    return {"status": "Session created", "session_id": session_id}

@app.get("/redis/get_session/{session_id}")
async def get_session(session_id: str):
    redis_client = RedisClient()
    session_data = redis_client.list_get(session_id)
    redis_client.disconnect()
    if session_data:
        return {"session_id": session_id, "session_data": session_data}
    else:
        return {"status": "Session not found"}

@app.get("/questions/get_standard_questions")
async def get_standard_questions():
    questions = QUESTIONS["STANDARD"]['questions']
    number_of_questions = 9
    random_questions = random.sample(questions, min(len(questions), number_of_questions))
    return {"questions": random_questions}

@app.post("/survey/get_answer")
async def get_answer(session_id: str, answer: dict):
    redis_client = RedisClient()
    redis_client.list_set(session_id, answer)
    return {"status": "Answer saved"}

