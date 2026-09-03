# import libraries
import os
import pandas as pd
import numpy as np

# load data
path = f"{os.getcwd()}/data"
df_raw = pd.read_csv(f"{path}/SP500_raw.csv")

# ensure the data is ordered by date
df_raw.sort_values("Date")
# calculate returns (drop first row as no return can be calculated)
df_raw["ret"] = np.log(df_raw["Close"]).diff()
# calculate volatility estimator
df_raw["var"] = (np.log(df_raw["High"] / df_raw["Close"]) *
             np.log(df_raw["High"] / df_raw["Open"]) +
             np.log(df_raw["Low"] / df_raw["Close"]) *
             np.log(df_raw["Low"] / df_raw["Open"])
             )
# remove variables which aren't required and drop first row as no return can be calculated
df_clean = df_raw[["Date", "ret", "var"]].dropna()

# save data
df_clean.to_csv(f"{path}/SP500_clean.csv", index=False)
