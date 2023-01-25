import statistics as st
import math as ma


def check():
    while True:
        try:
            input_number = input(" 値の入力(終了時はfinを入力) :")
            if input_number == "fin":
                return "fin"
            else:
                float(input_number)
                return float(input_number)
        except ValueError:
            print("  *Error!!!")
            continue
#inputする装置と正しい値を入力していないときの判別装置
#正直に言うと小数でも入力できるようにした．
#finと入力したときのみ文字列"fin"を出力する．

def line():
    print("---------------------------------")
#見やすいようにラインを出力してくれるクソ関数

#ここから説明文
line()
print("平均値と標準偏差を出力するプログラム")
line()
print("データの入力")
line()
#ここまで説明文

li = []
#リストliの作成
#この中にデータを入力していく．

count = 0
while True: 
    print("[" + str(count + 1) + "個目]")
    deta = check()
    if deta == "fin":
        break
    else:
        li.append(deta)
        count += 1
#finと入力されるまで値をリストliに入力するループ
#データの今の個数が分かるようにした．

line()
print("データの個数 :" + str(count))
line()

av_li = sum(li) / count
print("平均値 :" + str(av_li))
#リストを足し合わせたものを個数で割った数を出力した

st_av_li = st.mean(li)
print("平均値(statistics) :" + str(st_av_li))
#statisticsのmean関数を用いて平均を出力した

print("平均の比較結果 :" + str(av_li == st_av_li))
#二つの平均が等しいかどうかの判別装置
#等しい場合はTrue, 等しくない場合はFalseを出力する．

line()

li2 = []
#リストli2の作成

for n in range(count):
    c = li[n] ** 2
    li2.append(c)
#リストli2にリストliの2乗を追加していく．

sx_li_2 = (sum(li2) / count) - (av_li ** 2)
#(2乗の平均) - (平均の2乗)で分散を定義
sx_li = ma.sqrt(sx_li_2)
#分散の平方根をとった
print("標準偏差 :" + str(sx_li))
#自力で求めた標準偏差を出力した

st_sx_li = st.pstdev(li)
print("標準偏差(statistics) :" + str(st_sx_li))
#statisticsのpstdev関数を用いた標準偏差を出力した

print("標準偏差の比較結果 :" + str(st_sx_li == sx_li))
#二つの標準偏差が等しいかどうかの判別装置
#等しい場合はTrue, 等しくない場合はFalseを出力する．

line()
i = input("Enter → exit :")
exit()