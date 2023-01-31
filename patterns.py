number = int(input())
for c in range(1, number + 1):
    for l in range(0, c):
        print("*", end='')
    print()
for c in range(number - 1, 0, -1):
    for l in range(0, c):
        print("*", end='')
    print()
