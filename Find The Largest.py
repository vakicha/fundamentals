given_number = input()
my_list = []
result = ""
for iteration in given_number:
    my_list.append(iteration)
my_list.sort(reverse=True)
for number in my_list:
    result += str(number)
print(result)
