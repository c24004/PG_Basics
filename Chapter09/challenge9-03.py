import csv
n = [["Top Gun","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]
with open("test3.csv","w") as f:
    w = csv.writer(f, delimiter = ",")
    for i in n:
        w.writerow(i)
