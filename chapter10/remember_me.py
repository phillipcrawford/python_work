from pathlib import Path
import json

path = Path('remember_me.json')

def write_user():
    contents = {}
    contents['first name'] = input("What is your first name? ")
    contents['last name'] = input("what is your last name? ")
    contents['age'] = input("What is your age? ")
    contents = json.dumps(contents)
    path.write_text(contents)

def read_user():
    contents = path.read_text()
    lines = json.loads(contents)
    prompt = input(f'Are you {lines["first name"]}? Type \'yes\' to confirm ')
    if prompt == 'yes':
        for key, values in lines.items():
            print(f'Your {key} is {values}')
    else:
        write_user()
        
def greet_user():
    if path.exists():
        read_user()
    else:
        write_user()
greet_user()