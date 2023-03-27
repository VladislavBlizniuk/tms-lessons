from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/ping')
def ping():
    return f'<a href="/pong">ping</a>'
@app.route('/pong')
def pong():
    return f'<a href="/ping">pong</a>'

if __name__ == '__main__':
    app.run(port=8002, debug= True)