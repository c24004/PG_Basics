
import csv
n = [["トップガン","リスキービジネス","マイナリティーリポート"],["タイタニック","ザリベナント","インセプション"],["トレーニングデイ","マンオンファイアー","フライト"]]
with open("test4.csv","w") as f:
    w = csv.writer(f, delimiter = ",")
    for i in n:
        w.writerow(i)
