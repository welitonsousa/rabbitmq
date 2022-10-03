import zmq
import threading
import time
from random import choice
from utils import *
from Constants import *

port = get_args(1, Constants.DEFAULT_PORT())

context = zmq.Context()
socket  = context.socket(zmq.REQ)
connection = f"tcp://{Constants.HOST()}:{port}"
socket.connect(connection)

while True:
	selected_message = choice(Constants.DEFAULT_MESSAGES())
	print(selected_message)
	send_msg = str.encode(selected_message)
	socket.send(send_msg)
	msg = socket.recv()
	result = bytes.decode(msg)
	print (result)
	time.sleep(2)