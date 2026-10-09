name = "Dharsan"
age = 21
job_title = "Software Engineer"
monthly_salary = "1800"
university = "IIT"
print("Name: ", name, type(name))
print("Age: ", age, type(age))
print("Job Title: ",job_title, type(job_title))
print("Monthly Salary: ", monthly_salary, type(monthly_salary))
print("University: ",university, type(university))

if age>20:
    print("Adult")
else:
    print("Child")


height = 172.5
is_employed = True

print("Height: ", height, type(height))
print("Is Employed? ", is_employed, type(is_employed))

monthly_salary = int(monthly_salary)
print("Monthly Salary: ", monthly_salary, type(monthly_salary))

bonus = 200

total = monthly_salary + bonus
print("Total: ", total)


# Lists

students = ["Aarav", "Kamal", "Nimal", "Saman"]
print(students)
print(type(students))

print(students[0])
print(students[1])
print(students[2])
print(students[3])
# print(students[4])

print("Number of Students", len(students))

students.append("Dharsan")

students.append("Ravi")
print(students)
students.remove("Kamal")
print(students)
print(len(students))


students.append("Dharsan")
print(students)
students.remove("Dharsan")
print(students)

# Loops
for student in students:
    print(student)

marks = [75, 82, 64, 40, 58]
for mark in marks:
    print(mark)

for mark in marks:
    if mark >=50:
        # print(mark, "Passed")
        print(f"Passed: {mark}") #f-string
    else:
        # print(mark, "Failed")
        print(f"Failed: {mark}")

print(students)
print(students[0:3]) #starts at 0 index- 0,1,2
print(students[:3]) #starts at 0 index- 0,1,2

print(students[2:]) #Starts at index 2 and continue to the end

print(students[:]) #copy the whole list

print(students[-1]) #give me the last item
print(students[-3]) #this is suitable when we want last few items without knowing the number of items

print(students[-1])
print(students[-2])
print(students[2:])
print(students[:2])


#Exercise 1
salaries = [1800,2200,1500,3000,1950]
for salary in salaries:
    if salary>=2000:
        print(f"{salary} - High Salary")
    else:
        print(f"{salary} - Below 2000")

#Exercise2
students = ["Aarav", "Nimal", "Saman", "Ravi", "Dharsan"]
print(students[0])
print(students[-1])
print(students[0:3])
print(len(students))

#Exercise 4
marks2 = [45,72,33,90,61,48]
no_students_passed = 0
for mark in marks2:
    if mark>=50:
        print(f"{mark} - Passed")
        no_students_passed = no_students_passed + 1
    else:
        print(f"{mark} - Failed")

print(f"Number of Students Passed: {no_students_passed}")


salaries = [1800, 2500, 3200, 5200, 4100, 2750]
maxnumber = 1800
for salary in salaries:
    if salary>maxnumber:
        maxnumber = salary
print(f"Maximum: {maxnumber}")


marks = [45, 72, 33, 90, 61, 48, 85, 29]
passStudents = 0
failStudents = 0
highestMark = 0
for mark in marks:
    if mark >=50:
        print(f"{mark} - Passed")
        passStudents = passStudents + 1
    else: 
        print(f"{mark} - Failed")
        failStudents = failStudents + 1

    if mark > highestMark:
        highestMark = mark

print(f"Number of Students Passed: {passStudents}")
print(f"Number of Students Failed: {failStudents}")
print(f"Highest Mark: {highestMark}")


#Dictionaries
student = {
    "name": "Kamal",
    "age": 22,
    "marks": 85
}

print(student)
print(student["name"])
print(student["age"])
print(student["marks"])

student["marks"] = 90

print(student)
print(student["name"])
print(student["age"])
print(student["marks"])

student["university"] = "SLIIT"

print(student)
print(student["name"])
print(student["age"])
print(student["marks"])
print(student["university"])

employee = {
    "name": "Dharsan",
    "age": 27,
    "job": "Software Engineer",
    "salary": 1800
}

print(employee)
print(employee["name"])
print(employee["salary"])
employee["salary"] = 2000
employee["company"] = "Cubesys"

print(employee)

print(employee.keys()) # Getting all the keys

for key in employee.keys():
    print(key)

print(employee.values())

for value in employee.values():
    print(value)

print(employee.items())

for key, value in employee.items():
    print(f"{key} => {value}")
