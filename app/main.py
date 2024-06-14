from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model import qa_model

app = FastAPI()

@app.get("/api/v1/qa")
async def qa(q: str | None = None):
    try:        
        answer = qa_model(q)
            
        return JSONResponse(content={"question": q, "answer": answer})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)