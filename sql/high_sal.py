employees = [
    {"name": "Prashanth", "salary": 50000},
    {"name": "Rahul", "salary": 70000},
    {"name": "Kiran", "salary": 60000},
    {"name": "Raj", "salary": 90000}
]

highest_salary = max(emp["salary"] for emp in employees)

print("Highest Salary:", highest_salary)