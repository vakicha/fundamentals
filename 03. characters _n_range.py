char_1 = input()
char_2 = input()


def characters_between(ch1, ch2):
    for ch in range(ord(ch1) + 1, ord(ch2)):
        print(chr(ch), end=" ")


characters_between(char_1, char_2)
