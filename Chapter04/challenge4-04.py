def numberA(numX):
    """
    この関数は、整数を引数として受け取り、その整数を２で割る。
    その結果を出力してプログラムに返す。
    引数：numX
    戻り値：numXを２で割ったもの
    """
    return numX // 2
def numberB(numY):
    """
    この関数は、整数を引数として受け取り、その整数を４でかける。
    その結果を出力してプログラムに返す。
    引数：numY
    戻り値：numYを４でかけた数
    """
    return numY * 4
numberC = numberA(6)
print(numberB(numberC))

