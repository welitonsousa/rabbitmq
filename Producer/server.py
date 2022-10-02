import zmq
import sys
import threading
from MessageCollector import message_collector

QUANTITY_PORTS = sys.argv[1] or 1
INITIAL_PORT = sys.argv[2] or 8000
HOST = '127.0.0.1'

context = zmq.Context()
socket = context.socket(zmq.REP)

for index in range(INITIAL_PORT, INITIAL_PORT + QUANTITY_PORTS):
  port = f"tcp://{HOST}:{index}"
  print(port)
  s.bind(port)

threads = []
while True:
  thread = threading.Thread(target=message_collector)
  threads.append(thread)
  thread.start()
