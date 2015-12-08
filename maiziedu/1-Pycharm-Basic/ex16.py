# break & continue example

number = 59

while True:
    guess = int(raw_input('Enter an integer: '))
    if guess == number:
        break
    if guess < number:
        print "No, the number is higher than that, keep guessing"
        continue
    else:
        print "No, the number is a  lower than that, keep guessing"
        continue
print "Bingo! you guessed it right."
print "but you do not win any prizes!"
print "Done"

# continue and pass difference

a_list = [0, 1, 2]
print("using continue:")
for i in a_list:
    if not i:
        continue
    print i
print("using pass:")
for i in a_list:
    if not i:
        pass
    print i