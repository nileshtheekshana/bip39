f = open("english.txt", "r")
k = []

lent = int(input('how many letters in word: '))
fletter = input('what is first letter of word : ')
    

if lent==1:
    letter1= input('what is the fist letter')
    for i in f:
        if len(i)==lent+1:
            if i[0]==letter1:
                k.append(i)
                print(k)

if lent==2:
    letter1= input('what is the fist letter')
    letter2= input('what is the second letter')
    for i in f:
        if len(i)==lent+1:
            if i[0]==letter1:
                if i[1]==letter2:
                    k.append(i)
                    print(k)

if lent==3:
    fl= input('what is the fist letter')
    for i in f:
        if len(i)==lent+1:
            if i[0]==f1:
                k.append(i)
                print(k)

if lent==4:
    fl= input('what is the fist letter')
    for i in f:
        if len(i)==lent+1:
            if i[0]==f1:
                k.append(i)
                print(k)                

if lent==5:
    fl= input('what is the fist letter')
    for i in f:
        if len(i)==lent+1:
            if i[0]==f1:
                k.append(i)
                print(k)
if lent==6:
    fl= input('what is the fist letter')
    for i in f:
        if len(i)==lent+1:
            if i[0]==f1:
                k.append(i)
                print(k) 

if lent==7:
    fl= input('what is the fist letter')
    for i in f:
        if len(i)==lent+1:
            if i[0]==f1:
                k.append(i)
                print(k)                               