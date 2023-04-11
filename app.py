from flask import Flask
import json

app = Flask(__name__)

def __get_very_long_response__():
    response = []
    for index in range(10):
        with open('data.json', 'r') as f:
            response.append(json.load(f))
    return response

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/delay')
def delay():
    return __get_very_long_response__()

if __name__ == '__main__':
    app.run()
