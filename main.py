from fastapi import FastAPI
from pydantic import BaseModel
from code_agents.explain_agent import explain_code
from code_agents.fix_agent import fix_code
from code_agents.generate_agent import generate_code
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

class CodeInput(BaseModel):
    code: str

class TaskInput(BaseModel):
    task: str



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/explain-code")
def explain_endpoint(request: CodeInput):
    explanation = explain_code(request.code)
    return {"explanation": explanation}

@app.post("/fix-code")
def fix_endpoint(request: CodeInput):
    fixed = fix_code(request.code)
    return {"fixed_code": fixed}

@app.post("/generate-code")
def generate_endpoint(request: TaskInput):
    generated = generate_code(request.task)
    return {"generated_code": generated}
