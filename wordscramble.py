import random
print("Welcome to Word Scrambler")
while True:
    word=input("enter the word:")
    if word.lower()=="quit":
        break
    letters=list(word)
    random.shuffle(letters)
    print(f"shuffled: {''.join(letters)}")
    

