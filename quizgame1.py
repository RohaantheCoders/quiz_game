#quiz game

import quizgame2

while game_start > 1:
        
    question1 = str(input(" What is the capital of Australia  :"))
    if question1 == "canberra":
        power += 1
        print("\n correct you have "+ str(lives) +" lives left")
        
    else:
        lives -= 1
        print("thats incorrect, you have " + str(lives) +" lives left")
    question2 = str(input("\n how is the color yellow made, ~hint: write as a equation "))
    if question2 == "blue + green":
        power += 1
        print("\n Correct. You still have " + str(lives) + " lives left")
        
              
              
        
        
