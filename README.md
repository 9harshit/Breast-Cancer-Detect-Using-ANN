# Breast Cancer: 
* This application detect whether the Mass in the breast is cancerous or not using Artificial Neural Network.
* Its uses measurement of mass present is the report for analyzing the mass.
* The patient can use this web application as a second opinion to confirm diagnosis.


## Code and Resources Used 
**Python Version:** 3.8  
**Packages:** pandas, numpy, matplotlib, sklearn, tensorflow 2, flask, json, pickle  
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  

## Data Set
Dataset is downloaded from kaggle.com
The data in in data.csv. The number of columns is 30 and the number of rows is 570. The columns are:
For more detail info please visit : https://www.kaggle.com/uciml/breast-cancer-wisconsin-data
## Model Building 

First, I have scaled the data with MinMaxScaler. I also split the data into train and tests sets with a test size of 20%.   

I have applied Artificial Neural Network (ANN) with four layers:
*	**Input Layer** – Units=30, activation=relu 
*	**Hidden Layer** – Units=10, activation=relu 
*	**Hidden Layer** – Units=10, activation=relu 
*	**Output Layer** – Units=1, activation=binary crossentropy

I have also applied early stopping.

## Model performance 
*	**Validation loss** : 0.35
*	**Validation Accuracy** : 0.97 or 97%
*	**Confusion matrix for label setosa** :
[[20  0]
 [ 0 10]]
*	**Confusion matrix for label versicolor** :
[[17  1]
 [ 1 11]]
*	**Confusion matrix for label virginica** :
[[22  0]
 [ 1  7]]

## Productionization 
In this step, I built a flask API endpoint that is hosted on Heroku. The API endpoint takes in a request with a list of values of breast mass measurements and returns whether the mass is cancerous or not.

**Application link:** https://breastcancer-detector.herokuapp.com/

![alt text](https://github.com/9harshit/Breast-Cancer-Detect-Using-ANN/blob/master/README_IMG/form.png "Breast Cancer Detect Form")

![alt text](https://github.com/9harshit/Breast-Cancer-Detect-Using-ANN/blob/master/README_IMG/prediction.png "Result")
