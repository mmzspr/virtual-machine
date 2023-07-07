from . import vm_error

class Stack:
    def __init__(self):
        self.items = [] # スタック要素
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.items:
            raise vm_error.Error("ERROR_POP_FROM_EMPTY_STACK")

        return self.items.pop()
    
    def is_empty(self):
        return not self.items
