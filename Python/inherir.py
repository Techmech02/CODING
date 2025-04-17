class person:
    def __init__(self,name):
        self.name=name
        
class emp(person):
    def __init__(self, name,sal):
        super().__init__(name)
        self.salary=sal