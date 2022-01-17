from flask import Flask, render_template, request

import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open("sales prediction-gb-model.pkl", 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':

##### Item_Weight
        Item_Weight = request.form['Item_Weight']

##### Item_Fat_Content
        Item_Fat_Content=request.form['Item_Fat_Content']
        if(Item_Fat_Content=='Low Fat'):
            Low_Fat=1
            Regular=0
        else:
            Low_Fat=0
            Regular=1

###### Item_Visibility
        Item_Visibility=float(request.form['Item_Visibility'])
        Item_Visibility=np.sqrt(Item_Visibility)

        Item_Type_Dairy=Item_Type_Soft_Drinks=Item_Type_Meat=Fruits_and_Vegetables=Household=Snack_Foods=Frozen_Foods=Breakfast=Health_and_Hygiene=Hard_Drinks=Canned=Breads=Starchy_Foods=Others=Seafood=0
        Item_Type=request.form['Item_Type']
        if(Item_Type=="Dairy"):
            Item_Type_Dairy=1
           
        elif(Item_Type=="Soft Drinks"):
            Item_Type_Soft_Drinks=1
        elif(Item_Type=='Meat'):
           Item_Type_Meat=1
        elif(Item_Type=="Fruits and Vegetables"):
           Fruits_and_Vegetables=1
        elif(Item_Type=="Household"):
          Household=1
        elif(Item_Type=="Snack Foods"):
            Snack_Foods=1
        elif(Item_Type=="Frozen Foods"):
           Frozen_Foods=1
        elif(Item_Type=="Breakfast"):
            Breakfast=1
        elif(Item_Type=="Health and Hygiene"):
           Health_and_Hygiene=1
        elif(Item_Type=="Hard Drinks"):
            Hard_Drinks=1
        elif(Item_Type=="Canned"):
            Canned=1
        elif(Item_Type=="Breads"):
            Breads=1
        elif(Item_Type=="Starchy Foods"):
           Starchy_Foods=1
        elif(Item_Type=="Others"):
          Others=1
        else:
           Seafood=1

### Item_MRP
        Item_MRP=float(request.form['Item_MRP'])

### Outlet_Establishment_Year
        Outlet_Establishment_Year=int(request.form['Outlet_Establishment_Year'])

## Outlet Location Type
        Outlet_Location_Type= request.form['Outlet_Location_Type']
        if(Outlet_Location_Type=="Tier 1"):
            Tier2=0
            Tier3=0
        elif(Outlet_Location_Type=="Tier 2"):
            Tier2=1
            Tier3=0
        else:
            Tier2=0
            Tier3=1


## Outlet Size
        Outlet_Size=request.form['Outlet_Size']
        if(Outlet_Size=="Medium"):
            Value=1
        elif(Outlet_Size=="Small"):
            Value=2
        else:
            Value=0

        Outlet_Type = request.form['Outlet_Type']

        if(Outlet_Type=="Supermarket Type1"):
            SupermarketType1 =1 
            SupermarketType2 =0
            SupermarketType3 =0
        elif(Outlet_Type=="Supermarket Type2"):
            SupermarketType1 =0 
            SupermarketType2 =1
            SupermarketType3 =0
        elif(Outlet_Type=="Supermarket Type3"):
            SupermarketType1 =0 
            SupermarketType2 =0
            SupermarketType3 =1       
        else:
            SupermarketType1 =0 
            SupermarketType2 =0
            SupermarketType3 =0

      
        prediction=model.predict(([[Item_Weight,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Value,Regular,Breads,Breakfast,Canned,Item_Type_Dairy,Frozen_Foods,Fruits_and_Vegetables,Hard_Drinks,Health_and_Hygiene,Household,Item_Type_Meat,Others,Seafood,Snack_Foods,Item_Type_Soft_Drinks,Starchy_Foods,Tier2,Tier3,SupermarketType1,SupermarketType2,SupermarketType3]]))
        print(prediction)
        prediction=np.round(prediction,2)
        return render_template('index.html',Price=prediction)
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)