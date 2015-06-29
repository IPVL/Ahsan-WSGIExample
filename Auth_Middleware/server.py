if __name__ == "__main__":
    from paste import httpserver
    from simplest import sample_app
    from authentication import Auth
    httpserver.serve(Auth(sample_app), host="localhost", port="8080")
