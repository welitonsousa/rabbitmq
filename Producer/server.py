import zmq
import sys

QUANTITY_PORTS = sys.argv[1] or 1
INITIAL_PORT = sys.argv[2] or 8000


context = zmq.Context()
socket = context.socket(zmq.REP)

# p1 = f"tcp://{HOST}:{PORT1}" 
# p2 = f"tcp://{HOST}:{PORT2}"
# s.bind(p1)
# s.bind(p2)

# while True:
# 	msg = s.recv()
# 	decoded = bytes.decode(msg)
	
# 	print("Received:", decoded)

# 	decoded = str.split(decoded)
# 	if len(decoded) == 3:
# 		a, operation, b = decoded
# 		a = float (a)
# 		b = float (b)
# 	else:
# 		operation = 'invalid'
	
# 	if (operation == '+'):
# 		result = a+b
# 	elif (operation == '*'):
# 		result = a*b
# 	elif (operation == '**'):
# 		result = a**b
# 	else:
# 		result = 'invalid input'
	
# 	s.send(str.encode("{:.2f}".format(result)))