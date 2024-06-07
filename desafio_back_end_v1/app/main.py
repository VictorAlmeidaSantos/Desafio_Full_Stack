from fastapi import FastAPI,HTTPException,Request,status,Response
from app.endpoints import cat_question, test

app = FastAPI()

app.include_router(test.router, prefix="/test", tags=["test"])
app.include_router(cat_question.router, prefix="/cat_question", tags=["Cat Question"])