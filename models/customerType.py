class CustomerType:
    
    def __init__(self, typeID, typeName, ratePerUnit):
        self.typeID = typeID
        self.typeName = typeName
        self.ratePerUnit = ratePerUnit

    def getRatePerUnit(self):
        return self.ratePerUnit