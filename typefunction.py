import pandas as pd

def categoricalOrdinal(x):
    for key,value in cat_ord.items():
        if x==key:
            x=value
            return x
    return x