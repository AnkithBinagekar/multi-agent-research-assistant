from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import sys
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    topic: str

@app.get("/")
def root():
    return {"status": "Backend running"}

@app.post("/run")
def run_agents(query: Query):
    try:
        result = subprocess.run(
            [sys.executable, "main.py", query.topic],   # ✅ REAL interpreter
            cwd=os.path.dirname(__file__),              # ✅ run inside backend
            capture_output=True,
            text=True
        )

        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)

        return {
            "output": result.stdout if result.stdout else result.stderr
        }

    except Exception as e:
        return {"error": str(e)}
