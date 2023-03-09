list_of_int = []
integer_1 = int(input())
list_of_int.append(integer_1)
integer_2 = int(input())
list_of_int.append(integer_2)
integer_3 = int(input())
list_of_int.append(integer_3)


def smallest_num(list_nums):
    print(min(list_nums))


smallest_num(list_of_int)

