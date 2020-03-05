'''
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

'''
if __name__ == '__main__':
    n = int(input())
    lst = []

    for _ in range(n):
        cmd, *args = input().split()
        if cmd !='print':
            cmd += '('+ ','.join(args) +')'
            eval('lst.'+cmd)
        else:
            print(lst)

    # my task resolution ))))))
    # while N > 0:
    #     command =[]
    #     command = list(map(str, input().rstrip().split()))
    #     N -= 1
    #     # run command
    #     # insert i e: Insert integer e at position i.
    #     if command[0] == 'insert':
    #         lst.insert(int(command[1]), int(command[2]))

    #     # print: Print the list.
    #     elif command[0] == 'print':
    #         print(lst)

    #     # remove e: Delete the first occurrence of integer e.
    #     elif command[0] == 'remove':
    #         lst.remove(int(command[1]))

    #     # append e: Insert integer  at the end of the list.
    #     elif command[0] == 'append':
    #         lst.append(int(command[1]))

    #     # sort: Sort the list.
    #     elif command[0] == 'sort':
    #         lst.sort()

    #     # pop: Pop the last element from the list.
    #     elif command[0] == 'pop':
    #         lst.pop()

    #     # reverse: Reverse the list.
    #     elif command[0] == 'reverse':
    #         lst.sort(reverse=True)
    # print(command)
    # print(lst)
