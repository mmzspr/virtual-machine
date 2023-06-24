# virtual-machine
Pythonで実装した仮想スタックマシン

# 実行
```
python main.py プログラムファイル名
```

# テスト
```
pytest test.py -v
```

# 命令セット
| 命令 | 説明 |
|------|------|
|push_int n| スタックにnをpush |
|push_float n| スタックにnをpush |
|push_char n| スタックにnをpush |
| add | スタックから2つpopして，加算した結果をpush |
| sub | スタックから2つpopして，減算した結果をpush |
| mul | スタックから2つpopして，乗算した結果をpush |
| div | スタックから2つpopして，除算した結果をpush |
| dup | スタックから1つpopして，2回push |
| store_global n| スタックから1つポップして，グローバル変数nに格納 |
| load_global n | グローバル変数nの値をスタックにプッシュ |
| store_local n| スタックから1つポップして，ローカル変数nに格納 |
| load_local n | ローカル変数nの値をスタックにプッシュ |
| print | スタックから1つpopして，画面に出力 |
| print_char | スタックから1つpopして，文字(ASCII)で画面に出力 |
| if_equal n|スタックから2つpopして，比較演算(==)が真であればn行目へジャンプ|
| if_greater n|スタックから2つpopして，比較演算(>)が真であればn行目へジャンプ|
| if_less n|スタックから2つpopして，比較演算(<)が真であればn行目へジャンプ|
| call n| リターンスタックにプログラムカウンタを格納，プログラムカウンタをnにしてサブルーチンを呼び出し |
| exit | リターンスタックにデータが存在する場合はサブルーチンを抜ける, そうでなければプログラム終了 |
| # | コメント(#から改行までの文字列を無視する) |

# ディレクトリ構成
    .
    ├── sample                  # 仮想スタックマシンで実行するサンプルコード
    ├── vm_modules              # 仮想スタックマシン関連のモジュール
    │   ├── virtual_machine.py      # 命令の解析・実行
    │   ├── vm_error.py             # エラー処理
    │   └── vm_stack                # スタック
    ├── main.py                 # プログラム実行用ファイル
    └── test.py                 # 単体テスト
    
