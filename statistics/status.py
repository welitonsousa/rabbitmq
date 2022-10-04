import Pyro4
import sys
import time

arg = sys.argv

ns = Pyro4.locateNS()
uri = ns.lookup('obj')
proxy = Pyro4.Proxy(uri)

def statistic(rule: str) -> None:
    statistic = proxy.statistic(rule)
    print(statistic["quantity_add"], "messages received per minute")
    print(statistic["quantity_remove"], "messages delivered per minute")
    print(statistic["max"], "maximum size the queue has reached") 

def help():
    print("-p\t\t  retorna a quantidade de produtores conectados.")
    print("-c\t\t  retorna a quantidade de consumidores conectados.")
    print("-f\t\t  retorna as filas criadas.")
    print("-f <nome_fila> -t retorna o tamanho da fila.")
    print("-c\t\t  retorna a quantidade de consumidores conectados.")
    print("-f <nome_fila> -s retorna a estatística da fila.")
    print("-s <SEGUNDOS>     retorna a estatística de todas as filas com o intervalo de SEGUNDOS.")


def status():
    if(arg[1] == '-p'):
        print(proxy.quantity_producers())
    elif(arg[1] == '-c'):
        print(proxy.quantity_consumers())
    elif(arg[1] == '-f' and len(arg)>= 4 and arg[3] == '-t'):
        if(proxy.exist_queue(arg[2])):
            print(proxy.quantity_queues(arg[2]))
        else:
            print("queue not find")
    elif(arg[1] == '-f' and len(arg)>= 4 and arg[3] == '-s'):
        if(proxy.exist_queue(arg[2])):
            statistic(arg[2])
        else:
            print("queue not find")
    elif(arg[1] == '-f'):
        rule_queues = proxy.rule_queues()
        for rule in rule_queues:
            print(rule)
    elif(arg[1] == '-s'):
        while(True):
            rule_queues = proxy.rule_queues()
            for rule in rule_queues:
                print(rule)
                statistic(rule)
                print("\n")
            time.sleep(int(arg[2]))
    elif(arg[1] == '-h'):
        help()
    else:
        print("command not found")
        print("type -h for help")

        

    


status()