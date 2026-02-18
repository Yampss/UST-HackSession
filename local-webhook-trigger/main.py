from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

TOKEN = "123"

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if f"token={TOKEN}" in self.path:
            subprocess.run(["bash", "maintenance.sh"]) 
            self.send_response(200)
            self.wfile.write(b"Done")
        else:
            self.send_response(403)

HTTPServer(("0.0.0.0", 8000), H).serve_forever()
