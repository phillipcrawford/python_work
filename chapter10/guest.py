from pathlib import Path

path = Path('guest.txt')
name = input("Hello, what is your name? ")
path.write_text(name)