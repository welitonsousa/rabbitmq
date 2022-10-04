import Pyro4
import threading
import time

@Pyro4.expose
class Swapper(object):
  __queues = {}
  __consumers = []
  __producers = 0

  def __create_queue(self, rule: str) -> None:
    if (self.__queues.get(rule) is None):
      self.__queues[rule] = {"value": [], "condition": threading.Condition(), "quantity_add": 0, "quantity_remove": 0, "time_initial": time.time(), "max": 0}

  def __add_message(self, rule: str, message: str, index: int) -> None:
    self.__queues[rule]["condition"].acquire()
    self.__queues[rule]["value"].insert(index, message)
    print("enviado: {} para fila {}".format(message, rule))
    if(len(self.__queues[rule]["value"]) > self.__queues[rule]["max"]):
      self.__queues[rule]["max"] = len(self.__queues[rule]["value"])
    self.__queues[rule]["quantity_add"] += 1
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
        if (self.__consumers.index(rule) != -1):
          message = self.__queues[rule]["value"].pop(0)
          self.__queues[rule]["quantity_remove"] += 1
        print("{} recebeu: {}".format(rule, message))  
        break
      self.__queues[rule]["condition"].wait()
    self.__queues[rule]["condition"].release()
    return message

  def new_consumer(self, rule: str) -> None:
    self.__consumers.insert(0, rule)
    print(self.__consumers)

  def new_producer(self) -> None:
    self.__producers += 1
    print(self.__producers)

  def quantity_producers(self) -> int:
    print(self.__producers)
    return self.__producers

  def quantity_consumers(self) -> int:
    return len(self.__consumers)

  def rule_queues(self) -> list:
    rules = []
    for rule in self.__queues: 
        rules.append(rule)
    return rules

  def quantity_queues(self, rule) -> int:
    return len(self.__queues[rule]["value"])

  def statistic(self, rule):
    time_total = time.time()- self.__queues[rule]["time_initial"]
    max = self.__queues[rule]["max"]
    quantity_add = self.__queues[rule]["quantity_add"]
    quantity_remove = self.__queues[rule]["quantity_remove"]
    quantity_add = quantity_add * 60 / time_total
    quantity_remove = quantity_remove * 60 / time_total
    return {"max": max, "quantity_add": quantity_add, "quantity_remove": quantity_remove}

  def exist_queue(self, rule) -> bool:
    a= self.__queues.get(rule)
    if(a == None):
      return False
    return True


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
