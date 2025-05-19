import random
import string

password=""
while True:
    adj=input("choose a adjective:")
    noun=input("choose a noun:")
    num=int(input("choose a number:"))
    for i in range (0,3,1):
        adjective=random.choice(adj)
        noun1=random.choice(noun)
        number=random.randint(0,num)
        chara=random.choice(string.punctuation)
        password=adjective+noun1+str(number)+chara
        print(password)
    a=input("wants anther passowrd (yes/no)?")
    if a.lower()=="yes":
        continue
    else:
        break
