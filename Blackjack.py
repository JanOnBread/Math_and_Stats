
"""
=========================== PYTHON BLACKJACK v2 ===============================

Play an interactive jack black using the console! 
Note:
    Ace = 11 point 
    Jack, Queen, and King = 10 points
    
    Also, there is no way to stop the game unless you stop the current command from the console
    
    A memory system has been added so the same card is not drawn twice.
    
    You can now choose what points to play with
    

===============================================================================

"""
#=============================================================================
# SETTING UP FUNCTIONS AND VARIABLES 
#=============================================================================

# SETING UP HANDS
p_1_hand=[]
p_2_hand=[]
Memory=[]

# ENSURING HAND ARE CLEAR
p_1_hand.clear()
p_2_hand.clear()
Memory.clear()

#IMPORTING
import numpy as np
import time as t

#FUNCTIONS 

def p1_turn ():
    """
    Ask player 1 if they want to stick or twist 
    """
    print("------------------------------------------------------------------------")
    print("                   Player 1, {}, Turn. Twist or Sick?             ". format(p_1))
    print("------------------------------------------------------------------------")
    
def p2_turn ():
    """
    Ask player 2 if they want to stick or twist 
    """
    print("------------------------------------------------------------------------")
    print("                   Player 2, {}, Turn. Twist or Sick?             ". format(p_2))
    print("------------------------------------------------------------------------")   
    

def Hand_worth():
    """
    Shows Player 1 and Player 2's current hand's value 
    """
    t.sleep(1)
    print("------------------------------------------------------------------------")
    print ("                Player 1, {}, your hand is worth {}. ".format(p_1,sum(p_1_hand)))
    print ("                Player 2, {}, your hand is worth {}. ".format(p_2,sum(p_2_hand)))
    print("------------------------------------------------------------------------\n")  
    t.sleep(1)
 

def pick_a_card():
    """
    Draws a card from a standard deck, displays its value, which player has drawn it and adds it to the player's hand.
    """
    # CHOOSE A SUITES
    suites=["Hearts","Dimonds","Spades","Clubs"]
    suites_no= np.random.randint(0,4)
    choose_suite=suites[suites_no]
    if suites_no == 0:
        memory_no_suites =0
    elif suites_no == 1:
        memory_no_suites  =100
    elif suites_no == 2:
        memory_no_suites  =200
    else:
        memory_no_suites  =300      
        
        
    #PICKING A CARD NUMBER + ADDING TO HAND 
    Card_no=np.random.randint(1,14)
    
    #CHECKING IF CARD IS IN MEMEORY 
    # if Spades = 200, king= 13, 200 + 13= 213. Check if 213 is in memeory, if not, run code again. If it is then it appends it to Memeoy.
    memory_card= Card_no + memory_no_suites
    if memory_card not in Memory: 
        Memory.append(memory_card)
        
        if Card_no == 1:
            Card_type="Ace" 
            Card_no= 11
            if Turn==1:
                   p_1_hand.append(11)
            else:
                    p_2_hand.append(11)
        elif Card_no == 11:
            Card_type="Jack"   
            Card_no= 10
            if Turn==1:
                   p_1_hand.append(10)
            else:
                    p_2_hand.append(10)
        elif Card_no == 12:
            Card_type="Queen"    
            Card_no =10
            if Turn==1:
                   p_1_hand.append(10)
            else:
                    p_2_hand.append(10)
        elif Card_no == 13:
            Card_type="King"
            Card_no =10 
            if Turn==1:
                   p_1_hand.append(10)
            else:
                    p_2_hand.append(10)
        else:
            Card_type=str(Card_no)
            if Turn==1:
                   p_1_hand.append(int(Card_no))
            else:
                    p_2_hand.append(int(Card_no))
                    
        # DISPLAY THE CARD'S VALUE 
        if  Turn == 1:
            t.sleep(1)
            print("~~~~  {} picked the {} of {} worth {}  ~~~~".format(p_1,Card_type,choose_suite,Card_no) )
            t.sleep(1)
            
        else:
            t.sleep(1)
            print("~~~~  {} picked the {} of {} worth {}  ~~~~".format(p_2,Card_type,choose_suite,Card_no) )
            t.sleep(1)
    else: 
        pick_a_card()

