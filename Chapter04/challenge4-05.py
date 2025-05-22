def chara_str(c):
    chara = float(c)
    """
    この関数は、文字列を浮動小数点数に変換する。
    その結果を出力してプログラムに返す。
    例外処理として、ValueError の時にメッセージを出力してプログラムに返す。
    """
    return chara
try:
    f = chara_str("1")
    print(f)
except ValueError:
    print("数字入れて")

