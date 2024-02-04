from icecream import ic

import pandas as pd

grades_list = [
    ["Alice", 85, 90, 92],
    ["Bob", 70, 80, 75],
    ["Charlie", 90, 85, 88],
    ["Diana", 77, 92, 85],
]


def create_data_frame(list_):
    return pd.DataFrame(
        list_,
        columns=["Name", "Math", "Science", "History"],
    )


ic(create_data_frame(grades_list))