def Stick_or_Twist():
    """
    Allows the player to pick twist, which goes through the pick_a_card functions, or stick where it skips a turn.
    """
    t.sleep(1)
    Choice = input("Please type 'stick' or 'twist!'\n")
    if Choice == "twist" or Choice == "Twist":
            pick_a_card()
    elif Choice == "Stick" or Choice == "stick":
            if Turn == 1:
                t.sleep(1)
                print("~~~~  Player 1 had choosen not to draw !  ~~~~" )
            else:
                t.sleep(1)
                print("~~~~  Player 2 had choosen not to draw ! ~~~~" )
    else:
        t.sleep(1)
        print("Sorry, I didn't recongise that.")
        Stick_or_Twist()

        
#=============================================================================
#   INTRODUCTION + PLAYER NAMES
#=============================================================================

print("=======================================================================")
print("\n ~~~~~~~~~~~~~~~~~~~~ Welcome to python blackjack! ~~~~~~~~~~~~~~~~~~~~\n")
print("=======================================================================")

p_1= input("What would player 1 like to be called?\n")
t.sleep(1)

p_2= input("How about player 2? What do you go by?\n")
t.sleep(1)

print("------------------------------------------------------------------------")
print("Welcome {} and {} to python blackjack where the goal is to get to \n21 or your chosen number but not over! Who passes that number first loses \nbut, reach exactly that number, and you win automatically!".format(p_1,p_2))
t.sleep(2)
print("Player 1, {}, goes first then player 2, {}. After the inital \ncard draw you have the option to stick or twist.".format(p_1,p_2))
t.sleep(2)
print("------------------------------------------------------------------------")
print("   Sticking= not drawing another card, Twisting = drawing another card ")
print("------------------------------------------------------------------------")
t.sleep(2)

#   CHOOSING YOUR NUMBER 
Choosen_number=input("Please type your chosen number! By default, Blackjack is played \nwith 21 cards but you can decide how many points to achieve here!\n")

looking_for_number= 0

try:
    int(Choosen_number)
except:
    Choosen_number= input("Sorry but this is not a (notural) number! Please try again\n")
    while looking_for_number ==  0:
        looking_for_number = 1
        try:
            int(Choosen_number)
        except ValueError:
            Choosen_number= input("Sorry but this is not a (notural) number! Please try again\n")
            looking_for_number=0 

Choosen_number=int(Choosen_number)
print("Perfect! We shall play this game using {} points!\n". format (Choosen_number))


#   STARTING MESSAGE 
Starting= input("Are you ready to start? (Say 'Yes'!)\n")

if Starting == "Yes":
    print("Perfect, lets start!")
else:
    while Starting != "Yes":
        print("Sorry, seems like I misheard you. Please type 'Yes' to start!")
        Starting= input("Are you ready to start? (Say 'Yes!')\n  ")
        if Starting == "Yes":
            print("Perfect, lets start!")
t.sleep(1)
#-------------------------------------------------------
#   ITITAL DRAW 
print("=======================================================================")
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~ Inital drawing ~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("=======================================================================\n")

t.sleep(1)
print("------------------------------------------------------------------------")
print("                        Player 1, {}, inital draw                     ". format(p_1))
print("------------------------------------------------------------------------")

Turn= 1
#   STARTING MESSAGE 
p1_inital=input("Please type 'pick_a_card' to draw a card!\n")
if p1_inital == "pick_a_card":
    pick_a_card()
    pick_a_card()
  
else:
    while p1_inital != "pick_a_card":
        print("Sorry, seems like you misstyped. Please type 'pick_a_card' to draw!")
        p1_inital= input( "Please type 'pick_a_card' to draw a card!\n")
    if p1_inital == "pick_a_card":
            pick_a_card()
            pick_a_card()
t.sleep(1)
print("------------------------------------------------------------------------")
print ("         Player 1, {}, your hand is worth {}. Player 2's turn.".format(p_1,sum(p_1_hand)))
print("------------------------------------------------------------------------")
t.sleep(1)
print("=======================================================================\n")
t.sleep(1)
print("------------------------------------------------------------------------")
print("                        Player 2, {}, inital draw                     ". format(p_2))
print("------------------------------------------------------------------------")
    
