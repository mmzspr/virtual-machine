from vm_modules import virtual_machine
import pytest
# テスト実行コマンド
# pytest test.py -v

# ==============================
#          基本操作
# ==============================

# 型
def test_type(capsys):
    text = "push_float 1.5\n"\
           "push_int 2\n"\
           "push_char 65\n"\
           "print\n"\
           "print\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "A\n2\n1.5\n"
    assert exit_info.value.code == 0

# 出力
def test_print(capsys):
    text = "push_float 1\n"\
           "push_float 2\n"\
           "print\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "2.0\n1.0\n"
    assert exit_info.value.code == 0

# 改行
def test_newline(capsys):
    text = "push_float 1\n\n"\
           "push_float 2\n"\
           "print\n\n\n"\
           "print\n"\
           "exit\n\n\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "2.0\n1.0\n"
    assert exit_info.value.code == 0

# コメント
def test_comment(capsys):
    text = "push_float 1\n"\
           "  push_float   2   # test\n"\
           "  #    comment\n"\
           "#\n"\
           "print\n\n\n"\
           "print\n"\
           "exit\n\n\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "2.0\n1.0\n"
    assert exit_info.value.code == 0

# 文字として出力
def test_print_c(capsys):
    text = "push_float 10\n"\
           "push_float 111\n"\
           "push_float 108\n"\
           "push_float 108\n"\
           "push_float 101\n"\
           "push_float 72\n"\
           "print_char\n"\
           "print_char\n"\
           "print_char\n"\
           "print_char\n"\
           "print_char\n"\
           "print_char\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    print(out)
    assert out == "Hello\n"
    assert exit_info.value.code == 0

# 加算
def test_add(capsys):
    text = "push_float 1\n"\
           "push_float 2\n"\
           "add\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "3.0\n"
    assert exit_info.value.code == 0


# 減算
def test_sub(capsys):
    text = "push_float 3\n"\
           "push_float 5\n"\
           "sub\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "2.0\n"
    assert exit_info.value.code == 0


# 乗算
def test_mul(capsys):
    text = "push_float 7\n"\
           "push_float 3\n"\
           "mul\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "21.0\n"
    assert exit_info.value.code == 0

# 除算
def test_div(capsys):
    text = "push_float 2\n"\
           "push_float 10\n"\
           "div\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "5.0\n"
    assert exit_info.value.code == 0

# if 3 == 3
def test_if_equal1(capsys):
    text = "push_float 3\n"\
           "push_float 3\n"\
           "if_equal 6\n"\
           "push_float 1\n"\
           "print\n"\
           "push_float 2\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "2.0\n"
    assert exit_info.value.code == 0

# if 2 == 3
def test_if_equal2(capsys):
    text = "push_float 2\n"\
           "push_float 3\n"\
           "if_equal 6\n"\
           "push_float 1\n"\
           "print\n"\
           "push_float 2\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "1.0\n2.0\n"
    assert exit_info.value.code == 0

# if 5 > 3
def test_if_greater1(capsys):
    text = "push_float 3\n"\
           "push_float 5\n"\
           "if_greater 6\n"\
           "push_float 1\n"\
           "print\n"\
           "push_float 2\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "2.0\n"
    assert exit_info.value.code == 0

# if 2 > 3
def test_if_greater2(capsys):
    text = "push_float 3\n"\
           "push_float 2\n"\
           "if_greater 6\n"\
           "push_float 1\n"\
           "print\n"\
           "push_float 2\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "1.0\n2.0\n"
    assert exit_info.value.code == 0

# if 3 > 3
def test_if_greater2(capsys):
    text = "push_float 3\n"\
           "push_float 3\n"\
           "if_greater 6\n"\
           "push_float 1\n"\
           "print\n"\
           "push_float 2\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "1.0\n2.0\n"
    assert exit_info.value.code == 0


# if 2 < 3
def test_if_lessr1(capsys):
    text = "push_float 3\n"\
           "push_float 2\n"\
           "if_less 6\n"\
           "push_float 1\n"\
           "print\n"\
           "push_float 2\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "2.0\n"
    assert exit_info.value.code == 0

# if 5 < 3
def test_if_less2(capsys):
    text = "push_float 3\n"\
           "push_float 5\n"\
           "if_less 6\n"\
           "push_float 1\n"\
           "print\n"\
           "push_float 2\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "1.0\n2.0\n"
    assert exit_info.value.code == 0

