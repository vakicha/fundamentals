import sys
count = 0
biggest_num = -sys.maxsize
while count != 3:
    input_num_1 = int(input())
    count += 1
    if input_num_1 > biggest_num:
        biggest_num = input_num_1
print(biggest_num)