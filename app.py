from flask import Flask, redirect, url_for, render_template, request, session
import numpy as np
from keras.models import load_model
import keras
from keras.models import Sequential
from keras.layers import Dense
import joblib

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


@app.route("/", methods = ["POST", "GET"])  # this sets the route to this page
def home():
    if request.method == "POST":
        data = np.zeros(30)
        j =0 

        model = load_model('breast_cancer_detect.h5')

        session.permanent = True
        for i in ["radius_mean", "texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave_points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave_points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave_points_worst","symmetry_worst","fractal_dimension_worst"]:

            data[j] = float(request.form[i])
            j+=1

        sc = joblib.load('detect_scaler.pkl')
        data = data.reshape(1, -1)

        data = sc.fit(data).transform(data)


        # Initialising the ANN
    
        y = model.predict(data)
        if y > 0.5:
            session["result"] = 1
        else:
            session["result"] = 0

        return redirect(url_for("results"))
    else:
        return render_template("home.html")


@app.route("/results", methods = ["POST", "GET"])
def results():
    if request.method == "GET": 
            return render_template("results.html", content = session["result"])
    else:
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
