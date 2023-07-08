import os
import sys
from simple_chatgpt.ask import ask

def main():
  args = sys.argv[1:]

  if len(args) == 0:
    prompt = input('Are there anything that I can help? ')
  elif len(args) == 1 and args[0] == "-":
    prompt = sys.stdin.read()
  else:
    prompt = ' '.join(args)

  print(ask(prompt))

if __name__ == "__main__":
  main()
