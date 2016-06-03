from flask import Flask

app = Flask('hello')

def index():
        return 'Hello, World!'

app.add_url_rule('/', 'index', index)

app.run(host='0.0.0.0')
