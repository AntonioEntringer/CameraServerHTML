import numpy as np
import cv2
import time
from is_wire.core import Channel,Subscription,Message
from is_msgs.image_pb2 import Image


def to_np(input_image):

    if isinstance(input_image, np.ndarray):
        output_image = input_image
    elif isinstance(input_image, Image):
        buffer = np.frombuffer(input_image.data, dtype=np.uint8)
        output_image = cv2.imdecode(buffer, flags=cv2.IMREAD_COLOR)
    else:
        output_image = np.array([], dtype=np.uint8)
    return output_image


if __name__ == '__main__':

    broker_uri = "amqp://10.10.2.211:30000"
    channel_1 = Channel(broker_uri)
    
    subscription_1 = Subscription(channel=channel_1,name=f"Intelbras_Camera_{camera}")
    subscription_1.subscribe(topic=f'CameraGateway.{camera}.Frame')

    while True:
        time1 = time.time()
        msg = channel_1.consume()  
        frame = msg.unpack(Image)
        frame = to_np(frame)

        cv2.imshow("img", frame)

#        print(time.time() - time1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
