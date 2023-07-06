import os
import sys
from vm_modules import virtual_machine


# ==============================
#        メイン処理
# ==============================
def main():
    # 引数チェック
    if len(sys.argv) <= 1:
        print("ファイル名を指定してください")
        sys.exit(1)
    if os.path.exists(sys.argv[1]) == False:
        print(f"ファイルが存在しません: {sys.argv[1]}")
        sys.exit(1)
    
    if len(sys.argv) > 1:
        for arg in sys.argv[2:]:
            if arg == "-time":
                virtual_machine.time_flag = True
    
    file_path = sys.argv[1]

    # ファイル読み込み
    text = load_file(file_path)
    # 実行
    virtual_machine.run(text)


# ==============================
#       ファイル読み込み
# ==============================
def load_file(file_name):
    result = []
    with open(file_name, 'r', encoding="utf8") as f:
        result = f.read()
    return result

# 実行
if __name__ == '__main__':
    main()
