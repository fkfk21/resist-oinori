#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#登録完了を表示
import sqlite3
import csv
import sys
import io
import cgi

# windowsにおける文字化け回避
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# 使用するデータベースを指定
db_path = "sample.db"

# sample.dbを使ってsqlite3を起動
con = sqlite3.connect("sample.db")

# 属性名で値を取り出すように設定
con.row_factory = sqlite3.Row

# カーソル(sqlでデータベースを操作するやつ)を作成
cur = con.cursor()

htmlText = ""


# 以下sqlの実行
try:
   cur.execute(
       "create table sampleTable(id integer primary key autoincrement, name text);"
   )
except sqlite3.Error as e:
   print("ERROR:", e.args[0])

try:
   cur.execute("insert into sampleTable(name)values('test');")
except sqlite3.Error as e:
   print("ERROR:", e.args[0])

try:
   cur.execute("select * from sampleTable;")
except sqlite3.Error as e:
   print("ERROR:", e.args[0])

rows = cur.fetchall()

# データベースから値を取り出す
if not rows:
   htmlText = "No Data"
else:
   for row in rows:
       if str(row["id"]):
           htmlText += str(row[0]) + "|" + str(row[1]) + "</br>"


# 以下のコードを書かないと、htmlとして読み込んでもらえない。
print("Content-type: text/html; charset=utf-8")


# htmlの部分。printでHTMLコードを表示させることで、ブラウザがHTMLコードとして認識してくれる。
#
print(

    """
     <html>
       <head>
           <meta http-equiv=\"Content-Type\" content=\ "text/html
           charset=utf-8\" / >
           <meta charset="utf-8">
           <title>入力完了</title>
       </head>
       <body>
          <h1>入力完了</h1>
          <h5>登録が完了しました。</h5>
          <br/>
          <p>ありがとうございました！</p>
              <a href="index.py">企業一覧へ</a>
       </body>
     </html>
  """
   ) 