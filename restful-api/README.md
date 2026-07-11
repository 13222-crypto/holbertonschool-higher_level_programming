# RESTful API Project

## Task 2: Consuming data from an API
Uses Python `requests` library to fetch data and export it into a CSV file.

## Task 3: Simple API with http.server
A basic native Python server providing custom path routing.

## Task 4: Simple API with Flask
A lightweight Flask API simulating CRUD capabilities in memory.

## Task 5: API Security and Authentication Techniques
Implements security layers on API endpoints using HTTP Basic Auth and Token-based Auth via JWT.

### Endpoints:
* `GET /basic-protected` -> Access secured by Basic Auth.
* `POST /login` -> Exchanges valid credentials for a JWT Token.
* `GET /jwt-protected` -> Standard route protected by JWT.
* `GET /admin-only` -> Route restricted to users with the 'admin' role.
