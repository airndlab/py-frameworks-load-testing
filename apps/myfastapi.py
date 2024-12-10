import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class StatusResponse(BaseModel):
    status: str


class QuestionRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    answer: str


@app.get("/", response_model=StatusResponse)
async def status():
    return StatusResponse(status="UP")


@app.post("/asking", response_model=AnswerResponse)
async def ask(request: QuestionRequest) -> AnswerResponse:
    return AnswerResponse(answer=f"Your question: {request.question}")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
