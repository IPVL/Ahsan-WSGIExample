__author__ = 'arun'

if __name__ == '__main__':
    from paste import httpserver
    from paste.deploy import loadapp
    httpserver.serve(loadapp('config:setup.cfg', relative_to='.'), host='127.0.0.1', port='8888')
    print "Server "
