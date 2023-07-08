import openai
import bardapi

def ask(prompt):
  if prompt == '':
    return 'Please ask a question!'

  return ask_bard(prompt)
  #return ask_chatgpt(prompt)

def ask_bard(prompt):
  answer = bardapi.core.Bard().get_answer(prompt)
  return answer['content']

def ask_chatgpt(prompt):
  res = openai.ChatCompletion.create(
      model='gpt-3.5-turbo',
      messages=[{'role':'user','content':prompt}],
      temperature=1,
      max_tokens=512,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
      )

  choice = res.choices[0]

  return choice.message.content
