import zmq
import threading
from utils import *
from Constants import *

QUANTITY_PORTS = get_args(1, Constants.QUANTITY_PORTS())
INITIAL_PORT = get_args(2, Constants.DEFAULT_PORT())

context = zmq.Context()
socket = context.socket(zmq.REP)

for index in range(INITIAL_PORT, INITIAL_PORT + QUANTITY_PORTS):
  port = f"tcp://{Constants.HOST()}:{index}"
  print(port)
  socket.bind(port)

threads = []
while True:
  print("join while")
  message_collector(socket)
  # thread = threading.Thread(target=message_collector, args=(socket,))
  # threads.append(thread)
  # thread.start()
