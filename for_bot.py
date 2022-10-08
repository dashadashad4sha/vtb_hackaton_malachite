import pandas as pd
from ml import prediction_for_acc, prediction_for_gd

dataset_example = pd.read_csv(f"csv_file.csv", encoding='cp1251')


def super_main_def(role, dataset):
    df = dataset["text"]

    if role == "Бухгалтер":
        dataset["raiting"] = prediction_for_acc(df)

    if role == "Гендир":
        dataset["raiting"] = prediction_for_gd(df)

    # Сейчас датафрейм с отмеченным рейтингом в переменной dataset

    sorted_ds = dataset.sort_values(by='raiting', ascending=False).head(10)

    # Надо убрать дублирования и положить в переменную sorted_ds

    return sorted_ds["href"].head(3)
