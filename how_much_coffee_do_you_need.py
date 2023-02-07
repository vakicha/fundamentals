input_line = input()
coffee_count = 0
while input_line != "END":
    if input_line == "coding":
        coffee_count += 1
    elif input_line == "dog":
        coffee_count += 1
    elif input_line == "cat":
        coffee_count += 1
    elif input_line == "movie":
        coffee_count += 1
    elif input_line == "CODING":
        coffee_count += 2
    elif input_line == "DOG":
        coffee_count += 2
    elif input_line == "CAT":
        coffee_count += 2
    elif input_line == "MOVIE":
        coffee_count += 2
    else:
        input_line = input()
        continue
    input_line = input()
if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)
