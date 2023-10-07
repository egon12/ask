import json
import os
import openai
import sys

def save_conv(conv):
    """Save conversation to a file."""
    # Get the filename from the user
    f = get_file()
    json.dump(conv, f)
    f.write("\n")
    f.close()

def reset_conv():
    """Reset conversation to empty."""
    rm_file()

    # Reset the conversation list

def get_file():
    """Get the filename from the user."""
    filepath = "./chat.jsonl"
    if not os.path.exists(filepath):
        return open(filepath, "w")
    return open(filepath, "a")

def rm_file():
    """Remove the file."""
    filepath = "./chat.jsonl"
    if os.path.exists(filepath):
        os.remove(filepath)

def read_messages():
    """Read the messages from the file."""
    filepath = "./chat.jsonl"
    if not os.path.exists(filepath):
        return []
    f = open(filepath, "r")
    messages = []
    for line in f:
        messages.append(json.loads(line))
    f.close()
    return messages

def chat(prompt):
    msg = {"role":"user","content":prompt}
    messages = read_messages()
    messages.append(msg)

    res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=1,
            max_tokens=512,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )

    content = res.choices[0].message.content
    reply_msg = {"role":"assistant","content":content}
    save_conv(msg)
    save_conv(reply_msg)
    print(content)


def get_prompt():
  args = sys.argv[1:]

  if len(args) == 0:
      prompt = input('Could you type?: ')
  elif len(args) == 1 and args[0] == "-":
      if sys.stdin.isatty():
          print('Type and press Ctrl+D after finish.')
      prompt = sys.stdin.read()
  else:
      prompt = ' '.join(args)

  return prompt

def just_chat():
    prompt = get_prompt()
    chat(prompt)

def rchat():
    reset_conv()
    just_chat()


#save_conv({"role":"assistant", "text":"Hello there"})


