from flask import Flask
import subprocess
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0")
