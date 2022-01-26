# This is the Magic 8-Ball, a program for telling fortune

import random

print("You are in front of the Magic Ball and are allowed to ask one question")

name = input("What is your name?: ")
question = input("What is your question for the Magic Ball? (Only Y/N questions): ")
answer = ""

print(name + " asks: " + question)
print("The Magic 8-Ball answers: ", answer)

random_number = random.randint(1, 9)
#print(random_number)

if question != "":
  if random_number == 1:
    answer = "Yes - definitely"
    print(answer)
  elif random_number == 2:
    answer = "It is decidedly so"
    print(answer)
  elif random_number == 3:
    answer = "Without a doubt"
    print(answer)
  elif random_number == 4:
    answer = "Reply hazy, try again"
    print(answer)
  elif random_number == 5:
    answer = "Ask again later"
    print(answer)
  elif random_number == 6:
    answer = "Better not tell you now"
    print(answer)
  elif random_number == 7:
    answer = "My sources say no"
    print(answer)
  elif random_number == 8:
    answer = "Outlook not so good"
    print(answer)
  elif random_number == 9:
    answer = "Very doubtful"
    print(answer)
  else:
    answer = "An error ocurred"
else:
  print(name + ", you did not enter a question!")
