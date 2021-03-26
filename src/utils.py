import re
import numpy as np

def clean_years(x):
    x = "".join(re.findall(r"\d{4}", str(x)))
    if x:
        return int(x)
    else: 
        return "Undefined"

def get_month(x):
    if "-" in x:
        x = x.split("-")
        return x[1]
    else:
        return np.nan