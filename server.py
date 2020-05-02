import pyqrcode

from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    messagetosend = bytes('welcome to Booking Jini',"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    print(self.requestline)
    return

qr_code = pyqrcode.create('Wizards')
server_address_httpd = ('192.168.43.29',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('starting server')
httpd.serve_forever()
print(qr_code.terminal(quiet_zone=1))
