from pathlib import Path

path = Path('python_reader.txt')
contents = path.read_text()
print(contents)
#lines = contents.splitlines()
#for line in lines:
#    print(line)