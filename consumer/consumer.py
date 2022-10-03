import Pyro4
import threading
import sys

def exit_handler():
  print("exist consumer - {}".format(rule))
  proxy.remove_consumer(rule)

def consumer(rule: str) -> None:
  while True:
    message = proxy.receive_message(rule) 
    print("{}: {}".format(rule, message))



uri = input("URI:").strip()
rule = input("Rule:")

proxy = Pyro4.Proxy(uri)
proxy.new_consumer(rule)
thread = threading.Thread(target=consumer, args=(rule,))

try:
  thread.start()
  thread.join()
except KeyboardInterrupt:
  print("O consumidor foi encerrado")
  sys.exit()
  