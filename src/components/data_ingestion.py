import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# decorator to enable us to create class variables without __init__ function
@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts', 'train.csv') #Create a folder called artifact and create data.csv file in it
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component") # Logging the start of data process
        try:
            df = pd.read_csv(r"notebooks\data\StudentsPerformance.csv") # Reading the data from local machine
            logging.info("Read the dataset as dataframe") # Logging the reading of the data

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) # Making a directory with the path name of train data path

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True) # raw data into raw_data_path

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Ingestion of data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
