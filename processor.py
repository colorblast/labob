#! /usr/bin/python

import cgi

import cgitb
cgitb.enable()

HTML_HEADER = 'Content-type: text/html'

HEAD = '''
<!DOCTYPE html>
<html lang='en'>
    <head>
          <meta charset="UTF-8">
          <title>Processed</title>
    </head>
    <body>
'''

END = '''
    </body>
</html>    
'''

def main():
	print HTML_HEADER
	print HEAD
	print END
main()
