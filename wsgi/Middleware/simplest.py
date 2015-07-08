__author__ = 'ahsanul'

import time

def simple_app(environ, start_response):
    """Simplest possible application object"""
    print "Enter to simple_app"
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    print "Before calling start_response"
    time.sleep(10)
    start_response(status, response_headers)
    print "After calling start_response"
    return ['Hello world!\n']

