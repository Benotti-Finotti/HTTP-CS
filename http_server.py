#!/usr/bin/env python3

import socket
import sys
import datetime

PORT = 8080
HOST = '127.0.0.1'

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Server up and listening on {0}:{1}".format(HOST, PORT))
        while True:
            print("waiting for the next connection")
            conn, addr = s.accept()
            print("Got a connection from {0}".format(addr))

            with conn:
                process_http_request(conn)

def process_http_request(conn):
    buff = ''
    while True:
        data = conn.recv(1024)
        if not data:
            break
        buff += data.decode('utf-8', 'ignore')
        if buff.endswith("\r\n\r\n"):
            break
    print("Request: ")
    print(buff)
    response = respond_404('')
    print("Response: ")
    print(response)
    conn.sendall(str.encode(response))

def respond_404(url):
    html = '''<!DOCTYPE html>
    <HTML><HEAD><TITLE>404 Not Found</TITLE></HEAD>
    <BODY>
        <H1>404 Not Found</H1>
        <p>The requested URL was not found on this server.</p>
        </BODY>
        </HTML>
    '''
    return make_header("404 Not Found", html)

def make_header(response_code, payload):
    header = "HTTP/1.0 {0}\r\n".format(response_code)
    header += "Date:{0}\r\n".format(datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT'))
    header += "Server: my_python_server\r\n"
    header += "Content-length: {0}\r\n".format(len(payload))
    header += "Connection: close\r\n"
    header += "Content-type: text/html\r\n"
    header += "\r\n"
    return header + payload

if __name__ == "__main__":
    main()