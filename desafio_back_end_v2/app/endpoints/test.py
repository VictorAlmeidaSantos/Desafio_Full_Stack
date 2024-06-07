from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
def root():
    return {"Hello World"}
