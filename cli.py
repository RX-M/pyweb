# The ssl.wrap_socket parameter cert_reqs specifies whether a certificate is 
# required from the other side of the connection, and whether it will be 
# validated if provided. It must be one of the three values:
#   - CERT_NONE (certificates ignored)
#   - CERT_OPTIONAL (not required, but validated if provided)
#   - CERT_REQUIRED (required and validated)
# If the value of this parameter is not CERT_NONE, then the ca_certs parameter 
# must point to a file of CA certificates.

import ssl
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('github.com', 443))
s.connect(('localhost', 443))
s = ssl.wrap_socket(s, 
                    keyfile=None, 
                    certfile=None, 
                    server_side=False, 
                    cert_reqs=ssl.CERT_NONE, 
                    ssl_version=ssl.PROTOCOL_SSLv23)
s.sendall("GET / HTTP/1.1\r\nHost: github.com\r\nConnection: close\r\n\r\n")

while True:
    new = s.recv(4096)
    if len(new) <= 0:
      s.close()
      break
    print new
