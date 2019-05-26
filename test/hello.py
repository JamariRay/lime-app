from flask import Flask, url_for
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/usr/<name>')
def user(name):
    return '{}'.format(name)


if __name__ == '__main__':
    app.run()
