__author__ = 'arun'
def sample_app(environ, start_response):
    print "Sample _ Application"
    status = "200 OK"
    res_headers = [('Content-Type', 'text/plain'),('name','ovi'),('password','test')]
    start_response(status, res_headers)
    ret = ["%s: %s\n" % (key, value)
           for key, value in environ.iteritems()]
    return ret



