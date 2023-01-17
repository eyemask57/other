import random as r
count = 0
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

while count < 3:
    count += 1
    print("s = " + str(count))
    input_han = input("select your number :")
    if is_int(input_han):
        pass
    else:
        continue
    input_hand = int(input_han)
    hand = input_hand % 3
    print("your hand is " + str(hand))
    z = r.randint(0,2)
    print("enemy's hand is " + str(z))
    if z == hand:
        print("retry!!")
        continue
    elif (z == 2 and hand == 1) or (z == 1 and hand == 0) or (z == 0 and hand == 2):
        print("You Lose!!!")
    else:
        print("You win!!!")
    I = input("continue ? y/N :")
    if count == 3:
        break
    if I == "y":
        continue
    elif I == "N":
        print("bye!!!")
        exit()
    else:
        continue
print("sorry, that's over...")
print("bye!!!")
exit()