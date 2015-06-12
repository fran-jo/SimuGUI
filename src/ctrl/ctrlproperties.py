'''
Created on 12 jun 2015

@author: fragom
'''
from java.util import Properties
from java.io import File, FileInputStream, FileOutputStream
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
        self.prop= Properties()
        propFile = File(params[0])
        self.prop.load(FileInputStream(propFile))
        
    def setModelPath(self, _modelPath):
        separateValues= _modelPath.split(os.sep)
        modelPath = '/'.join(separateValues)
        self.properties['modelPath']= modelPath
        print modelPath
        
    def setlibraryPath(self, _libraryPath):
        separateValues= _libraryPath.split(os.sep)
        libraryPath = '/'.join(separateValues)
        self.properties['libraryPath']= libraryPath
        print libraryPath
        
    def setmodelFile(self, _modelFile):
        separateValues= _modelFile.split(os.sep)
        modelFile = separateValues[:,-1]
        self.properties['modelFile']= modelFile
        print modelFile
        
    def setlibraryFile(self, _libraryFile):
        separateValues= _libraryFile.split(os.sep)
        libraryFile = separateValues[:,-1]
        self.properties['libraryFile']= libraryFile
        print libraryFile
       
    def setmodelName(self, _modelName):
        separateValues= _modelName.split(os.sep)
        modelName = separateValues[:,-1]
        self.properties['modelName']= modelName
        print modelName
         
    def setoutputPath(self, _outputPath):
        separateValues= _outputPath.split(os.sep)
        outputPath = '/'.join(separateValues)
        self.properties['outputPath']= outputPath
        print outputPath
    
    def saveProperties(self):
        self.prop.setProperty('modelPath', self.properties['modelPath'])
        self.prop.setProperty('libraryPath', self.properties['libraryPath'])
        self.prop.setProperty('modelFile', self.properties['modelFile'])
        self.prop.setProperty('libraryFile', self.properties['libraryFile'])
        self.prop.getProperty("modelName", self.properties['modelName'])
        self.prop.setProperty('outputPath', self.properties['outputPath'])
        out = FileOutputStream(self.prop);
        self.prop.store(out, "This is an optional header comment string");
    
    def loadProperties(self):
        self.properties['modelPath']= str(self.prop.getProperty("modelPath"))
        self.properties['libraryPath']= str(self.prop.getProperty("libraryPath"))
        self.properties['modelFile']= str(self.prop.getProperty("modelFile"))
        self.properties['libraryFile']= str(self.prop.getProperty("libraryFile"))
        self.properties['modelName']= str(self.prop.getProperty("modelName"))
        self.properties['outputPath']= str(self.prop.getProperty("outputPath"))
        
    
class PropertiesParams(CtrlProperties):
    '''
    classdocs
    '''
    
    def __init__(self):
        ''' a '''
        