import time
import zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    print("Received request: %s" % message)

    # 不可以连续接收
    # message = socket.recv()

    # 模拟耗时
    time.sleep(1)

    socket.send(("world: " + str(message)).encode("utf-8"))