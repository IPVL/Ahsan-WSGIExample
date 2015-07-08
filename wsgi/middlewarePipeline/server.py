__author__ = 'ahsanul'

if __name__ == '__main__':
    from paste import httpserver
    from simplest import simple_app
    from Middle2 import Caseless
    from Middle1 import GreetingSetter
    print("starting the server")
    httpserver.serve(Caseless(GreetingSetter(simple_app)),
                     host='127.0.0.1', port='8080')
    print("Ending the server")