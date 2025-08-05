import pandas as pd
import numpy as np
import sys



class Patrol():

    #fixing a threshold
    threshold=0.62

    def __init__(self, data=None, model=None, features=None, threshold=None):
        """
        data:  The pandas dataframe containing all the necessary columns for model calculation.
        model: This should be a pretrained model that has the .predict_proba() method available.
        features: List of predictors for the model to produce the final score.
        """

        if data is None or type(data) is not pd.DataFrame:
            raise Exception('Dataframe provided is not a valid pandas.DataFrame!')

        if model is None or hasattr(model, 'predict_proba') is False:
            raise Exception('The model provided is non-existent or has no predict_proba method!')

        if features is None or isinstance(features, list) is False:
            raise Exception('The features provided are non-existent or they are not a list!')

        if pd.Series(features).isin(data.columns).all() is False:
            raise Exception('The features provided are not all present in the data provided!')

        self.data=data
        self.model=model
        self.features=features

        if type(threshold) is float:
            self.threshold=threshold


    def d(self, data=None):
        """additional method for adding new dataframe"""
        if data is None or type(data) is not pd.DataFrame:
            raise Exception('Dataframe provided is not a valid pandas.DataFrame!')       
        
        self.data=data
        return self       

    def m(self, model=None):
        """additional method for adding new model"""

        if model is None or hasattr(model, 'predict_proba') is False:
            raise Exception('The model provided is non-existent or has no predict_proba method!')

        self.model=model
        return self   

    def f(self, features=None):
        """additional method for adding model features"""

        if features is None or isinstance(features, list) is False:
            raise Exception('The features provided are non-existent or they are not a list!')

        if pd.Series(features).isin(data.columns).all() is False:
            raise Exception('The features provided are not all present in the data provided!')

        self.features=features
        return self   

    def t(self, threshold=None):
        """additional method for changing threshold"""

        if type(threshold) is float:
            self.threshold=threshold
        
        return self   


    def check_transaction(self, transaction_column=None, transaction_id=None):
        """Calculating probability of fraud for given transaction in the given data and comparing it
        to the threshold for determining fraud. Returning a decision to LOCK or NO_LOCK the client 
        based on the value of the score and the value of the threshold."""

        try:
            df_=self.data[self.data[transaction_column]==transaction_id]
            if len(df_)<=0:
                raise Exception('No transaction with given ID in the dataset!')
            if len(df_)>1:
                raise Exception('More transactions with given ID in the dataset!')
        except Exception as err:
            print(f'Could not find the given transaction in the dataset!')
            raise

        try:
            df_['model_score']=self.model.predict_proba(df_[self.features])[:,1]
            final_score=df_['model_score'].reset_index(drop=True)[0]
            if final_score>1:
                raise Exception('Score is greater than 1!')      
            if final_score<0:
                raise Exception('Score is smaller than 0!')      
        except Exception as err:
            print(f'Could not calculate the final score!')
            raise

        if final_score>self.threshold:
            print(f'Final score {final_score} is greater than threshold {self.threshold}  ->LOCK')
            return 'LOCK'
        else:
            print(f'Final score {final_score} is smaller than threshold {self.threshold}  ->PASS')
            return 'PASS'


 