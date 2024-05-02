import pandas as pd
from icecream import ic

data = {
    "name": ["Jack", "Piper", "Mia", "Ulysses"],
    "salary": [19666, 74754, 62509, 54866],
}

employees = pd.DataFrame(data)
employees["salary"] = employees["salary"].apply(lambda x: x * 2)
ic(employees)
