
def clean_years(x):
    import re
    pattern = r"\d{4}"
    x = "".join(re.findall(pattern, str(x)))
    if x:
        return int(x)
    else: 
        return "Undefined"

def get_month(x):
    if "-" in x:
        x = x.split("-")
        return x[1]
    else:
        return "UNK"