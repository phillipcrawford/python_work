from pathlib import Path

animals = ['cats.txt', 'dogs.txt']
for animal in animals:
    path = Path(animal)
    contents = path.read_text()

    lines = contents.splitlines()
    for line in lines:
        print(line)



