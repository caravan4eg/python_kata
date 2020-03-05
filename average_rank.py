"""
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
Sample Output

sam=99912222
Not found
harry=12299933
"""


phone_book = {}
queries = []
n = int(input())

# filling phone book
for i in range(n):
    name, phone = input().split()
    phone_book[name] = phone

# getting query names
while True:
    query_name = input()
    if not query_name:
        break
    else:
        queries.append(query_name)

# filter phone_book by query names
for query in queries:
    if query in phone_book:
        print(f'{query}={phone_book[query]}')
    else:
        print('Not found')
