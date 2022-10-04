import Pyro4
import random
import time
import threading
from generate_message import *
from rules import *
import sys

def connect_proxy():
  ns = Pyro4.locateNS()
  uri = ns.lookup('obj')
  return Pyro4.Proxy(uri)

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

time_sleep = None

try:
  time_sleep = 60 / int(sys.argv[1].split("=")[1])
  if time_sleep == None or time_sleep == '': 
    raise 
except:
  print("mps=<integer_number>\n \033[91m parameter is required \033[0m")
  sys.exit()

proxy = connect_proxy()
proxy.new_producer()
print('connected')


thread_prod = threading.Thread(target=producer)

try:
  thread_prod.start()
  thread_prod.join()
except KeyboardInterrupt:
  proxy = connect_proxy()
  proxy.remove_producer()
  print("O produtor foi encerrado")
  
  sys.exit()
  