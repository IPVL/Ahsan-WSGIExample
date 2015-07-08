def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    return ['''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    ''']

if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(simple_app, host='127.0.0.1', port='8080')
