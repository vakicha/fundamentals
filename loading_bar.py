def loading_bar(number):
    if number == 100:
        return print("100% Complete!\n[%%%%%%%%%%]")
    else:
        return print(f"{number}% [{'%' * (number // 10)}{'.' * (10 - number // 10)}]\n"
                     f"Still loading...")


input_num = int(input())
loading_bar(input_num)
