import os
import sys
import numpy as np
import pandas as pd
import dill 
from sklearn.metrics import r2_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException


def save_object(file_path, obj):
    """
    This function saves object to a given location. It takes a file location
    and an object as argument and saves the object into the given file.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    """
    This function is used to train models and predictions. 
    """

    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i] # Selecting the model to train
            param_ = param[ list(models.keys())[i] ] # Selecting the parameters associated with selected model in param

            # rs = RandomizedSearchCV(model, param_, cv=3)
            # rs.fit(X_train, y_train)

            gs = RandomizedSearchCV(model, param_, cv=3) #Initializing RandomizedSearchCV with selected model and parameters
            gs.fit(X_train, y_train) # Training RandomizedSearchCV

            model.set_params(**gs.best_params_) # Setting the best parameters to the model
            model.fit(X_train, y_train) # Retraining the model with the best parameters

            #y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test) # Making Prediction with the trained model

            #train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred) # Determining the R2 of the trained model

            report[list(models.keys())[i]] = test_model_score # Storing the R2 in the report dict

            return report
    except Exception as e:
        raise CustomException(e, sys)



