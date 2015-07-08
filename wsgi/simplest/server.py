__author__ = 'ahsanul'


if __name__ == '__main__':
    from paste import httpserver
    from simplest import simple_app
    httpserver.serve(simple_app, host='127.0.0.1', port='8080')