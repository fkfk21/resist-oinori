#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#input.pyで入力された情報を引き継いで表示
import cgi
import sys
import io
import sqlite3


#name属性を使って入力値を変数に代入してテーブルにデータの挿入ができるようにする。
form = cgi.FieldStorage()
name = form.getfirst('name','')
number = form.getfirst('number','')
note = form.getfirst('note','')

conn = sqlite3.connect('sample.db')
c = conn.cursor()

# データの挿入
c.execute('INSERT INTO users(namae,hyouka,riyu) VALUES(?,?,?)',[name, number, note])

# 挿入した結果を保存（コミット）する
conn.commit()

# データベースへのアクセスが終わったら close する
conn.close()

# 以下のコードを書かないと、htmlとして読み込んでもらえない。
print("Content-type: text/html; charset=utf-8")


# htmlの部分。printでHTMLコードを表示させることで、ブラウザがHTMLコードとして認識してくれる。

print(

"""
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>悪評入力フォーム</title>
</head>
<body>
<h3>確認</h3>
  <p>企業名</p>{0}<br>
  <p>評価</P>{1}<br>
  <p>評価理由</p>{2}<br>
  <p>こちらでよろしいでしょうか</p>
<a href = "complete.py"> 送信 </a>
</body>
</html>
"""
.format(name,number,note)
)