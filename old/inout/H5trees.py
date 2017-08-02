'''
Created on Nov 17, 2015

@author: ekj05
'''
import h5py

"""this class is to find the h5 trees form its structure 
return the list of the variables and the items from h5 file
"""
class H5trees(object):
    list=[]
    group=''
    time=[]
    sig=[]
    mag=[]
    ang=[]
    subgroup=''
    combolist='enam'
    
    def __init__(self,file):
        self.file=file
    
    def fopen(self):
        f=h5py.File(self.file, 'r')
        return f
    def fileOpen(self):
        f=h5py.File(self.file, 'r')
        self.group=f[f.keys()[0]]
        self.subgroup=f.keys()[0]
        return self.group
    def returnfilename(self):
        return self.file,'/'+str(self.subgroup)+'/'
    def load_Value_In_Matlab(self,combo):
        self.combo=combo
        return self.file,'/'+str(self.subgroup)+'/'+self.combo 
    def groupTree(self):
        self.list=[]
        for name in self.group:
            self.list.append(name)
        return self.list
    
    def dataSetNames(self,name):
        self.name=name
        signalsNames= self.group.get(self.name)
        #print 'signalNames', signalsNames
        self.sig= signalsNames[0]
        #print 'self.sig', self.sig
        return self.sig[0],self.sig[1],self.sig[2]
    
    def dataSetValues(self,name):
        self.name=name
        signalsValues= self.group.get(self.name)
        #print 'signalValues', signalsValues
#         self.time= signalsValues[0]
#         print 'self.sig', self.time
        
        for x, y, z, in self.group.get(self.name):
            self.time.append(x)
            self.mag.append(y)
            self.ang.append(z)
        return self.time, self.mag, self.ang
    def ModEstimationValues(self,name):
        self.name=name
        signalsValues= self.group.get(self.name)
        #print 'signalValues', signalsValues
#         self.time= signalsValues[0]
#         print 'self.sig', self.time
        
        for x, in self.group.get(self.name):
            self.time.append(x)
            #self.mag.append(y)
        
        return self.time
        

#         for x, y, z, in self.group.get(self.name):
#             return self.sig.append(z)
#         
        
    
    
        
        
    
             
        
        
    
