import pandas as pd
from icecream import ic


data = {
    "name": ["Piper", "Grace", "Georgia", "Willow", "Finn", "Thomas"],
    "salary": [4548, 28150, 1103, 6593, 74576, 24433],
}

df = pd.DataFrame(data)
df["bonus"] = df["salary"] * 2
ic(df)
