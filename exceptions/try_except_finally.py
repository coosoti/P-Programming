#!/usr/bin/python3
def read_file(file_path):
    file = None
    try:
        file = open(file_path, "r")
        content = file.read()
        return content
    except FileNotFoundError:
        print("File not found!")
    finally:
        if file is not None:
            file.close()

print(read_file("myfile.txt"))

