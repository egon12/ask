import os
import sys
from simple_chatgpt.ask import ask

def main(args):
  prompt = ' '.join(args)
  res = ask(prompt)
  print(res)

if __name__ == "__main__":
  main(sys.argv[1:])
