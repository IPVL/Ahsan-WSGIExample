__author__ = 'arun'
class Caseless:
    def __init__(self, app):
        self.app = app
        print "Caseless initialized with app:",app

    def __call__(self, environ, start_response):
        for chunk in self.app(environ, start_response):
            print "chunk.lower: ", chunk.lower()
            tar = chunk.lower()
            print "tar : ", tar
            if "bienvenu, bharney!" in tar:
                yield "akkas "
            else:
                yield "trueasfd"

            print "Caseless"


