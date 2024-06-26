import pandas as pd
from icecream import ic

# Example DataFrame
data = {
    "customer_id": [1, 2, 3, 4, 5, 6],
    "name": ["Ella", "David", "Zachary", "Alice", "Finn", "Violet"],
    "email": [
        "emily@example.com",
        "michael@example.com",
        "sarah@example.com",
        "john@example.com",
        "john@example.com",
        "alice@example.com",
    ],
}

df = pd.DataFrame(data)
df = df.drop_duplicates(subset="email")
ic(df)
