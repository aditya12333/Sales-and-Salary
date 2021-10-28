
# importing the necessary dependencies
from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle

application = Flask(__name__) # initializing a flask app
# app=application
@application.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@application.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            Store=int(request.form['Store'])
            DayOfWeek = int(request.form['DayOfWeek'])
            Customers = float(request.form['Customers'])
            Open = float(request.form['Open'])
            Promo = int(request.form['Promo'])
            StateHoliday = int(request.form['StateHoliday'])
            SchoolHoliday = int(request.form['SchoolHoliday'])

            filename = 'Sales_prediction_model.pkl'
            loaded_model = pickle.load(open('Sales_prediction_model.pkl', 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[Store,DayOfWeek,Customers,Open,Promo,StateHoliday,SchoolHoliday]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=round(100*prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	application.run(debug=True) # running the app