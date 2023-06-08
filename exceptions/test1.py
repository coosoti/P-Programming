#!/usr/bin/python3
"""read and display the content of a file"""
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found!"

print(read_file("file.txt"))
