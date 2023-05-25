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
        self.instructions = self._parseLines(self.lines) # パース済み命令リスト
        self.stack = vm_stack.Stack() # スタック
    
    # ===== 実行 =====
    def run(self):

        pc = 0 # プログラムカウンタ
        while True:
            if pc >= len(self.instructions):
                 vm_error.index_error_pc(pc + 1)
            
            operand = self.instructions[pc]["operand"]
            opecode = self.instructions[pc]["opecode"]
            try:
                # オペランドに応じて実行
                match operand:
                    case "push":
                        self.cmd_push(opecode)
                    case "add":
                        self.cmd_add()
                    case "sub":
                        self.cmd_sub()
                    case "mul":
                        self.cmd_mul()
                    case "print":
                        self.cmd_print()
                    case "exit":
                        return
                    case _:
                        raise vm_error.Error("ERROR_UNDEFINED_OPCODE")
            except vm_error.Error as e:
                n_line = pc + 1       # 行番号
                code = self.lines[pc] # エラーが発生したコード
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
            pc+=1
    
    # ===== 構文解析 =====
    def _parseLines(self, lines):
        result = []
        if lines[-1] == "":
            lines = lines[:-1]

        for line in lines:
            data = line.split(" ")
            operand = data[0]
            opecode = [float(i) for i in data[1:]]
            result.append({"operand":operand, "opecode":opecode})
        return result
    

    # ==============================
    #          コマンド
    # ==============================
    def cmd_push(self, opcode):
        if len(opcode) == 0:
            raise vm_error.Error("ERROR_MISSING_OPERAND")
        self.stack.push(opcode[0])
    
    def cmd_add(self):
        x = self.stack.pop()
        y = self.stack.pop()
        self.stack.push(x + y)
    
    def cmd_sub(self):
        x = self.stack.pop()
        y = self.stack.pop()
        self.stack.push(x - y)
    
    def cmd_mul(self):
        x = self.stack.pop()
        y = self.stack.pop()
        self.stack.push(x * y)
    
    def cmd_print(self):
        x = self.stack.pop()
        print(x)