from pathlib import Path

path = Path('python_reader.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)