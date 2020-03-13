"""Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of ."""

def print_formatted(number):
    num = len(bin(number))-1
    for i in range(1,number+1):
        print("{0:{m}d}{0:{n}o}{0:{n}X}{0:{n}b}".format(i,m=num-1,n=num))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
