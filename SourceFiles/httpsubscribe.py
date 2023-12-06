import argparse
import numpy as np
import cv2
import time
from flask import Flask, render_template, Response
from is_wire.core import Channel, Subscription, Message
from is_msgs.image_pb2 import Image

app = Flask(__name__)
video_feed = None


def to_np(input_image):
    if isinstance(input_image, np.ndarray):
        output_image = input_image
    elif isinstance(input_image, Image):
        buffer = np.frombuffer(input_image.data, dtype=np.uint8)
        output_image = cv2.imdecode(buffer, flags=cv2.IMREAD_COLOR)
    else:
        output_image = np.array([], dtype=np.uint8)
    return output_image


def image_stream(camera_index):
    global video_feed
    broker_uri = "amqp://10.10.2.211:30000"
    channel_1 = Channel(broker_uri)
    subscription_1 = Subscription(channel=channel_1, name=f"Intelbras_Camera_{camera_index}")
    subscription_1.subscribe(topic=f'CameraGateway.{camera_index}.Frame')

    while True:
        msg = channel_1.consume()
        frame = msg.unpack(Image)
        frame = to_np(frame)
        ret, jpeg = cv2.imencode('.jpg', frame)

        video_feed = jpeg.tobytes()
        #time.sleep(0.3)


@app.route('/')
def index():
    return render_template('index.html')


def generate():
    while True:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + video_feed + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed_route():
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    from threading import Thread
    import argparse

    parser = argparse.ArgumentParser(description='Start the video streaming server.')
    parser.add_argument('--camera', type=int, default=2, help='Camera index (default: 2)')
    parser.add_argument('--port', type=int, default=5000, help='Port number (default: 5000)')
    args = parser.parse_args()

    video_thread = Thread(target=image_stream, args=(args.camera,))
    video_thread.daemon = True
    video_thread.start()

    app.run(host='0.0.0.0', debug=True, threaded=True, port=args.port)

