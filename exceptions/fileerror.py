def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return content

print(read_file("my_text.txt"))
