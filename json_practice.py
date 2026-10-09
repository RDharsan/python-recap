import json

with open("employee.json", "r") as file:
    employee = json.load(file)

print(employee)
print(employee["name"])
print(employee["skills"])
print(employee["skills"][0])

employee["salary"] = 3500

with open("employee.json", "w")as file:
    json.dump(employee, file, indent=4)