# if 5 < 5
def test_if_less3(capsys):
    text = "push_float 5\n"\
           "push_float 5\n"\
           "if_less 6\n"\
           "push_float 1\n"\
           "print\n"\
           "push_float 2\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "1.0\n2.0\n"
    assert exit_info.value.code == 0

# ジャンプ
def test_if_jump(capsys):
    text = "push_float 1\n"\
           "print\n"\
           "jump 6\n"\
           "push_float 2\n"\
           "print\n"\
           "push_float 3\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "1.0\n3.0\n"
    assert exit_info.value.code == 0

# コピー
def test_if_dup(capsys):
    text = "push_float 0\n"\
           "push_float 1\n"\
           "add\n"\
           "dup\n"\
           "dup\n"\
           "print\n"\
           "push_float 5\n"\
           "if_equal 10\n"\
           "jump 2\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "1.0\n2.0\n3.0\n4.0\n5.0\n"
    assert exit_info.value.code == 0

# サブルーチン (スタックの先頭を二乗する)
def test_subroutine(capsys):
    text = "push_float 2\n"\
           "call 12\n"\
           "dup\n"\
           "print\n"\
           "call 12\n"\
           "dup\n"\
           "print\n"\
           "call 12\n"\
           "dup\n"\
           "print\n"\
           "exit\n"\
           "dup\n"\
           "mul\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

# サブルーチン (多重呼び出し)
def test_subroutine_multiple_call(capsys):
    text = "push_float 1\n"\
           "call 16\n"\
           "print\n"\
           "print\n"\
           "print\n"\
           "print\n"\
           "print\n"\
           "print\n"\
           "print\n"\
           "exit\n"\
           "push_float 3\n"\
           "call 20\n"\
           "push_float 5\n"\
           "push_float 6\n"\
           "exit\n"\
           "push_float 2\n"\
           "call 11\n"\
           "push_float 7\n"\
           "exit\n"\
           "push_float 4\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "7.0\n6.0\n5.0\n4.0\n3.0\n2.0\n1.0\n"
    assert exit_info.value.code == 0

# グローバル変数
def test_print(capsys):
    text = "push_float 0\n"\
           "store_global 0\n"\
           "push_float 1\n"\
           "store_global 1\n"\
           "push_float 2\n"\
           "store_global 2\n"\
           "push_float 3\n"\
           "store_global 3\n"\
           "load_global 1\n"\
           "load_global 3\n"\
           "load_global 0\n"\
           "load_global 2\n"\
           "print\n"\
           "print\n"\
           "print\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "2.0\n0.0\n3.0\n1.0\n"
    assert exit_info.value.code == 0

# ローカル変数
def test_local(capsys):
    text = "push_float 0\n"\
           "push_float 1\n"\
           "store_local 0\n"\
           "store_local 1\n"\
           "call 20\n"\
           "load_local 1\n"\
           "load_local 0\n"\
           "print\n"\
           "print\n"\
           "exit\n"\
           "\n"\
           "# === 12行目 === \n"\
           "push_float 3\n"\
           "push_float 4\n"\
           "store_local 1\n"\
           "store_local 0\n"\
           "exit\n"\
           "\n"\
           "# === 19行目 ===\n"\
           "push_float 2\n"\
           "store_local 0\n"\
           "call 13\n"\
           "load_local 0\n"\
           "print\n"\
           "exit\n"\
           
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "2.0\n1.0\n0.0\n"
    assert exit_info.value.code == 0

# グロ－バル配列変数
def test_array(capsys):
    text = "new_array_int 5\n"\
           "store_global 0\n"\
           "push_int 10\n"\
           "push_int 0\n"\
           "store_global_array 0\n"\
           "push_int 30\n"\
           "push_int 2\n"\
           "store_global_array 0\n"\
           "push_int 20\n"\
           "push_int 1\n"\
           "store_global_array 0\n"\
           "call 28\n"\
           "push_int 0\n"\
           "load_global_array 0\n"\
           "push_int 1\n"\
           "load_global_array 0\n"\
           "push_int 2\n"\
           "load_global_array 0\n"\
           "push_int 3\n"\
           "load_global_array 0\n"\
           "print\n"\
           "print\n"\
           "print\n"\
           "print\n"\
           "exit\n"\
           "\n"\
           "# === 27行目 ===\n"\
           "push_int 40\n"\
           "push_int 3\n"\
           "store_global_array 0\n"\
           "push_int 2\n"\
           "load_global_array 0\n"\
           "print\n"\
           "exit\n"

           
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "30\n40\n30\n20\n10\n"
    assert exit_info.value.code == 0

