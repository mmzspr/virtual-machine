# virtual-machine
Pythonで実装した仮想スタックマシン

# 命令セット
| 命令 | 説明 |
|------|------|
|push n| スタックにnをpush |
| add | スタックから2つpopして，加算した結果をpush |
| sub | スタックから2つpopして，減算した結果をpush |
| mul | スタックから2つpopして，乗算した結果をpush |
| copy | スタックから1つpopして，2回push |
| print | スタックから1つpopして，画面に出力 |
| print_char | スタックから1つpopして，文字(ASCII)で画面に出力 |
| if_equal n|スタックから2つpopして，比較演算(==)が真であればn行目へジャンプ|
| if_greater n|スタックから2つpopして，比較演算(>)が真であればn行目へジャンプ|
| if_lesss n|スタックから2つpopして，比較演算(<)が真であればn行目へジャンプ|
| jump n | n行目へジャンプ |
| exit | 終了 |

# 実行
```
python main.py プログラムファイル名
```

# テスト
```
pytest test.py -v
```
