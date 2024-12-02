from pathlib import Path

path = Path('python_reader.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    line = line.replace('python', 'c')
    print(line)