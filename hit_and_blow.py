import random as r

def pl():
    print("---------------------------------------------")

def make_list(n, t, u, v):
    listed = list()
    if n == 1:
        for i in range(t):
            listed.append(r.randint(u, v))
        return listed
    
    elif n == 2:
        for i in range(t):
            w = 1
            listed.append(0)
            while w == 1:
                w = 0
                m = r.randint(u, v)
                for k in listed:
                    if k == m:
                         w = 1
            else:
                listed[i] = m
        return listed
                

pl()
print("Hit & Blow")
pl()
print(">>> game rule <<<")
print("1. Normal / numbers duplicate")
print("2. Normal / numbers don't duplicate")
print("3. custum game")
pl()

while True:
    try:
        game_select = int(input("select rule: "))
        if game_select > 3 or game_select < 1:
            pl()
            print("Enter 1 or 2 or 3 !!!!")
            pl()
            continue
        else:
            break
    except:
        pl()
        print("Enter 1 or 2 or 3 !!!!")
        pl()
        continue

pl()
u = 1

if game_select != 3:
    n = game_select
    t = 4
    v = 6
else:
    while True:
        try:
            t = int(input("counts of number (10 > t > 0): "))
            if t > 9 or t < 1:
                print("error")
                continue
            else:
                break
        except:
            print("error")
            continue
    pl()
    while True:
        try:
            v = int(input("kinds of number (10 > v > 0): "))
            if v > 9 or v < 1:
                print("error")
                continue
            else:
                break
        except:
            print("error")
            continue
    pl()
    if v < t:
        n = 1
    else:
        while True:
            d = input("deplicate? y/n: ")
            if d == "y":
                n = 1
                pl()
                break
            elif d == "n":
                n = 2
                pl()
                break
            else:
                print("error")
                continue

print("counts: " + str(t))
print("kinds: " + str(v))
if n == 1:
    print("deplicate: yes")
else:
    print("depricate: no")
pl()
print(">>> game start!!! <<<")
pl()
e = 0
while e == 0:
    lista = make_list(n, t, u, v)
    liste = list()
    k = 0
    print("split by back slash ( / )")
    print("if you want to give up, please enter giveup")
    pl()
    while lista != liste:
        liste = list()
        hit = 0
        blow = 0
        input_a = input("answer: ").split("/")
        a = 0
        
        if input_a[0] == "giveup":
            print("you give up")
            print("it's answer: " + str(lista))
            pl()
            liste = list()
            for f in range(len(lista)):
                liste.append(lista[f])
            a = 1

        if len(lista) != len(input_a) and a == 0:
            print("counts are wrong")
            pl()
            continue

        if a == 0:
            try:
                for i in input_a:
                    liste.append(int(i))
            except:
                print("error")
                pl()
                continue
        
            k += 1
            seta = set()

            for i in range(len(lista)):
                seta.add(lista[i])
                if lista[i] == liste[i]:
                   hit += 1

            if hit == len(lista):
                print(">>> you win!! <<<")
                print("answer: "+ str(lista) + " / result: "+ str(k))
                continue

            else:
                for i in seta:
                    s = 0
                    o = 0
                    for g in range(len(lista)):
                        if i == liste[g]:
                            s += 1
                        if i == lista[g]:
                            o += 1
                    blow += min(s, o)
                blow -= hit
        
            print(str(k)+ ". " +str(hit)+" hit / " + str(blow) + " blow")
            pl()
            continue
    else:
        p = input("continue? y/n: ")
        if p == "y":
            pl()
            continue
        else:
            exit()