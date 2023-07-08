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
