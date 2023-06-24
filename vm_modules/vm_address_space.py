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
    
    def store_array(self, name, index, value):
        self.items[name].store(index, value)
    
    def load_array(self, name, index):
        return self.items[name].load(index)

