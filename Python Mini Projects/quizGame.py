print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
        
print("Okay! let's play :)")
score = 0


answer = input("What does CPU stands for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score = score + 1
else:
    print("You are wrong!")
    
answer = input("What does GPU stands for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score = score + 1
else:
    print("You are wrong!")
    
answer = input("What does RAM stands for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score = score + 1
else:
    print("You are wrong!")
    

answer = input("What does PSU stands for? ").lower()
if answer == "power supply":
    print("Correct!")
    score = score + 1
else:
    print("You are wrong!")

print("You got " + str(score) + " questions correct!")
