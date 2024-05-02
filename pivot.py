import pandas as pd

data = {
    "city": [
        "Jacksonville",
        "Jacksonville",
        "Jacksonville",
        "Jacksonville",
        "Jacksonville",
        "ElPaso",
        "ElPaso",
        "ElPaso",
        "ElPaso",
        "ElPaso",
    ],
    "month": [
        "January",
        "February",
        "March",
        "April",
        "May",
        "January",
        "February",
        "March",
        "April",
        "May",
    ],
    "temperature": [13, 23, 38, 5, 34, 20, 6, 26, 2, 43],
}

weather = pd.DataFrame(data)
weather_pivoted = weather.pivot(index="month", columns="city", values="temperature")
print(weather_pivoted)
