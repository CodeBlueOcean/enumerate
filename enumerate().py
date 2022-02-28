# enumerate we get the index of the items
for i, char in enumerate('Helllooo'):
    print(i, char)

# enumerate: list
for i, char in enumerate([1,2,3]):
    print(i, char)

# enumerate: turple
for i, char in enumerate((1,2,3)):
    print(i, char)

# enumerate: turple
for i, char in enumerate(list(range(100))):
    print(i, char)

# enumerate: turple
for i, char in enumerate(list(range(100))):
    print(i, char)
    if char == 50:
        print(f'index of 50 is: {i}')

