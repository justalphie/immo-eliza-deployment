from fastapi import FastAPI
from typing import Union, Literal, Optional
from pydantic import BaseModel
import pickle
import pandas as pd
import sklearn
from preprocess_utils import *

class Item(BaseModel):
    property_id: int = 999999999
    price: Optional[float] = None
    locality_name: str
    postal_code: int
    latitude: float
    longitude: float
    property_type: Literal['APARTMENT']
    property_subtype: Optional[Literal['FLAT_STUDIO', 'APARTMENT', 'DUPLEX', 'GROUND_FLOOR', 'PENTHOUSE', 'SERVICE_FLAT', 'LOFT', 'TRIPLEX', 'KOT']]
    type_of_sale: Optional[Literal['BUY_REGULAR', 'PUBLIC_SALE', 'LIFE_ANNUITY']]
    number_of_rooms: float
    living_area: float
    kitchen_type: Optional[Literal['NOT_INSTALLED', 'USA_SEMI_EQUIPPED', 'INSTALLED', 'SEMI_EQUIPPED', 'HYPER_EQUIPPED', 'USA_INSTALLED', 'USA_HYPER_EQUIPPED', 'USA_UNINSTALLED']]
    fully_equipped_kitchen: Optional[float]
    furnished: Optional[float]
    open_fire: Optional[int]
    terrace: Optional[float]
    terrace_area: Optional[float]
    garden: Optional[float]
    garden_area: Optional[float]
    surface_of_good: Optional[float]
    number_of_facades: float
    swimming_pool: Optional[float]
    state_of_building: Optional[Literal['TO_BE_DONE_UP', 'AS_NEW', 'GOOD', 'TO_RENOVATE', 'JUST_RENOVATED', 'TO_RESTORE']]
    main_city: Optional[str]
    province: Optional[str]

  
with open ("../apartments/models/ridge.pickle", "rb") as f:
    ridge = pickle.load(f)

with open("../apartments/preprocessings/preprocessings.pickle", "rb") as f1:
    preprocessings = pickle.load(f1)

app = FastAPI()

@app.get("/")
def new():
    return "alive"

@app.post("/predict/")
def predict(item: Item):
    df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    df = clean_dataset(df)
    X_test = df.iloc[:, 1:]
    X_train, X_test = apply_preprocessings(preprocessings, X_train=None, X_test=X_test)
    y_pred = ridge.predict(X_test)
    y_pred_df = pd.DataFrame(y_pred, index=X_test.index, columns=["price_pred"])
    output_dict = list(y_pred_df.to_dict(orient='index').values())[0]
    return output_dict
    
