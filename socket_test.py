#!/usr/bin/python

import socket

s = socket.socket()
web_url = 'www.google.com'
s.connect((web_url, 80))

s.send('GET / HTTP/1.1\r\n')
s.send('Host: '+ web_url + '\r\n\r\n')

response = s.recv(50)

print response
words = response.split(' ')
print words
print words[1]
if words[1] == '200':
    print "web server checks out"

s.close

