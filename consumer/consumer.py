import Pyro4
import threading
import atexit

def exit_handler():
  print('My application is ending!')

atexit.register(exit_handler)
uri = input("URI:").strip()
proxy = Pyro4.Proxy(uri)


def consumer(rule: str) -> None:
  while True:
    print("asd")
    message = proxy.receive_message(rule) 
    print("{}: {}".format(rule, message))


rule = input("Rule:")
thread = threading.Thread(target=consumer, args=(rule,))
proxy.new_consumer(rule)
thread.start()
thread.join()


