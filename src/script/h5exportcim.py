from PyCIM import PrettyPrintXML
from PyCIM import RDFXMLWriter
from inout.streamh5cim import StreamH5CIM

def h5import(filemou):
    ''' select group and dataset from an h5 file, store it into memory with
    PyCIM classes PowerSystemResource and Analog / AnalogValue'''
    dbh5= StreamH5CIM('./db/simulation', 'TwoAreas_AVRPSSE_wNoise')
    dbh5.open('TwoAreas_AVRPSSE_wNoise')
    cimMeasures= []
    if dbh5.exist_PowerSystemResource('bus1'):
        cimresource= dbh5.select_PowerSystemResource('bus1')
    if dbh5.exist_AnalogMeasurement('V'):
        cimMeasures.append(dbh5.select_AnalogMeasurement_CIM('V'))
    cimresource.setMeasurements(cimMeasures)
    internalModel= dbh5.internalModel
    internalModel[cimresource.UUID]= cimresource
    return internalModel

def cimexport(internalModel, encoding="utf-8"):
    nameMeasurementFile= 'TwoAreas_AVRPSSE_wNoise_bus1.xml'
    tmp = "/Users/fran_jo/Desktop/PhD_CODE/SimuGUI/res/"+ nameMeasurementFile
    RDFXMLWriter.cimwrite(internalModel, tmp) 
#    print(PrettyPrintXML.xmlpp(tmp))
    
if __name__ == "__main__":
    dictmodel= h5import('/Users/fran_jo/Desktop/PhD_CODE/SimuGUI/db/simulation/TwoAreas_AVRPSSE_wNoise.h5')
    cimexport(dictmodel)
    

