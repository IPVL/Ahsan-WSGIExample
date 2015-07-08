__author__ = 'arun'

class Configured:
    def __init__(self, name, greeting):
        self.name = name
        self.greeting = greeting
        print "Configured Initialized"

    def __call__(self, environ, start_response):
        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain')]
        start_response(status, response_headers)
        print "Configured ya"
        return ['%s, %s!\n' % (self.greeting, self.name)]

def app_factory(global_config, name='Johnny', greeting='Howdy'):
    return Configured(name, greeting)

from caseless import Caseless
def filter_factory(app, global_config):
    print "app: ", app
    print "Caseless(app): ", Caseless(app)
    return Caseless(app)

