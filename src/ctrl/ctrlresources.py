'''
Created on 12 jun 2015

@author: fragom
'''
import os

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
    cimPath= ''
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
        self.__cimfolder = ''
        self.__modelfolder= ''
        self.__libraryfolder= ''
        self.__outputfolder= ''
        self.__modelfile= ''
        self.__libraryfile= ''
        self.__modelname= ''
        StreamProperties.__init__(self, params)
        self.properties= {'cimPath':'','modelPath':'','libraryPath':'','modelFile':'',\
                          'libraryFile':'','modelName':'','outputPath':''}
    
    
    ''' getter/setter methods with properties '''
    @property
    def cimfolder(self):
        self.__cimfolder= self.properties['cimPath']
        return self.__cimfolder
    @cimfolder.setter
    def cimfolder(self, path):
        self.properties['cimPath']= path
        self.__cimfolder= path;
        
    @property
    def modelfolder(self):
        self.__modelfolder= self.properties['modelPath']
        return self.__modelfolder
    @modelfolder.setter
    def modelfolder(self, path):
        self.properties['modelPath']= path
        self.__modelfolder= path;
        
    @property
    def libraryfolder(self):
        self.__libraryfolder= self.properties['libraryPath']
        return self.__libraryfolder
    @libraryfolder.setter
    def libraryfolder(self, path):
        self.properties['libraryPath']= path
        self.__libraryfolder= path;
    
    @property
    def outputfolder(self):
        self.__outputfolder= self.properties['outputPath']
        return self.__outputfolder
    @outputfolder.setter
    def outputfolder(self, path):
        self.properties['outputPath']= path
        self.__outputfolder= path;
    
    @property
    def modelname(self):
        self.__modelname= self.properties['modelName']
        return self.__modelname
    @modelname.setter
    def modelname(self, path):
        self.properties['modelName']= path
        self.__modelname= path;
    
    #
    ''' save mehtods to store resources from GUI to the resource file '''
        
        
    def set_modelFile(self, _filename):
        separateValues= _filename.split(os.sep)
        modelFile = separateValues[-1]
        self.properties['modelFile']= modelFile
#         print modelFile
        
    def set_libraryFile(self, _filename):
        separateValues= _filename.split(os.sep)
        libraryFile = separateValues[-1]
        self.properties['libraryFile']= libraryFile
#         print libraryFile
