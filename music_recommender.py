import random
print("MUSIC RECOMMENDER")
genres={
    "rock":["taylor","queen"],
    "pop":["sound ","pop"]
}
choice=input("Enter your choice(rock/pop):")
if choice not in genres:
    print("sorry we dont have it")
else:
    print("try it {}".format(random.choice(genres.get(choice))))
