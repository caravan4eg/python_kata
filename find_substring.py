

def count_substring(string, sub_string):
    i = 0
    count = 0
    while i <= len(string):
        if string.find(sub_string, i, len(string)) != -1:
            count += 1
            i = string.find(sub_string, i, len(string)) + 1
        else:
            break

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
