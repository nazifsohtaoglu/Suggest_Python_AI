from fastapi import FastAPI, HTTPException
from suggest import generate_suggestion

app = FastAPI()

MAX_INPUT_LENGTH = 40

@app.get("/suggest")
async def suggest(prompt: str):
    check_input_length(prompt)
    res = generate_suggestion(prompt)
    return {"message": res}

def check_input_length(prompt:str):
    if len(prompt)>= MAX_INPUT_LENGTH:
        raise HTTPException(status_code=400, detail="Input length is too long. Must be under {MAX_INPUT_LENGTH} ")
    pass