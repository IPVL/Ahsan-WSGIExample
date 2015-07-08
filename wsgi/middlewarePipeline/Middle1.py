
class GreetingSetter:

    def __init__(self,app):
        self.app = app
        print "Initializing Middleware 1"

    def __call__(self,environ, start_response):
        print "Entering middleware 1 callable"
        environ['GREETING'] = 'Bonjour, le monde!'
        print "Greeting is set"
        return self.app(environ, start_response)