class Taxi:
    def __init__(self, name, id) -> None:
        self._id = id
        self._name = name
        self._avaliable = False
    
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def available(self):
        return self._avaliable