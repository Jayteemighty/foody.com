from fastapi import APIRouter, HTTPException
from services.ai_service import ask_food_related_question

router = APIRouter()

@router.post("/ask/")
async def ask_question(question: str):
    if not question:
        raise HTTPException(status_code=400, detail="Question is required.")
    
    answer = await ask_food_related_question(question)
    return {"question": question, "answer": answer}