print("\n")


employee2 = {
    "name": "Kamal",
    "age": 25,
    "job": "Software Engineer",
    "salary": 2400,
    "company": "ABC Technologies"
}


for key, value in employee2.items():
    print(f"{key}: {value}")
    # if key=="salary":
    #     if value >= 2000:
    #         print("Salary Status: High Salary")
    #     else:
    #         print("Below 2000")

    if employee2["salary"] >=2000:
        print("High Salary")
    else:
        print("Below 2000")


employee3 = {
    "name": "Nimal",
    "age": 25,
    "job":"Software Engineer",
    "salary":2400,
    "performance_score":82
}
print("\n")
for employee_key, employee_value in employee3.items():
    print(f"{employee_key}: {employee_value}")

if employee3["performance_score"] >=80:
    print(f"{employee3['performance_score']} - Performance: Excellent")
elif employee3["performance_score"] >= 60 and employee3["performance_score"] < 80:
    print(f"{employee3['performance_score']} - Performance:  Good")
else:
    print(f"{employee3['performance_score']} - Performance:  Needs Improvement")

if employee3["salary"]>=2000:
    print(f"Salary Status: {employee3['salary']}: High Salary")
else:
    print(f"Salary Status: {employee3['salary']}: Below 2000")
print("\n")


employees = [
    {
        "name": "Kamal",
        "age": 27,
        "salary": 2400
    },
    {
        "name": "Dharsh",
        "age": 27,
        "salary": 3500
    },
    {
        "name": "Kavin",
        "age": 25,
        "salary": 1800
    },
    
]


print(employees)
print(employees[0])
print(employees[0]["name"])
print(employees[1]["name"])
print(employees[2]["name"])

print(employees[0]["age"])
print(employees[1]["age"])
print(employees[2]["age"])


for employee in employees:
    # print(employee)
    print(f"{employee['name']}: {employee['salary']}AUD")

print("\n")


employees = [
    {
        "name":"kamal",
        "salary": 2400
    },
    {
        "name":"Nimal",
        "salary": 1800
    },
    {
        "name":"Ravi",
        "salary": 3200
    },
    {
        "name":"Saman",
        "salary": 1950
    },
    {
        "name":"Aarav",
        "salary": 2800
    },
]

count_employee = 0
highest_salary = 0 
for employee in employees:
    print(f"{employee['name']} - {employee['salary']}")
    if employee["salary"]>=2000:
        count_employee = count_employee + 1

    if employee["salary"] > highest_salary:
        highest_salary = employee["salary"]

print(f"Employees earning 2000 or more: {count_employee}")
print(f"Highest Salary: {highest_salary}")
print("\n")
# for employee in employees:
#     for key, value in employee.items():
#         print(f"{key}: {value}")


employees = [
    {
        "name": "Kamal",
        "salary": 2400
    },
    {
        "name": "Nimal",
        "salary": 1800
    },
    {
        "name": "Ravi",
        "salary": 3200
    },
    {
        "name": "Saman",
        "salary": 1950
    },
    {
        "name": "Aarav",
        "salary": 2800
    }
]

count_employee = 0
highest_salary = 0
print("Employees earning 2000 or more:")
for employee in employees:
    if employee["salary"] >= 2000:
        print(employee["name"])
        count_employee = count_employee + 1

    if employee["salary"] > highest_salary:
        highest_salary = employee["salary"]    

print(f"Number of employees: {count_employee}")
print(f"Highest Salary: {highest_salary}")
print("\n")

employee_found = False
for employee in employees:
    if employee["name"] == "Ravi":
        print(f"Employee Found: {employee['name']}\nSalary: {employee['salary']}")
        employee_found = True

if employee_found == False:
    print("Employee not found")


for employee in employees:
    if employee["salary"] < 2000:
        employee["salary"] = float(employee["salary"]*1.10)
        print(f"{employee['name']} - Updated Salary:{employee['salary']: .1f}")


print("\n")
employee_exist = False
for employee in employees:
    if employee["name"] == "Ravi":
        employee_exist = True
        print(f"Salary of {employee['name']} is {employee['salary']:.1f}")
        if employee["salary"] > 3000:
            print("Senior Salary Range")
        else :
            print("Normal Salary Range")

if employee_exist == False:
    print("Employee not found")

print("\n")
#Functions

