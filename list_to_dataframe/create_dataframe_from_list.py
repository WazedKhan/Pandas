import pandas as pd

student_data = [[1, 15], [2, 11], [3, 11], [4, 20]]


def createDataframe(student_data):
    return pd.DataFrame(
        student_data,
        columns=["student_id", "age"],
        dtype=int,
    )


print(createDataframe(student_data=student_data))
