#!/usr/bin/python
import socket

# loglevels: 1 == minimal; 5 == all
loglevel = 5
logfilename = "./scorebot.log"

def openlogfile(filename):
    logfile = open(filename, "a")

def logevent(event, level):
    if level <= loglevel:
        logfile.write(event)

# check_dns tries to resolve ns1.team.ctf.  Here we assume that the usma.ctf
# DNS server is properly referring to team servers.
def check_dns(team):
    dns_url = 'ns1.' + team + '.ctf'
    s = socket.socket()

    try:
        s.gethostbyname(web_url)
    except IOError:
        logevent(team + ": Unable to resolve DNS server (ns1." + team + ".ctf", 5)
    else:
        logevent(team + ": DNS server resolves correctly", 5)

def check_web(team):
    web_url = 'www.' + team + '.ctf'
    s = socket.socket()

    try:
        s.connect((web_url, 80))

        s.send('GET / HTTP/1.1\r\n')
        s.send('Host: '+ web_url + '\r\n\r\n')

        response = s.recv(20)

        # print response
        words = response.split(' ')
        # print words
        # print words[1]
        if words[1] == '200':
            logevent(team + ": Web server providing 200 OKAY response", 5)
            success = 1
        else:
            logevent(team + ": Web server BAD RESPONSE", 5)
            success = 0

        s.close()
    except IOError:
        logevent(team + ": Connection to web server failed", 5)


def check_ftp(team):
    ftp_url - 'ftp.' + team + '.ctf'
    s = socket.socket()
    s.connect((ftp_url, 21))

    response = s.recv(8) #should be enough to get '220' response
    words = response.split(' ')
    if words[0] == '220':
        logevent(team + ": FTP server providing 220 (OKAY) response", 5)
        success = 1
    else:
        logevent(team + ": FTP server: BAD RESPONSE", 5)
        success = 0

def main():

    logfile = open(logfilename, "a")
    
    teams = ['team1', 'team2', 'team3', 'team4', 'team5']
    for team in teams:
        result = check_web(team)


if __name__ == "__main__":
    main()
