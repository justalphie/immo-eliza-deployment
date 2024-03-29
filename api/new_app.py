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
    locality_name: str = "brussel"
    postal_code: int = "1000"
    latitude: float = 50.872696
    longitude: float = 4.315854
    property_type: Literal['APARTMENT'] = "APARTMENT"
    property_subtype: Optional[Literal['FLAT_STUDIO', 'APARTMENT', 'DUPLEX', 'GROUND_FLOOR', 'PENTHOUSE', 'SERVICE_FLAT', 'LOFT', 'TRIPLEX', 'KOT']] = "APARTMENT"
    type_of_sale: Optional[Literal['BUY_REGULAR', 'PUBLIC_SALE', 'LIFE_ANNUITY']] = "BUY_REGULAR"
    number_of_rooms: float = 2.0
    living_area: float = 60.0
    kitchen_type: Optional[Literal['NOT_INSTALLED', 'USA_SEMI_EQUIPPED', 'INSTALLED', 'SEMI_EQUIPPED', 'HYPER_EQUIPPED', 'USA_INSTALLED', 'USA_HYPER_EQUIPPED', 'USA_UNINSTALLED']] = "INSTALLED"
    fully_equipped_kitchen: Optional[float] = 1.0
    furnished: Optional[float] = 0.0
    open_fire: Optional[int] = 0.0 
    terrace: Optional[float] = 0.0
    terrace_area: Optional[float] = 0.0
    garden: Optional[float] = 0.0
    garden_area: Optional[float] = 0.0
    surface_of_good: Optional[float]= 0.0
    number_of_facades: float = 1.0
    swimming_pool: Optional[float] = 0.0
    state_of_building: Optional[Literal['TO_BE_DONE_UP', 'AS_NEW', 'GOOD', 'TO_RENOVATE', 'JUST_RENOVATED', 'TO_RESTORE']] = "GOOD"
    main_city: Optional[str] = "brussel"
    province: Optional[str] = "brussel"

  
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
    y_pred_df = pd.DataFrame(y_pred, index=X_test.index, columns=["Price prediction, €: "])
    output_dict = list(y_pred_df.to_dict(orient='index').values())[0]
    output_dict["Price prediction, €: "] = round(output_dict["Price prediction, €: "], 2)
    # TODO output_dict["Status"] = how to print out status??
    return output_dict
    
