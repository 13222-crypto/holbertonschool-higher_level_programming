# RESTful API Project

## Task 2: Consuming and processing data from an API using Python
Fetches data from JSONPlaceholder using `requests` and exports it to a CSV file (`posts.csv`).

## Task 3: Develop a simple API using Python with the `http.server` module
An HTTP server built entirely with Python's built-in `http.server` module. It handles routing and serves plain text and JSON responses for defined endpoints.

### Endpoints:
* `/` -> Returns plain text greeting.
* `/data` -> Returns sample JSON dataset.
* `/status` -> Returns `OK`.
* `/info` -> Returns API metadata in JSON.
* Any other path -> Returns a `404 Endpoint not found` error.

### How to run Task 3:
```bash
python3 task_03_http_server.py
