try:
    with open('sushu.txt', 'r') as file:
        content = file.read()
        print("File contents:\n", content)
except FileNotFoundError:
    print("File not found!")
