from git import Git
from .ask import ask

commit_message_prompt = 'Please generate commit message based on this diff\n\n'

def generate_commit_message():
    git = Git()
    diff = git.diff('--staged')
    commit_message = ask(commit_message_prompt + diff)
    return commit_message

def main():
    print(generate_commit_message())

if __name__ == '__main__':
    main()
