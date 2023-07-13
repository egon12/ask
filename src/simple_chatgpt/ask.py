import openai

def ask(prompt):
  if prompt == "":
    return "Please ask a question!"

  res = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role":"user","content":prompt}],
      temperature=1,
      max_tokens=512,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
      )

  choice = res.choices[0]

  return choice.message.content

def main():
  try:
    prompt = get_prompt()
    print(ask(prompt))
  except KeyboardInterrupt:
    print('\nCanceled!')
    sys.exit(0)

def get_prompt():
  args = sys.argv[1:]

  if len(args) == 0:
    prompt = input('Are there anything that I can help? ')
  elif len(args) == 1 and args[0] == "-":
    if sys.stdin.isatty():
      print('Type your prompt and press Ctrl+D to finish.')
    prompt = sys.stdin.read()
  else:
    prompt = ' '.join(args)

  return prompt

if __name__ == "__main__":
  main()
