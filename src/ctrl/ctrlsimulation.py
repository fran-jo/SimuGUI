'''
Created on 4 apr 2014

@author: fragom
'''
from java.util import Properties
import os

class SimulationConfiguration(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        params[0]: .properties file
        '''
        self.propertyF= Properties()
        self.properties= {'default':'property'}
        
    def save_Properties(self, _filename, _comment):
        for key in self.properties:
            self.propertyF.setProperty(key, self.properties[key])
        fle= open(_filename,'w')
        self.propertyF.store(fle, _comment)
    
    def load_Properties(self, _filename):
        fle= open(_filename,'r')
        self.propertyF.load(fle)
        for key in self.properties:
            self.properties[key]= str(self.propertyF.getProperty(key))
        print self.properties
    
    def get_Properties(self):
        '''
        This function works after storing or loading properties into the dictionary object
        '''
        return self.properties.values()

class SimulationConfigOMCDY(SimulationConfiguration):
    '''
    classdocs
    '''
    
    def __init__(self):
        ''' 
        Constructor
        '''
        SimulationConfiguration.__init__(self)
        self.properties= {'startTime':'','stopTime':'','numberOfIntervals':'',\
                          'tolerance':'','method':'','outputFormat':''}
        self.compiler= 'openmodelica'
        
    #
    
    def get_starttime(self):
        return self.properties['startTime']
    
    def get_stoptime(self):
        return self.properties['stopTime']
    
    def get_intervals(self):
        return self.properties['numberOfIntervals']
    
    def get_tolerance(self):
        return self.properties['tolerance']
    
    def get_method(self):
        return self.properties['method']
    
    def get_outputformat(self):
        return self.properties['outputFormat']
    #
    
    def set_starttime(self, _value):
        self.properties['startTime']= _value
        
    def set_stoptime(self, _value):
        self.properties['stopTime']= _value
        
    def set_intervals(self, _value):
        self.properties['numberOfIntervals']= _value
        
    def set_tolerance(self, _value):
        self.properties['tolerance']= _value
       
    def set_method(self, _value):
        self.properties['method']= _value
         
    def set_outputformat(self, _value):
        self.properties['outputFormat']= _value

#     def get_Properties(self):
#         '''
#         This function works after storing or loading properties into the dictionary object
#         '''
#         simulate_options = ''
#         for k, v in self.properties.iteritems():
#             simulate_options = simulate_options + "," + str(k) + "=" + str(v)
#         print simulate_options
#         return simulate_options
    
class SimulationConfigJM(SimulationConfigOMCDY):
    '''
    classdocs
    '''
    
    def __init__(self):
        ''' 
        Constructor
        '''
        SimulationConfigOMCDY.__init__(self)
        self.properties= {'start_time':'','final_time':'','algorithm':'',\
                          'ncp':'','solver':'','initialize':''}
    
    #
    def get_starttime(self):
        return self.properties['start_time']
        
    def get_stoptime(self):
        return self.properties['final_time']
        
    def get_intervals(self):
        return self.properties['ncp']
        
    def get_algorithm(self):
        return self.properties['algorithm']
       
    def get_method(self):
        return self.properties['solver']
         
    def get_initialization(self):
        return self.properties['initialize']
    
    #   
    def set_starttime(self, _value):
        self.properties['start_time']= _value
        
    def set_stoptime(self, _value):
        self.properties['final_time']= _value
        
    def set_intervals(self, _value):
        self.properties['ncp']= _value
        
    def set_algorithm(self, _value):
        self.properties['algorithm']= _value
       
    def set_method(self, _value):
        self.properties['solver']= _value
         
    def set_initialization(self, _value):
        self.properties['initialize']= _value
