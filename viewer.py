#! /usr/bin/python

import cgi

import cgitb
import urllib2, cStringIO
import hmac
from hashlib import sha1
cgitb.enable()
from bs4 import BeautifulSoup

HTML_HEADER = 'Content-type: text/html\n'

HEAD = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Papers</title>
        <meta charset="UTF-8">
    </head>
    <body>
'''

END = '''
    </body>
</html>    
'''

def screenshotlayer(access_key, secret_keyword, url, args):

    # encode URL
    query = urllib2.urlencode(dict(url=url, **args))

    # generate md5 secret key
    secret_key = hashlib.md5('{}{}'.format(url, secret_keyword)).hexdigest()

    return "https://api.screenshotlayer.com/api/capture?access_key=%s&secret_key=%s&%s" % (access_key, query)

params = {
    'fullpage': '1',
    'width': '',
    'viewport': '',
    'format': '',
    'css_url': '',
    'delay': '',
    'ttl': '',
    'force': '',
    'placeholder': '',
    'user_agent': '',
    'accept_lang': '',
    'export': ''
};

access_key = "b2b1a6a29159797f73e852ab0e012372"
url = ''

def main():
    print HTML_HEADER
    print HEAD
    d = urllib2.urlopen('http://marge.stuy.edu/~jonathan.wong/labob/contribs')
    links = []
    soup = BeautifulSoup(f)
    for i in soup.find_all('a', href=True):
        links.append(a['href'])
    for i in range(len(links)):
        url = "http://marge.stuy.edu/~jonathan.wong/labob/contribs" + links[i]
        print screenshotlayer(access_key, secret_keyword, url, params)
        print links[i]
    print END
main()    