import difflib

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

with open("data/data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

class Query(BaseModel):
    text: str

class QuizAnswers(BaseModel):
    answers: dict

def get_closest_match(user_input: str, questions: list):
    user_input = user_input.lower()

    closest_match = difflib.get_close_matches(user_input, questions, n=1, cutoff=0.6)

    if closest_match:
        return closest_match[0]
    return None


@app.post("/ask")
async def ask_question(query: Query):
    user_input = query.text
    questions = [q["question"].lower() for q in data["questions"]]

    closest_question = get_closest_match(user_input, questions)

    if closest_question:
        for item in data["questions"]:
            if item["question"].lower() == closest_question:
                return {"answer": item["answer"], "suggestions": item.get("next_topics", [])}

    raise HTTPException(status_code=404, detail="No matching question found")


@app.get("/questions")
async def get_questions():
    questions = [item["question"] for item in data["questions"]]
    return {"questions": questions}