def check_salary(salary):
    if salary >= 2000:
        print("High Salary")
    else: 
        print("Below 2000")

check_salary(2400)
check_salary(1800)
check_salary(3200)


def calculate_bonus(salary, bonus_percentage):
    bonus = (salary * bonus_percentage/100)
    return bonus

def total_salary(salary, bonus_percentage):
    bonus = salary * bonus_percentage/100
    return salary + bonus
print(calculate_bonus(2000,10))
print(calculate_bonus(3000,15))

print(total_salary(2000, 10))


def performance_status(score):
    if score >= 80:
        return "Excellent"
    elif score >=60:
        return "Good"
    else:
        return "Needs Improvement"


print(performance_status(85))
print(performance_status(72))
print(performance_status(45))
print("\n")

marks = [85, 72, 45, 91, 58]
for mark in marks:
    print(f"{mark}: {performance_status(mark)}")
print("\n")

marks = [85, 72, 45, 91, 58]

def analyze_marks(marks):
    count_students = 0
    for mark in marks:
        if mark >= 80:
            count_students = count_students + 1
            print(f"{mark} - Excellent")
            
        elif mark >=60:
            print(f"{mark} - Good")
        else:
            print(f"{mark} - Needs Improvement")

    return count_students

excellent_students = analyze_marks(marks)

print(f"Number of Excellent Students: {excellent_students}\n")



employees = [
    {
        "name": "Kamal",
        "salary": 2400
    },
    {
        "name": "Nimal",
        "salary": 1800
    },
    {
        "name": "Ravi",
        "salary": 3200
    },
    {
        "name": "Saman",
        "salary": 1950
    },
    {
        "name": "Aarav",
        "salary": 2800
    }
]

def find_high_salary_employees(employees):
    count_employee = 0
    for employee in employees:
        if employee["salary"] >=2000:
            count_employee = count_employee + 1
            print(f"{employee["name"]}")

    return count_employee

# find_high_salary_employees(employees)
print(f"Number of High Salary Employees: {find_high_salary_employees(employees)}")
print("\n")


def get_high_salary_employees(employees):
    high_salary_employees = []

    for employee in employees:
        if employee["salary"] >= 2000:
            high_salary_employees.append(employee)

    return high_salary_employees

result = get_high_salary_employees(employees)
# print(result)
for employee in result:
    print(f"{employee['name']} - {employee['salary']}")
print("\n")


employee_low_salary = 2000
increase_percentage = 0.1
def give_salary_increase(employees):
    low_salary_employees = []
    for employee in employees:
        if employee["salary"] < employee_low_salary:
            bonus = employee["salary"] * increase_percentage
            employee["salary"] = employee["salary"] + bonus
        low_salary_employees.append(employee)

    return low_salary_employees

updated_employees = give_salary_increase(employees)
# print(updated_employees)
for employee in updated_employees:
    print(f"{employee["name"]} - {employee["salary"]:.1f}")


name = "Dharsan"

def greet():
    message = "Hello"
    print(message)
    print(name)

greet()
print(name)


x = 10
def test():
    x = 20
    print(x)

test()
print(x)


def clean_name(name):
    name = name.strip().upper()
    return name

print(clean_name("     Dharsan   "))

def check_username(username):
    username = username.strip().lower()
    if username == "dharsan":
        return "Username found"
    else:
        return "Username not found"


print(check_username("   Dharsan  "))


def count_python(text):
    words = text.lower().split()
    count = 0

    for word in words:
        if word == "is":
            count = count + 1

    return count

text = "Python is great. I am learning Python because Python is popular."
print(count_python(text))

skills = "Python, FastAPI, SQL, Azure, GitHub Actions"

def show_skills(skills):
    words = skills.split(",") 
    count_skills = 0

    for skill in words:
        skill = skill.strip()
        # print(skill)
        count_skills = count_skills + 1

    return count_skills

skill_count = show_skills(skills)
print(f"Number of Skills: {skill_count}")

employees = [
    {
        "name": "Kamal",
        "skills": "Python, SQL, Azure"
    },
    {
        "name": "Nimal",
        "skills": "Java, Spring Boot, MySQL"
    },
    {
        "name": "Ravi",
        "skills": "Python, FastAPI, Azure, Docker"
    },
    {
        "name": "Saman",
        "skills": "JavaScript, React, Node.js"
    }
]



