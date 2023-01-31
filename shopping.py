budget = int(input())
input_line = input()
needed_money = 0
while input_line != "End":
    needed_money += int(input_line)
    if needed_money > budget:
        print("You went in overdraft!")
        break
    input_line = input()
if needed_money <= budget:
    print("You bought everything needed.")