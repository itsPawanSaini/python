print("Marvel Quiz Game")

playing=input("Do you want to play?\n")
if playing != 'yes':
    quit()

print("\nOkay! Let's play: \nBest of Luck\nScore 70% to win this game\n")

socre=0;

ans=input("\nHow many Infinity Stones are there?")
if ans=="6":
    print("Correct!")
    socre += 1;
else:
    print("Incorrect!")


ans=input("\nWho rescued Tony Stark and Nebula from space?")
if ans=="Captain Marvel" or ans=="captain marvel":
    print("Correct!")
    socre += 1;
else:
    print("Incorrect!")


ans=input("\nHawkeye has how many children?")
if ans=="3" or ans=="three" or ans=="Three":
    print("Correct!")
    socre += 1;
else:
    print("Incorrect!")


ans=input("\nWhat is Tony Stark’s daughter’s name?")
if ans=="Morgan Stark" or ans=="morgan stark":
    print("Correct!")
    socre += 1;
else:
    print("Incorrect!")


ans=input("\nThor played what video game in Avengers: Endgame?")
if ans=="Fortnite" or ans=="fortnite":
    print("Correct!")
    socre += 1;
else:
    print("Incorrect!")


ans=input("\nWho is the firstborn child of Odin?")
if ans=="Hela" or ans=="hela":
    print("Correct!")
    socre += 1;
else:
    print("Incorrect!")


ans=input("\nOn what planet was the Soul Stone in Infinity War?")
if ans=="Vormir" or ans=="vormir":
    print("\nCorrect!")
    socre += 1;
else:
    print("\nIncorrect!")


ans=input("\nWho is Tony Stark’s father?")
if ans=="Howard Stark" or ans=="howard stark":
    print("Correct!")
    socre += 1;
else:
    print("Incorrect!")


ans=input("\nWhere is Captain America from?")
if ans=="Brooklyn" or ans=="brooklyn":
    print("\nCorrect!")
    socre += 1;
else:
    print("\nIncorrect!")


ans=input("\nWhat is the real name of Black Widow?")
if ans=="Natasha Romanoff" or ans=="natasha romanoff":
    print("Correct!")
    socre += 1;
else:
    print("Incorrect!")


print("\nYou got "+str(socre)+" questions correct!")


if socre>= 7:
    print("\nWoohoo! You made it!")
    print("\nYou score "+str((socre/10)*100)+"%")
else:
    print("\nYou have to watch Marvel movies to pass this game")