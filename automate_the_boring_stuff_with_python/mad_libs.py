"""
Create a Mad Libs program that reads in text files and lets the user add their own text
anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.
The program would find these occurrences and prompt the user to replace them.
Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck
The following text file would then be created:
The silly panda walked to the chandelie
"""


def get_content(file):
    # Get content from file
    with open(file, 'r') as mad_libs_txt:
        content = mad_libs_txt.read()
        return content


def change(content):
    # Ask new content
    noun = input('Введите существительное: ')
    adj = input('Введите прилагательное: ')
    verb = input('Введите глагол: ')

    # Change content
    content = content.replace('ADJECTIVE', adj)
    content = content.replace('VERB', verb)
    content = content.replace('NOUN', noun)
    return content


def write_content(file, new_content):
    # Write new content to file
    with open(file, 'a') as mad_libs_txt:
        mad_libs_txt.write(new_content)


def main():
    file = '/home/alex/dev/python_kata/automate_the_boring_stuff_with_python/mad_libs.txt'

    content = get_content(file)
    new_content = change(content)
    write_content(file, new_content)


if __name__ == "__main__":
    main()
