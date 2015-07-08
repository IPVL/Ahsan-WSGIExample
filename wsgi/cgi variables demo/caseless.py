__author__ = 'arun'
class Caseless:
    def __init__(self, app):
        print 'Caseless'
        self.app = app

    def __call__(self, environ, start_response):
        print "Case Less __call__"
        for chunk in self.app(environ, start_response):
            print "Case Less"
            yield chunk.lower()
        print "Case Less end"

