#!/usr/bin/env python3
# Author ID: 100851187

def read_file_string(file_name):
    f = open('data.txt', 'r')
    read_data = f.read()
    f.close()
    return read_data
    # Takes file_name as string for a file name, returns its entire contents as a string

def read_file_list(file_name):
   with open(file_name, 'r') as f:
        return [line.strip() for line in f]  # Read file and strip newline characters from each line
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))