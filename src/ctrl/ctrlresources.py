'''
Created on 12 jun 2015

@author: fragom
'''
from java.util import Properties
import os

class SimulationResources(object):
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
#         print self.properties
    
    def get_Properties(self):
        '''
        This function works after storing or loading properties into the dictionary object
        '''
        return self.properties.values()
    
class ParameterResources(SimulationResources):
    '''
    classdocs
    modelPath=''
    libraryPath=''
    modelFile=''
    libraryFile=''
    modelName=''
    outputPath= ''
    '''
    properties= {} 
    
    def __init__(self):
        '''
        Constructor
        '''
        SimulationResources.__init__(self)
        self.properties= {'modelPath':'','libraryPath':'','modelFile':'',\
                          'libraryFile':'','modelName':'','outputPath':''}
    
    #
    
    ''' get methods for getting the properties from the resource file to GUI '''
    def get_modelFile(self):
        fullfile= self.properties['modelPath']+ '/'+ self.properties['modelName']
        return fullfile
    
    def get_libraryFile(self):
        fulllib= self.properties['libraryPath']+ '/'+ self.properties['libraryFile']
        return fulllib
    
    def get_modelName(self):
        return self.properties['modelName']
    
    def get_outputPath(self):
        return self.properties['outputPath']
    
    #
    ''' save mehtods to store resources from GUI to the resource file '''
    def set_modelPath(self, _modelPath):
        separateValues= _modelPath.split(os.sep)
        modelPath = '/'.join(separateValues[:-1])
        self.properties['modelPath']= modelPath
#         print modelPath
    
    def set_libraryPath(self, _libraryPath):
        separateValues= _libraryPath.split(os.sep)
        libraryPath = '/'.join(separateValues[:-1])
        self.properties['libraryPath']= libraryPath
#         print libraryPath
        
    def set_modelFile(self, _modelFile):
        separateValues= _modelFile.split(os.sep)
        modelFile = separateValues[-1]
        self.properties['modelFile']= modelFile
#         print modelFile
        
    def set_libraryFile(self, _libraryFile):
        separateValues= _libraryFile.split(os.sep)
        libraryFile = separateValues[-1]
        self.properties['libraryFile']= libraryFile
#         print libraryFile
       
    def set_modelName(self, _modelName):
        separateValues= _modelName.split(os.sep)
        modelName = separateValues[-1]
        self.properties['modelName']= modelName
#         print modelName
         
    def set_outputPath(self, _outputPath):
        separateValues= _outputPath.split(os.sep)
        outputPath = '/'.join(separateValues)
        self.properties['outputPath']= outputPath
#         print outputPath
