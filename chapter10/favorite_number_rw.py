from pathlib import Path
import json

path = Path('fav_num.json')

if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"your favorite number is {favorite_number}")
else:
    favorite_number = input("what is your favorite number? ")
    contents = json.dumps(favorite_number) 
    path.write_text(contents)