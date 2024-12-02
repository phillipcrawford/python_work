from pathlib import Path

animals = ['cats.txt', 'dogs.txt']
for animal in animals:
    path = Path(animal)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
        #print(f"Sorry, the file, {path} does not exist.")
    else:
        lines = contents.splitlines()
        for line in lines:
            print(line)



