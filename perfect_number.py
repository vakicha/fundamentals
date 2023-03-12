def perfect_number_check(num):
    sum_of_elements = 0
    for el in range(1, num):
        if num % el == 0:
            sum_of_elements += el
    if sum_of_elements == num:
        return True
    return False


number = int(input())
if perfect_number_check(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
