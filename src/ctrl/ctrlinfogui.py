'''
Created on 12 jun 2015

@author: fragom
'''
#from java.util import Properties
#from java.util import 
import os
import sys
 

class StreamProperties(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        params[0]: .properties file
        params[1]: reading mode
        '''
        self.fitxer= params[0].replace('\\','/')
        self.readingMode= params[1]
        self.properties= {'default':'property'}
        
    def save_Properties(self):
        fle= open(self.fitxer,'w')
        for key in self.properties:
            fle.writelines(key+"="+str(self.properties[key])+"\n")
            ''' TODO: write the dictionary structure to a file - Complete '''
    def save_Properties1(self):
        fle= open(self.fitxer,'w')
        for key in self.properties:
            
#             options=key.join('=')
#             self.properties[options[0]]=options[1]
            fle.writelines(key+"="+self.properties[key]+"\n")
    
    def load_Properties(self):
        fle= open(self.fitxer,self.readingMode)
        for line in fle:
            options=line.split('=')
            self.properties[options[0]]= options[1]
#         print self.properties
    
    def get_Properties(self):
        '''
        This function works after storing or loading properties into the dictionary object
        '''
        return self.properties.values()
    
class SimulationResources(StreamProperties):
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
        '''
        StreamProperties.__init__(self, params)
        self.properties= {'modelPath':'','libraryPath':'','modelFile':'',\
                          'libraryFile':'','modelName':'','outputPath':''}
    
    #
    
    ''' get methods for getting the properties from the resource file to GUI '''
    def get_modelFile(self):
        fullfile= self.properties['modelPath'][:-1]+ self.properties['modelFile'][:-1]
        return fullfile
    
    def get_libraryFile(self):
        fulllib= self.properties['libraryPath'][:-1]+ self.properties['libraryFile'][:-1]
        return fulllib
    
    def get_modelName(self):
        return self.properties['modelName'][:-1]
    
    def get_outputPath(self):
        return self.properties['outputPath'][:-1]
    
    #
    ''' save mehtods to store resources from GUI to the resource file '''
    def set_modelPath(self, _modelPath):
#         separateValues= _modelPath.split(os.sep)
#         modelPath = '/'.join(separateValues[:-1])
        #modelPath = separateValues[:-1]
        self.properties['modelPath']= _modelPath
        #print modelPath+'Here I am '
    
    def set_libraryPath(self, _libraryPath):
#         separateValues= _libraryPath.split(os.sep)
#         libraryPath = '/'.join(separateValues[:-1])
        #libraryPath = separateValues[:-1]
        self.properties['libraryPath']= _libraryPath
        #print libraryPath+'Here I am 2 '
        
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


class SimulationConfigurationOMC(StreamProperties):
    '''
    classdocs
    startTime='' - Start Time
    stopTime='' - Stop Time
    numberOfIntervals='' - Interval
    tolerance='' - Tolerance
    method='' - solver
    outputFormat= '' - Output Format
    '''
    def __init__(self, params):
        ''' 
        Constructor
        '''
        StreamProperties.__init__(self, params)
        self.properties= {'startTime':'','stopTime':'','numberOfIntervals':'',\
                          'tolerance':'','method':'','outputFormat':''}
        self.compiler= 'openmodelica'
        
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
        
    
