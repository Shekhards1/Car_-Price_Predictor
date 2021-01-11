import numpy as np
from flask import Flask, request, render_template
import pickle
from sklearn.preprocessing import StandardScaler

app=Flask(__name__)
model=pickle.load(open('random_forest_regression_model_original4.pkl','rb'))

@app.route('/',methods=['GET'])
def home():
    return render_template("index.html")

standard_to=StandardScaler()
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        no_years=int(request.form['years_'])
        km_driven=int(request.form['Kilometers_'])
        Fuel_type=request.form['option_']
        Owner=request.form['owners_']
        transmission=request.form['rdiobtn1']
        seller_type=request.form['rdiobtn2']


        if(Fuel_type =='fuel_Diesel'):
            Fuel_Diesel =1
            Fuel_LPG=0
            Fuel_Petrol=0
            Fuel_Electric=0
        
        elif (Fuel_type =='fuel_Petrol'):
            Fuel_Diesel =0
            Fuel_LPG = 0
            Fuel_Petrol =1
            Fuel_Electric = 0

        elif (Fuel_type =='fuel_Electric'):
            Fuel_Diesel = 0
            Fuel_LPG = 0
            Fuel_Petrol= 0
            Fuel_Electric = 1


        elif (Fuel_type =='fuel_LPG'):
            Fuel_Diesel = 0
            Fuel_LPG = 1
            Fuel_Petrol = 0
            Fuel_Electric = 0

        else:
            Fuel_Diesel = 0
            Fuel_LPG = 0
            Fuel_Petrol = 0
            Fuel_Electric = 0

        if (transmission == "transmission_Manual"):
            transmission_Manual=1
        else:
            transmission_Manual= 0


        if (seller_type=="seller_type_Individual"):
            seller_Trustmark_dealer=0
            seller_type_Individual=1

        elif(seller_type =="seller_Trustmark_dealer"):
            seller_Trustmark_dealer = 1
            seller_type_Individual = 0
        else:
            seller_Trustmark_dealer = 0
            seller_type_Individual = 0

        if (Owner=="test_drive_car"):
            test_drive_car=1
            second_owner=0
            third_owner=0
            Fourth_and_above=0

        if (Owner=="second_Owner"):
            test_drive_car = 0
            second_owner = 1
            third_owner = 0
            Fourth_and_above = 0

        if (Owner=="third_owner"):
            test_drive_car = 0
            second_owner = 0
            third_owner = 1
            Fourth_and_above = 0
        if (Owner == "Four and above owner"):
            test_drive_car = 0
            second_owner = 0
            third_owner = 0
            Fourth_and_above = 1
        else:
            test_drive_car = 0
            second_owner = 0
            third_owner = 0
            Fourth_and_above = 0


        prediction = model.predict([[km_driven, no_years, Fuel_Diesel,Fuel_Electric,Fuel_LPG,Fuel_Petrol,seller_type_Individual,seller_Trustmark_dealer,transmission_Manual,Fourth_and_above,second_owner,test_drive_car,third_owner]])
        output=round(prediction[0],0)

        if output<0:
            return render_template("index.html",prediction_text="Sorry you can not sell your car")
        else:
            return render_template("index.html",prediction_text="You can sell your car at Rs {}".format(output))
    else:
        return render_template("index.html")


if __name__ == "__main__":

    app.run(debug=True)