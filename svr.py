# To generate a self signed cert:
# $ openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365

import BaseHTTPServer, SimpleHTTPServer
import ssl

httpd = BaseHTTPServer.HTTPServer(('localhost', 443), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='./key.pem', certfile='./cert.pem', server_side=True)
httpd.serve_forever()
