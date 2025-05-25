from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Query

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

marks_data = {
    "Alice": 85,
    "Bob": 90,
    "X": 10,
    "Y": 20
}

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    results = [marks_data.get(n, 0) for n in name]
    return {"marks": results}
