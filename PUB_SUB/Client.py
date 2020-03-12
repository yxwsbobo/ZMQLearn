import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")

#必须设置才能接受到
socket.setsockopt(zmq.SUBSCRIBE,''.encode('utf-8'))
while True:
    response = socket.recv();
    print("response: %s" % response)