# ローカル配列変数
def test_local(capsys):
    text = "new_array_int 5\n"\
           "store_local 0\n"\
           "push_int 10\n"\
           "push_int 0\n"\
           "store_local_array 0\n"\
           "call 13\n"\
           "push_int 0\n"\
           "load_local_array 0\n"\
           "print\n"\
           "exit\n"\
           "\n"\
           "# === 12行目 === \n"\
           "new_array_int 5\n"\
           "store_local 0\n"\
           "push_int 8\n"\
           "push_int 0\n"\
           "store_local_array 0\n"\
           "push_int 0\n"\
           "load_local_array 0\n"\
           "print\n"\
           "exit"
     
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "8\n10\n"
    assert exit_info.value.code == 0
# ==============================
#          複合
# ==============================

# push_float[-2] -> push_float[-2, 3] -> push_float[-2, 3, 5] -> add[-2, 8]
# -> push_float[-2, 8, -1] -> mul[-2, -8] -> sub[-6] -> print[]
def test_mix(capsys):
    text = "push_float -2\n"\
           "push_float 3\n"\
           "push_float 5\n"\
           "add\n"\
           "push_float -1\n"\
           "mul\n"\
           "sub\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert out == "-6.0\n"
    assert exit_info.value.code == 0


# ==============================
#          エラー
# ==============================

_color_red = "\033[31m"
_color_reset = "\033[0m"

# 空のスタックからpop
def test_error_pop(capsys):
    text = "push_float 7\n"\
           "add\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert err == f"{_color_red}index error (pop from empty): line 2, \"add\"{_color_reset}\n"
    assert exit_info.value.code == 1


# 不明なオペコード
def test_error_undefined_opcode(capsys):
    text = "aaa 7\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert err == f"{_color_red}syntax error (undefined opcode): line 1, \"aaa 7\"{_color_reset}\n"
    assert exit_info.value.code == 1


# オペランドが不足
def test_error_missing_operand(capsys):
    text = "push_float 1\n"\
           "push_float\n"\
           "add\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert err == f"{_color_red}syntax error (missing operand): line 2, \"push_float\"{_color_reset}\n"
    assert exit_info.value.code == 1


# プログラムカウンタが範囲外
def test_error_pc_out_of_range(capsys):
    text = "push_float -1\n"\
           "push_float 7\n"\
           "sub\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert err == f"{_color_red}index error (program counter out of range): line 4{_color_reset}\n"
    assert exit_info.value.code == 1

# 定義されていないグローバル変数を参照
def test_error_undefined_global_variable(capsys):
    text = "push_float 1\n"\
           "store_global 0\n"\
           "load_global 1\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert err == f"{_color_red}syntax error (undefined variable): line 3, \"load_global 1\"{_color_reset}\n"
    assert exit_info.value.code == 1

# 定義されていないローカル変数を参照
def test_error_undefined_local_variable(capsys):
    text = "push_float 1\n"\
           "store_local 0\n"\
           "call 7\n"\
           "exit\n"\
           "\n"\
           "# === 6行目 ===\n"\
           "load_local 0\n"\
           "print\n"\
           "exit\n"
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert err == f"{_color_red}syntax error (undefined variable): line 7, \"load_local 0\"{_color_reset}\n"
    assert exit_info.value.code == 1

# 削除済みのローカル変数を参照
def test_error_undefined_local_variable_after_free(capsys):
    text = "push_int 1\n"\
           "store_local 0\n"\
           "free_local 0\n"\
           "load_local 0\n"\
           "print\n"\
           "exit\n"\
           "\n"
    
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert err == f"{_color_red}syntax error (undefined variable): line 4, \"load_local 0\"{_color_reset}\n"
    assert exit_info.value.code == 1

# 削除済みのグローバル変数を参照
def test_error_undefined_global_variable_after_free(capsys):
    text = "push_int 1\n"\
           "store_global 0\n"\
           "free_global 0\n"\
           "load_global 0\n"\
           "print\n"\
           "exit\n"\
           "\n"
    
    with pytest.raises(SystemExit) as exit_info:
        virtual_machine.run(text)

    out, err = capsys.readouterr()
    assert err == f"{_color_red}syntax error (undefined variable): line 4, \"load_global 0\"{_color_reset}\n"
    assert exit_info.value.code == 1
