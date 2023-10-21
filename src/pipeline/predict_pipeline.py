import sys
import pandas as pd
from src.exception import CustomException

from src.components.data_transformation import DataTransformationConfig
from src.components.data_transformation import DataTransformation
from src.utils import load_object 

# Creating a model for prediction
class PredictPipeline:
    def __init__(self):
        pass


    def predict(self,features):
        try:
            model_path = 'artifacts\model.pkl'  # path of the model
            preprocessor_path = 'artifacts\preprocessor.pkl' # path of the preprocessor
            model = load_object(file_path = model_path) # Loading the model
            preprocessor = load_object(file_path=preprocessor_path) # Loading the preprocessor
            data_scaled = preprocessor.transform(features) # Transforming the features with the preprocessor
            preds = model.predict(data_scaled) # Making predictions with the loaded model

            return preds
        except Exception as e:
            raise CustomException(e, sys)

# A model for the place holders of the data to make predictions for. This will be received from the html form
class CustomData:
    def __init__(self,
        gender:str,
        race_ethnicity: str,
        parental_level_of_education:str,
        lunch:str,
        test_preparation_course:str,
        reading_score:int,
        writing_score:int
                 ):
        
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score


    def get_data_as_data_frame(self):

        """
        This function takes the arguments received from the html form and create a dictionary with them.
        The dictionary is used to create a dataframe. The data frame will be preprocessed and then a prediction made
        for the data
        """
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity":[self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch":[self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score":[self.reading_score],
                "writing_score":[self.writing_score]
            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)

       
