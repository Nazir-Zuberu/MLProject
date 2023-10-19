import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl') # Creating a path for our columns transformer

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig() # Assigning the created path to a variable

    def get_data_transformer_object(self):

        """
        This function is responsible for data transformation
        """
        try:
            numerical_columns = ['reading_score','writing_score'] # list of numerical columns

            categorical_columns = [
                'gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course',
                ] # list of cat columns
            
            # Transforming numerical columns
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )
            logging.info("Numerical variable transformation completed")

            # Transforming cat columns
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_endcoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )
            logging.info("Categorical variable encoding completed")

            # Applying column transformer to the pipelines for column transformation
            preprocessor = ColumnTransformer(
                [
                ("num_pipeline", num_pipeline, numerical_columns),
                ("cat_pipeline", cat_pipeline, categorical_columns)
            ])

            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)
        
    # A function to perform the column transformation
    def initiate_data_transformation(self, train_path, test_path):

        try:
            train_df = pd.read_csv(repr(train_path)[1:-1])
            test_df = pd.read_csv(repr(test_path)[1:-1])

            logging.info("Read train and test data completed")
            
            logging.info("Obtaining preprocessor object")

            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "math_score"  # target variable
            numerical_columns = ["writing_score", "reading_score"]

            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1) # droping target variable from training set
            target_feature_train_df = train_df[target_column_name] # target for training set

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1) # droping target variable from the test set
            target_feature_test_df = test_df[target_column_name] # target for testing set

            logging.info(f"Applying preprocessing object on training and testing dataframes")

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.fit_transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ] # Combining input feature and the target for training set

            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ] # Combining input features and the target for testing set

            logging.info("Saved Preprocessing Object")

            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            ) # Saving the column transformer object

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
 
        except Exception as e:
            raise CustomException(e, sys)


            
            
            


