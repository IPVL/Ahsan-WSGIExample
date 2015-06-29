class Auth:
    def __init__(self, app):
        self.app = app
        self.username = 'ovi'
        self.password ='test'

    def __call__(self, environ, start_response):
        chunk = iter(self.app(environ, start_response))
        username = next(chunk)
        password = next(chunk)
        if(username == self.username and password == self.password):
            return ["Hello",username]
        else:
            return ["Sorry!"]

