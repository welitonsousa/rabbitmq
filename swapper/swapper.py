import Pyro4
import threading

@Pyro4.expose
class Swapper(object):
  __queues = {}
  __consumers = []

  def __create_queue(self, rule: str) -> None:
    if (self.__queues.get(rule) is None):
      self.__queues[rule] = {"value": [], "condition": threading.Condition()}

  def __add_message(self, rule: str, message: str, index: int) -> None:
    self.__queues[rule]["condition"].acquire()
    self.__queues[rule]["value"].insert(index, message)
    print("enviado: {} para fila {}".format(message, rule))  
    self.__queues[rule]["condition"].notify()
    self.__queues[rule]["condition"].release()
        
  def __fanout(self, message):
    for rule in self.__queues:
      self.__create_queue(rule)
      self.__add_message(rule, message, 0)

  def send_message(self, rule: str, message: str) -> None:
    print(self.__consumers)
    if rule == "fanout":
      self.__fanout(message)
    else:
      self.__create_queue(rule)
      self.__add_message(rule, message, len(self.__queues[rule]["value"]))      

  def receive_message(self, rule: str) -> None:
    self.__create_queue(rule)
    self.__queues[rule]["condition"].acquire()
    message = None
    while True:
      if self.__queues[rule]["value"]:
        message = self.__queues[rule]["value"].pop(0)
        print("{} recebeu: {}".format(rule, message))  
        break
      self.__queues[rule]["condition"].wait()
    self.__queues[rule]["condition"].release()
    return message

  def new_consumer(self, rule: str) -> None:
    self.__consumers.insert(0, rule)
    print(self.__consumers)
  def remove_consumer(self, rule: str) -> None:
    # self.__consumers.remove(rule)
    print(self.__consumers)

daemon = Pyro4.Daemon()
uri = daemon.register(Swapper)
print("running:", uri)
daemon.requestLoop()


# daemon = Pyro4.Daemon()
# uri = daemon.register(Swapper)
# ns = Pyro4.locateNS()
# ns.register('obj', uri)

# print("Ready.")
# daemon.requestLoop()   
