'''
Created on 12 jun 2015

@author: fragom
'''
from java.util import Properties
import os

class CtrlProperties(object):
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
    
    def __init__(self, params):
        '''
        Constructor
        params[0]: .properties file
        '''
        self.property= Properties()
        self.properties= {'modelPath':'','libraryPath':'','modelFile':'',\
                          'libraryFile':'','modelName':'','outputPath':''}
        
    def setmodelPath(self, _modelPath):
        separateValues= _modelPath.split(os.sep)
        modelPath = '/'.join(separateValues[:-1])
        self.properties['modelPath']= modelPath
        print modelPath
        
    def setlibraryPath(self, _libraryPath):
        separateValues= _libraryPath.split(os.sep)
        libraryPath = '/'.join(separateValues[:-1])
        self.properties['libraryPath']= libraryPath
        print libraryPath
        
    def setmodelFile(self, _modelFile):
        separateValues= _modelFile.split(os.sep)
        modelFile = separateValues[-1]
        self.properties['modelFile']= modelFile
        print modelFile
        
    def setlibraryFile(self, _libraryFile):
        separateValues= _libraryFile.split(os.sep)
        libraryFile = separateValues[-1]
        self.properties['libraryFile']= libraryFile
        print libraryFile
       
    def setmodelName(self, _modelName):
        separateValues= _modelName.split(os.sep)
        modelName = separateValues[-1]
        self.properties['modelName']= modelName
        print modelName
         
    def setoutputPath(self, _outputPath):
        separateValues= _outputPath.split(os.sep)
        outputPath = '/'.join(separateValues)
        self.properties['outputPath']= outputPath
        print outputPath
    
    def saveProperties(self, _filename, _comment):
        for key in self.properties:
            self.property.setProperty(key, self.properties[key])
        fle= open(_filename,'w')
        self.property.store(fle, _comment)
    
    def loadProperties(self, _filename):
        fle= open(_filename,'r')
        self.property.load(fle)
        for key in self.paramName:
            self.properties[key]= str(self.property.getProperty(key))
        print self.property
        
    
class PropertiesParams(CtrlProperties):
    '''
    classdocs
    '''
    
    def __init__(self):
        ''' a '''
        