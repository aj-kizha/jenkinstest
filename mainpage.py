from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "hello world"


if __name__ == '__main__':
    _dict = {}
    a =+ 3
    usernmame = 'aaa'
    print("hello")
    print(eval('1+2'))
    app.run('0.0.0.0')
