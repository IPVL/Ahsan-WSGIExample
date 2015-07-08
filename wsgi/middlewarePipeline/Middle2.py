__author__ = 'ahsanul'

class Caseless:

    def __init__(self, app):
        self.app = app
        print "Initializing Middleware 2"

    def __call__(self, environ, start_response):
        print "Entering middleware 2 callable"
        for chunk in self.app(environ, start_response):
            yield chunk.lower()

        print "chunk is lower cased"
