import SimpleHTTPServer
import SocketServer

PORT = 3000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT

target = open('index.html', 'w+')
value = "HELLO, SERVER"
html = "<html><head></head><body><h1>" + value +"</h1></body></html>"
target.write(html)
target.close()

httpd.serve_forever()
