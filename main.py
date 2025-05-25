from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

marks_dict = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
}

@app.get("/api")
def get_marks(name: list[str] = Query([])):
    results = [marks_dict.get(n, 0) for n in name]
    return {"marks": results}
