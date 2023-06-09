from . import vm_error

class AddressSpace:
    def __init__(self):
        self.items = {}
    
    def store(self, name, value):
        self.items[name] = value
    
    def load(self, name):
        if name not in self.items:
            raise vm_error.Error("ERROR_LUNDEFINED_VAR")
        
        return self.items[name]


