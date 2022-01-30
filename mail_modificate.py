import sqlite3
import sys
import io

class AccessDB:
    def __init__(self, db_name):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        self.db = sqlite3.connect(db_name) # 'sample.db'
        self.cursor = self.db.cursor()
    
    def __del__(self):
        self.cursor.close()

    def get_input_html(self):
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
        # テーブルの作成
        self.cursor.execute('CREATE TABLE IF NOT EXISTS users (namae text, hyouka integer, riyu text);')
        self.db.commit()


    def get_confirm_html(self):
        self.db.row_factory = sqlite3.Row
        htmlText = ""
        # 以下sqlの実行
        try:
            self.cursor.execute(
            "create table sampleTable(id integer primary key autoincrement, name text);"
            )
        except sqlite3.Error as e:
            print("ERROR:", e.args[0])

        try:
            self.cursor.execute("insert into sampleTable(name)values('test');")
        except sqlite3.Error as e:
            print("ERROR:", e.args[0])

        try:
            self.cursor.execute("select * from sampleTable;")
        except sqlite3.Error as e:
            print("ERROR:", e.args[0])

        rows = self.cursor.fetchall()

        # データベースから値を取り出す
        if not rows:
            htmlText = "No Data"
        else:
            for row in rows:
                if str(row["id"]):
                    htmlText += str(row[0]) + "|" + str(row[1]) + "</br>"
        self.db.commit()

        # 以下のコードを書かないと、htmlとして読み込んでもらえない。
        print("Content-type: text/html; charset=utf-8")

        # htmlの部分。printでHTMLコードを表示させることで、ブラウザがHTMLコードとして認識してくれる。
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
    

    def get_bad_reputation_html(self):
        htmlTable = ""
        try:
            self.cursor.execute("select * from users;")
        except sqlite3.Error as e:
            print("ERROR:", e.args[0])

        rows = self.cursor.fetchall()

        # データベースから値を取り出す
        if not rows:
            htmlTable = "No Data"
        else:
            for row in rows:
                htmlTable += str(row[0]) + "|" + str(row[1]) + "|" + str(row[2]) +"</br>"

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


class MailModificator:
    oinori_words = []
    convert_format = []
    def __init__(self):
        # お祈り判定用の設定
        self.oinori_threshold = 3
        self.oinori_words.append( (1, '応募') )
        self.oinori_words.append( (1, 'せっかく') )
        self.oinori_words.append( (1, '落選') )
        self.oinori_words.append( (1, '申し訳') )
        self.oinori_words.append( (1, '活躍') )
        self.oinori_words.append( (1, '残念') )
        self.oinori_words.append( (1, '慎重に') )
        self.oinori_words.append( (1, '見合わせ') )
        self.oinori_words.append( (1, '添いかねる') )
        self.oinori_words.append( (1, '添えない') )
        self.oinori_words.append( (1, '添えず') )
        self.oinori_words.append( (2, 'ご縁') )
        self.oinori_words.append( (2, 'ご希望に') )
        self.oinori_words.append( (2, '見送らせて') )
        self.oinori_words.append( (3, 'お祈り') )
        self.oinori_words.append( (3, '不合格') )
        # 改変後の文章パターン: {}に社名
        # pattern 1
        self.convert_format.append(
            "よお、元気か？\n" \
            "\nこないだお前が受けた{}だけど\n" \
            "残念ながら不合格だってさ\n" \
            "ドンマイドンマイ\n" \
            "\nまあ、企業なんて星の数だけあるんだから気にすんな\n" \
            "切り替えてけ\n"
        )
        # pattern 2
        self.convert_format.append(
            "{}の選考結果：不合格\n"
        )
        # pattern 3
        self.convert_format.append(
            "よお、元気か？\n" \
            "\nこないだお前が受けた{}だけど\n" \
            "不合格だってさ、見る目ねぇよな\n" \
            "\nでも正直応募しただけ偉い！！\n" \
            "\nというかもう生きてるだけで偉い！！！！\n" 
        ) 

    def is_oinori_mail(self, text):
        point = 0
        for p, word in self.oinori_words:
            point += p*text.count(word)
        return point > self.oinori_threshold

    # 差出人、本文のいずれかから会社名を抽出
    def extract_company_name(from_addr, body_text):
        # 差出人の中から社名取得
        target=' '
        if(target in from_addr):
            idx=from_addr.find(target) #空白位置を取得
            name=from_addr[:idx] #空白より前の部分を取得(社名) 
        # 本文の中から社名取得
        # name = body_text
        return name

    # 文面作成関数(入力：変換パターン番号、差出人、本文)
    def convert(self, pattern, from_addr, body_text):
        # 社名取得
        company_name = self.extract_company_name(from_addr, body_text)

        #本文書き換え
        body = self.convert_format[pattern].format(company_name)
        return body #出力：本文
