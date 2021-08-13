from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/papa/{post_id}")
def read_post(post_id: int, q: Optional[str] = None):
    return {"post_id": post_id, "q": q}
