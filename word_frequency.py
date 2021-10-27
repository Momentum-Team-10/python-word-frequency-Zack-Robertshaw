STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

# open the file



# remove the stop words

#go through the file word by word and keep a count of how often each word is used
print("hello world")

# def remove_from_file(STOP_WORDS):
#     return [ item for item in file if item != STOP_WORDS]           

# remove_from_file(file, STOP_WORDS)




def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as text:
        lines = text.readlines()
        print(f"{len(lines)} lines in the file.")
        # print(lines)
        for line in lines:
            line = line.replace(",", " ")
            line = line.replace(".", " ")
            line = line.replace("_", " ")
            line = line.replace("?", " ")
            line = line.replace(":", " ")
            line = line.replace("’", " ")
            line = line.replace("-", " ")
            line = line.lower()
            line = line.split(' ')
            # line = line.remove("brim")
            print(line)



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)



