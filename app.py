from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! Welcome to my Harness demo application.'

if __name__ == '__main__':
    # Note: App Engine runs the application on port 8080 by default.
    app.run(host='0.0.0.0', port=8080, debug=True)
