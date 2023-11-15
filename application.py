from flask import Flask
import socket

response_test = socket.gethostname()

application = Flask(__name__)
application.add_url_rule('/', 'index', (lambda: response_test))

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)