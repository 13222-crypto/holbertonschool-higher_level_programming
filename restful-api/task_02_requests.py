import csv
import requests

def fetch_and_print_posts():
    """يقوم بجلب المنشورات وطباعة كود الحالة وعناوين المنشورات."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])

def fetch_and_save_posts():
    """يقوم بجلب المنشورات وحفظ الحقول (id, title, body) داخل ملف CSV."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        # هيكلة البيانات المطلوبة فقط باستخدام List Comprehension
        structured_data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]
        
        fieldnames = ["id", "title", "body"]
        
        # كتابة البيانات داخل ملف posts.csv
        with open("posts.csv", mode="w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_data)
