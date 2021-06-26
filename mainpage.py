from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "hello world dev"


if __name__ == '__main__':
    print(eval('1+2'))
    app.run('0.0.0.0')
