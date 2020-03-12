import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

for i in range(1000):
    socket.send(("current times:" + str(i)).encode("utf-8"))
    time.sleep(1)    