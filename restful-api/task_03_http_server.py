from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "localhost"
PORT = 8000

class SimpleAPIHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # 1. المسار الأساسي /
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))
            
        # 2. مسار البيانات /data
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))
            
        # 3. مسار الحالة /status
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("OK".encode("utf-8"))
            
        # 4. مسار المعلومات /info
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode("utf-8"))
            
        # 5. أي مسار آخر غير موجود 404
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode("utf-8"))

def run_server():
    server = HTTPServer((HOST, PORT), SimpleAPIHandler)
    print(f"Server is running on http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        server.server_close()

if __name__ == "__main__":
    run_server()
