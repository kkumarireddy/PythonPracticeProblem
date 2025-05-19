import random
lives=9
characters=["pizza","odd"]
s=random.choice(characters)
clue=list('?????')
heart_symbol=u'\u2764'
correctGuess=False
def update_clue(letter, clue, s):
    index=0
    while index<len(s):
        if letter==s[index]:
            clue[index]==letter
        index=index+1
while lives>0:
    print(clue)
    print(heart_symbol*lives)
    guess=input("guess a letter or whole word")
    if guess==s:
        correctGuess=True
        break
    if guess in s:
        update_clue(guess,clue,s)
    else:
        lives=lives-1
        print("incorrect , you lose life",lives)
if correctGuess:
    print("you won,the secret word:" ,s)
else:
    print("you lost, the secret word:",s)
