from . import vm_error

class Array:
    def __init__(self, array_type, size):
        self.items = [0] * size
        self.type = array_type
    
    def store(self, index, value):
        if type(value) is not self.type:
            raise vm_error.Error("ERROR_MISMATCHING_ARRAY_TYPE")
        self.items[index] = value
    
    def load(self, index):    
        return self.items[index]


