# write to file
import os


def main():
    path = '/home/alex/dev/python_kata/automate_the_boring_stuff_with_python/'
    file = 'hello.txt'
    f_name = os.path.join(path, file)
    print('New file full name: ', f_name)
    with open(f_name, 'w') as f:
        f.write('Hello, Alex!')

    with open(f_name, 'r') as f:
        file_content = f.read()
        print('File content: ', file_content)

    file = 'sonnet29.txt'
    with open(os.path.join(path, file), 'r') as sonnet_file:
        lines = sonnet_file.readlines()
        print('Sonnet file lines: ', lines)
        file = 'hello.txt'
        comment = '\n\n# Adding new text\n\n'
        with open(os.path.join(path, file), 'a') as hello_file:
            hello_file.write(comment)
            hello_file.write(''.join(lines))


if __name__ == "__main__":
    main()
