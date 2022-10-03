import time
import sys

def get_args(index: int, default: int) -> int:
  if len(sys.argv) >= index + 1:
    return int(sys.argv[index])
  return default
