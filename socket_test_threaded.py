#!/usr/bin/python

import Queue
import threading
import socket
import sys

def sock_test(log_q, url):

    s = socket.socket()
    
    try:
        s.connect((url, 80))

        s.send('GET / HTTP/1.1\r\n')
        s.send('Host: '+ url + '\r\n\r\n')

        response = s.recv(50)
    
        words = response.split(' ')

        if words[1] == '200':
            log_q.put("web server checks out")
        
            s.close

    except IOError:
        log_q.put("Connection to " + url + "failed\n")

# queue for log entries from threads
log_data = Queue.Queue()

thread_list = []

theurls = ['www.google.com', 'www.cnn.com', 'www.googl1e.com']

# Create and listify the threads
for url in theurls:
    t = threading.Thread(target=sock_test, args=(log_data, url))
    thread_list.append(t)

# Start the threads
for thread in thread_list:
    thread.start()

# Joins threads and dumps a log entry
for thread in thread_list:
    thread.join()
    print log_data.get()

                      
