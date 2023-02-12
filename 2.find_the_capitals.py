string = input()
string_list = []
for ch in string:
    string_list.append(ch)
final_list = []
for index, element in enumerate(string_list):
    if element.isupper():
        final_list.append(index)
print(final_list)
