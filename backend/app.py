from flask import Flask, render_template
from flask_cors import CORS
from flask_sock import Sock

app = Flask(__name__,
    template_folder='./www',
    static_folder='./www',
    static_url_path='/'
)
CORS(app)  # Allow access from all domains
sock = Sock(app)

@app.route('/')
def index():
    return "Hello, World! Flask server is running."

@sock.route('/echo')
def echo(ws):
    while True:
        data = ws.receive()
        if data is None:
            break
        ws.send(f"Echo: {data}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
