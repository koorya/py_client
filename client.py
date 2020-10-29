import zmq
import json
import json_coder.py.json_coder as json_coder
from json_coder.py.messagetypes import *
import cv2

context = zmq.Context()
#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5554")



kill_task = ServiceTask("capture")
j_str = json.dumps(kill_task, cls=json_coder.coder.CustomEncoder)
socket.send(bytes(j_str, 'utf-8'))
capture_answer_str = socket.recv().decode('utf-8')
j_cap_answ = json.loads(capture_answer_str, object_hook=json_coder.decoder.decode_object)
print(j_cap_answ)
if isinstance(j_cap_answ, CNNAnswer):
	img = j_cap_answ.image
	cv2.imshow("client", img)
	cv2.waitKey(2000)
elif isinstance(j_cap_answ, ServiceTask):
	srv_err: ServiceTask = j_cap_answ
	print(srv_err.command)

kill_task = ServiceTask("kill")
j_str = json.dumps(kill_task, cls=json_coder.coder.CustomEncoder)
socket.send(bytes(j_str, 'utf-8'))

print("wait for last resp")
capture_answer_str = socket.recv().decode('utf-8')
j_cap_answ = json.loads(capture_answer_str, object_hook=json_coder.decoder.decode_object)
print(j_cap_answ)
if isinstance(j_cap_answ, CNNAnswer):
	img = j_cap_answ.image
	cv2.imshow("client", img)
	cv2.waitKey(2000)
elif isinstance(j_cap_answ, ServiceTask):
	srv_err: ServiceTask = j_cap_answ
	print(srv_err.command)