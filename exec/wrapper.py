import imp
import sys
import StringIO

def application(environ, start_response):
    # trap the exit handler, we don't want scripts exiting randomly
    # we might want to do something with the return code later
    retcode = None
    def exit_handler(rc):
        retcode = rc

    sys.exit = exit_handler

    # trap the output buffer
    outbuf = StringIO.StringIO()
    sys.stdout = outbuf

    # catch stderr output in the parent's error stream
    sys.stderr = environ['wsgi.errors']

    # import the script
    script = environ['processor.py']
    f = open(script, "rb")
    imp.load_module('__main__', f, script, ("py", "rb", imp.PY_SOURCE))
    f.close()

    # outbuf has a typical CGI response, headers separated by a double
    # newline, then content
    (header, content) = outbuf.getvalue().split('\n\n', 1)
    headers = [tuple(x.split(': ', 1)) for x in header.split('\n')]

    # return it wsgi style
    start_response('200 OK', headers)
    return [content]
