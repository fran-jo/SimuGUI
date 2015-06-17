'''
Created on 12 jun 2015

@author: fragom
'''
from java.util import Properties
import os

class CtrlProperties(object):
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
        
    def saveProperties(self, _filename, _comment):
        for key in self.properties:
            self.propertyF.setProperty(key, self.properties[key])
        fle= open(_filename,'w')
        self.propertyF.store(fle, _comment)
    
    def loadProperties(self, _filename):
        fle= open(_filename,'r')
        self.property.load(fle)
        for key in self.paramName:
            self.propertyF[key]= str(self.propertyF.getProperty(key))
        print self.property
        
    
class PrptResources(CtrlProperties):
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
        CtrlProperties.__init__(self)
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
       
        
class PrptConfigurationOMCDY(CtrlProperties):
    '''
    classdocs
    '''
    
    def __init__(self):
        ''' 
        Constructor
        '''
        CtrlProperties.__init__(self)
        self.properties= {'startTime':'','stopTime':'','numberOfIntervals':'',\
                          'tolerance':'','method':'','outputFormat':''}
        self.compiler= 'openmodelica'
        
    def setstarttime(self, _value):
        self.properties['startTime']= _value
        print _value
        
    def setstoptime(self, _value):
        self.properties['stopTime']= _value
        print _value
        
    def setintervals(self, _value):
        self.properties['numberOfIntervals']= _value
        print _value
        
    def settolerance(self, _value):
        self.properties['tolerance']= _value
        print _value
       
    def setmethod(self, _value):
        self.properties['method']= _value
        print _value
         
    def setoutputformat(self, _value):
        self.properties['outputFormat']= _value
        print _value


class PrptConfigurationJM(PrptConfigurationOMCDY):
    '''
    classdocs
    '''
    
    def __init__(self):
        ''' 
        Constructor
        '''
        PrptConfigurationOMCDY.__init__(self)
        self.properties= {'start_time':'','final_time':'','algorithm':'',\
                          'ncp':'','solver':'','initialize':''}
        
    def setstarttime(self, _value):
        self.properties['start_time']= _value
        print _value
        
    def setstoptime(self, _value):
        self.properties['final_time']= _value
        print _value
        
    def setintervals(self, _value):
        self.properties['ncp']= _value
        print _value
        
    def setalgorithm(self, _value):
        self.properties['algorithm']= _value
        print _value
       
    def setmethod(self, _value):
        self.properties['solver']= _value
        print _value
         
    def setinitialization(self, _value):
        self.properties['initialize']= _value
        print _value
