import time

def message_collector():
  msg = s.recv()
  decoded = bytes.decode(msg)
  print("{} - Received: {}".format(time.time(), decoded))
  time.sleep(2)
  s.send(str.encode("{} - response".format(decoded)))