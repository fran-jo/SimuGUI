'''
Created on 4 apr 2014

@author: fragom
'''

class CompilerConfiguration(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        params[0]: .properties file
        params[1]: reading mode
        '''
        self.__fitxer= params[0].replace('\\','/')
        self.__readingMode= params[1]
        self._properties= {'startTime':'','stopTime':'','numberOfIntervals':'',\
                          'fixStepSize':'','tolerance':'','method':'','outputFormat':''}
        self._startTime = ''
        self._stopTime= ''
        self._numberOfIntervals= ''
        self._method= ''
        self._compiler= 'openmodelica'

    def save_Properties(self):
        fle= open(self.__fitxer,'w')
        for key in self._properties:
            fle.writelines(key+"="+str(self._properties[key])+"\n")
    
    def load_Properties(self):
        fle= open(self.__fitxer,self.__readingMode)
        self._properties= {}
        for line in fle:
            options=line.split('=')
            self._properties[options[0]]= options[1]

    @property
    def startTime(self):
        self._startTime= self._properties['startTime'].rstrip('\n')
        return self._startTime
    @startTime.setter
    def startTime(self, valor):
        self._properties['startTime']= valor
        self._startTime= valor;
        
    @property
    def stopTime(self):
        self._stopTime= self._properties['stopTime'].rstrip('\n')
        return self._stopTime
    @stopTime.setter
    def stopTime(self, valor):
        self._properties['stopTime']= valor
        self._stopTime= valor;

    @property
    def numberOfIntervals(self):
        self._numberOfIntervals= self._properties['numberOfIntervals'].rstrip('\n')
        return self._numberOfIntervals
    @numberOfIntervals.setter
    def numberOfIntervals(self, valor):
        self._properties['numberOfIntervals']= valor
        self._numberOfIntervals= valor;
        
    @property
    def method(self):
        self._method= self._properties['method'].rstrip('\n') #without char \n
        return self._method
    @method.setter
    def method(self, valor):
        self._properties['method']= valor
        self._method= valor
    
    @property
    def compiler(self):
        return self._compiler
    @compiler.setter
    def compiler(self, valor):
        self._compiler= valor;
        
    @property
    def configuration(self):
        return self._properties

class DymolaConfiguration(CompilerConfiguration):
    '''
    classdocs
    '''
    def __init__(self, params):
        ''' 
        Constructor
        '''
        self.__fixStepSize= ''
        self.__tolerance= ''
        self.__outputFormat= ''
        self.__modelName= ''
        CompilerConfiguration.__init__(self, params)
        
    def load_Properties(self):
        CompilerConfiguration.load_Properties(self)
        self._startTime = self._properties['startTime'].rstrip('\n')
        self._stopTime= self._properties['stopTime'].rstrip('\n')
        self.__numberOfIntervals= self._properties['numberOfIntervals'].rstrip('\n')
        self.__fixStepSize= self._properties['fixStepSize'].rstrip('\n')
        self.__tolerance= self._properties['tolerance'].rstrip('\n')
        self._method= self._properties['method'].rstrip('\n')
        self.__outputFormat= self._properties['outputFormat'].rstrip('\n')
    #
    ''' getter/setter methods with _properties '''
    @property
    def fixStepSize(self):
        self.__fixStepSize= self._properties['fixStepSize'].rstrip('\n')
        return self.__fixStepSize
    @fixStepSize.setter
    def fixStepSize(self, valor):
        self._properties['fixStepSize']= valor
        self.__fixStepSize= valor;
    
    @property
    def tolerance(self):
        self.__tolerance= self._properties['tolerance'].rstrip('\n')
        return self.__tolerance
    @tolerance.setter
    def tolerance(self, valor):
        self._properties['tolerance']= valor
        self.__tolerance= valor
    
    @property
    def outputFormat(self):
        self.__outputFormat= self._properties['outputFormat'].rstrip('\n') #without char \n
        return self.__outputFormat
    @outputFormat.setter
    def outputFormat(self, valor):
        self._properties['outputFormat']= valor
        self.__outputFormat= valor
        
    @property
    def modelName(self):
        self.__modelname= self._properties['modelName']
        return self.__modelname
    @modelName.setter
    def modelName(self, name):
        self._properties['modelName']= name
        self.__modelname= name;
        
class OpenModelicaConfiguration(CompilerConfiguration):
    '''
    classdocs
    '''
    
    def __init__(self, params):
        ''' 
        Constructor
        '''
        self.__fixStepSize= ''
        self.__tolerance= ''
        self.__outputFormat= ''
        self.__modelName= ''
        CompilerConfiguration.__init__(self, params)
        
    def load_Properties(self):
        CompilerConfiguration.load_Properties(self)
        self._startTime = self._properties['startTime'].rstrip('\n')
        self._stopTime= self._properties['stopTime'].rstrip('\n')
        self._numberOfIntervals= self._properties['numberOfIntervals'].rstrip('\n')
        self.__fixStepSize= self._properties['fixStepSize'].rstrip('\n')
        self.__tolerance= self._properties['tolerance'].rstrip('\n')
        self._method= self._properties['method'].rstrip('\n')
        self.__outputFormat= self._properties['outputFormat'].rstrip('\n')
    #
    ''' getter/setter methods with _properties '''
    @property
    def fixStepSize(self):
        self.__fixStepSize= self._properties['fixStepSize'].rstrip('\n')
        return self.__fixStepSize
    @fixStepSize.setter
    def fixStepSize(self, valor):
        self._properties['fixStepSize']= valor
        self.__fixStepSize= valor;
    
    @property
    def tolerance(self):
        self.__tolerance= self._properties['tolerance'].rstrip('\n')
        return self.__tolerance
    @tolerance.setter
    def tolerance(self, valor):
        self._properties['tolerance']= valor
        self.__tolerance= valor
    
    @property
    def outputFormat(self):
        self.__outputFormat= self._properties['outputFormat'].rstrip('\n') #without char \n
        return self.__outputFormat
    @outputFormat.setter
    def outputFormat(self, valor):
        self._properties['outputFormat']= valor
        self.__outputFormat= valor
        
    @property
    def modelName(self):
        self.__modelname= self._properties['modelName']
        return self.__modelname
    @modelName.setter
    def modelName(self, name):
        self._properties['modelName']= name
        self.__modelname= name;
    
class JModelicaConfiguration(CompilerConfiguration):
    '''
    classdocs
    '''
    
    def __init__(self, params):
        ''' 
        Constructor
        '''
        self.__algorithm= ''
        self.__initialize= ''
        self.__outputFormat= ''
        CompilerConfiguration.__init__(self, params)
        self.compiler= 'jmodelica'
        self._properties= {'start_time':'','final_time':'','algorithm':'',\
                          'ncp':'','solver':'','initialize':'', 'outputFormat':''}
        
    def load_Properties(self, _filename):
        CompilerConfiguration.load_Properties(self, _filename)
        self._startTime = self._properties['start_time']
        self._stopTime= self._properties['final_time']
        self.__algorithm= self._properties['algorithm']
        self._numberOfIntervals= self._properties['ncp']
        self._method= self._properties['solver']
        self.__initialize= self._properties['initialize']
        self.__outputFormat= self._properties['outputFormat']
    #
    ''' getter/setter methods with _properties '''
    @property
    def start_time(self):
        self._startTime= self._properties['start_time']
        return self._startTime
    @start_time.setter
    def start_time(self, valor):
        self._properties['start_time']= valor
        self._startTime= valor;
        
    @property
    def final_time(self):
        self._stopTime= self._properties['final_time']
        return self._stopTime
    @final_time.setter
    def final_time(self, valor):
        self._properties['final_time']= valor
        self._stopTime= valor;
    
    @property
    def algorithm(self):
        self.__algorithm= self._properties['algorithm']
        return self.__algorithm
    @algorithm.setter
    def algorithm(self, valor):
        self._properties['algorithm']= valor
        self.__algorithm= valor;
    
    @property
    def ncp(self):
        self._numberOfIntervals= self._properties['ncp']
        return self._numberOfIntervals
    @ncp.setter
    def ncp(self, valor):
        self._properties['ncp']= valor
        self._numberOfIntervals= valor;
    
    @property
    def solver(self):
        self._method= self._properties['solver']
        return self._method
    @solver.setter
    def solver(self, valor):
        self._properties['solver']= valor
        self._method= valor;
        
    @property
    def initialize(self):
        self.__initialize= self._properties['initialize']
        return self.__initialize
    @initialize.setter
    def initialize(self, valor):
        self._properties['initialize']= valor
        self.__initialize= valor;
    
    @property
    def outputFormat(self):
        self.__outputFormat= self._properties['outputFormat']
        return self.__outputFormat
    @outputFormat.setter
    def outputFormat(self, valor):
        self._properties['outputFormat']= valor
        self.__outputFormat= valor;
