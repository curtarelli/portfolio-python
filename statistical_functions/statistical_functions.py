'''
@author:	Victor Pedroso Curtarelli
@linkedin:	https://www.linkedin.com/in/victorcurtarelli/
@github:	https://github.com/curtarelli

@date: 06-01-2020
-------------------------------------------------------------------------------
This is a script of statistical tools to compare two data series. A reference one, and a predict one.
'''
##  Importing packages needed.
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error as mse
from matplotlib import pyplot as plt

###############################################################################
########################## Base statistic #####################################
###############################################################################
def mape(y_true, y_pred):
    '''
	Function to calculate the Mean Absolute Percentage Error (MAPE) using a reference
	and a predict data series.
    
    ----------
    Parameters
    ----------
    y_true [Series]
        Sampling reference data series, field "true".
        
        Ex.: Field mesurementes, laboratory analysis, etc.
        
    y_pred [Series]
        Predict sampling dataset, estimated values.

        Ex.: Simulated values from field or image application.
    
    -------
    Returns
    -------
    MAPE [Value]
		Calculated value for MAPE using y_true and y_pred.
    '''
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

###############################################################################
def correlation_coeff(y_true, y_pred):
    '''
	Function to calculate the Correlation Coefficient (r) using a reference
	and a predict data series.
    
    ----------
    Parameters
    ----------
    y_true [Series]
        Sampling reference data series, field "true".
        
        Ex.: Field mesurementes, laboratory analysis, etc.
        
    y_pred [Series]
        Predict sampling dataset, estimated values.

        Ex.: Simulated values from field or image application.
    
    -------
    Returns
    -------
    r [Value]
		Calculated value for r using y_true and y_pred.
    '''
    df_temp = pd.DataFrame({'Real': y_true, 'predicted': y_pred})
    return (df_temp.corr().iloc[1].iloc[0])

###############################################################################
def determination_coeff(y_true, y_pred):
    '''
	Function to calculate the Determination Coefficient (R²) using a reference
	and a predict data series.
    
    ----------
    Parameters
    ----------
    y_true [Series]
        Sampling reference data series, field "true".
        
        Ex.: Field mesurementes, laboratory analysis, etc.
        
    y_pred [Series]
        Predict sampling dataset, estimated values.

        Ex.: Simulated values from field or image application.
    
    -------
    Returns
    -------
    R² [Value]
		Calculated value for R² using y_true and y_pred.
    '''
    df_temp = pd.DataFrame({'Real': y_true, 'predicted': y_pred})
    return (df_temp.corr().iloc[1].iloc[0]) ** 2

###############################################################################
def bias_error(y_true, y_pred):
    '''
	Function to calculate the bias error using a reference
	and a predict data series.
    ----------
    Parameters
    ----------
    y_true [Series]
        Sampling reference data series, field "true".
        
        Ex.: Field mesurementes, laboratory analysis, etc.
        
    y_pred [Series]
        Predict sampling dataset, estimated values.

        Ex.: Simulated values from field or image application.
    
    -------
    Returns
    -------
    Bias [Value]
		Calculated value for bias error using y_true and y_pred.
    '''
    return np.mean(y_pred - y_true)
    
def rmse(y_true, y_pred):
    '''
	Function to calculate the Root-Mean Square Error (RMSE) using
	a reference and a predict data series.
    
    ----------
    Parameters
    ----------
    y_true [Series]
        Sampling reference data series, field "true".
        
        Ex.: Field mesurementes, laboratory analysis, etc.
        
    y_pred [Series]
        Predict sampling dataset, estimated values.

        Ex.: Simulated values from field or image application.
    
    -------
    Returns
    -------
    RMSE [Value]
		Calculated value for RMSE using y_true and y_pred.
    '''
    return np.sqrt(mse(y_true, y_pred))
