import uvicorn
from muffin import Application

app = Application()


@app.route("/", methods=["GET"])
async def status(request):
    return {"status": "UP"}


@app.route("/asking", methods=["POST"])
async def ask(request):
    data = await request.json()
    question = data['question']
    return {"answer": f"Your question: {question}"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
