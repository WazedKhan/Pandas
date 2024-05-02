import pandas as pd
from icecream import ic

data = {
    "student_id": [101, 53, 128, 3],
    "name": ["Ulysses", "William", "Henry", "Henry"],
    "age": [13, 10, 6, 11],
}

df = pd.DataFrame(data)

result = df[(df["student_id"].isin([101, 53]))][["name", "age"]]
ic(result)
