year = int(input())
while True:
    year += 1
    year_as_str = str(year)
    set_index = ""
    for index in year_as_str:
        set_index += index
    if len(year_as_str) == len(set(set_index)):
        print(year)
        break
    else:
        continue