Turn= 2
#   STARTING MESSAGE 
p2_inital=input("Please type 'pick_a_card' to draw a card!\n")
if p2_inital == "pick_a_card":
    pick_a_card()
    pick_a_card()
  
else:
    while p2_inital != "pick_a_card":
        print("Sorry, seems like you misstyped. Please type 'pick_a_card' to draw!")
        p2_inital= input( "Please type 'pick_a_card' to draw a card!\n")
    if p2_inital == "pick_a_card":
            pick_a_card()
            pick_a_card()


t.sleep(1)     
print("------------------------------------------------------------------------")
print ("              Player 2,{}, your hand is worth {}. ".format(p_2,sum(p_2_hand)))
print("------------------------------------------------------------------------\n")  
t.sleep(1)     
Hand_worth()
t.sleep(1)
#=============================================================================
# MAIN GAME
#=============================================================================
print("=======================================================================")
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Game Start ! ~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("=======================================================================\n")
#INITALLY SET TURN TO 1
#   Turn = 1 = player 1
#   Turn = 2 = player 2
t.sleep(1)     
Turn=1
while sum(p_1_hand)< Choosen_number or sum(p_2_hand)<Choosen_number:
    if Turn==1:
        p1_turn()
        Stick_or_Twist()
        Hand_worth()
        Turn=2
        if sum(p_1_hand)>=Choosen_number or sum(p_2_hand)>=Choosen_number:
            break
        
    else:
        p2_turn()
        Stick_or_Twist()
        Hand_worth()
        Turn=1
        if sum(p_1_hand)>=Choosen_number or sum(p_2_hand)>=Choosen_number:
            break
#=============================================================================
# CHOOSING A WINNER
#=============================================================================

#   PLAYER 1 WINS WITH THE CHOOSEN NUMBER OF POINTS
if sum(p_1_hand)==Choosen_number:
    t.sleep(1)
    print("=======================================================================\n")
    print("                            {} WINS!\n". format(p_1))
    t.sleep(1)
    print("------------------------------------------------------------------------\n")  
    print("Player 1,{} has reached exacly {}! That means the win by automatically!". format(p_1,Choosen_number))
    print("Better luck nex time player 2!")
    print("=======================================================================\n")
    
#   PLAYER 2 WINS WITH THE CHOOSEN NUMBER OF POINTS
elif sum(p_2_hand)==Choosen_number:
    t.sleep(1)
    print("=======================================================================\n")
    print("                            {} WINS!\n". format(p_2))
    t.sleep(1)
    print("------------------------------------------------------------------------\n")  
    print("Player 2,{} has reached exacly {}! That means the win by automatically!". format(p_2,Choosen_number))
    print("Better luck nex time player 1!")
    print("=======================================================================\n")
    
#   PLAYER 1 DRAWS MORE THEN THE CHOOSEN NUMBER OF POINTS, PLAYER 2 WINS 
elif sum(p_1_hand)>Choosen_number:
    t.sleep(1)
    print("=======================================================================\n")
    print("                            {} WINS!\n". format(p_2))
    t.sleep(1)
    print("------------------------------------------------------------------------\n")  
    print("Player 1,{}, has drawn more then {} point! That means the player 2, {},\nwin automatically!". format(p_1,Choosen_number,p_2))
    print("Better luck nex time player 1!")
    print("=======================================================================\n")
    
#   PLAYER 2 DRAWS MORE THEN THE CHOOSEN NUMBER OF POINTS, PLAYER 1 WINS 
else:
    t.sleep(1)
    print("=======================================================================\n")
    print("                            {} WINS!\n". format(p_1))
    t.sleep(1)
    print("------------------------------------------------------------------------\n")  
    print("Player 2,{}, has drawn more then {} point! That means the player 1, {},\nwin automatically!". format(p_2,Choosen_number,p_1))
    print("Better luck nex time player 2!")
    print("=======================================================================\n")
    
        