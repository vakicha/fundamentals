countries = input().split(', ')
cities = input().split(', ')
# result = {countries[index]: cities[index] for index in range(len(countries))}
result = dict(zip(countries, cities))
for country, city in result.items():
    print(f"{country} -> {city}")
