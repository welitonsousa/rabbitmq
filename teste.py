# import time
# import threading

# filas = {}

# def test(key, message):
#   if (filas.get("a") is None):
#     filas[key] = {"value": [], "condition": threading.Condition()}
#   time.sleep(2)
#   filas[key]["value"].append(message)

# threads = []
# thread1 = threading.Thread(target=test, args=("tcc", "teste"))
# thread2 = threading.Thread(target=test, args=("tcc2", "teste2"))

# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print(filas)
# for i in filas:
#   print(i)


a = [1]
if (a):
  print("entrou") 

if __name__ == "__main__":
  print("entrou")