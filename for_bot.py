import pandas as pd
from ml import prediction_for_acc, prediction_for_gd
from no_doubles import doubles_find
dataset_example = pd.read_csv(f"csv_file.csv", encoding='cp1251')


def super_main_def(role, dataset):
    df = dataset["text"]

    if role == "Бухгалтер":
        dataset["raiting"] = prediction_for_acc(df)

    if role == "Гендир":
        dataset["raiting"] = prediction_for_gd(df)

    sorted_ds = dataset.sort_values(by='raiting', ascending=False).head(10)

    sorted_ds = doubles_find(sorted_ds)

    return sorted_ds["href"].head()
