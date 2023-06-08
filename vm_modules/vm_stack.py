from . import vm_error

class Stack:
    def __init__(self):
        self.items = [] # スタック要素
        self.sp = -1    # スタックポインタ
    
    def push(self, item):
        self.sp += 1
        if self.sp == len(self.items):
            self.items.append(item)
        else:
            self.items[self.sp] = item
    
    def pop(self):
        if self.sp == -1:
            raise vm_error.Error("ERROR_POP_FROM_EMPTY_STACK")
        
        result = self.items[self.sp]
        self.sp -= 1
        return result
    
    def is_empty(self):
        return self.sp == -1
