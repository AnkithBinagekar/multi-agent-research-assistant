from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import json
import sys

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    topic: str

@app.post("/run")
def run_agents(query: Query):
    try:
        result = subprocess.run(
            [sys.executable, "main.py", query.topic],
            capture_output=True,
            text=True
        )

        return json.loads(result.stdout)

    except Exception as e:
        return {"final": f"Backend error: {str(e)}"}
