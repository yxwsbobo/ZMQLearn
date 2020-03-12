import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://*:5557")

for i in range(1000):
    socket.send(("test message" + str(i)).encode("utf-8"))
    time.sleep(1)