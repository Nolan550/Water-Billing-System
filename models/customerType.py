class Customer_Type:
    
    def __init__(self, type_ID, type_name, rate_per_unit):
        self.type_ID = type_ID
        self.type_name = type_name
        self.rate_per_unit = rate_per_unit

    def get_rate_per_unit(self):
        return self.rate_per_unit