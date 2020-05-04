import pyqrcode
from http.server import BaseHTTPRequestHandler, HTTPServer

request = None

users=["deepak","nitesh","anurag","dibyarupa"]
login_id=["12345","23145","32145","42315"]
for i in range(len(login_id)):
    s=login_id[i]
    qr_code = pyqrcode.create('Wizards')
    print(qr_code.terminal(quiet_zone=1))
    print(users[i])


class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global request
    request = self.requestline
    request = request[5 : int(len(request)-9)]
    print(request)
    if request is in (login_id):
        messagetosend = bytes('yes',"utf")
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(messagetosend))
        self.end_headers()
        self.wfile.write(messagetosend)
        print(messagetosend)
    
    if request == '12345Wizards':
        messagetosend = bytes('yes',"utf")
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(messagetosend))
        self.end_headers()
        self.wfile.write(messagetosend)
        print(messagetosend)
        
    if request == 'opened':
        print("Door is opened")
    if request == 'closed':
        print("Door is closed")
    
    return

server_address_httpd = ('192.168.43.106',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)

httpd.serve_forever()
