from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book API Starter")


class BookIn(BaseModel):
    title: str
    author: str


books = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin"},
    {"id": 2, "title": "Fluent Python", "author": "Luciano Ramalho"},
]


@app.get("/books")
def list_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", status_code=201)
def create_book(payload: BookIn):
    new_id = max(book["id"] for book in books) + 1 if books else 1
    new_book = {"id": new_id, "title": payload.title, "author": payload.author}
    books.append(new_book)
    return new_book
