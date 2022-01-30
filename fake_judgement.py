#疑似メールアドレス判定
#メールアドレス（string）を入力し、判定（bool）を返す

class FakeJudgement:
    #セミコロン内のアドレスは適当に作成したものなので、実際に使用する疑似返信用メールアドレスに変更する必要がある。
    fake_address = "fake@m.titech.ac.jp" 
    bad_words = []
    def __init__(self, fake_address):
        # 疑似返信用のアドレス
        self.fake_address = fake_address
        # 本文判定用の設定
        self.bad_threshold = 4
        self.bad_words.append( (2,'落とした') )
        self.bad_words.append( (2,'台無し') )
        self.bad_words.append( (2,'見る目') )
        self.bad_words.append( (2,'許さない') )
        self.bad_words.append( (3,'許さない') )
        self.bad_words.append( (3,'ごみ') )
        self.bad_words.append( (3,'ゴミ') )
        self.bad_words.append( (5,'死ね') )
        self.bad_words.append( (5,'しね') )
        self.bad_words.append( (5,'シネ') )
        self.bad_words.append( (5,'ボケ') )
        self.bad_words.append( (5,'頭悪い') )
        self.bad_words.append( (5,'許せん') )
        self.bad_words.append( (5,'クズ') )
        self.bad_words.append( (5,'クソ') )

    # fakeアドレスからであればTrue
    def judge_from_address(self, target_address):
        return target_address == self.fake_address
    
    # 本文の内容がやばそうだったら止める
    def judge_from_body(self, body_text):
        point = 0
        for p, word in self.bad_words:
            point += p*body_text.count(word)
        return point > self.bad_threshold

