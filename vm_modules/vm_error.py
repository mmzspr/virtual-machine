import sys

_color_red = "\033[31m"
_color_reset = "\033[0m"

# 例外発生に用いるクラス
class Error(Exception):
    pass

# エラーメッセージを出力して終了
def _error(text):
    print(f"{_color_red}{text}{_color_reset}", file=sys.stderr)
    # print(text, file=sys.stderr)
    sys.exit(1)

# ====================
#     エラーリスト
# ====================
# 不明なオペコード
def syntax_error_undefined_opcode(n_line, code):
    _error(f"syntax error (undefined opcode): line {n_line}, \"{code}\"")

# オペランドが不足
def syntax_error_missing_operand(n_line, code):
    _error(f"syntax error (missing operand): line {n_line}, \"{code}\"")

# 宣言されていない変数を参照
def syntax_error_undefined_var(n_line, code):
    _error(f"syntax error (undefined variable): line {n_line}, \"{code}\"")

# 空のスタックからpop
def index_error_pop(n_line, code):
    _error(f"index error (pop from empty): line {n_line}, \"{code}\"")

# プログラムカウンタが範囲外
def index_error_pc(n_line):
    _error(f"index error (program counter out of range): line {n_line}")

def syntax_error_mismatching_array_type(n_line, code):
    _error(f"syntax error (mismatching array type): line {n_line}, \"{code}\"")

# 不明なエラー
def unknown_error(n_line, code):
    _error(f"unknown error: line {n_line} \"{code}\"")
