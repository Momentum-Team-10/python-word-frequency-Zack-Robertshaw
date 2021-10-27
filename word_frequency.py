from os import linesep, sep


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
        lines = text.read()
        # print(f"{len(lines)} lines in the file.")
        # print(lines)
        # for line in lines:
        lines = lines.replace(",", " ")
        lines = lines.replace(".", " ")
        lines = lines.replace("_", " ")
        lines = lines.replace("?", " ")
        lines = lines.replace(":", " ")
        lines = lines.replace("’", "")
        lines = lines.replace("-", " ")
        lines = lines.replace("\n", " ")
        lines = lines.lower()

        lines = lines.split(' ')


# correct use of a for loop would work here with STOP_WORDS
        while 'a' in lines:
            lines.remove('a')
        while 'an' in lines:
            lines.remove('an')
        while 'and' in lines:
            lines.remove('and')
        while 'are' in lines:
            lines.remove('are')
        while 'as' in lines:
            lines.remove('as')
        while 'at' in lines:
            lines.remove('at')
        while 'be' in lines:
            lines.remove('be')
        while 'by' in lines:
            lines.remove('by')
        while 'for' in lines:
            lines.remove('for')
        while 'from' in lines:
            lines.remove('from')
        while 'has' in lines:
            lines.remove('has')
        while 'he' in lines:
            lines.remove('he')
        while 'i' in lines:
            lines.remove('i')
        while 'in' in lines:
            lines.remove('in')
        while 'is' in lines:
            lines.remove('is')
        while 'it' in lines:
            lines.remove('it')
        while 'its' in lines:
            lines.remove('its')
        while 'of' in lines:
            lines.remove('of')
        while 'on' in lines:
            lines.remove('on')
        while 'that' in lines:
            lines.remove('that')
        while 'the' in lines:
            lines.remove('the')
        while 'to' in lines:
            lines.remove('to')
        while 'were' in lines:
            lines.remove('were')
        while 'will' in lines:
            lines.remove('will')
        while 'with' in lines:
            lines.remove('with')
        while '' in lines:
            lines.remove('')

            




        # while 'a' == False: 
        #     lines.remove('a')

        print(lines)


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



