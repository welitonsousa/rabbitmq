import time
import sys

def message_collector(socket) -> None:
  msg = socket.recv()
  decoded = bytes.decode(msg)
  print("{} - Received: {}".format(time.time(), decoded))
  time.sleep(2)
  socket.send(str.encode("{} - response".format(decoded)))

def get_args(index: int, default: int) -> int:
  if len(sys.argv) >= index + 1:
    return int(sys.argv[index])
  return default
