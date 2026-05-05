import os
from openai import OpenAI

def ask(prompt):
  if prompt == '':
    return 'Please ask a question!'

  return ask_server(prompt)


def ask_server(prompt):
  api_key = os.getenv("OPENROUTER_API_KEY")

  client = OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key=api_key,
  )

  res = client.chat.completions.create(
      model="openrouter/free", # Replace with any model available on OpenRouter
      messages=[
          {"role": "user", "content": prompt}
      ]
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
