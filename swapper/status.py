import Pyro4
from threading import Thread

ns = Pyro4.locateNS()
uri = ns.lookup('obj')

acesso = Pyro4.Proxy(uri)
def status():
    while True:
        op = input("\n-t (tamanho das filas)\n-f (filas criadas)\n-c (consumidores)\n-p (consumidores)\n")
        stt = acesso.status(op)
        print(stt)
    
thread_prod = Thread(target=status)
thread_prod.start()
thread_prod.join()