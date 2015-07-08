__author__ = 'arun'
if __name__ == "__main__":
    from paste import httpserver
    from simplest import sample_app
    from caseless import Caseless
    httpserver.serve(Caseless(sample_app), host="localhost", port="8080")
    print "Server "
