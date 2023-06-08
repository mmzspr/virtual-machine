from vm_modules import virtual_machine
import pytest
# テスト実行コマンド
# pytest test.py -v

# ==============================
#          基本操作
# ==============================
# 出力
def test_print(capsys):
    text = "push 1\n"\
           "push 2\n"\
           "print\n"\
           "print\n"\
           "exit\n"
    virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert out == "2.0\n1.0\n"

# 文字として出力
def test_print_c(capsys):
    text = "push 10\n"\
           "push 111\n"\
           "push 108\n"\
           "push 108\n"\
           "push 101\n"\
           "push 72\n"\
           "print_char\n"\
           "print_char\n"\
           "print_char\n"\
           "print_char\n"\
           "print_char\n"\
           "print_char\n"\
           "exit\n"
    virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert out == "Hello\n"

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

# if 3 == 3
def test_if_equal1(capsys):
    text = "push 3\n"\
           "push 3\n"\
           "if_equal 6\n"\
           "push 1\n"\
           "print\n"\
           "push 2\n"\
           "print\n"\
           "exit\n"
    virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert out == "2.0\n"

# if 2 == 3
def test_if_equal2(capsys):
    text = "push 2\n"\
           "push 3\n"\
           "if_equal 6\n"\
           "push 1\n"\
           "print\n"\
           "push 2\n"\
           "print\n"\
           "exit\n"
    virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert out == "1.0\n2.0\n"

# if 5 > 3
def test_if_greater1(capsys):
    text = "push 3\n"\
           "push 5\n"\
           "if_greater 6\n"\
           "push 1\n"\
           "print\n"\
           "push 2\n"\
           "print\n"\
           "exit\n"
    virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert out == "2.0\n"

# if 2 > 3
def test_if_greater2(capsys):
    text = "push 3\n"\
           "push 2\n"\
           "if_greater 6\n"\
           "push 1\n"\
           "print\n"\
           "push 2\n"\
           "print\n"\
           "exit\n"
    virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert out == "1.0\n2.0\n"

# if 3 > 3
def test_if_greater2(capsys):
    text = "push 3\n"\
           "push 3\n"\
           "if_greater 6\n"\
           "push 1\n"\
           "print\n"\
           "push 2\n"\
           "print\n"\
           "exit\n"
    virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert out == "1.0\n2.0\n"


# if 2 < 3
def test_if_lessr1(capsys):
    text = "push 3\n"\
           "push 2\n"\
           "if_less 6\n"\
           "push 1\n"\
           "print\n"\
           "push 2\n"\
           "print\n"\
           "exit\n"
    virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert out == "2.0\n"

# if 5 < 3
def test_if_less2(capsys):
    text = "push 3\n"\
           "push 5\n"\
           "if_less 6\n"\
           "push 1\n"\
           "print\n"\
           "push 2\n"\
           "print\n"\
           "exit\n"
    virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert out == "1.0\n2.0\n"

# if 5 < 5
def test_if_less3(capsys):
    text = "push 5\n"\
           "push 5\n"\
           "if_less 6\n"\
           "push 1\n"\
           "print\n"\
           "push 2\n"\
           "print\n"\
           "exit\n"
    virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert out == "1.0\n2.0\n"

# ジャンプ
def test_if_jump(capsys):
    text = "push 1\n"\
           "print\n"\
           "jump 6\n"\
           "push 2\n"\
           "print\n"\
           "push 3\n"\
           "print\n"\
           "exit\n"
    virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert out == "1.0\n3.0\n"

# コピー
def test_if_dup(capsys):
    text = "push 0\n"\
           "push 1\n"\
           "add\n"\
           "dup\n"\
           "dup\n"\
           "print\n"\
           "push 5\n"\
           "if_equal 10\n"\
           "jump 2\n"\
           "exit\n"
    virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert out == "1.0\n2.0\n3.0\n4.0\n5.0\n"

# サブルーチン
def test_subroutine(capsys):
    text = "push 2\n"\
           "call 13\n"\
           "dup\n"\
           "print\n"\
           "call 13\n"\
           "dup\n"\
           "print\n"\
           "call \n"\
           "dup\n"\
           "print\n"\
           "exit\n"\
           "\n"\
           "dup\n"\
           "mul\n"\
           "exit\n"
    virtual_machine.run(text)
    out, err = capsys.readouterr()
    assert out == "2.0\n4.0\n8.0\n"
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