import random
name = input("What is your name?\n")
print(f"Welcome {name} to the Magic 8 Ball!")
q = input("What do you want to ask me?")
print(f"{name} ask: {q}")
randomnumber = random.randint(1,12)
if randomnumber == 1:
    print("Yes, defenitely")
elif randomnumber == 2:
    print("It is decidedly so.")
elif randomnumber == 3:
    print("Without a doubt.")
elif randomnumber == 4:
    print("Reply hazy, tray again.")
elif randomnumber == 5:
    print("Ask again later.")
elif randomnumber == 6:
    print("Better not tell you now.")
elif randomnumber == 7:
    print("My sources say No.")
elif randomnumber == 8:
    print("Outlook not so good.")
elif randomnumber == 9:
    print("Of course.")
elif randomnumber == 10:
    print("Certaintly.")
elif randomnumber == 11:
    print("Obviously. ;)")
elif randomnumber == 12:
    print("Obviously not.")
else:
    print("Very doubtful")
