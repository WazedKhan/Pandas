import pandas as pd
from icecream import ic

data = {
    "student_id": [32, 217, 779, 849],
    "name": ["Piper", None, "Georgia", "Willow"],
    "age": [5, 19, 20, 14],
}

students = pd.DataFrame(data)
students = students.loc[students["name"].isnull() == False]
ic(students)
