import zmq

context = zmq.Context()
#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5554")


socket.send(bytes("kill", 'utf-8'))
print("message send")
message = socket.recv().decode('utf-8')
print("recieve message: {0}".format(message))