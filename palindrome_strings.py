words = input().split()
palindrome = input()
list_of_all_palindromes = [element for element in words if element == element[::-1]]
count = 0
for element in list_of_all_palindromes:
    if element == palindrome:
        count += 1
print(list_of_all_palindromes)
print(f"Found palindrome {count} times")
