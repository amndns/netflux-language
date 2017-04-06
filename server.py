import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

target = open('index.html', 'w+')
value = "HELLO, SERVER"
html = "<html><head></head><body><h1>" + value +"</h1></body></html>"
target.write(html)
target.close()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
