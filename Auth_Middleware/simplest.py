def sample_app(environ, start_response):
    print "Sample _ Application"
    status = "200 OK"
    body =['ovi','test1']
    res_headers = [('Content-Type', 'text/plain')]
    start_response(status, res_headers)

    return body



