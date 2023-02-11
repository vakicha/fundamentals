input_divisor = int(input())
input_bound = int(input())
sum_container = 0
last_sum = 0
count = 1
while sum_container <= input_bound:
    last_sum = sum_container
    sum_container = input_divisor * count
    count += 1
print(last_sum)