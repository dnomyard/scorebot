#!/usr/bin/python
import socket

verbose = 1

def check_web(team):
    web_url = 'www.' + team + '.ctf'
    s = socket.socket()
    s.connect((web_url, 80))

    s.send('GET / HTTP/1.1\r\n')
    s.send('Host: '+ web_url + '\r\n\r\n')

    response = s.recv(50)

    # print response
    words = response.split(' ')
    # print words
    print words[1]
    if words[1] == '200':
        if verbose:
            print "web server checks out"
        success = 1

    else:
        success = 0

    s.close

def main():
    
    teams = ['team1', 'team2', 'team3', 'team4', 'team5']
    for team in teams:
        


if __name__ == "__main__":
    main()
