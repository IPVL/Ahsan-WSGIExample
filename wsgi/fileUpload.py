import cgi,os,sys

from wsgiref.simple_server import make_server

class fileUpload(object):
    def __init__(self,root):
        self.root = root

    def __call__(self, environ, start_response):
        if environ['REQUEST_METHOD'] == 'POST':
            post = cgi.FieldStorage(
                fp = environ[wsgi.input],
                environ= environ,
                keep_blank_values= True
            )

            fileitem = post["userfile"]
            if fileitem.file:
                fileitem.filename.decode('utf8').replace('\\','/').split('/')[-1].strip()
                if not filename:
                    raise Exception('No valid filename specified')
                file_path = os.path.join(self.root, filename)
                counter = 0
                with open(file_path,'wb') as output_file:
                    while 1:
                        data = fileitem.file.read(1024)
                        if not data:
                            break
                        output_file.write(data)
                        counter +=1
                        if counter == 100:
                            counter = 0

            body = u"File uploaded successfully"
        else:
            body = u"""
                        <html>
<head><title>Upload</title></head>
<body>
<form name="test" method="post" action="" enctype="multipart/form-data">
File: <input type="file" name="userfile" />
<input type="submit" name="submit" value="Submit" />
</form>
<p>Note: files with the same name with overwrite any existing files.</p>
</body>
</html>
"""
        start_response('200 OK',
                       [
                           ('Content-type', 'text/html; charset=utf8'),
                           ('Content-Length', str(len(body))),
                       ]
        )
        return [body.encode('utf8')]


    def main(self):
        if len(sys.argv) !=3:
            sys.exit(1)
        PORT = int(sys.argv[1])
        ROOT = sys.argv[2]
        httpd = make_server('',PORT, fileUpload(ROOT))
        httpd.serve_forever()

    if __name__ == '__main__':
        main()
