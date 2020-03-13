import threading
import zmq

def step1(context=None):
    """Step 1"""
    context = context or zmq.Context.instance()

    sender = context.socket(zmq.PAIR)
    sender.connect("inproc://step2")
    message="step1 ready".encode('utf-8')
    sender.send(message)


def step2(context=None):
    """Step 2"""
    context = context or zmq.Context.instance()
    receiver = context.socket(zmq.PAIR)
    receiver.bind("inproc://step2")

    msg = receiver.recv()
    print(msg)
    sender = context.socket(zmq.PAIR)
    sender.connect("inproc://step3")
    message="step2 ready".encode('utf-8')
    sender.send(message)

def step3(context=None):
    context = zmq.Context.instance()
    receiver = context.socket(zmq.PAIR)
    receiver.bind("inproc://step3")

    string= receiver.recv()
    print(string)
    print("Test successful!")
    receiver.close()
    context.term()


def main():
    """ server routine """

    thread1 = threading.Thread(target=step1)
    thread1.start()

    thread2 = threading.Thread(target=step2)
    thread2.start()

    thread3 = threading.Thread(target=step3)
    thread3.start()


main()