from vm_modules import virtual_machine
import pytest
# テスト実行コマンド
# pytest test.py -v

# ==============================
#          基本操作
# ==============================

# 加算
def test_add(capsys):
    text = "push 1\n"\
           "push 2\n"\
           "add\n"\
           "print\n"\
           "exit\n"
    virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert out == "3.0\n"


# 減算
def test_sub(capsys):
    text = "push 3\n"\
           "push 5\n"\
           "sub\n"\
           "print\n"\
           "exit\n"
    virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert out == "2.0\n"


# 乗算
def test_mul(capsys):
    text = "push 7\n"\
           "push 3\n"\
           "mul\n"\
           "print\n"\
           "exit\n"
    virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert out == "21.0\n"


# ==============================
#          複合
# ==============================

# push[-2] -> push[-2, 3] -> push[-2, 3, 5] -> add[-2, 8]
# -> push[-2, 8, -1] -> mul[-2, -8] -> sub[-6] -> print[]
def test_mix(capsys):
    text = "push -2\n"\
           "push 3\n"\
           "push 5\n"\
           "add\n"\
           "push -1\n"\
           "mul\n"\
           "sub\n"\
           "print\n"\
           "exit\n"
    virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert out == "-6.0\n"


# ==============================
#          エラー
# ==============================

_color_red = "\033[31m"
_color_reset = "\033[0m"

# 空のスタックからpop
def test_error_pop(capsys):
    text = "push 7\n"\
           "add\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit):
        virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert err == f"{_color_red}index error (pop from empty): line 2, \"add\"{_color_reset}\n"


# 不明なオペコード
def test_error_undefined_opcode(capsys):
    text = "aaa 7\n"\
           "exit\n"
    with pytest.raises(SystemExit):
        virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert err == f"{_color_red}syntax error (undefined opcode): line 1, \"aaa 7\"{_color_reset}\n"


# オペランドが不足
def test_error_missing_operand(capsys):
    text = "push 1\n"\
           "push\n"\
           "add\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit):
        virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert err == f"{_color_red}syntax error (missing operand): line 2, \"push\"{_color_reset}\n"


# プログラムカウンタが範囲外
def test_error_pc_out_of_range(capsys):
    text = "push -1\n"\
           "push 7\n"\
           "sub\n"
    with pytest.raises(SystemExit):
        virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert err == f"{_color_red}index error (program counter out of range): line 4{_color_reset}\n"