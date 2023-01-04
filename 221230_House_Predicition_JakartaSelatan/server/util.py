import json
import pickle
import numpy as np

__garasi = None
__data_columns = None
__model = None

def get_estimated_price(LT,LB,KT,KM,garasi):
    a = np.zeros(len(__data_columns))
    a[0] = LT
    a[1] = LB
    a[2] = KT
    a[3] = KM
    if garasi == 'ADA':
        a[4] = 1
        a[5] = 0
    elif garasi == 'TIDAK ADA':
        a[4] = 0
        a[5] = 1

    price = __model.predict([a])[0]
    price = round(price, -7)
    price = int(price)

    return price


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __garasi

    with open("./server/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __garasi = __data_columns[4:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('./server/artifacts/jakarta_selatan_house_price_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_garasi_status():
    return __garasi

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_garasi_status())
    print(get_estimated_price(250,250,4,1,'TIDAK ADA'))