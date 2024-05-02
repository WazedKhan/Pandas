import pandas as pd

data = {
    "product": ["Umbrella", "SleepingBag"],
    "quarter_1": [417, 800],
    "quarter_2": [224, 936],
    "quarter_3": [379, 93],
    "quarter_4": [611, 875],
}

report = pd.DataFrame(data)
melt_report = report.melt(
    id_vars=["product"],
    value_vars=[
        "quarter_1",
        "quarter_2",
        "quarter_3",
        "quarter_4",
    ],
    value_name="quarter",
    var_name="sales",
)
print(melt_report)
