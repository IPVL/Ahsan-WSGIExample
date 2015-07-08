# TEST :
# 		curl -v -X PUT -T <filepath to upload> http://127.0.0.1:8080/<optional filepath>
# Example : curl -v -X PUT -T test_wsgi1.txt http://127.0.0.1:8080/wsgi.txt

import pprint
import os


def sample_app(environ, start_response):
	# pprint.pprint(environ)
	# print

	# The environment variable CONTENT_LENGTH may be empty or missing
	try:
		request_body_size = int(environ.get('CONTENT_LENGTH', 0))
	except (ValueError):
		request_body_size = 0

	# Get file path from PATH env
	path = environ['PATH_INFO']
	file_path = 'downloaded/downloaded.txt'
	if path:
		file_path = 'downloaded' + path

	# Create directory for download if not exist.
	if not os.path.exists(os.path.dirname(file_path)):
		os.makedirs(os.path.dirname(file_path))

	# When the method is POST the query string will be sent
	# in the HTTP request body which is passed by the WSGI server
	# in the file like wsgi.input environment variable.
	request_body = environ['wsgi.input'].read(request_body_size)
	# print request_body
	with open(file_path, 'w') as f:
		f.write(request_body)

	status = "200 OK"
	body =['successfully uploaded\n']
	res_headers = [('Content-Type', 'text/plain')]
	start_response(status, res_headers)

	return body

if __name__ == "__main__":
    from paste import httpserver
    httpserver.serve(sample_app, host='127.0.0.1', port='8080')
