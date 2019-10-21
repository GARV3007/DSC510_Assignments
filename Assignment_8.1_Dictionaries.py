# File : Assignment 8.1.py
# Name : Gourav Verma
# Date : 10/20/2019
# Course : DSC-510 - Introduction to Programming
# Des  : Week-8 : Dictionaries, Tuples, and JSON Data

import string

def process_line(line, gba_dict):
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        # for x in s:
        #     words = words.replace(x,'')
        add_word(word, gba_dict)

def add_word(word, gba_dict):
    if word not in gba_dict:
        gba_dict[word] = 1
    else:
        gba_dict[word] += 1

def pretty_print(gba_dict):
    print("Length of the Dictionary: " + str(len(gba_dict)))
    print("{:<15} {:<15}".format('Word', 'Count'))
    print("_"*21)
    for i, j in gba_dict.items():
        print("{:<15} {:<15}".format(i, j))

def main():
    gba_file = open('gettysburg.txt', 'r')
    gba_dict = {}

    for line in gba_file:
        process_line(line, gba_dict)
    pretty_print(gba_dict)


if __name__ == "__main__":
    main()
