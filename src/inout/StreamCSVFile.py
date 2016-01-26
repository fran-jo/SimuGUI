'''
Created on 7 apr 2015

@author: fragom
'''
from datetime import datetime
import pandas as panda
from data import signal

class StreamCSVFile(object):
    '''
    Class observer for PMU data, in .csv file format from PMU 
    TODO: handle saving/loading data from the simulation engine 
    _csvFile file object with reference to the .csv file
    cgroup object to keep in memory a group from the .h5 file
    cdataset objet to keep in memory the dataset of signals from the .h5 file
    '''
    _csvFile= None
    _header= []
    _dsenyal= {}

    def __init__(self, sourceFile, delimiter=','):
        '''
        Constructor
        sourceFile: .csv file path
        delimiter: delimiter of fields
        '''
        self._csvFile= panda.read_csv(sourceFile, sep=delimiter)
        
    def get_fileName(self):
        return self._csvFile
    
    def get_senyal(self, componame):
        ''' return signal object '''
        return self._dsenyal[componame]
        
    def load_csvHeader(self):
        self._header= list(self._csvFile.columns.values)
        
    def get_csvHeader(self):
        return self._header
    
    def timestamp2sample(self, measurementTime):
        tiempos= [datetime.strptime(x,"%Y/%m/%d %H:%M:%S.%f") for x in measurementTime]
        sampletime= [(t- tiempos[0]).microseconds/1000 for t in tiempos]
#         print sampletime
        return sampletime

    def pmu_from_cmp(self, a_instance):
        '''Given an instance of A, return a new instance of B.'''
        return signal.SignalPMU(a_instance.field)  
            
            
class InputCSVStream(StreamCSVFile):
    '''
    Class observer for PMU data, in .csv file format
    Header format: 
    '''
    
    sampleTime= []
    signalValues= []
    
    def __init__(self, sourceFile, delimiter=','):
        super(InputCSVStream, self).__init__(sourceFile, delimiter)

    def open_csv(self):
        ''' Opens and existing csv file in reading mode '''
        pass
         
    def load_csvValues(self, componame, senyalR, senyalI):
        ''' Loads signal data from a specific variable form a specific component
        senyal: variable name of the signal, column name
        senyalR: name of the real,magnitude signal
        senyalI: name of the imaginary,phase signal 
        '''
        csenyal= signal.SignalPMU()
        if (senyalI != []):
            csenyal.set_signalPolar(list(self._csvFile['Time']), 
                                    list(self._csvFile[senyalR]), list(self._csvFile[senyalI]))
        else:
            ''' array of 0 of the same length as samples '''
            emptyarray= [-1 for x in self._csvFile['Time']]
            csenyal.set_signalPolar(list(self._csvFile['Time']), 
                                    list(self._csvFile[senyalR]), emptyarray)
        csenyal.set_ccomponent(componame)    
        self._dsenyal[componame]= csenyal
    
    def load_csvSignal(self, columnheader):
#         senyal= signal.SignalPMU()
#         emptyarray= [-1 for x in self._csvFile['Timestamp']]
#         senyal.set_signalPolar(list(self._csvFile['Timestamp']), 
#                                 list(self._csvFile[columnheader]), emptyarray)
        self.sampleTime= self.timestamp2sample(list(self._csvFile['Timestamp']))
        print columnheader
        self.signalValues= list(self._csvFile[columnheader])
        
#     def timestamp2sample(self, componame, all=True):
#         '''converts the timestamp value from pmu measurement into sample value as sample time 
#         componame name of the measurement to get the signal from 
#         '''
#         tiempos= [datetime.strptime(x,"%Y/%m/%d %H:%M:%S.%f") 
#                   for x in self._dsenyal[componame].get_sampleTime()]
#         sampletime= [(t- tiempos[0]).microseconds/1000 for t in tiempos]
#         self._dsenyal[componame].set_sampleTime(sampletime)
#         csenyal= signal.SignalPMU()
#         csenyal.set_signalPolar(sampletime, self._dsenyal[componame].get_signalMag(), 
#                                 self._dsenyal[componame].get_signalPolar())
#         self._dsenyal[componame]= csenyal
    
    def timestamp2sample(self, measurementTime):
        tiempos= [datetime.strptime(x,"%Y/%m/%d %H:%M:%S.%f") for x in measurementTime]
        sampletime= [(t- tiempos[0]).microseconds/1000 for t in tiempos]
#         print sampletime
        return sampletime
    
    def get_h5signal(self):
        ''' array with sampletime, magnitude and angle '''
        return self.sampleTime, self.signalValues
    
    def del_csvSignal(self):
        self.sampleTime= []
        self.signalValues= []
        
    def close_csv(self):
        self._csvFile.close()
        
