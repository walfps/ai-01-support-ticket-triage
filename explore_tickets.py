import pandas as pd

ALLOWED = ["billing", "technical", "delivery"]

df = pd.read_csv("tickets.csv")
print(df.head())
print(df.shape)
print(df["category"].value_counts())
condition = ~ df["category"].isin(ALLOWED)
print(df[condition])
print(df)