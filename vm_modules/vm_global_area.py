from . import vm_error

class GlobalArea:
    def __init__(self):
        self.items = {}
    
    def store(self, name, value):
        self.items[name] = value
    
    def load(self, name):
        if name not in self.items:
            raise vm_error.Error("ERROR_LOAD_FROM_EMPTY_GLOBAL_VAR")
        
        return self.items[name]


