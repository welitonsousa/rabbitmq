import Pyro4
import random
import time
import threading
from generate_message import *
from rules import *
import sys

uri = input("URI:").strip()
time_sleep = 60 / int(input("messages/minutes:").strip())
proxy = Pyro4.Proxy(uri)
print('connected')


def producer():
  while(True):
    index = random.randint(0, len(rules))
    message = generate_message()
    if index == len(rules):
      rule = "fanout"
      proxy.send_message(rule, message)
      print("all: {}".format(message))
    else:
      rule = random.choice(rules)
      proxy.send_message(rule, message)
      print("{}: {}".format(rule, message))
    
    time.sleep(time_sleep)

thread_prod = threading.Thread(target=producer)
thread_prod.start()
thread_prod.join()

try:
  thread_prod.start()
  thread_prod.join()
except KeyboardInterrupt:
  print("O produtor foi encerrado")
  sys.exit()
  