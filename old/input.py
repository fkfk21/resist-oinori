#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 以下のコードを書かないと、htmlとして読み込んでもらえない。
#入力画面とデータベースの作成
print("Content-type: text/html; charset=utf-8")

print(

"""
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>悪評入力フォーム</title>
</head>

<body>
    入力フォーム<br> <br>
    <form name="form" method="post" action="confirm.py">
      企業名:<br>
        <input type="text" name="name"  required>＊必須項目 <br> <br>
      評価(1~10):<br>
        <input type="number" name="number" placeholder="半角数字" required>＊必須項目<br> <br>
      評価理由:<br>
        <textarea name="note" value=""></textarea>
        <br> <br>
      <input type="submit" value="確認">
    </form>
</body>
</html>
"""
)


import sys
import io
import sqlite3
import cgi

# windowsにおける文字化け回避
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# データベースに接続する
#データベースファイルを作る
conn = sqlite3.connect('sample.db')
#カーソルを作成する
c = conn.cursor()

# テーブルの作成
c.execute('CREATE TABLE IF NOT EXISTS users (namae text, hyouka integer, riyu text);')
