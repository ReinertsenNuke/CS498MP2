from flask import Flask, request

import socket


app = Flask(__name__)


@app.route('/',methods=['POST'])
def do_post():
    subprocess.Popen("stress_cpu.py")

@app.route('/',methods=['GET'])
def do_get():
    return socket.gethostname()

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)