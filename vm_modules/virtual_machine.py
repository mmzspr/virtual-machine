from . import vm_error
from . import vm_stack

__all__ = ["run"]


# ==============================
#     バーチャルマシン実行
# ==============================
def run(text):
    virtual_machine = VirtualMachine(text)
    virtual_machine.run()


# ==============================
#    バーチャルマシン内部処理
# ==============================
class VirtualMachine:

    # ===== 初期化 =====
    def __init__(self, text):
        self.lines = text.split("\n") # 改行区切りのリスト
        self.progmem = self._parseLines(self.lines) # パース済み命令リスト
        self.data_stack = vm_stack.Stack() # スタック
        self.return_stack = vm_stack.Stack() # スタック
        self.pc = 0 # プログラムカウンタ
    
    # ===== 実行 =====
    def run(self):
        while True:
            if self.pc >= len(self.progmem):
                 vm_error.index_error_pc(self.pc + 1)
            
            operand = self.progmem[self.pc]["operand"]
            opcode = self.progmem[self.pc]["opcode"]
            try:
                # オペランドに応じて実行
                match operand:
                    case "":
                        pass
                    case "push":
                        self.cmd_push(opcode)
                    case "add":
                        self.cmd_add()
                    case "sub":
                        self.cmd_sub()
                    case "mul":
                        self.cmd_mul()
                    case "dup":
                        self.cmd_dup()
                    case "print":
                        self.cmd_print()
                    case "print_char":
                        self.cmd_print_char()
                    case "if_equal":
                        self.cmd_if_equal(opcode)
                    case "if_greater":
                        self.cmd_if_greater(opcode)
                    case "if_less":
                        self.cmd_if_less(opcode)
                    case "jump":
                        self.cmd_jump(opcode)
                    case "call":
                        self.cmd_call(opcode)
                    case "exit":
                        self.cmd_exit()
                    case _:
                        raise vm_error.Error("ERROR_UNDEFINED_OPCODE")
            except vm_error.Error as e:
                n_line = self.pc + 1       # 行番号
                code = self.lines[self.pc] # エラーが発生したコード
                match e.args[0]:
                    case "ERROR_POP_FROM_EMPTY_STACK":
                        vm_error.index_error_pop(n_line, code)
                    case "ERROR_MISSING_OPERAND":
                        vm_error.syntax_error_missing_operand(n_line, code)
                    case "ERROR_UNDEFINED_OPCODE":
                        vm_error.syntax_error_undefined_opcode(n_line, code)
                    case _:
                        vm_error.unknown_error(n_line, code)
            
            # プログラムカウンタを進める
            self.pc+=1
    
    # ===== 構文解析 =====
    def _parseLines(self, lines):
        result = []
        if lines[-1] == "":
            lines = lines[:-1]

        for line in lines:
            data = line.split(" ")
            operand = data[0]
            opcode = [float(i) for i in data[1:]]
            result.append({"operand":operand, "opcode":opcode})
        return result
    

    # ==============================
    #          コマンド
    # ==============================
    def cmd_push(self, opcode):
        if len(opcode) == 0:
            raise vm_error.Error("ERROR_MISSING_OPERAND")
        self.data_stack.push(opcode[0])
    
    def cmd_add(self):
        x = self.data_stack.pop()
        y = self.data_stack.pop()
        self.data_stack.push(x + y)
    
    def cmd_sub(self):
        x = self.data_stack.pop()
        y = self.data_stack.pop()
        self.data_stack.push(x - y)
    
    def cmd_mul(self):
        x = self.data_stack.pop()
        y = self.data_stack.pop()
        self.data_stack.push(x * y)

    def cmd_dup(self):
        x = self.data_stack.pop()
        self.data_stack.push(x)
        self.data_stack.push(x)
    
    def cmd_if_equal(self, opcode):
        if len(opcode) == 0:
            raise vm_error.Error("ERROR_MISSING_OPERAND")
        x = self.data_stack.pop()
        y = self.data_stack.pop()
        if x == y:
            self.pc = int(opcode[0]) -2
    
    def cmd_if_greater(self, opcode):
        if len(opcode) == 0:
            raise vm_error.Error("ERROR_MISSING_OPERAND")
        x = self.data_stack.pop()
        y = self.data_stack.pop()
        if x > y:
            self.pc = int(opcode[0]) -2
    
    def cmd_if_less(self, opcode):
        if len(opcode) == 0:
            raise vm_error.Error("ERROR_MISSING_OPERAND")
        x = self.data_stack.pop()
        y = self.data_stack.pop()
        if x < y:
            self.pc = int(opcode[0]) -2
    
    def cmd_jump(self, opcode):
        if len(opcode) == 0:
            raise vm_error.Error("ERROR_MISSING_OPERAND")
        self.pc = int(opcode[0]) -2
    
    def cmd_print(self):
        x = self.data_stack.pop()
        print(x)
    
    def cmd_print_char(self):
        x = self.data_stack.pop()
        print(chr(int(x)), end="")
    
    def cmd_call(self, opcode):
        if len(opcode) == 0:
            raise vm_error.Error("ERROR_MISSING_OPERAND")
        self.return_stack.push(self.pc)
        self.pc = int(opcode[0]) -2
    
    def cmd_exit(self):
        if self.return_stack.is_empty():
            exit(0)
        self.pc = self.return_stack.pop()
