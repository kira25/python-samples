import pandas as pd


def my_function(file):
    input_columns = [2, 3, 4, 6, 10]

    df = pd.read_excel(file,
                       sheet_name="NUTRICIÓN", header=0, usecols=input_columns)

    df = df[df["SEXO"] == "m"]
    df_cols = df.columns
    for col in df_cols:
        print(df[col].head(5))

