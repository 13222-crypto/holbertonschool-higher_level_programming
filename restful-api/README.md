# RESTful API Project

## Task 2: Consuming and processing data from an API using Python
Fetches data from JSONPlaceholder using `requests` and exports it to a CSV file (`posts.csv`).

## Task 3: Develop a simple API using Python with the `http.server` module
An HTTP server built entirely with Python's built-in `http.server` module.

## Task 4: Develop a Simple API using Python with Flask
A robust and lightweight RESTful API implemented using the Flask web framework. It supports memory storage, user creation via POST requests, and field validation.

### Endpoints:
* `GET /` -> Returns greeting text.
* `GET /status` -> Returns `OK`.
* `GET /data` -> Returns a JSON list of all stored usernames.
* `GET /users/<username>` -> Returns full details of a specific user.
* `POST /add_user` -> Creates a new user (Requires valid JSON body).

### How to run Task 4:
```bash
python3 task_04_flask.py
