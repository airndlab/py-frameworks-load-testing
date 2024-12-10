import uvicorn
from sanic import Sanic, json

app = Sanic(__name__)


@app.get("/")
async def status(request):
    return json({"status": "UP"})


@app.post("/asking")
async def ask(request):
    data = request.json
    question = data['question']
    return json({"answer": f"Your question: {question}"})


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
