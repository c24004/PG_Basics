
import random
def hangman(word):
    wrong = 0
    stages = ["",
              "|___|",
              "  |",
              "  |",
              "  |",
              "  |",
              "  |",
              "  |",
              " _|_",
              "|   |"
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ")
    print("".join(board))
    while wrong < len(stages) -1:
        print("\n")
        msg = "文字を予想してね :"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = None
        else:
            wrong += 1
        print(("".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print("".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print(f"あなたの負け！正解は{word}")

question = ["cat","dog","bird"]
i = random.randint(0,len(question))
hangman(question[i])
