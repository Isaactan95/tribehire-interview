from flask import Flask
app = Flask(__name__)

isConnected = False

@app.before_first_request
def get_data():
    pass

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()