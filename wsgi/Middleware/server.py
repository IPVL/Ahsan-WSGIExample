__author__ = 'ahsanul'


if __name__ == '__main__':
    from paste import httpserver
    from simplest import simple_app
    from Middle import Caseless
    print "Starting the server"
    httpserver.serve(Caseless(simple_app), host='127.0.0.1', port='8080')
    print("Ending the server")