def palindrome(string):
    if string == string[::-1]:
        return True
    return False


input_line = input().split(", ")
for element in input_line:
    print(palindrome(element))
