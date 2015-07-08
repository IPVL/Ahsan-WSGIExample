


class Caseless:

    def __init__(self, app):
        print "Middleware initialized"
        self.app = app

    def __call__(self, environ, start_response):
        print "Middleware callable called"
        for chunk in self.app(environ, start_response):
            yield chunk.lower()
        print "Middleware callable end"