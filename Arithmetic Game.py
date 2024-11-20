import random

# This is the code for the addition portion of the alghorithm.
def addition_game(list_1,list_2):
    num_1=random.choice(list_1)
    num_2=random.choice(list_2)
    var = int(input("What is " + str(num_1) + "+" + str(num_2) + "? "))
    while (True):
        if var== num_1 + num_2:
            print("That is correct. Onto the next question!")
            break
        else:
            print("That is not the right answer. Move on to the next question.")
            var = int(input("Enter   again! What is " + str(num_1) + "+" + str(num_2) + "? "))
        
#This is the code for the subtraction portion of the algorithm
def subtraction_game(list_1, list_2):
    num_3=random.choice(list_1)
    num_4= random.choice(list_2)
    var = int(input("What is " + str(num_3) + "-" + str(num_4) + "? "))
    while (True):
        if var== num_3 - num_4:
            print("That is correct. Onto the next question!")
            break
        else:
            print("That is not the right answer.")
            var = int(input("Enter again! What is " + str(num_3) + "-" + str(num_4) + "? "))
#This is the code for the multiplication portion of the algorithm
def multiplication_game(list_3):
    num_4=random.choice(list_3)
    num_5= random.choice(list_3)
    var = int(input("What is " + str(num_4) + "*" + str(num_5) + "? "))
    while (True):
        if var== num_4 * num_5:
            print("That is correct. Onto the next question")
            break
        else:
            print("That is not the right answer. Try again.")
            var = int(input("Enter again! What is " + str(num_4) + "*" + str(num_5) + "? "))
#This is the code for the division portion of the algorithm     
def division_game(list_4, list_5):
    num_6=random.choice(list_4)
    num_7= random.choice(list_5)
    var = int(input("What is " + str(num_7) + "/" + str(num_6) + "? "))
    while (True):
        if var== num_7 / num_6:
            print("That is correct. Onto the next question!")
            break
        else:
            print("That is not the right answer.")
            var = int(input("Enter again! What is " + str(num_7) + "/" + str(num_6) + "? "))
#This is the final question. The question to end things off. 
def last_question():
    var=int(input("On a scale of 1 to 10, how did you like this game? "))
    if var>=7:
        print("Glad to hear it")
    else:
        print("Sorry to hear that")

#This is just a basic introduction to the game. 
print("Hello, welcome to my personal arithmetic game.")
print("You will be asked 8 questions")
print("PLEASE DO NOT USE A CALCULATOR!!!! A piece of paper or your head should only be used.")
print("Make sure you keep track of the question you got wrong. It will be important later.")


# These lists contain integers for the  addition and subtractions portion of the game. 
list_1=[41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80] 
list_2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40] 
#This list contains intergers for the multiplication portion of this assignment.
list_3=[1,2,3,4,5,6,7,8,9,10,11,12]
#These lists contain intergers for the division portion of this assignemnt. 
list_4=[1,2,4]
list_5=[4,8,12,16,24,72,76,96,100,44,40,88,84,80]

for i in range(2):
    addition_game(list_1,list_2)
    subtraction_game(list_1, list_2)
    multiplication_game(list_3)
    division_game(list_4, list_5)
    last_question()




















