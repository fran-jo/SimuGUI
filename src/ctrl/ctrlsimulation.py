'''
Created on 4 apr 2014

@author: fragom
'''

class StreamConfiguration(object):
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
        self._properties= {}
        self._compiler= 'openmodelica'

    def save_Properties(self):
        fle= open(self.fitxer,'w')
        for key in self._properties:
            fle.writelines(key+"="+str(self._properties[key])+"\n")
    
    def load_Properties(self):
        fle= open(self.fitxer,self.readingMode)
        self._properties= {}
        for line in fle:
            options=line.split('=')
            self._properties[options[0]]= options[1]

    @property
    def compiler(self):
        return self._compiler
    @compiler.setter
    def compiler(self, valor):
        self._compiler= valor;
        
    @property
    def configuration(self):
        return self._properties

class SimulationConfigOMCDY(StreamConfiguration):
    '''
    classdocs
    '''
    
    def __init__(self, params):
        ''' 
        Constructor
        '''
        self.__startTime = ''
        self.__stopTime= ''
        self.__numberOfIntervals= ''
        self.__tolerance= ''
        self.__method= ''
        self.__outputFormat= ''
        self.__modelName= ''
        StreamConfiguration.__init__(self, params)
        self._properties= {'startTime':'','stopTime':'','numberOfIntervals':'',\
                          'tolerance':'','method':'','outputFormat':''}
        
    def load_Properties(self):
        StreamConfiguration.load_Properties(self)
        self.__startTime = self._properties['startTime'].rstrip('\n')
        self.__stopTime= self._properties['stopTime'].rstrip('\n')
        self.__numberOfIntervals= self._properties['numberOfIntervals'].rstrip('\n')
        self.__tolerance= self._properties['tolerance'].rstrip('\n')
        self.__method= self._properties['method'].rstrip('\n')
        self.__outputFormat= self._properties['outputFormat'].rstrip('\n')
    #
    ''' getter/setter methods with _properties '''
    @property
    def startTime(self):
        self.__startTime= self._properties['startTime'].rstrip('\n')
        return self.__startTime
    @startTime.setter
    def startTime(self, valor):
        self._properties['startTime']= valor
        self.__startTime= valor;
        
    @property
    def stopTime(self):
        self.__stopTime= self._properties['stopTime'].rstrip('\n')
        return self.__stopTime
    @stopTime.setter
    def stopTime(self, valor):
        self._properties['stopTime']= valor
        self.__stopTime= valor;
    
    @property
    def numberOfIntervals(self):
        self.__numberOfIntervals= self._properties['numberOfIntervals'].rstrip('\n')
        return self.__numberOfIntervals
    @numberOfIntervals.setter
    def numberOfIntervals(self, valor):
        self._properties['numberOfIntervals']= valor
        self.__numberOfIntervals= valor;
    
    @property
    def tolerance(self):
        self.__tolerance= self._properties['tolerance'].rstrip('\n')
        return self.__tolerance
    @tolerance.setter
    def tolerance(self, valor):
        self._properties['tolerance']= valor
        self.__tolerance= valor
    
    @property
    def method(self):
        self.__method= self._properties['method'].rstrip('\n') #without char \n
        return self.__method
    @method.setter
    def method(self, valor):
        self._properties['method']= valor
        self.__method= valor
    
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
    
class SimulationConfigJM(StreamConfiguration):
    '''
    classdocs
    '''
    
    def __init__(self, params):
        ''' 
        Constructor
        '''
        self.__start_time = ''
        self.__final_time= ''
        self.__algorithm= ''
        self.__ncp= ''
        self.__solver= ''
        self.__initialize= ''
        self.__outputFormat= ''
        StreamConfiguration.__init__(self, params)
        self.compiler= 'jmodelica'
        self._properties= {'start_time':'','final_time':'','algorithm':'',\
                          'ncp':'','solver':'','initialize':'', 'outputFormat':''}
        
    def load_Properties(self, _filename):
        StreamConfiguration.load_Properties(self, _filename)
        self.__start_time = self._properties['start_time']
        self.__final_time= self._properties['final_time']
        self.__algorithm= self._properties['algorithm']
        self.__ncp= self._properties['ncp']
        self.__solver= self._properties['solver']
        self.__initialize= self._properties['initialize']
        self.__outputFormat= self._properties['outputFormat']
    #
    ''' getter/setter methods with _properties '''
    @property
    def start_time(self):
        self.__start_time= self._properties['start_time']
        return self.__start_time
    @start_time.setter
    def start_time(self, valor):
        self._properties['start_time']= valor
        self.__start_time= valor;
        
    @property
    def final_time(self):
        self.__final_time= self._properties['final_time']
        return self.__final_time
    @final_time.setter
    def final_time(self, valor):
        self._properties['final_time']= valor
        self.__final_time= valor;
    
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
        self.__ncp= self._properties['ncp']
        return self.__ncp
    @ncp.setter
    def ncp(self, valor):
        self._properties['ncp']= valor
        self.__ncp= valor;
    
    @property
    def solver(self):
        self.__solver= self._properties['solver']
        return self.__solver
    @solver.setter
    def solver(self, valor):
        self._properties['solver']= valor
        self.__solver= valor;
        
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
