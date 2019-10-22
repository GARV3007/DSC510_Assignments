# File : Assignment 9.1.py
# Name : Gourav Verma
# Date : 10/21/2019
# Course : DSC-510 - Introduction to Programming
# Des  : Week-8 : File Operations, Error Handling

import string

# This function take a line of characters as input.
# it will extract words from the line by first removing punctuation characters from the line,
# and changing all characters to lowercase, it then calls the add_word function to add it the
# dictionary gba_dict.
def process_line(line, gba_dict):
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        add_word(word, gba_dict)

# This function adds the word to the dictionary.
def add_word(word, gba_dict):
    if word not in gba_dict:
        gba_dict[word] = 1
    else:
        gba_dict[word] += 1

# This function writes the output result into user provided file name.
# It displays the value and key of the dictionary in a tabular format.
def process_file(file_name, gba_dict):
    with open(file_name, 'w') as output_f:
        for i, j in gba_dict.items():
            output_f.write("\n{:<15} {:<15}".format(i, j))


# The main function of this program will open the file,
# processes the file line-by-line,
# then prints the number of words in the file
# followed by each word and the number of repetitions in a tabular format.
def main():
    gba_file = open('gettysburg.txt', 'r')
    gba_dict = {}

    for line in gba_file:
        process_line(line, gba_dict)

    file_name = input("Provide output file name, like 'filename.txt' : ")
    with open(file_name, 'w') as output_f:
        output_f.write("Length of the Dictionary: " + str(len(gba_dict)))
        output_f.write("\n{:<15} {:<15}\n".format("Word", "Count"))
        output_f.write("_" * 21)
        process_file(file_name, gba_dict)

    gba_file.close()


if __name__ == "__main__":
    main()
