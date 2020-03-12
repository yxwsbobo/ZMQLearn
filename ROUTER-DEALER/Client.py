import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5561")

for request in range(1000):
    print("Sending request %s …" % request)
    socket.send(bytes("Hello" + str(request),encoding = "utf8"))
    
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))