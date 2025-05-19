def guess_animal(guess,choice):
    global score
    attempt=0
    while True and attempt<3:
        
        if guess.lower()==choice:
            score=+1
            break
        else:
            if attempt<2:
                guess=input("sorry wrong answer , try again:")
            attempt=attempt+1
        if attempt==3:
            print("correct answer is ", choice)
score=0
guess1=input("Which animal lives at the north pole?")
guess_animal(guess1,"polar bear")
guess2=input("Which is the fastest animal?")
guess_animal(guess2,"cheetah")
guess3=input("which is the largest animal?")
guess_animal(guess3,"whale")
print("total score:" ,score)
