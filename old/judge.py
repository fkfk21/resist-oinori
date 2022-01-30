#お祈りメール判定
#メール本文（string）を入力し、判定（bool）を返す

def oinori_judge(text):
    threshold = 3
    point = text.count('応募') + 3*text.count('お祈り') + text.count('せっかく') + text.count('落選') + text.count('申し訳') + text.count('活躍') + 2*text.count('ご縁') + text.count('慎重に') + 2*text.count('ご希望に') + text.count('残念') + 2*text.count('見送らせて') + text.count('見合わせ') + text.count('添いかねる') + text.count('添えない') + text.count('添えず')
    if point > threshold:
        return True
    else:
        return False