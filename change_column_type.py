import pandas as pd

data = {
    "student_id": [1, 2],
    "name": ["Ava", "Kate"],
    "age": [6, 15],
    "grade": [73.0, 87.0],
}

students = pd.DataFrame(data)
students = students.astype({"grade": int, "age": "float"})
print(students)
