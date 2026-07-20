import http.server, socketserver, os

DIR = "/Users/sproits/Desktop/Sales Dashboard - Claude Code"
PORT = 8777

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=DIR, **k)
    def log_message(self, *a):
        pass

os.chdir(DIR)
with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print(f"Serving {DIR} at http://127.0.0.1:{PORT}")
    httpd.serve_forever()
