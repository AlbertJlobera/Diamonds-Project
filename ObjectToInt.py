import os
import dotenv
dotenv.load_dotenv()

modif_num = {"D":1, "E":2, "F":3, "G":4, "H":5, "I":6, "J":7}

def modificaciones(x):
    for a,b in modif_num.items():
        if x==a:
            x=b
            return x
    return x