from . import vm_error
from . import vm_stack
from . import vm_address_space
import re

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
        self.return_stack = vm_stack.Stack() # リターンスタック

        self.pc = -1 # プログラムカウンタ
        self.local_area_stack = vm_stack.Stack() # ローカル変数領域のスタック
        self.local_area = vm_address_space.AddressSpace() # ローカル変数領域
        self.global_area = vm_address_space.AddressSpace() # グローバル変数領域

    
    # ===== 実行 =====
    def run(self):
        
        while True:
            # プログラムカウンタを進める
            self.pc+=1

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
                    case "div":
                        self.cmd_div()
                    case "dup":
                        self.cmd_dup()
                    case "store_global":
                        self.cmd_store_global(opcode)
                    case "load_global":
                        self.cmd_load_global(opcode)
                    case "store_local":
                        self.cmd_store_local(opcode)
                    case "load_local":
                        self.cmd_load_local(opcode)
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
                    case "ERROR_LUNDEFINED_VAR":
                        vm_error.syntax_error_undefined_var(n_line, code)
                    case _:
                        vm_error.unknown_error(n_line, code)
    
    # ===== 構文解析 =====
    def _parseLines(self, lines):
        result = []
        if lines[-1] == "":
            lines = lines[:-1]

        for line in lines:
            line = re.sub(r"#.*","", line) # コメント除去
            data = line.split()

            operand = data[0] if len(data) else "" # オペランドがあれば取得
            opcode = [float(x) for x in data[1:] if x != ''] # オペコードがあれば取得
            result.append({"operand":operand, "opcode":opcode})
        return result
    

    # ==============================
    #          コマンド
    # ==============================
    def cmd_push(self, opcode):
        if len(opcode) == 0:
            raise vm_error.Error("ERROR_MISSING_OPERAND")
        self.data_stack.push(opcode[0])
    
    def cmd_store_global(self, opcode):
        if len(opcode) == 0:
            raise vm_error.Error("ERROR_MISSING_OPERAND")
        name = opcode[0]
        value = self.data_stack.pop()
        self.global_area.store(name, value)
    
    def cmd_load_global(self, opcode):
        if len(opcode) == 0:
            raise vm_error.Error("ERROR_MISSING_OPERAND")
        name = opcode[0]
        value = self.global_area.load(name)
        self.data_stack.push(value)
    
    def cmd_store_local(self, opcode):
        if len(opcode) == 0:
            raise vm_error.Error("ERROR_MISSING_OPERAND")
        name = opcode[0]
        value = self.data_stack.pop()
        self.local_area.store(name, value)
    
    def cmd_load_local(self, opcode):
        if len(opcode) == 0:
            raise vm_error.Error("ERROR_MISSING_OPERAND")
        name = opcode[0]
        value = self.local_area.load(name)
        self.data_stack.push(value)
    
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

    def cmd_div(self):
        x = self.data_stack.pop()
        y = self.data_stack.pop()
        self.data_stack.push(x / y)
    
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
        
        # メモリ領域確保
        self.local_area_stack.push(self.local_area)
        self.local_area = vm_address_space.AddressSpace()
        # プログラムカウンタ変更
        self.return_stack.push(self.pc)
        self.pc = int(opcode[0]) -2
    
    def cmd_exit(self):
        if self.return_stack.is_empty():
            exit(0)
        # 呼び出し前のメモリ領域に戻す
        self.local_area = self.local_area_stack.pop()
        # プログラムカウンタを戻す
        self.pc = self.return_stack.pop()