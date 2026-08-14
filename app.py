from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from 𝐌𝐑 𝐁𝐑𝐈𝐉𝐄𝐒𝐇'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
