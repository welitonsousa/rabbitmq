import Pyro4
import random
import time
import threading
from generate_message import *
from rules import *

uri = input("URI:").strip()
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
    
    time.sleep(random.randint(0, 10))

producer()
# thread_prod = threading.Thread(target=producer)
# thread_prod.start()
# thread_prod.join()
