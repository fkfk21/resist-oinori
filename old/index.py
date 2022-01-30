#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#これまで蓄積したデータを表示(会社名と評価の一覧)
import sys
import io
import sqlite3
import cgi

# データベースに接続する
conn = sqlite3.connect('sample.db')
c = conn.cursor()

htmlTable = ""

try:
   c.execute("select * from users;")
except sqlite3.Error as e:
   print("ERROR:", e.args[0])

rows = c.fetchall()

# データベースから値を取り出す
if not rows:
   htmlTable = "No Data"
else:
   for row in rows:
       htmlTable += str(row[0]) + "|" + str(row[1]) + "|" + str(row[2]) +"</br>"

c.close()

# 以下のコードを書かないと、htmlとして読み込んでもらえない。
print("Content-type: text/html; charset=utf-8")

# htmlの部分。printでHTMLコードを表示させることで、ブラウザがHTMLコードとして認識してくれる。
print(
(
'''
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title>企業一覧画面</title>
  </head>
  <body>


<h1>企業一覧</h1> <br> <br>

%s

  <a href="input.py">自分の企業評価を記入する</a>
  </body>
</html>
'''
) % htmlTable )