from pathlib import Path

path = Path('guest_book.txt')
content = ''
while True:
    print("Enter 'q' to quit")
    name = input("Please enter a name: ")
    if name == 'q':
        break
    content += f'{name}\n'
path.write_text(content)