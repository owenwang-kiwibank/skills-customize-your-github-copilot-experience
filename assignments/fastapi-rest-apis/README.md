# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI so you can practice defining endpoints, validating request data, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Set up a FastAPI app and implement basic endpoints for managing a list of books.

#### Requirements
Completed program should:

- Create a FastAPI app with endpoints for listing all books and getting one book by ID.
- Return JSON responses with clear keys such as id, title, and author.
- Return a helpful error message when a requested book ID does not exist.


### 🛠️ Add Create and Validation Logic

#### Description
Add a POST endpoint to create new books and validate incoming data using Pydantic models.

#### Requirements
Completed program should:

- Define a Pydantic model for incoming book data with required fields.
- Implement a POST endpoint that adds a new book and returns the created record.
- Validate invalid input and return appropriate HTTP status codes.
