import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5],
    "first": ["Mason", "Ava", "Taylor", "Georgia", "Thomas"],
    "last": ["King", "Wright", "Hall", "Thompson", "Moore"],
    "age": [6, 7, 16, 18, 10],
}

students = pd.DataFrame(data)
students.rename(
    columns={"first": "first_name", "last": "last_name"},
    inplace=True,
    errors="raise",
)
print(students)
