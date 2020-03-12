import time
import zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:5560")

while True:
    message = socket.recv()
    print("Received request: %s" % message)

    time.sleep(1)

    socket.send(("world: " + str(message)).encode("utf-8"))