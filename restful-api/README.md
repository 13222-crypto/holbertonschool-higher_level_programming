# Task 2: Consuming and processing data from an API using Python

## Description
This project focuses on using Python's `requests` library to interact with a public RESTful API (JSONPlaceholder). It demonstrates how to send HTTP GET requests, parse JSON data, and export structured information into a CSV file.

## Files
* `task_02_requests.py`: Contains the core logic with two main functions:
  * `fetch_and_print_posts()`: Fetches all posts and prints their titles along with the HTTP status code.
  * `fetch_and_save_posts()`: Fetches all posts and saves their structured data (`id`, `title`, `body`) into a CSV file.
* `main_02_requests.py`: A script used to test and execute the functions.
* `posts.csv`: The generated output file containing the fetched posts.

## Requirements
* Python 3.9
* `requests` library

## How to Run
1. Install dependencies:
   ```bash
   pip3 install requests
