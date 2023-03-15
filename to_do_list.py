notes = input()
list_priority = ['0'] * 10
while notes != "End":
    tokens = notes.split("-")
    priority = int(tokens[0]) - 1
    action = tokens[1]
    list_priority.pop(priority)
    list_priority.insert(priority, action)
    notes = input()
result = [element for element in list_priority if element != "0"]
print(result)
