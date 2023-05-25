# virtual-machine
Pythonで実装した仮想スタックマシン

# 命令セット
| 命令 | 説明 |
|------|------|
|push n| スタックにnをpush |
| add | スタックから2つpopして，加算した結果をpush |
| add | スタックから2つpopして，減算した結果をpush |
| mul | スタックから2つpopして，乗算した結果をpush |
| print | スタックから1つpopして，画面に出力 |
| exit | 終了 |

# 実行
```
python main.py プログラムファイル名
```

# テスト
```
pytest test.py -v
```
