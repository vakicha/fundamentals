data = input()
company = {}

while data != "End":
    company_name, employee_id = data.split(" -> ")
    if company_name not in company:
        company[company_name] = []
    if employee_id in company[company_name]:
        data = input()
        continue
    else:
        company[company_name].append(employee_id)
    data = input()
for company_name in company.keys():
    print(company_name)
    for employee_id in company[company_name]:
        print(f"-- {employee_id}")
