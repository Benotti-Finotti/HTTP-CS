#!/usr/bin/env python3
import socket
import sys

HOST = sys.argv[1]
if(len(sys.argv) < 1):
    page = '/'
else:
    PAGE = sys.argv[2]

print("We will fetch '{0}{1}'".format(HOST, PAGE))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, 80))
    http_request = "GET {0} HTTP/1.0\r\n\r\n".format(PAGE)
    print("HTTP Request: ")
    print(http_request)
    s.sendall(str.encode(http_request))
    response_buffer = b''
    while True:
        data = s.recv(1024)
        response_buffer += data
        if len(data) == 0:
                break
    print("HTTP response: ")
    print(response_buffer.decode('utf-8', 'ignore'))