'''
Created on 27 jan 2016

@author: fragom
'''

import dyntools

class StreamOUTClass(object):
    '''
    _channels contains names of all the output signals from the .out file
    _channel_data contains the values of a specific channel
    '''
    _chanfobj= None

    def __init__(self, params):
        '''
        Constructor
        '''
        self._chanfobj = dyntools.CHNF([str(params[0])])
        

    def get_chanfobj(self):
        return self._chanfobj


    def set_chanfobj(self, value):
        self._chanfobj = value


    def del_chanfobj(self):
        del self._chanfobj

    chanfobj = property(get_chanfobj, set_chanfobj, del_chanfobj, "chanfobj's docstring")
        
    
class InputOUTStream(StreamOUTClass):
    '''
        classdata
    '''
    
    __channels= []
    __sampleTime= []
    __channel_data= []
    
    def __init__(self, nameFile):
        super(InputOUTStream, self).__init__([nameFile])
        
    def load_channels(self):
        sh_ttl, ch_id = self._chanfobj.get_id()
        self.__channels = [ch_id[index] for index in range(1, len(ch_id)- 1)]
            
    def load_channel_data(self, chanel):
        sh_ttl, ch_id, ch_data= self._chanfobj.get_data()
        index= ch_id.values().index(str(chanel))+ 1
        self.__sampleTime= ch_data['time']
        self.__channel_data= ch_data[index]
            
    def get_channels(self):
        return self.__channels

    def get_channel_data(self):
        return self.__channel_data
    
    def get_sampleTime(self):
        return self.__sampleTime


    def set_channels(self, value):
        self.__channels = value

    def set_channel_data(self, value):
        self.__channel_data = value

    def set_sampleTime(self, value):
        self.__sampleTime = value


    def del_channels(self):
        del self.__channels

    def del_channel_data(self):
        del self.__channel_data
        
    def del_sampleTime(self):
        del self.__sampleTime

    channels = property(get_channels, set_channels, del_channels, "channels's docstring")
    sampleTime= property(get_sampleTime, set_sampleTime, del_sampleTime, "sampleTime's docstring")
    channel_data = property(get_channel_data, set_channel_data, del_channel_data, "channel_data's docstring")
