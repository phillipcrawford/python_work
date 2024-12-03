from pathlib import Path
import json

path = Path('remember_me.json')

if path.exists():
    #read
    contents = path.read_text()
    lines = json.loads(contents)
    for key, values in lines.items():
        print(f'Your {key} is {values}')
else:
    #write
    contents = {}
    contents['first name'] = input("What is your first name? ")
    contents['last name'] = input("what is your last name? ")
    contents['age'] = input("What is your age? ")
    contents = json.dumps(contents)
    path.write_text(contents)
