from flask import Flask, render_template, Response
from capture import Video
import pdb
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def gen(capture):
    while True:
        frame = capture.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/stream')
def stream():
    return Response(gen(Video()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)