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
    
    def get_Properties(self):
        '''
        This function works after storing or loading properties into the dictionary object
        '''
        return self.properties.values()

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
        StreamConfiguration.__init__(self, params)
        self.properties= {'startTime':'','stopTime':'','numberOfIntervals':'',\
                          'tolerance':'','method':'','outputFormat':''}
        self.compiler= 'openmodelica'
        
    def load_Properties(self, _filename):
        StreamConfiguration.load_Properties(self, _filename)
        self.__startTime = self.properties['startTime']
        self.__stopTime= self.properties['stopTime']
        self.__numberOfIntervals= self.properties['numberOfIntervals']
        self.__tolerance= self.properties['tolerance']
        self.__method= self.properties['method']
        self.__outputFormat= self.properties['outputFormat']
    #
    ''' getter/setter methods with properties '''
    @property
    def startTime(self):
        self.__startTime= self.properties['startTime']
        return self.__startTime
    @startTime.setter
    def startTime(self, valor):
        self.properties['startTime']= valor
        self.__startTime= valor;
        
    @property
    def stopTime(self):
        self.__stopTime= self.properties['stopTime']
        return self.__stopTime
    @stopTime.setter
    def stopTime(self, valor):
        self.properties['stopTime']= valor
        self.__stopTime= valor;
    
    @property
    def numberOfIntervals(self):
        self.__numberOfIntervals= self.properties['numberOfIntervals']
        return self.__numberOfIntervals
    @numberOfIntervals.setter
    def numberOfIntervals(self, valor):
        self.properties['numberOfIntervals']= valor
        self.__numberOfIntervals= valor;
    
    @property
    def tolerance(self):
        self.__tolerance= self.properties['tolerance']
        return self.__tolerance
    @tolerance.setter
    def tolerance(self, valor):
        self.properties['tolerance']= valor
        self.__tolerance= valor;
    
    @property
    def method(self):
        self.__method= self.properties['method']
        return self.__method
    @method.setter
    def method(self, valor):
        self.properties['method']= valor
        self.__method= valor;
    
    @property
    def outputFormat(self):
        self.__outputFormat= self.properties['outputFormat']
        return self.__outputFormat
    @outputFormat.setter
    def outputFormat(self, valor):
        self.properties['outputFormat']= valor
        self.__outputFormat= valor;
        
    
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
        self.properties= {'start_time':'','final_time':'','algorithm':'',\
                          'ncp':'','solver':'','initialize':'', 'outputFormat':''}
        
    def load_Properties(self, _filename):
        StreamConfiguration.load_Properties(self, _filename)
        self.__start_time = self.properties['start_time']
        self.__final_time= self.properties['final_time']
        self.__algorithm= self.properties['algorithm']
        self.__ncp= self.properties['ncp']
        self.__solver= self.properties['solver']
        self.__initialize= self.properties['initialize']
        self.__outputFormat= self.properties['outputFormat']
    #
    ''' getter/setter methods with properties '''
    @property
    def start_time(self):
        self.__start_time= self.properties['start_time']
        return self.__start_time
    @start_time.setter
    def start_time(self, valor):
        self.properties['start_time']= valor
        self.__start_time= valor;
        
    @property
    def final_time(self):
        self.__final_time= self.properties['final_time']
        return self.__final_time
    @final_time.setter
    def final_time(self, valor):
        self.properties['final_time']= valor
        self.__final_time= valor;
    
    @property
    def algorithm(self):
        self.__algorithm= self.properties['algorithm']
        return self.__algorithm
    @algorithm.setter
    def algorithm(self, valor):
        self.properties['algorithm']= valor
        self.__algorithm= valor;
    
    @property
    def ncp(self):
        self.__ncp= self.properties['ncp']
        return self.__ncp
    @ncp.setter
    def ncp(self, valor):
        self.properties['ncp']= valor
        self.__ncp= valor;
    
    @property
    def solver(self):
        self.__solver= self.properties['solver']
        return self.__solver
    @solver.setter
    def solver(self, valor):
        self.properties['solver']= valor
        self.__solver= valor;
        
    @property
    def initialize(self):
        self.__initialize= self.properties['initialize']
        return self.__initialize
    @initialize.setter
    def initialize(self, valor):
        self.properties['initialize']= valor
        self.__initialize= valor;
    
    @property
    def outputFormat(self):
        self.__outputFormat= self.properties['outputFormat']
        return self.__outputFormat
    @outputFormat.setter
    def outputFormat(self, valor):
        self.properties['outputFormat']= valor
        self.__outputFormat= valor;
