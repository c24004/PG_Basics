x = [2,4,6,8]
while True:
    n = input(":")
    try:
        n = int(n)
        if n in x:
            print("正解")
        else:
            print("不正解")
    except ValueError:
        if n == "q":
            break
        else:
            print("数字を入力するか、qで終了します")
        

