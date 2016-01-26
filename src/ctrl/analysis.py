'''
Created on 26 jan 2016

@author: fragom
'''
import numpy as np
from data import signal

class QuantitativeAnalysis(object):
    '''
    classdocs
    '''
    _signalOut= None
    _signalRef= None
    
    def __init__(self, params):
        '''
        Constructor
        '''
        self._signalOut= params[0]
        self._signalRef= params[1]
        
    def qaRMSE(self):
        arrayRef= np.array(self._signalRef)
        arrayOut= np.array(self._signalOut)
        mse= np.mean(np.power(arrayRef - arrayOut, 2))
        rmse= np.sqrt(np.mean(np.power(arrayRef - arrayOut, 2)))
        return mse, rmse
    
    def qaSignalError(self):
        error= np.subtract(np.array(self._signalRef), np.array(self._signalOut))
        return error