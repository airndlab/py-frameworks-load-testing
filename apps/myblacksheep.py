from dataclasses import dataclass

import uvicorn
from blacksheep import Application, post, get, FromJSON
from blacksheep.server.openapi.v3 import OpenAPIHandler
from openapidocs.v3 import Info

app = Application()

docs = OpenAPIHandler(info=Info(title="Example API", version="0.0.1"))
docs.bind_app(app)


@dataclass
class StatusResponse:
    status: str


@dataclass
class QuestionRequest:
    question: str


@dataclass
class AnswerResponse:
    answer: str


@get("/")
async def status() -> StatusResponse:
    return StatusResponse("UP")


@post("/asking")
async def ask(body: FromJSON[QuestionRequest]) -> AnswerResponse:
    request: QuestionRequest = body.value
    return AnswerResponse(answer=f"Your question: {request.question}")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
