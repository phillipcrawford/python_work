from pathlib import Path

path = Path('moby_dick_or_the_whale.txt')
contents = path.read_text()
print(contents.count('the '))