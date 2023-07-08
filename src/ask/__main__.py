import openai
import os
import sys

def main():
  prompt = ' '.join(sys.argv[1:])
  res = ask(prompt)
  print(res.choices[0].message.content)

def ask(prompt):
  return openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role":"user","content":prompt}],
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
      )

if __name__ == "__main__":
  main()
