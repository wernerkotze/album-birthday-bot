from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

todos = [
    {
        "id": "1",
        "item": "Read a book."
    },
    {
        "id": "2",
        "item": "Cycle around town."
    }
]

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", tags=["root"])
async def read_root() -> dict:
	return {"message": "Welcome to the best album birthday generator on the internet!"}

@app.get("/todo", tags=["todos"])
async def get_todos() -> dict:
	return { "data": todos }
