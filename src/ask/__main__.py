import openai
import os
import sys

def main():
    prompt = ' '.join(sys.argv[1:])
    res = ask(prompt)
    print(res.choices[0].text)

def ask_from_file(filename):
    f = open(filename)
    prompt = f.read()
    res = ask(prompt)
    print(res.choices[0].text)

def ask(prompt):
    return openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt + "\n",
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.0,
    )

if __name__ == "__main__":
    main()
    #ask_from_file("diff.txt")
