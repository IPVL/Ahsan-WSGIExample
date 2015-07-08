# TEST :
# 	
# Example : curl -v -X GET -T test_wsgi1.txt http://127.0.0.1:8080/wsgi.txt
# 
import pprint
import os


def sample_app(environ, start_response):
	
	
	path = environ['PATH_INFO']

	if path:
		file_path = path
     
	# Create directory for download if not exist.
	if not os.path.exists(os.path.dirname(file_path)):
		print "Can't find the file"

        print file_path
	f = open(file_path, 'r')
	data = f.read()

        print data
        fi = open("downloaded.txt","w")
	fi.write(data)
        fi.close()
	status = "200 OK"
	body =['successfully Downloaded\n']
	res_headers = [('Content-Type', 'text/plain')]
	ball=start_response(status, res_headers)
        print ball
	return body

if __name__ == "__main__":
    from paste import httpserver
    httpserver.serve(sample_app, host='127.0.0.1', port='8080')
