from http.server import HTTPServer , BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html lang="en">
<head>
<title>My Webserver</title>
</head>
<body>
<h1>11 TIMES TABLES</h1>
<h2>11 X 0 = 0<br>
11 X 1 = 11<br>
11 X 2 = 22<br>
11 X 3 = 33<br>
11 X 4 = 44<br>
11 X 5 = 55<br>
11 X 6 = 66<br>
11 X 7 = 77<br>
11 X 8 = 88<br>
11 X 9 = 99<br>
11 X 10 = 110<br>
</h2>
</body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request recieved")

        #To create response header
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        #To send the respose
        self.wfile.write(content.encode())

#To create server address
server_address = ('',80)

#To create server object
httpd = HTTPServer(server_address,MyHandler)

#To listen at the specified port
print("My webserver is running...")
httpd.serve_forever()