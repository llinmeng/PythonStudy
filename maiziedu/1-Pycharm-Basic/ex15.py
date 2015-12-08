# -*- coding: utf-8 -*-
number = 59
num_chances = 3
print "you have only 3 chances to guess"

for i in range(1, num_chances + 1):
    print("chance " + str(i))
    guess = int(raw_input("Enter an integer: "))
    if guess == number:
        print "Bingo! you guessed it right."
        print "but you do not win any prizes!"
        break
    elif guess < number:
        print "No, the number is higher than that, keep guessing, you have ' + str(num_chances - i) + ' chances left"
    else:
        print "No, the number is lower than that, keep guessing, you have ' + str(num_chances - i) + ' chances left"
print "Done"
