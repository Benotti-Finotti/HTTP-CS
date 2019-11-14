# HTTP Client & Server
This is an HTTP client program writen with Python.
It uses the "socket" library and the class assignment was to implement the HTTP protocol itself. One can connect to "google.com" for example and get the page "index.html" in which it will print an appropriate HTTP response on success.
The "http_server.py" program parses HTTPv1.0 requests, looking for a GET request(s) in the local directory and responds with a 200 code and the contents of the file, along with appropriate content-type (currently only supports HTML). And if the file does not exist, it will return a 404 code.
