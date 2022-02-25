import uuid
from objects.envDetails import EnvDetails
from objects.workLoadDetails import WorkLoadDetails

class Test(object):
    def __init__(self):
        self.id = uuid.uuid1()
        self.date = None
        self.data = None
        self.subjectDetails = None
        self.envDetails = EnvDetails()
        self.workLoadCount = None
        self.endWorkLoad = None
        self.workLoads = []

        # Initiate load object
        self.workLoads.append( Load(self) )

    def getWorkLoads(self):
        return self.workLoads

    def addWorkLoad(self, load):
        self.workLoads.append(load)

    def createLoad(self):
        newLoad = Load()
        self.workLoads.append( newLoad )
        return newLoad

    def nWorkLoads(self):
        return len(self.workLoads)

    def getEnvDetails(self):
        return self.envDetails

    def setId(self, id):
        self.id = id

class Load(object):
    def __init__(self, parentTest):
        self.name = None
        self.parentTest = parentTest
        self.details = WorkLoadDetails()
    
    def getDetails(self):
        return self.details

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
    
    def setDemoDetails(self):
        print('Setting demo details')
        self.details.setValue('VO2', 2)
        self.details.setUnit('VO2_unit', 'l/min')

        self.details.setValue('Q', 13)
        self.details.setUnit('Q_unit', 'l/min')

        self.details.setValue('Hb', 13)
        self.details.setUnit('Hb_unit', 'g/dl')

        self.details.setValue('SaO2', 99)
        self.name = 'Demo'
        self.parentTest.setId('Demo')