def find_python_developers(employees):
    python_dev_count = 0

    for employee in employees:
        skills = employee["skills"].split(",") #it becomes list. skill list

        for skill in skills: #go inside each skill in list
            skill = skill.lower().strip()

            if skill =="python":
                print(employee["name"])
                python_dev_count = python_dev_count + 1
                break

    return python_dev_count

python_developers = find_python_developers(employees)
print(f"number of Python Developers: {python_developers}")



employees = [
    {
        "name": "Kamal",
        "salary": 2400,
        "skills": "Python, SQL, Azure"
    },
    {
        "name": "Nimal",
        "salary": 1800,
        "skills": "Java, Spring Boot, MySQL"
    },
    {
        "name": "Ravi",
        "salary": 3200,
        "skills": "Python, FastAPI, Azure, Docker"
    },
    {
        "name": "Saman",
        "salary": 1950,
        "skills": "JavaScript, React, Node.js"
    },
    {
        "name": "Aarav",
        "salary": 2800,
        "skills": "Python, SQL, Docker"
    }
]

print("\n")

def analyze_employees(employee):

    python_developers = 0
    for employee in employees:
        name = employee["name"]
        salary = employee["salary"]

        #Print name, salary and salary classification
        if salary >=3000:
            salary_status = "High Salary"
        elif salary >=2000:
            salary_status = "Normal Salary"
        else:
            salary_status = "Low Salary"

        print(f"{name} - Salary: {salary} - {salary_status}")

        #Clean the skills
        skills = employee["skills"].split(",")
        cleaned_skills = []

        # print(skills)

        for skill in skills:
            cleaned_skill = skill.strip()
            cleaned_skills.append(cleaned_skill)

        #Check for python
        if "Python" in cleaned_skills:
            print(f"Python Developer: {name}")
            python_developers +=1

    return python_developers

number_of_python_developers = analyze_employees(employees)
print(f"Number of Python Developers: {number_of_python_developers}")


# analyze_employees(employees)


print("\n")

for number in [10,20,30,40,50,60]:
    print(number)
    if number == 30:
        break #Stops the loop immediately

    # print(number)
        

print("\n")

employees = [
    {"name": "Kamal", "salary": 2400},
    {"name": "Nimal", "salary": 1800},
    {"name": "Ravi", "salary": 3200}
]

employee_name = "Ravi"

for employee in employees:
    name = employee["name"]
    if employee["name"] == employee_name: 
        print(f"Employee Found: {name}")
        break 

print("\n")
numbers = [5,10,15,20,25,30]

for number in numbers:
    print(number)
    if number == 20:
        break
print("\n")
numbers = [5,10,15,20,25]
for number in numbers:
    if number ==15:
        continue

    print(number)

numbers = [10, 15, 20, 25, 30, 35]

print("\n")
for number in numbers:
    if number == 20:
        continue

    print(number)


# print(int("hello"))

try:
    age = int(input("Enter your age: "))
    print(f"your age is {age}")

except:
    print("Please enter a valid number.!")


try:

    number = int(input("Enter a number: "))
    print(number*2)
except:
    print("Invalid Number")


try:
    file = open("hello.txt", 'r')
    content = file.read()
    # print(content)

except:
    print("Could not read the file")

else: 
    print("File read successfully")
    print(content)

finally:
    print("Finished")


try:
    file = open("helo.txt", "r")
    content = file.read()

except FileNotFoundError:
    print("The File does not exist")

try:
    number = int("hello")

except ValueError:
    print("You didn't provide a valid number")


try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("You cannot divide by zero")


# age = -5
# if age < 0:
#     raise ValueError("Age cannot be negative")


try:

    age = -5
    if age<0:
        raise ValueError("Age cannot be negative")

except ValueError:
    print("Invalid Age\n")


try:

    age = -5
    if age<0:
        raise ValueError("Age cannot be negative")

except ValueError as error:
    print(error)


try:
    with open("hello.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File does not exist")


try:
    #Write to the file
    with open("hello.txt", "w") as file1:
        file1.write("Hello Dharsan\n")
        file1.write("I am learning Python")

    #read from the file
    with open("hello.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File does not exist")


lines = [
    "Hello Kavin\n"
    "I am learning new\n"
    "File handling is interesting"
]

try:
    with open("new.txt", "w") as file2:
        print(file2.writable())
        file2.writelines(lines)

    with open("new.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist")


