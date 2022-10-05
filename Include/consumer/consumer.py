import Pyro4
import threading
import sys

def consumer(rule: str) -> None:
  while True:
    message = proxy.receive_message(rule) 
    print("{}: {}".format(rule, message))

def connect_proxy():
  ns = Pyro4.locateNS()
  uri = ns.lookup('obj')
  return Pyro4.Proxy(uri)

rule = None
try:
  rule = sys.argv[1].split("=")[1]
  if rule == None or rule == '': 
    raise 
except:
  print("rule=<character_alphabet>\n \033[91m parameter is required \033[0m")
  sys.exit()
proxy = connect_proxy()
print("connected")
proxy.new_consumer(rule)
thread = threading.Thread(target=consumer, args=(rule,))

try:
  thread.start()
  thread.join()
except KeyboardInterrupt:
  proxy = connect_proxy()
  proxy.remove_consumer(rule)
  print("O consumidor foi encerrado")
  sys.exit()
  