__author__ = 'ahsanul'


def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    print "before calling start_response"
    start_response(status, response_headers)
    print "after calling start_response"
    return ['%s\n' % environ.get('GREETING', 'Hello world!')]
