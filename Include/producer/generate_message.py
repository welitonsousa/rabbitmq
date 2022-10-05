import random

def generate_message():
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  res = random.choices(alphabet, k=random.randint(2, 10))
  return "".join(res)
