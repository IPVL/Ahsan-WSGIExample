def green(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return ['%s\n' % environ.get('GREETING', 'Hello world!')]


def greetingSetter(app):

    def _curried(environ, start_response):
        environ['GREETING'] = 'Bonjour, le monde!'
        return app(environ, start_response)

    return _curried

if __name__ == '__main__':
    from paste import httpserver
    from caseless import Caseless	
    httpserver.serve(Caseless(greetingSetter(green)), host='127.0.0.1', port='8080')



