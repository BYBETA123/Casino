import random
from re import A
import pygame

def winnings():
    pass

def Deck_of_cards():
    
    Deck=["ASpades","2Spades","3Spades","4Spades","5Spades","6Spades","7Spades","8Spades","9Spades","0Spades","JSpades","QSpades","KSpades","AClubs","2Clubs","3Clubs","4Clubs","5Clubs","6Clubs","7Clubs","8Clubs","9Clubs","0Clubs","JClubs","QClubs","KClubs","ADiamonds","2Diamonds","3Diamonds","4Diamonds","5Diamonds","6Diamonds","7Diamonds","8Diamodns","9Diamonds","0Diamonds","JDiamonds","QDiamonds","KDiamonds","AHearts","2Hearts","3Hearts","4Hearts","5Hearts","6Hearts","7Hearts","8Hearts","9Hearts","0Hearts","JHearts","QHearts","KHearts"]
    return Deck

def draw_cards_original(new_cards):
    card=random.choice(new_cards)
    return card

def draw_cards(card_list):
    card=random.choice(card_list)
    return card

def remove_card_original(new_cards,card_list,your_card):
    found=False
    for i in range(len(new_cards)):
        if found==False:
            if your_card==new_cards[i]:
                found=True
            else:
                card_list.append(new_cards[i])
        else:
            card_list.append(new_cards[i])
    return card_list

def remove_card(card_list,your_card):
    found=False
    new_card_list=[]
    for i in range(len(card_list)):
        if found==False:
            if your_card==card_list[i]:
                found=True
            else:
                new_card_list.append(card_list[i])
        else:
            new_card_list.append(card_list[i])
    card_list=new_card_list
    return card_list

def hilo():
    done=False
    player_score=0
    computer_score=0
    computer_guess=""
    array=['H','L']
    original_number=random.randint(1,1000)
    while not done:
        new_number=random.randint(1,1000)
        while new_number==original_number:
            new_number=random.randint(1,1000)

        if new_number>original_number:
            correct_ans="H"
        if new_number <original_number:
            correct_ans="L"

        guess=input(f"H or L than {original_number} ")
        if guess==correct_ans:
            player_score+=1
        if 500>original_number:
            computer_guess=="H"
        elif 500<original_number:
            computer_guess="L"
        else:
            computer_guess=random.choice(array)
        # computer_guess=random.choice(array)
        if computer_guess==correct_ans:
            computer_score+=1

        print(f"{player_score} : {computer_score}")
        original_number=new_number
        if player_score==7:
            print("Player Wins")
            answer=input("Do you want to play again (Y/N)")
            if answer=="Y":
                pass
            else:
                done=True

        if computer_score==7:
            print("Computer Wins")
            answer=input("Do you want to play again (Y/N) ")
            if answer=="Y":
                pass
            else:
                done=True

def hilo_graphics():

    pygame.init()
    screen=pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    finished=True

    done=False
    player_score=0
    computer_score=0
    computer_guess=""
    array=['H','L']
    original_number=random.randint(1,1000)
    while not done:
        new_number=random.randint(1,1000)
        while new_number==original_number:
            new_number=random.randint(1,1000)

        if new_number>original_number:
            correct_ans="H"
        if new_number <original_number:
            correct_ans="L"

        guess=input(f"H or L than {original_number} ")
        if guess==correct_ans:
            player_score+=1
        if 500>original_number:
            computer_guess=="H"
        elif 500<original_number:
            computer_guess="L"
        else:
            computer_guess=random.choice(array)
        # computer_guess=random.choice(array)
        if computer_guess==correct_ans:
            computer_score+=1

        print(f"{player_score} : {computer_score}")
        original_number=new_number
        if player_score==7:
            print("Player Wins")
            answer=input("Do you want to play again (Y/N)")
            if answer=="Y":
                pass
            else:
                done=True

        if computer_score==7:
            print("Computer Wins")
            answer=input("Do you want to play again (Y/N) ")
            if answer=="Y":
                pass
            else:
                done=True
    pygame.quit()

def princess_card_counter(cards):
    
    card_count_list=[0,0,0,0,0,0,0,0]
    card_guess=[]
    for item in cards:
        card_count_list[cards[item].card_value()-1]+=1
    highest=0
    card_count_list[0]=0
    for item in card_count_list:
        if item.card_value()>highest:
            highest=item.card_value()
    for card in card_count_list:
        if card_count_list[card]==highest:
            card_guess.append(card+1)
    print(card_guess)
    guess=random.choice(card_guess)
    return guess
        


    pass

def princess1(cards):
    answer=""
    while answer!="9":
        print("===========")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Extreme")
        print("==========")
        ans=input("Which option do you want? ")
        if ans=="1":
            princess_easy(cards)
        if ans=="2":
            princess_medium(cards)
        if ans=="3":
            princess_hard(cards)
        if ans=="4":
            princess_extreme(cards)

def princess_easy(cards):
    your_protection=False
    computer_protection=False
    new_cards=[]
    print("==============")
    new_cards=cards
    card_list=[]
    your_card=draw_cards_original(new_cards)
    card_list=remove_card_original(new_cards, card_list, your_card)
    computer_card=draw_cards(card_list)
    card_list=remove_card(card_list, computer_card)
    done=False
    counter=1
    temp_list=[]

    while not done:

        def Resolve_Guard(Opponent_Card, Opponent_Protection):
            temp_list=[]
            guess=int(input("Please Guess What Card You Think Your Opponent Has"))
            
            if Opponent_Protection == True:
                print("The Opponent Is Protected By Handmaid")
                result=False
                temp_list.append(result)
                outcome="The Opponent Played Guard"
                temp_list.append(outcome)
            
            else:
                if guess==1:
                    print("Incorrect")
                    result=False
                    temp_list.append(result)
                    outcome="The Opponent Played Guard And Guessed Incorrectly"
                    temp_list.append(outcome)

                elif guess==Opponent_Card.card_value():
                        print("The Opponent Discarded {}".format(Opponent_Card))
                        print("You Win")
                        result=True
                        temp_list.append(result)
                else:
                    print("Incorrect")
                    result=False
                    temp_list.append(result)
                    if guess==2:
                        outcome="The Opponent Played Guard And Guessed You As Priest"
                    if guess==3:
                        outcome="The Opponent Played Guard And Guessed You As Baron"
                    if guess==4:
                        outcome="The Opponent Played Guard And Guessed You As Handmaid"
                    if guess==5:
                        outcome="The Opponent Played Guard And Guessed You As Prince"
                    if guess==6:
                        outcome="The Opponent Played Guard And Guessed You As King"
                    if guess==7:
                        outcome="The Opponent Played Guard And Guessed You As Countess"
                    if guess==8:
                        outcome="The Opponent Played Guard And Guessed You As Princess"
                    temp_list.append(outcome)
            
            return temp_list

        def Resolve_Priest(Opponent_Card, Opponent_Protection):
            
            temp_list=[]
            result=False
            temp_list.append(result)
            if Opponent_Protection == True:
                print("The Opponent Is Protected By Handmaid")
                outcome="The Opponent Played Priest and saw your card: " + str(Opponent_Card)
                temp_list.append(outcome)
            
            else:
                print(f"The Opponent Has {Opponent_Card}")
                outcome="The Opponent Saw Your Card"
                temp_list.append(outcome)
            
            return temp_list

        def Resolve_Baron(Baron_Card, Opponent_Card, Opponent_Protection):
            temp_list=[]
            
            if Opponent_Protection == True:
                print("The Opponent Is Protected By Handmaid")
                outcome="The Opponent Played Baron"
                result=False
            else:
                
                if Baron_Card.card_value()>Opponent_Card.card_value():
                    print("The Opponent Discarded {}".format(Opponent_Card))
                    print("You Win")
                    outcome=""
                    result=True
                
                elif Baron_Card.card_value()<Opponent_Card.card_value():
                    print("You Discarded {} As The Opponent Had {}".format(Baron_Card, Opponent_Card))
                    print("You Lose")
                    outcome=""
                    result=True
                
                elif Baron_Card.card_value()==Opponent_Card.card_value():
                    print("It Is A Draw, You And Your Opponent Both Have {}".format(Baron_Card))
                    result=False
                    outcome="The Opponent Played Baron And It Was A Draw"
            
            temp_list.append(result)
            temp_list.append(outcome)
            return temp_list

        def Resolve_Handmaid(Your_Protection):
            temp_list=[]
            print("You Have Been Protected For 1 Turn")
            result=False
            outcome="The Opponent Played Handmaid"
            Your_Protection=True
            temp_list.append(result)
            temp_list.append(outcome)
            temp_list.append(Your_Protection)
            return temp_list

        def Resolve_Prince(Your_Card, Your_Other_Card, Opponent_Card, Opponent_Protection, card_list):
            
            temp_list=[]
            if Your_Card.card_value()==7:
                temp_list=Resolve_Countess()
                Your_Card=Your_Other_Card
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                temp_list.append(card_list)
                return temp_list
            else:
                if Opponent_Protection==True:
                    print("The Opponent Is Protected By Handmaid")
                    if Your_Card.card_value()==8:
                        print("You Lose")
                        outcome=""
                        result=True
                
                    else:
                        outcome="The Opponent Played Prince And Discarded: "+ str(Your_Card)
                        Your_Card=random.choice(card_list)
                        if len(card_list)!=0:
                            card_list=remove_card(card_list, Your_Card)
                        result=False
                        print("Your New Card Is {}".format(Your_Card))

                else:
                    print("Do You Want To Discard Yourself (Y) Or Your Opponent (O)")
                    ans=str(input())
                    
                    if ans=="Y":
                    
                        if Your_Card.card_value()==8:
                            print("You Lose")
                            outcome=""
                            result=True
                    
                        else:
                            outcome="The Opponent Played Prince And Discarded: " + str(Your_Card)
                            Your_Card=random.choice(card_list)
                            if len(card_list)!=0:
                                card_list=remove_card(card_list, Your_Card)
                            print(f"Your New Card Is {Your_Card}")
                            result=False
                    
                    elif ans == "O":
                    
                        if Opponent_Card.card_value() == 8:
                            print("You Win")
                            outcome=""
                            result=True
                        else:
                            outcome="The Opponent Played Prince And Discarded Your Card: " + str(Opponent_Card)
                            Opponent_Card=random.choice(card_list)
                            if len(card_list)!=0:
                                card_list=remove_card(card_list, Opponent_Card)
                            result=False
                
                temp_list.append(result)
                temp_list.append(outcome)
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                temp_list.append(card_list)
                return temp_list
        
        def Resolve_King(Your_Card, Your_Other_Card, Opponent_Card, Opponent_Protection):
            
            temp_list=[]

            if Your_Card.card_value()==7:
                temp_list=Resolve_Countess()
                Your_Card=Your_Other_Card
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                return temp_list

            else:
                if Opponent_Protection == True:
                    print("The Opponent Is Protected By Handmaid")
                    temp_list=[]
                    result=False
                    outcome="The Opponent Played King"

                
                else:
                    temp=Your_Card
                    Your_Card=Opponent_Card
                    Opponent_Card=temp
                    print(f"Your New Card Is {Your_Card}")
                    temp_list=[]
                    result=False
                    outcome="The Opponent Played King"

                temp_list.append(result)
                temp_list.append(outcome)
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                return temp_list

        def Resolve_Countess():
            temp_list=[]
            outcome="The Opponent Played Countess"
            result=False
            temp_list.append(result)
            temp_list.append(outcome)
            return temp_list

        def Resolve_Princess():
            temp_list=[]
            print("You Lose")
            result=True
            temp_list.append(result)
            outcome=""
            temp_list.append(outcome)
            return temp_list

    
        def Resolve_Guard_Computer(Opponent_Card, Opponent_Protection):
            temp_list=[]
            guess=random.randint(2,8)

            if Opponent_Protection == True:
                result=False
                temp_list.append(result)
                outcome="The Computer Played Guard"
                temp_list.append(outcome)
            
            else:

                if guess==Opponent_Card.card_value():
                        print("You Lose")
                        result=True
                        temp_list.append(result)
                else:
                    result=False
                    temp_list.append(result)
                    if guess==2:
                        outcome="The Computer Played Guard And Guessed You As Priest"
                    if guess==3:
                        outcome="The Computer played guard And Guessed You As Baron"
                    if guess==4:
                        outcome="The Computer played guard And Guessed You As Handmaid"
                    if guess==5:
                        outcome="The Computer played guard And Guessed You As Prince"
                    if guess==6:
                        outcome="The Computer played guard And Guessed You As King"
                    if guess==7:
                        outcome="The Computer played guard And Guessed You As Countess"
                    if guess==8:
                        outcome="The Computer played guard And Guessed You As Princess"

                    temp_list.append(outcome)
            
            return temp_list

        def Resolve_Priest_Computer(Opponent_Card, Opponent_Protection):
            
            temp_list=[]
            result=False
            temp_list.append(result)
            if Opponent_Protection == True:
                outcome="The Computer Played Priest"
                temp_list.append(outcome)
            
            else:
                outcome="The Computer Played Priest And Saw Your Card: " + str(Opponent_Card)
                temp_list.append(outcome)
            
            return temp_list

        def Resolve_Baron_Computer(Baron_Card, Opponent_Card, Opponent_Protection):
            temp_list=[]
            
            if Opponent_Protection == True:
                outcome="The Computer Played Baron"
                result=False
            else:
                
                if Baron_Card.card_value()>Opponent_Card.card_value():
                    print("You Lose")
                    outcome=""
                    result=True
                
                elif Baron_Card.card_value()<Opponent_Card.card_value():
                    print("You Win")
                    outcome=""
                    result=True
                
                elif Baron_Card.card_value()==Opponent_Card.card_value():
                    result=False
                    outcome="The Computer Played Baron And It Was A Draw"
            
            temp_list.append(result)
            temp_list.append(outcome)
            return temp_list

        def Resolve_Handmaid_Computer(Your_Protection):
            temp_list=[]
            result=False
            outcome="The Computer Played Handmaid"
            Your_Protection=True
            temp_list.append(result)
            temp_list.append(outcome)
            temp_list.append(Your_Protection)
            return temp_list

        def Resolve_Prince_Computer(Your_Card, Your_Other_Card, Opponent_Card, Opponent_Protection, card_list):
            
            temp_list=[]
            if Your_Card.card_value()==7:
                temp_list=Resolve_Countess()
                Your_Card=Your_Other_Card
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                temp_list.append(card_list)
                return temp_list
            else:
                if Opponent_Protection==True:
                    if Your_Card.card_value()==8:
                        print("You Win")
                        outcome=""
                        result=True
                
                    else:
                        outcome="The Computer Played Prince And Discarded: "+ str(Your_Card)
                        Your_Card=random.choice(card_list)
                        if len(card_list)!=0:
                            card_list=remove_card(card_list, Your_Card)
                        result=False

                else:
                    selection=["Y","O"]
                    ans=random.choice(selection)
                    
                    if ans=="Y":
                    
                        if Your_Card.card_value()==8:
                            print("You Win")
                            outcome=""
                            result=True
                    
                        else:
                            outcome="The Computer Played Prince And Discarded: " + str(Your_Card)
                            Your_Card=random.choice(card_list)
                            if len(card_list)!=0:
                                card_list=remove_card(card_list, Your_Card)
                            result=False
                    
                    elif ans == "O":
                    
                        if Opponent_Card.card_value() == 8:
                            print("You Lose")
                            outcome=""
                            result=True
                        else:
                            outcome="The Computer Played Prince And Discarded Your Card: " + str(Opponent_Card)
                            Opponent_Card=random.choice(card_list)
                            if len(card_list)!=0:
                                card_list=remove_card(card_list, Opponent_Card)
                            result=False
                
                temp_list.append(result)
                temp_list.append(outcome)
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                temp_list.append(card_list)
                return temp_list
        
        def Resolve_King_Computer(Your_Card, Your_Other_Card, Opponent_Card, Opponent_Protection):
            
            temp_list=[]

            if Your_Card.card_value()==7:
                temp_list=Resolve_Countess()
                Your_Card=Your_Other_Card
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                return temp_list

            else:
                if Opponent_Protection == True:
                    temp_list=[]
                    result=False
                    outcome="The Computer Played King"

                
                else:
                    temp=Your_Card
                    Your_Card=Opponent_Card
                    Opponent_Card=temp
                    temp_list=[]
                    result=False
                    outcome="The Computer Played King and swapped your card with theirs"

                temp_list.append(result)
                temp_list.append(outcome)
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                return temp_list

        def Resolve_Countess_Computer():
            temp_list=[]
            outcome="The Computer Played Countess"
            result=False
            temp_list.append(result)
            temp_list.append(outcome)
            return temp_list

        def Resolve_Princess_Computer():
            temp_list=[]
            print("You Win")
            result=True
            temp_list.append(result)
            outcome=""
            temp_list.append(outcome)
            return temp_list    
    
        
        placeholder=input("")
        placeholder=placeholder
        print("===============")
        print("Player 1's Turn")
        print("===============")

        placeholder=input("")
        placeholder=placeholder
        if counter==0:
            print("=========")
            print("Summary")
            print(temp_list[1])
            print("==========")
        counter=0

        your_card_2=draw_cards(card_list)
        card_list=remove_card(card_list, your_card_2)
        print(f"1.{your_card}: {your_card.ability()}")
        print(f"2.{your_card_2}: {your_card_2.ability()}")
        answer=input("Which Card Would You Like To Play?")
        your_protection=False
        
        if answer=="1":
            if your_card.card_value()==1:
                temp_list=Resolve_Guard(computer_card, computer_protection)
                done=temp_list[0]

            if your_card.card_value()==2:
                temp_list=Resolve_Priest(computer_card, computer_protection)
                done=temp_list[0]

            if your_card.card_value()==3:
                temp_list=Resolve_Baron(your_card_2, computer_card, computer_protection)
                done=temp_list[0]

            if your_card.card_value()==4:
                temp_list=Resolve_Handmaid(your_protection)
                your_protection=temp_list[2]
                done=temp_list[0]

            if your_card.card_value()==5:
                temp_list=Resolve_Prince(your_card_2, your_card, computer_card, computer_protection, card_list)
                done=temp_list[0]
                your_card_2=temp_list[2]
                computer_card=temp_list[3]
                card_list=temp_list[4]

            if your_card.card_value()==6:
                temp_list=Resolve_King(your_card, your_card_2, computer_card, computer_protection)
                done=temp_list[0]
                your_card_2=temp_list[2]
                computer_card=temp_list[3]

            if your_card.card_value()==7:
                temp_list=Resolve_Countess()
                done=temp_list[0]

            if your_card.card_value()==8:
                temp_list=Resolve_Princess()
                done=temp_list[0]

            your_card=your_card_2

        if answer=="2":
            
            if your_card_2.card_value()==1:

                temp_list=Resolve_Guard(computer_card, computer_protection)
                done=temp_list[0]

            if your_card_2.card_value()==2:

                temp_list=Resolve_Priest(computer_card,computer_protection)
                done=temp_list[0]

            if your_card_2.card_value()==3:

                temp_list=Resolve_Baron(your_card, computer_card, computer_protection)
                done=temp_list[0]

            if your_card_2.card_value()==4:

                temp_list=Resolve_Handmaid(your_protection)
                done=temp_list[0]
                your_protection=temp_list[2]
            
            if your_card_2.card_value()==5:
                temp_list=Resolve_Prince()
                done=temp_list[0]
                your_card=temp_list[2]
                computer_card=temp_list[3]
                card_list=temp_list[4]

            if your_card_2.card_value()==6:
                temp_list=Resolve_King(your_card, your_card_2, computer_card, computer_protection)
                done=temp_list[0]
                your_card=temp_list[2]
                computer_card=temp_list[3]

            if your_card_2.card_value()==7:
                temp_list=Resolve_Countess()
                done=temp_list[0]

            if your_card_2.card_value()==8:
                temp_list=Resolve_Princess()
                done=temp_list[0]

        if done==False:
            print("===============")
            print("Computer's Turn")
            print("===============")
            computer_protection=False
            computer_card_2=draw_cards(card_list)
            card_list=remove_card(card_list,computer_card_2)
            answer=random.randint(1,2)
            if answer ==1:
                if computer_card.card_value()==1:

                    temp_list=Resolve_Guard_Computer(your_card, your_protection)
                    done=temp_list[0]

                if computer_card.card_value()==2:

                    temp_list=Resolve_Priest_Computer(your_card, your_protection)
                    done=temp_list[0]

                if computer_card.card_value()==3:

                    temp_list=Resolve_Baron_Computer(computer_card_2, your_card, your_protection)
                    done=temp_list[0]

                if computer_card.card_value()==4:

                    temp_list=Resolve_Handmaid_Computer(computer_protection)
                    done=temp_list[0]
                    computer_protection=temp_list[2]

                if computer_card.card_value()==5:
                    
                    temp_list=Resolve_Prince_Computer(computer_card, computer_card_2, your_card, your_protection, card_list)
                    done=temp_list[0]
                    your_card=temp_list[3]
                    computer_card=temp_list[2]  
                    card_list=temp_list[4]              

                if computer_card.card_value()==6:
                    
                    temp_list=Resolve_King(computer_card, computer_card_2,your_card,your_protection)
                    computer_card=temp_list[2]
                    your_card=temp_list[3]
                    done=temp_list[0]

                if computer_card.card_value()==7:
                    
                    temp_list=Resolve_Countess_Computer()
                    done=temp_list[0]

                if computer_card.card_value()==8:
                    
                    temp_list=Resolve_Princess_Computer()
                    done=temp_list[0]

                computer_card=computer_card_2
            if answer == 2:
                if computer_card_2.card_value()==1:
                    
                    temp_list=Resolve_Guard_Computer(your_card,your_protection)
                    done=temp_list[0]

                if computer_card_2.card_value()==2:
                    
                    temp_list=Resolve_Priest_Computer(your_card,your_protection)
                    done=temp_list[0]

                if computer_card_2.card_value()==3:
                    
                    temp_list=Resolve_Baron_Computer(computer_card,your_card,your_protection)
                    done=temp_list[0]

                if computer_card_2.card_value()==4:
                    
                    temp_list=Resolve_Handmaid_Computer(computer_protection)
                    done=temp_list[0]
                    computer_protection=temp_list[2]

                if computer_card_2.card_value()==5:
                    
                    temp_list=Resolve_Prince_Computer(computer_card,computer_card_2,your_card, your_protection,card_list)
                    done=temp_list[0]
                    your_card=temp_list[3]
                    computer_card=temp_list[2]
                    card_list=temp_list[4]
                if computer_card_2.card_value()==6:
                    temp_list=Resolve_King_Computer(computer_card,computer_card,your_card,your_protection)
                    done=temp_list[0]
                    computer_card=temp_list[2]
                    your_card=temp_list[3]

                if computer_card_2.card_value()==7:
                    temp_list=Resolve_Countess_Computer()
                    done=temp_list[0]
                if computer_card_2.card_value()==8:
                    temp_list=Resolve_Princess_Computer()
                    done=temp_list[0]

def princess_medium(cards):
    your_protection=False
    computer_protection=False
    new_cards=[]
    print("==============")
    new_cards=cards
    card_list=[]
    your_card=draw_cards_original(new_cards)
    card_list=remove_card_original(new_cards, card_list, your_card)
    computer_card=draw_cards(card_list)
    card_list=remove_card(card_list, computer_card)
    done=False
    counter=1
    temp_list=[]

    while not done:

        def Resolve_Guard(Opponent_Card, Opponent_Protection):
            temp_list=[]
            guess=int(input("Please Guess What Card You Think Your Opponent Has"))
            
            if Opponent_Protection == True:
                print("The Opponent Is Protected By Handmaid")
                result=False
                temp_list.append(result)
                outcome="The Opponent Played Guard"
                temp_list.append(outcome)
            
            else:
                if guess==1:
                    print("Incorrect")
                    result=False
                    temp_list.append(result)
                    outcome="The Opponent Played Guard And Guessed Incorrectly"
                    temp_list.append(outcome)

                elif guess==Opponent_Card.card_value():
                        print("The Opponent Discarded {}".format(Opponent_Card))
                        print("You Win")
                        result=True
                        temp_list.append(result)
                else:
                    print("Incorrect")
                    result=False
                    temp_list.append(result)
                    if guess==2:
                        outcome="The Opponent Played Guard And Guessed You As Priest"
                    if guess==3:
                        outcome="The Opponent Played Guard And Guessed You As Baron"
                    if guess==4:
                        outcome="The Opponent Played Guard And Guessed You As Handmaid"
                    if guess==5:
                        outcome="The Opponent Played Guard And Guessed You As Prince"
                    if guess==6:
                        outcome="The Opponent Played Guard And Guessed You As King"
                    if guess==7:
                        outcome="The Opponent Played Guard And Guessed You As Countess"
                    if guess==8:
                        outcome="The Opponent Played Guard And Guessed You As Princess"
                    temp_list.append(outcome)
            
            return temp_list

        def Resolve_Priest(Opponent_Card, Opponent_Protection):
            
            temp_list=[]
            result=False
            temp_list.append(result)
            if Opponent_Protection == True:
                print("The Opponent Is Protected By Handmaid")
                outcome="The Opponent Played Priest and saw your card: " + str(Opponent_Card)
                temp_list.append(outcome)
            
            else:
                print(f"The Opponent Has {Opponent_Card}")
                outcome="The Opponent Saw Your Card"
                temp_list.append(outcome)
            
            return temp_list

        def Resolve_Baron(Baron_Card, Opponent_Card, Opponent_Protection):
            temp_list=[]
            
            if Opponent_Protection == True:
                print("The Opponent Is Protected By Handmaid")
                outcome="The Opponent Played Baron"
                result=False
            else:
                
                if Baron_Card.card_value()>Opponent_Card.card_value():
                    print("The Opponent Discarded {}".format(Opponent_Card))
                    print("You Win")
                    outcome=""
                    result=True
                
                elif Baron_Card.card_value()<Opponent_Card.card_value():
                    print("You Discarded {} As The Opponent Had {}".format(Baron_Card, Opponent_Card))
                    print("You Lose")
                    outcome=""
                    result=True
                
                elif Baron_Card.card_value()==Opponent_Card.card_value():
                    print("It Is A Draw, You And Your Opponent Both Have {}".format(Baron_Card))
                    result=False
                    outcome="The Opponent Played Baron And It Was A Draw"
            
            temp_list.append(result)
            temp_list.append(outcome)
            return temp_list

        def Resolve_Handmaid(Your_Protection):
            temp_list=[]
            print("You Have Been Protected For 1 Turn")
            result=False
            outcome="The Opponent Played Handmaid"
            Your_Protection=True
            temp_list.append(result)
            temp_list.append(outcome)
            temp_list.append(Your_Protection)
            return temp_list

        def Resolve_Prince(Your_Card, Your_Other_Card, Opponent_Card, Opponent_Protection, card_list):
            
            temp_list=[]
            if Your_Card.card_value()==7:
                temp_list=Resolve_Countess()
                Your_Card=Your_Other_Card
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                temp_list.append(card_list)
                return temp_list
            else:
                if Opponent_Protection==True:
                    print("The Opponent Is Protected By Handmaid")
                    if Your_Card.card_value()==8:
                        print("You Lose")
                        outcome=""
                        result=True
                
                    else:
                        outcome="The Opponent Played Prince And Discarded: "+ str(Your_Card)
                        Your_Card=random.choice(card_list)
                        if len(card_list)!=0:
                            card_list=remove_card(card_list, Your_Card)
                        result=False
                        print("Your New Card Is {}".format(Your_Card))

                else:
                    print("Do You Want To Discard Yourself (Y) Or Your Opponent (O)")
                    ans=str(input())
                    
                    if ans=="Y":
                    
                        if Your_Card.card_value()==8:
                            print("You Lose")
                            outcome=""
                            result=True
                    
                        else:
                            outcome="The Opponent Played Prince And Discarded: " + str(Your_Card)
                            Your_Card=random.choice(card_list)
                            if len(card_list)!=0:
                                card_list=remove_card(card_list, Your_Card)
                            print(f"Your New Card Is {Your_Card}")
                            result=False
                    
                    elif ans == "O":
                    
                        if Opponent_Card.card_value() == 8:
                            print("You Win")
                            outcome=""
                            result=True
                        else:
                            outcome="The Opponent Played Prince And Discarded Your Card: " + str(Opponent_Card)
                            Opponent_Card=random.choice(card_list)
                            if len(card_list)!=0:
                                card_list=remove_card(card_list, Opponent_Card)
                            result=False
                
                temp_list.append(result)
                temp_list.append(outcome)
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                temp_list.append(card_list)
                return temp_list
        
        def Resolve_King(Your_Card, Your_Other_Card, Opponent_Card, Opponent_Protection):
            
            temp_list=[]

            if Your_Card.card_value()==7:
                temp_list=Resolve_Countess()
                Your_Card=Your_Other_Card
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                return temp_list

            else:
                if Opponent_Protection == True:
                    print("The Opponent Is Protected By Handmaid")
                    temp_list=[]
                    result=False
                    outcome="The Opponent Played King"

                
                else:
                    temp=Your_Card
                    Your_Card=Opponent_Card
                    Opponent_Card=temp
                    print(f"Your New Card Is {Your_Card}")
                    temp_list=[]
                    result=False
                    outcome="The Opponent Played King"

                temp_list.append(result)
                temp_list.append(outcome)
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                return temp_list

        def Resolve_Countess():
            temp_list=[]
            outcome="The Opponent Played Countess"
            result=False
            temp_list.append(result)
            temp_list.append(outcome)
            return temp_list

        def Resolve_Princess():
            temp_list=[]
            print("You Lose")
            result=True
            temp_list.append(result)
            outcome=""
            temp_list.append(outcome)
            return temp_list

    
        def Resolve_Guard_Computer_Medium(Opponent_Card, Opponent_Protection):
            temp_list=[]
            guess=8

            if Opponent_Protection == True:
                result=False
                temp_list.append(result)
                outcome="The Computer Played Guard"
                temp_list.append(outcome)
            
            else:

                if guess==Opponent_Card.card_value():
                        print("You Lose")
                        result=True
                        temp_list.append(result)
                else:
                    result=False
                    temp_list.append(result)
                    outcome="The Computer played guard And Guessed You As Princess"

                    temp_list.append(outcome)
            
            return temp_list

        def Resolve_Priest_Computer_Medium(Opponent_Card, Opponent_Protection):
            
            temp_list=[]
            result=False
            temp_list.append(result)
            if Opponent_Protection == True:
                outcome="The Computer Played Priest"
                temp_list.append(outcome)
            
            else:
                outcome="The Computer Played Priest And Saw Your Card: " + str(Opponent_Card)
                temp_list.append(outcome)
            
            return temp_list

        def Resolve_Baron_Computer_Medium(Baron_Card, Opponent_Card, Opponent_Protection):
            temp_list=[]
            
            if Opponent_Protection == True:
                outcome="The Computer Played Baron"
                result=False
            else:
                
                if Baron_Card.card_value()>Opponent_Card.card_value():
                    print("You Lose")
                    outcome=""
                    result=True
                
                elif Baron_Card.card_value()<Opponent_Card.card_value():
                    print("You Win")
                    outcome=""
                    result=True
                
                elif Baron_Card.card_value()==Opponent_Card.card_value():
                    result=False
                    outcome="The Computer Played Baron And It Was A Draw"

            temp_list.append(result)
            temp_list.append(outcome)
            return temp_list

        def Resolve_Handmaid_Computer_Medium(Your_Protection):
            temp_list=[]
            result=False
            outcome="The Computer Played Handmaid"
            Your_Protection=True
            temp_list.append(result)
            temp_list.append(outcome)
            temp_list.append(Your_Protection)
            return temp_list

        def Resolve_Prince_Computer_Medium(Your_Card, Your_Other_Card, Opponent_Card, Opponent_Protection, card_list):
            
            temp_list=[]
            if Your_Card.card_value()==7:
                temp_list=Resolve_Countess_Computer_Medium()
                Your_Card=Your_Other_Card
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                temp_list.append(card_list)
                return temp_list
            
            else:
                if Opponent_Protection==True:
                    if Your_Card.card_value()==8:
                        print("You Win")
                        outcome=""
                        result=True
                
                    else:
                        outcome="The Computer Played Prince And Discarded: "+ str(Your_Card)
                        Your_Card=random.choice(card_list)
                        if len(card_list)!=0:
                            card_list=remove_card(card_list, Your_Card)
                        result=False

                else:
                        if Opponent_Card.card_value() == 8:
                            print("You Lose")
                            outcome=""
                            result=True
                        else:
                            outcome="The Computer Played Prince And Discarded Your Card: " + str(Opponent_Card)
                            Opponent_Card=random.choice(card_list)
                            if len(card_list)!=0:
                                card_list=remove_card(card_list, Opponent_Card)
                            result=False
                
                temp_list.append(result)
                temp_list.append(outcome)
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                temp_list.append(card_list)
                return temp_list
        
        def Resolve_King_Computer_Medium(Your_Card, Your_Other_Card, Opponent_Card, Opponent_Protection):
            
            temp_list=[]

            if Your_Card.card_value()==7:
                temp_list=Resolve_Countess_Computer_Medium()
                Your_Card=Your_Other_Card
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                return temp_list

            else:
                if Opponent_Protection == True:
                    temp_list=[]
                    result=False
                    outcome="The Computer Played King"

                
                else:
                    temp=Your_Card
                    Your_Card=Opponent_Card
                    Opponent_Card=temp
                    temp_list=[]
                    result=False
                    outcome="The Computer Played King and swapped your card with theirs"

                temp_list.append(result)
                temp_list.append(outcome)
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                return temp_list

        def Resolve_Countess_Computer_Medium():
            temp_list=[]
            outcome="The Computer Played Countess"
            result=False
            temp_list.append(result)
            temp_list.append(outcome)
            return temp_list

        def Resolve_Princess_Computer_Medium():
            temp_list=[]
            print("You Win")
            result=True
            temp_list.append(result)
            outcome=""
            temp_list.append(outcome)
            return temp_list    
    
        
        placeholder=input("")
        placeholder=placeholder
        print("===============")
        print("Player 1's Turn")
        print("===============")

        placeholder=input("")
        placeholder=placeholder
        if counter==0:
            print("=========")
            print("Summary")
            print(temp_list[1])
            print("==========")
        counter=0

        your_card_2=draw_cards(card_list)
        card_list=remove_card(card_list, your_card_2)
        print(f"1.{your_card}: {your_card.ability()}")
        print(f"2.{your_card_2}: {your_card_2.ability()}")
        answer=input("Which Card Would You Like To Play?")
        your_protection=False
        
        if answer=="1":
            if your_card.card_value()==1:
                temp_list=Resolve_Guard(computer_card, computer_protection)
                done=temp_list[0]

            if your_card.card_value()==2:
                temp_list=Resolve_Priest(computer_card, computer_protection)
                done=temp_list[0]

            if your_card.card_value()==3:
                temp_list=Resolve_Baron(your_card_2, computer_card, computer_protection)
                done=temp_list[0]

            if your_card.card_value()==4:
                temp_list=Resolve_Handmaid(your_protection)
                your_protection=temp_list[2]
                done=temp_list[0]

            if your_card.card_value()==5:
                temp_list=Resolve_Prince(your_card_2, your_card, computer_card, computer_protection, card_list)
                done=temp_list[0]
                your_card_2=temp_list[2]
                computer_card=temp_list[3]
                card_list=temp_list[4]

            if your_card.card_value()==6:
                temp_list=Resolve_King(your_card, your_card_2, computer_card, computer_protection)
                done=temp_list[0]
                your_card_2=temp_list[2]
                computer_card=temp_list[3]

            if your_card.card_value()==7:
                temp_list=Resolve_Countess()
                done=temp_list[0]

            if your_card.card_value()==8:
                temp_list=Resolve_Princess()
                done=temp_list[0]

            your_card=your_card_2

        if answer=="2":
            
            if your_card_2.card_value()==1:

                temp_list=Resolve_Guard(computer_card, computer_protection)
                done=temp_list[0]

            if your_card_2.card_value()==2:

                temp_list=Resolve_Priest(computer_card,computer_protection)
                done=temp_list[0]

            if your_card_2.card_value()==3:

                temp_list=Resolve_Baron(your_card, computer_card, computer_protection)
                done=temp_list[0]

            if your_card_2.card_value()==4:

                temp_list=Resolve_Handmaid(your_protection)
                done=temp_list[0]
                your_protection=temp_list[2]
            
            if your_card_2.card_value()==5:
                temp_list=Resolve_Prince()
                done=temp_list[0]
                your_card=temp_list[2]
                computer_card=temp_list[3]
                card_list=temp_list[4]

            if your_card_2.card_value()==6:
                temp_list=Resolve_King(your_card, your_card_2, computer_card, computer_protection)
                done=temp_list[0]
                your_card=temp_list[2]
                computer_card=temp_list[3]

            if your_card_2.card_value()==7:
                temp_list=Resolve_Countess()
                done=temp_list[0]

            if your_card_2.card_value()==8:
                temp_list=Resolve_Princess()
                done=temp_list[0]

        if done==False:
            print("===============")
            print("Computer's Turn")
            print("===============")
            computer_protection=False
            computer_card_2=draw_cards(card_list)
            card_list=remove_card(card_list,computer_card_2)
            random_array=[0,0,0,1,1]
            if computer_card.card_value()==8:
                answer=2
            elif computer_card_2.card_value()==8:
                answer=1
            elif computer_card.card_value()==4:
                answer=1
            elif computer_card_2.card_value()==4:
                answer=2
            if random.choice(random_array)==1:
                print("hi")
            else:
                print("hi")
            answer=random.randint(1,2)
            if answer ==1:
                if computer_card.card_value()==1:

                    temp_list=Resolve_Guard_Computer_Medium(your_card, your_protection)
                    done=temp_list[0]

                if computer_card.card_value()==2:

                    temp_list=Resolve_Priest_Computer_Medium(your_card, your_protection)
                    done=temp_list[0]

                if computer_card.card_value()==3:

                    temp_list=Resolve_Baron_Computer_Medium(computer_card_2, your_card, your_protection)
                    done=temp_list[0]

                if computer_card.card_value()==4:

                    temp_list=Resolve_Handmaid_Computer_Medium(computer_protection)
                    done=temp_list[0]
                    computer_protection=temp_list[2]

                if computer_card.card_value()==5:
                    
                    temp_list=Resolve_Prince_Computer_Medium(computer_card, computer_card_2, your_card, your_protection, card_list)
                    done=temp_list[0]
                    your_card=temp_list[3]
                    computer_card=temp_list[2]  
                    card_list=temp_list[4]              

                if computer_card.card_value()==6:
                    
                    temp_list=Resolve_King_Computer_Medium(computer_card, computer_card_2,your_card,your_protection)
                    computer_card=temp_list[2]
                    your_card=temp_list[3]
                    done=temp_list[0]

                if computer_card.card_value()==7:
                    
                    temp_list=Resolve_Countess_Computer_Medium()
                    done=temp_list[0]

                if computer_card.card_value()==8:
                    
                    temp_list=Resolve_Princess_Computer_Medium()
                    done=temp_list[0]

                computer_card=computer_card_2
            if answer == 2:
                if computer_card_2.card_value()==1:
                    
                    temp_list=Resolve_Guard_Computer_Medium(your_card,your_protection)
                    done=temp_list[0]

                if computer_card_2.card_value()==2:
                    
                    temp_list=Resolve_Priest_Computer_Medium(your_card,your_protection)
                    done=temp_list[0]

                if computer_card_2.card_value()==3:
                    
                    temp_list=Resolve_Baron_Computer_Medium(computer_card,your_card,your_protection)
                    done=temp_list[0]

                if computer_card_2.card_value()==4:
                    
                    temp_list=Resolve_Handmaid_Computer_Medium(computer_protection)
                    done=temp_list[0]
                    computer_protection=temp_list[2]

                if computer_card_2.card_value()==5:
                    
                    temp_list=Resolve_Prince_Computer_Medium(computer_card,computer_card_2,your_card, your_protection,card_list)
                    done=temp_list[0]
                    your_card=temp_list[3]
                    computer_card=temp_list[2]
                    card_list=temp_list[4]

                if computer_card_2.card_value()==6:
                    temp_list=Resolve_King_Computer_Medium(computer_card,computer_card,your_card,your_protection)
                    done=temp_list[0]
                    computer_card=temp_list[2]
                    your_card=temp_list[3]

                if computer_card_2.card_value()==7:
                    temp_list=Resolve_Countess_Computer_Medium()
                    done=temp_list[0]
                if computer_card_2.card_value()==8:
                    temp_list=Resolve_Princess_Computer_Medium()
                    done=temp_list[0]

def princess_hard(cards):
    your_protection=False
    computer_protection=False
    new_cards=[]
    print("==============")
    new_cards=cards
    card_list=[]
    your_card=draw_cards_original(new_cards)
    card_list=remove_card_original(new_cards, card_list, your_card)
    computer_card=draw_cards(card_list)
    card_list=remove_card(card_list, computer_card)
    done=False
    counter=1
    temp_list=[]

    while not done:

        def Resolve_Guard(Opponent_Card, Opponent_Protection):
            temp_list=[]
            guess=int(input("Please Guess What Card You Think Your Opponent Has"))
            
            if Opponent_Protection == True:
                print("The Opponent Is Protected By Handmaid")
                result=False
                temp_list.append(result)
                outcome="The Opponent Played Guard"
                temp_list.append(outcome)
            
            else:
                if guess==1:
                    print("Incorrect")
                    result=False
                    temp_list.append(result)
                    outcome="The Opponent Played Guard And Guessed Incorrectly"
                    temp_list.append(outcome)

                elif guess==Opponent_Card.card_value():
                        print("The Opponent Discarded {}".format(Opponent_Card))
                        print("You Win")
                        result=True
                        temp_list.append(result)
                else:
                    print("Incorrect")
                    result=False
                    temp_list.append(result)
                    if guess==2:
                        outcome="The Opponent Played Guard And Guessed You As Priest"
                    if guess==3:
                        outcome="The Opponent Played Guard And Guessed You As Baron"
                    if guess==4:
                        outcome="The Opponent Played Guard And Guessed You As Handmaid"
                    if guess==5:
                        outcome="The Opponent Played Guard And Guessed You As Prince"
                    if guess==6:
                        outcome="The Opponent Played Guard And Guessed You As King"
                    if guess==7:
                        outcome="The Opponent Played Guard And Guessed You As Countess"
                    if guess==8:
                        outcome="The Opponent Played Guard And Guessed You As Princess"
                    temp_list.append(outcome)
            
            return temp_list

        def Resolve_Priest(Opponent_Card, Opponent_Protection):
            
            temp_list=[]
            result=False
            temp_list.append(result)
            if Opponent_Protection == True:
                print("The Opponent Is Protected By Handmaid")
                outcome="The Opponent Played Priest and saw your card: " + str(Opponent_Card)
                temp_list.append(outcome)
            
            else:
                print(f"The Opponent Has {Opponent_Card}")
                outcome="The Opponent Saw Your Card"
                temp_list.append(outcome)
            
            return temp_list

        def Resolve_Baron(Baron_Card, Opponent_Card, Opponent_Protection):
            temp_list=[]
            
            if Opponent_Protection == True:
                print("The Opponent Is Protected By Handmaid")
                outcome="The Opponent Played Baron"
                result=False
            else:
                
                if Baron_Card.card_value()>Opponent_Card.card_value():
                    print("The Opponent Discarded {}".format(Opponent_Card))
                    print("You Win")
                    outcome=""
                    result=True
                
                elif Baron_Card.card_value()<Opponent_Card.card_value():
                    print("You Discarded {} As The Opponent Had {}".format(Baron_Card, Opponent_Card))
                    print("You Lose")
                    outcome=""
                    result=True
                
                elif Baron_Card.card_value()==Opponent_Card.card_value():
                    print("It Is A Draw, You And Your Opponent Both Have {}".format(Baron_Card))
                    result=False
                    outcome="The Opponent Played Baron And It Was A Draw"
            
            temp_list.append(result)
            temp_list.append(outcome)
            return temp_list

        def Resolve_Handmaid(Your_Protection):
            temp_list=[]
            print("You Have Been Protected For 1 Turn")
            result=False
            outcome="The Opponent Played Handmaid"
            Your_Protection=True
            temp_list.append(result)
            temp_list.append(outcome)
            temp_list.append(Your_Protection)
            return temp_list

        def Resolve_Prince(Your_Card, Your_Other_Card, Opponent_Card, Opponent_Protection, card_list):
            
            temp_list=[]
            if Your_Card.card_value()==7:
                temp_list=Resolve_Countess()
                Your_Card=Your_Other_Card
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                temp_list.append(card_list)
                return temp_list
            else:
                if Opponent_Protection==True:
                    print("The Opponent Is Protected By Handmaid")
                    if Your_Card.card_value()==8:
                        print("You Lose")
                        outcome=""
                        result=True
                
                    else:
                        outcome="The Opponent Played Prince And Discarded: "+ str(Your_Card)
                        Your_Card=random.choice(card_list)
                        if len(card_list)!=0:
                            card_list=remove_card(card_list, Your_Card)
                        result=False
                        print("Your New Card Is {}".format(Your_Card))

                else:
                    print("Do You Want To Discard Yourself (Y) Or Your Opponent (O)")
                    ans=str(input())
                    
                    if ans=="Y":
                    
                        if Your_Card.card_value()==8:
                            print("You Lose")
                            outcome=""
                            result=True
                    
                        else:
                            outcome="The Opponent Played Prince And Discarded: " + str(Your_Card)
                            Your_Card=random.choice(card_list)
                            if len(card_list)!=0:
                                card_list=remove_card(card_list, Your_Card)
                            print(f"Your New Card Is {Your_Card}")
                            result=False
                    
                    elif ans == "O":
                    
                        if Opponent_Card.card_value() == 8:
                            print("You Win")
                            outcome=""
                            result=True
                        else:
                            outcome="The Opponent Played Prince And Discarded Your Card: " + str(Opponent_Card)
                            Opponent_Card=random.choice(card_list)
                            if len(card_list)!=0:
                                card_list=remove_card(card_list, Opponent_Card)
                            result=False
                
                temp_list.append(result)
                temp_list.append(outcome)
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                temp_list.append(card_list)
                return temp_list
        
        def Resolve_King(Your_Card, Your_Other_Card, Opponent_Card, Opponent_Protection):
            
            temp_list=[]

            if Your_Card.card_value()==7:
                temp_list=Resolve_Countess()
                Your_Card=Your_Other_Card
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                return temp_list

            else:
                if Opponent_Protection == True:
                    print("The Opponent Is Protected By Handmaid")
                    temp_list=[]
                    result=False
                    outcome="The Opponent Played King"

                
                else:
                    temp=Your_Card
                    Your_Card=Opponent_Card
                    Opponent_Card=temp
                    print(f"Your New Card Is {Your_Card}")
                    temp_list=[]
                    result=False
                    outcome="The Opponent Played King"

                temp_list.append(result)
                temp_list.append(outcome)
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                return temp_list

        def Resolve_Countess():
            temp_list=[]
            outcome="The Opponent Played Countess"
            result=False
            temp_list.append(result)
            temp_list.append(outcome)
            return temp_list

        def Resolve_Princess():
            temp_list=[]
            print("You Lose")
            result=True
            temp_list.append(result)
            outcome=""
            temp_list.append(outcome)
            return temp_list

    
        def Resolve_Guard_Computer_Hard(Opponent_Card, Opponent_Protection):
            temp_list=[]
            guess=random.randint(7,8)

            if Opponent_Protection == True:
                result=False
                temp_list.append(result)
                outcome="The Computer Played Guard"
                temp_list.append(outcome)
            
            else:

                if guess==Opponent_Card.card_value():
                        print("You Lose")
                        result=True
                        temp_list.append(result)
                else:
                    result=False
                    temp_list.append(result)
                    if guess==7:
                        outcome="The Computer played guard And Guessed You As Countess"
                    if guess==8:
                        outcome="The Computer played guard And Guessed You As Princess"

                    temp_list.append(outcome)
            
            return temp_list

        def Resolve_Priest_Computer_Hard(Opponent_Card, Opponent_Protection):
            
            temp_list=[]
            result=False
            temp_list.append(result)
            if Opponent_Protection == True:
                outcome="The Computer Played Priest"
                temp_list.append(outcome)
            
            else:
                outcome="The Computer Played Priest And Saw Your Card: " + str(Opponent_Card)
                temp_list.append(outcome)
            
            return temp_list

        def Resolve_Baron_Computer_Hard(Baron_Card, Opponent_Card, Opponent_Protection):
            temp_list=[]
            
            if Opponent_Protection == True:
                outcome="The Computer Played Baron"
                result=False
            else:
                
                if Baron_Card.card_value()>Opponent_Card.card_value():
                    print("You Lose")
                    outcome=""
                    result=True
                
                elif Baron_Card.card_value()<Opponent_Card.card_value():
                    print("You Win")
                    outcome=""
                    result=True
                
                elif Baron_Card.card_value()==Opponent_Card.card_value():
                    result=False
                    outcome="The Computer Played Baron And It Was A Draw"
            
            temp_list.append(result)
            temp_list.append(outcome)
            return temp_list

        def Resolve_Handmaid_Computer_Hard(Your_Protection):
            temp_list=[]
            result=False
            outcome="The Computer Played Handmaid"
            Your_Protection=True
            temp_list.append(result)
            temp_list.append(outcome)
            temp_list.append(Your_Protection)
            return temp_list

        def Resolve_Prince_Computer_Hard(Your_Card, Your_Other_Card, Opponent_Card, Opponent_Protection, card_list):
            
            temp_list=[]
            if Your_Card.card_value()==7:
                temp_list=Resolve_Countess()
                Your_Card=Your_Other_Card
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                temp_list.append(card_list)
                return temp_list
            
            else:
                if Opponent_Protection==True:
                    if Your_Card.card_value()==8:
                        print("You Win")
                        outcome=""
                        result=True
                
                    else:
                        outcome="The Computer Played Prince And Discarded: "+ str(Your_Card)
                        Your_Card=random.choice(card_list)
                        if len(card_list)!=0:
                            card_list=remove_card(card_list, Your_Card)
                        result=False

                else:
                    selection=["Y","O"]
                    ans=random.choice(selection)
                    
                    if ans=="Y":
                    
                        if Your_Card.card_value()==8:
                            print("You Win")
                            outcome=""
                            result=True
                    
                        else:
                            outcome="The Computer Played Prince And Discarded: " + str(Your_Card)
                            Your_Card=random.choice(card_list)
                            if len(card_list)!=0:
                                card_list=remove_card(card_list, Your_Card)
                            result=False
                    
                    elif ans == "O":
                    
                        if Opponent_Card.card_value() == 8:
                            print("You Lose")
                            outcome=""
                            result=True
                        else:
                            outcome="The Computer Played Prince And Discarded Your Card: " + str(Opponent_Card)
                            Opponent_Card=random.choice(card_list)
                            if len(card_list)!=0:
                                card_list=remove_card(card_list, Opponent_Card)
                            result=False
                
                temp_list.append(result)
                temp_list.append(outcome)
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                temp_list.append(card_list)
                return temp_list
        
        def Resolve_King_Computer_Hard(Your_Card, Your_Other_Card, Opponent_Card, Opponent_Protection):
            
            temp_list=[]

            if Your_Card.card_value()==7:
                temp_list=Resolve_Countess()
                Your_Card=Your_Other_Card
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                return temp_list

            else:
                if Opponent_Protection == True:
                    temp_list=[]
                    result=False
                    outcome="The Computer Played King"

                
                else:
                    temp=Your_Card
                    Your_Card=Opponent_Card
                    Opponent_Card=temp
                    temp_list=[]
                    result=False
                    outcome="The Computer Played King and swapped your card with theirs"

                temp_list.append(result)
                temp_list.append(outcome)
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                return temp_list

        def Resolve_Countess_Computer_Hard():
            temp_list=[]
            outcome="The Computer Played Countess"
            result=False
            temp_list.append(result)
            temp_list.append(outcome)
            return temp_list

        def Resolve_Princess_Computer_Hard():
            temp_list=[]
            print("You Win")
            result=True
            temp_list.append(result)
            outcome=""
            temp_list.append(outcome)
            return temp_list    
    
        
        placeholder=input("")
        placeholder=placeholder
        print("===============")
        print("Player 1's Turn")
        print("===============")

        placeholder=input("")
        placeholder=placeholder
        if counter==0:
            print("=========")
            print("Summary")
            print(temp_list[1])
            print("==========")
        counter=0

        your_card_2=draw_cards(card_list)
        card_list=remove_card(card_list, your_card_2)
        print(f"1.{your_card}: {your_card.ability()}")
        print(f"2.{your_card_2}: {your_card_2.ability()}")
        answer=input("Which Card Would You Like To Play?")
        your_protection=False
        
        if answer=="1":
            if your_card.card_value()==1:
                temp_list=Resolve_Guard(computer_card, computer_protection)
                done=temp_list[0]

            if your_card.card_value()==2:
                temp_list=Resolve_Priest(computer_card, computer_protection)
                done=temp_list[0]

            if your_card.card_value()==3:
                temp_list=Resolve_Baron(your_card_2, computer_card, computer_protection)
                done=temp_list[0]

            if your_card.card_value()==4:
                temp_list=Resolve_Handmaid(your_protection)
                your_protection=temp_list[2]
                done=temp_list[0]

            if your_card.card_value()==5:
                temp_list=Resolve_Prince(your_card_2, your_card, computer_card, computer_protection, card_list)
                done=temp_list[0]
                your_card_2=temp_list[2]
                computer_card=temp_list[3]
                card_list=temp_list[4]

            if your_card.card_value()==6:
                temp_list=Resolve_King(your_card, your_card_2, computer_card, computer_protection)
                done=temp_list[0]
                your_card_2=temp_list[2]
                computer_card=temp_list[3]

            if your_card.card_value()==7:
                temp_list=Resolve_Countess()
                done=temp_list[0]

            if your_card.card_value()==8:
                temp_list=Resolve_Princess()
                done=temp_list[0]

            your_card=your_card_2

        if answer=="2":
            
            if your_card_2.card_value()==1:

                temp_list=Resolve_Guard(computer_card, computer_protection)
                done=temp_list[0]

            if your_card_2.card_value()==2:

                temp_list=Resolve_Priest(computer_card,computer_protection)
                done=temp_list[0]

            if your_card_2.card_value()==3:

                temp_list=Resolve_Baron(your_card, computer_card, computer_protection)
                done=temp_list[0]

            if your_card_2.card_value()==4:

                temp_list=Resolve_Handmaid(your_protection)
                done=temp_list[0]
                your_protection=temp_list[2]
            
            if your_card_2.card_value()==5:
                temp_list=Resolve_Prince()
                done=temp_list[0]
                your_card=temp_list[2]
                computer_card=temp_list[3]
                card_list=temp_list[4]

            if your_card_2.card_value()==6:
                temp_list=Resolve_King(your_card, your_card_2, computer_card, computer_protection)
                done=temp_list[0]
                your_card=temp_list[2]
                computer_card=temp_list[3]

            if your_card_2.card_value()==7:
                temp_list=Resolve_Countess()
                done=temp_list[0]

            if your_card_2.card_value()==8:
                temp_list=Resolve_Princess()
                done=temp_list[0]

        if done==False:
            print("===============")
            print("Computer's Turn")
            print("===============")
            computer_protection=False
            computer_card_2=draw_cards(card_list)
            card_list=remove_card(card_list,computer_card_2)
            answer=random.randint(1,2)
            if answer ==1:
                if computer_card.card_value()==1:

                    temp_list=Resolve_Guard_Computer_Hard(your_card, your_protection)
                    done=temp_list[0]

                if computer_card.card_value()==2:

                    temp_list=Resolve_Priest_Computer_Hard(your_card, your_protection)
                    done=temp_list[0]

                if computer_card.card_value()==3:

                    temp_list=Resolve_Baron_Computer_Hard(computer_card_2, your_card, your_protection)
                    done=temp_list[0]

                if computer_card.card_value()==4:

                    temp_list=Resolve_Handmaid_Computer_Hard(computer_protection)
                    done=temp_list[0]
                    computer_protection=temp_list[2]

                if computer_card.card_value()==5:
                    
                    temp_list=Resolve_Prince_Computer_Hard(computer_card, computer_card_2, your_card, your_protection, card_list)
                    done=temp_list[0]
                    your_card=temp_list[3]
                    computer_card=temp_list[2]  
                    card_list=temp_list[4]              

                if computer_card.card_value()==6:
                    
                    temp_list=Resolve_King_Computer_Hard(computer_card, computer_card_2,your_card,your_protection)
                    computer_card=temp_list[2]
                    your_card=temp_list[3]
                    done=temp_list[0]

                if computer_card.card_value()==7:
                    
                    temp_list=Resolve_Countess_Computer_Hard()
                    done=temp_list[0]

                if computer_card.card_value()==8:
                    
                    temp_list=Resolve_Princess_Computer_Hard()
                    done=temp_list[0]

                computer_card=computer_card_2
            if answer == 2:
                if computer_card_2.card_value()==1:
                    
                    temp_list=Resolve_Guard_Computer_Hard(your_card,your_protection)
                    done=temp_list[0]

                if computer_card_2.card_value()==2:
                    
                    temp_list=Resolve_Priest_Computer_Hard(your_card,your_protection)
                    done=temp_list[0]

                if computer_card_2.card_value()==3:
                    
                    temp_list=Resolve_Baron_Computer_Hard(computer_card,your_card,your_protection)
                    done=temp_list[0]

                if computer_card_2.card_value()==4:
                    
                    temp_list=Resolve_Handmaid_Computer_Hard(computer_protection)
                    done=temp_list[0]
                    computer_protection=temp_list[2]

                if computer_card_2.card_value()==5:
                    
                    temp_list=Resolve_Prince_Computer_Hard(computer_card,computer_card_2,your_card, your_protection,card_list)
                    done=temp_list[0]
                    your_card=temp_list[3]
                    computer_card=temp_list[2]
                    card_list=temp_list[4]

                if computer_card_2.card_value()==6:
                    temp_list=Resolve_King_Computer_Hard(computer_card,computer_card,your_card,your_protection)
                    done=temp_list[0]
                    computer_card=temp_list[2]
                    your_card=temp_list[3]

                if computer_card_2.card_value()==7:
                    temp_list=Resolve_Countess_Computer_Hard()
                    done=temp_list[0]
                if computer_card_2.card_value()==8:
                    temp_list=Resolve_Princess_Computer_Hard()
                    done=temp_list[0]

def princess_extreme(cards):
    your_protection=False
    computer_protection=False
    new_cards=[]
    print("==============")
    new_cards=cards
    card_list=[]
    your_card=draw_cards_original(new_cards)
    card_list=remove_card_original(new_cards, card_list, your_card)
    computer_card=draw_cards(card_list)
    card_list=remove_card(card_list, computer_card)
    done=False
    counter=1
    temp_list=[]
    your_card_log=[]
    computer_card_log=[]
    interaction_log=[]

    while not done:

        def Resolve_Guard(Opponent_Card, Opponent_Protection):
            temp_list=[]
            guess=int(input("Please Guess What Card You Think Your Opponent Has"))
            
            if Opponent_Protection == True:
                print("The Opponent Is Protected By Handmaid")
                result=False
                temp_list.append(result)
                outcome="The Opponent Played Guard"
                temp_list.append(outcome)
            
            else:
                if guess==1:
                    print("Incorrect")
                    result=False
                    temp_list.append(result)
                    outcome="The Opponent Played Guard And Guessed Incorrectly"
                    temp_list.append(outcome)

                elif guess==Opponent_Card.card_value():
                        print("The Opponent Discarded {}".format(Opponent_Card))
                        print("You Win")
                        result=True
                        temp_list.append(result)
                else:
                    print("Incorrect")
                    result=False
                    temp_list.append(result)
                    if guess==2:
                        outcome="The Opponent Played Guard And Guessed You As Priest"
                    if guess==3:
                        outcome="The Opponent Played Guard And Guessed You As Baron"
                    if guess==4:
                        outcome="The Opponent Played Guard And Guessed You As Handmaid"
                    if guess==5:
                        outcome="The Opponent Played Guard And Guessed You As Prince"
                    if guess==6:
                        outcome="The Opponent Played Guard And Guessed You As King"
                    if guess==7:
                        outcome="The Opponent Played Guard And Guessed You As Countess"
                    if guess==8:
                        outcome="The Opponent Played Guard And Guessed You As Princess"
                    temp_list.append(outcome)
            
            return temp_list

        def Resolve_Priest(Opponent_Card, Opponent_Protection):
            
            temp_list=[]
            result=False
            temp_list.append(result)
            if Opponent_Protection == True:
                print("The Opponent Is Protected By Handmaid")
                outcome="The Opponent Played Priest and saw your card: " + str(Opponent_Card)
                temp_list.append(outcome)
            
            else:
                print(f"The Opponent Has {Opponent_Card}")
                outcome="The Opponent Saw Your Card"
                temp_list.append(outcome)
            
            return temp_list

        def Resolve_Baron(Baron_Card, Opponent_Card, Opponent_Protection):
            temp_list=[]
            
            if Opponent_Protection == True:
                print("The Opponent Is Protected By Handmaid")
                outcome="The Opponent Played Baron"
                result=False
            else:
                
                if Baron_Card.card_value()>Opponent_Card.card_value():
                    print("The Opponent Discarded {}".format(Opponent_Card))
                    print("You Win")
                    outcome=""
                    result=True
                
                elif Baron_Card.card_value()<Opponent_Card.card_value():
                    print("You Discarded {} As The Opponent Had {}".format(Baron_Card, Opponent_Card))
                    print("You Lose")
                    outcome=""
                    result=True
                
                elif Baron_Card.card_value()==Opponent_Card.card_value():
                    print("It Is A Draw, You And Your Opponent Both Have {}".format(Baron_Card))
                    result=False
                    outcome="The Opponent Played Baron And It Was A Draw"
            
            temp_list.append(result)
            temp_list.append(outcome)
            return temp_list

        def Resolve_Handmaid(Your_Protection):
            temp_list=[]
            print("You Have Been Protected For 1 Turn")
            result=False
            outcome="The Opponent Played Handmaid"
            Your_Protection=True
            temp_list.append(result)
            temp_list.append(outcome)
            temp_list.append(Your_Protection)
            return temp_list

        def Resolve_Prince(Your_Card, Your_Other_Card, Opponent_Card, Opponent_Protection, card_list):
            
            temp_list=[]
            if Your_Card.card_value()==7:
                temp_list=Resolve_Countess()
                Your_Card=Your_Other_Card
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                temp_list.append(card_list)
                return temp_list
            else:
                if Opponent_Protection==True:
                    print("The Opponent Is Protected By Handmaid")
                    if Your_Card.card_value()==8:
                        print("You Lose")
                        outcome=""
                        result=True
                
                    else:
                        outcome="The Opponent Played Prince And Discarded: "+ str(Your_Card)
                        Your_Card=random.choice(card_list)
                        if len(card_list)!=0:
                            card_list=remove_card(card_list, Your_Card)
                        result=False
                        print("Your New Card Is {}".format(Your_Card))

                else:
                    print("Do You Want To Discard Yourself (Y) Or Your Opponent (O)")
                    ans=str(input())
                    
                    if ans=="Y":
                    
                        if Your_Card.card_value()==8:
                            print("You Lose")
                            outcome=""
                            result=True
                    
                        else:
                            outcome="The Opponent Played Prince And Discarded: " + str(Your_Card)
                            Your_Card=random.choice(card_list)
                            if len(card_list)!=0:
                                card_list=remove_card(card_list, Your_Card)
                            print(f"Your New Card Is {Your_Card}")
                            result=False
                    
                    elif ans == "O":
                    
                        if Opponent_Card.card_value() == 8:
                            print("You Win")
                            outcome=""
                            result=True
                        else:
                            outcome="The Opponent Played Prince And Discarded Your Card: " + str(Opponent_Card)
                            Opponent_Card=random.choice(card_list)
                            if len(card_list)!=0:
                                card_list=remove_card(card_list, Opponent_Card)
                            result=False
                
                temp_list.append(result)
                temp_list.append(outcome)
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                temp_list.append(card_list)
                return temp_list
        
        def Resolve_King(Your_Card, Your_Other_Card, Opponent_Card, Opponent_Protection):
            
            temp_list=[]

            if Your_Card.card_value()==7:
                temp_list=Resolve_Countess()
                Your_Card=Your_Other_Card
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                return temp_list

            else:
                if Opponent_Protection == True:
                    print("The Opponent Is Protected By Handmaid")
                    temp_list=[]
                    result=False
                    outcome="The Opponent Played King"

                
                else:
                    temp=Your_Card
                    Your_Card=Opponent_Card
                    Opponent_Card=temp
                    print(f"Your New Card Is {Your_Card}")
                    temp_list=[]
                    result=False
                    outcome="The Opponent Played King"

                temp_list.append(result)
                temp_list.append(outcome)
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                return temp_list

        def Resolve_Countess():
            temp_list=[]
            outcome="The Opponent Played Countess"
            result=False
            temp_list.append(result)
            temp_list.append(outcome)
            return temp_list

        def Resolve_Princess():
            temp_list=[]
            print("You Lose")
            result=True
            temp_list.append(result)
            outcome=""
            temp_list.append(outcome)
            return temp_list
  
        def Resolve_Guard_Computer_Extreme(Opponent_Card, Opponent_Protection):
            temp_list=[]
            guess=Opponent_Card.card_value()

            if Opponent_Protection == True:
                result=False
                temp_list.append(result)
                outcome="The Computer Played Guard"
                temp_list.append(outcome)
            
            else:
                if guess==1:
                    outcome="The Computer Played Guard and guessed incorrectly"
                    result=False
                    temp_list.append(result)
                    temp_list.append(outcome)

                else:
                    print("You Lose: The Computer Played Guard And Guessed Correctly")
                    result=True
                    temp_list.append(result)
            
            return temp_list

        def Resolve_Priest_Computer_Extreme(Opponent_Card, Opponent_Protection):
            
            temp_list=[]
            result=False
            temp_list.append(result)
            if Opponent_Protection == True:
                outcome="The Computer Played Priest"
                temp_list.append(outcome)
            
            else:
                outcome="The Computer Played Priest And Saw Your Card: " + str(Opponent_Card)
                temp_list.append(outcome)
            
            return temp_list

        def Resolve_Baron_Computer_Extreme(Baron_Card, Opponent_Card, Opponent_Protection):
            temp_list=[]
            result=False
            outcome=""
            if Opponent_Protection == True:
                outcome="The Computer Played Baron"
                result=False
            else:
                
                if Baron_Card.card_value()>Opponent_Card.card_value():
                    print("You Lose The Computer Played Baron")
                    outcome=""
                    result=True
            
            temp_list.append(result)
            temp_list.append(outcome)
            return temp_list

        def Resolve_Handmaid_Computer_Extreme(Your_Protection):
            temp_list=[]
            result=False
            outcome="The Computer Played Handmaid"
            Your_Protection=True
            temp_list.append(result)
            temp_list.append(outcome)
            temp_list.append(Your_Protection)
            return temp_list

        def Resolve_Prince_Computer_Extreme(Your_Card, Your_Other_Card, Opponent_Card, Opponent_Protection, card_list):
            
            temp_list=[]
            if Your_Card.card_value()==7:
                temp_list=Resolve_Countess()
                Your_Card=Your_Other_Card
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                temp_list.append(card_list)
                return temp_list
            else:
                if Opponent_Protection==True:
                    if Your_Card.card_value()==2 or Your_Card.card_value()==6:
                        ans="Y"
                    else:
                        ans="O"
                    if ans=="Y":
                        outcome="The Computer Played Prince And Discarded: "+str(Your_Card)
                        Your_Card=random.choice(card_list)
                        if len(card_list)!=0:
                            card_list=remove_card(card_list,Your_Card)
                        result=False
                    if ans =="O":
                        outcome="The Computer Played Prince but didn't discard"
                        result=False

                else:
                    if Opponent_Card.card_value()==8:
                        ans="O"                    
                    elif Your_Card.card_value()==6:
                        ans="Y"
                    elif Your_Card.card_value()==8:
                        ans="O"
                    elif Your_Card.card_value()==2:
                        ans="Y"
                    else:
                        ans="O"
                    
                    if ans=="Y":
                    
                        outcome="The Computer Played Prince And Discarded: " + str(Your_Card)
                        Your_Card=random.choice(card_list)
                        if len(card_list)!=0:
                            card_list=remove_card(card_list, Your_Card)
                        result=False
                    
                    elif ans == "O":
                    
                        if Opponent_Card.card_value() == 8:
                            print("You Lose")
                            outcome=""
                            result=True
                        else:
                            outcome="The Computer Played Prince And Discarded Your Card: " + str(Opponent_Card)
                            Opponent_Card=random.choice(card_list)
                            if len(card_list)!=0:
                                card_list=remove_card(card_list, Opponent_Card)
                            result=False
                
                temp_list.append(result)
                temp_list.append(outcome)
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                temp_list.append(card_list)
                return temp_list
        
        def Resolve_King_Computer_Extreme(Your_Card, Your_Other_Card, Opponent_Card, Opponent_Protection):
            
            temp_list=[]

            if Your_Card.card_value()==7:
                temp_list=Resolve_Countess()
                Your_Card=Your_Other_Card
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                return temp_list

            else:
                if Opponent_Protection == True:
                    temp_list=[]
                    result=False
                    outcome="The Computer Played King"

                
                else:
                    temp=Your_Card
                    Your_Card=Opponent_Card
                    Opponent_Card=temp
                    temp_list=[]
                    result=False
                    outcome="The Computer Played King and swapped your card with theirs"

                temp_list.append(result)
                temp_list.append(outcome)
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                return temp_list

        def Resolve_Countess_Computer_Extreme():
            temp_list=[]
            outcome="The Computer Played Countess"
            result=False
            temp_list.append(result)
            temp_list.append(outcome)
            return temp_list

        def Resolve_Princess_Computer_Extreme():
            temp_list=[]
            print("You Win")
            result=True
            temp_list.append(result)
            outcome=""
            temp_list.append(outcome)
            return temp_list    
    
        
        placeholder=input("")
        placeholder=placeholder
        print("===============")
        print("Player 1's Turn")
        print("===============")

        placeholder=input("")
        placeholder=placeholder
        if counter==0:
            print("=========")
            print("Summary")
            print(temp_list[1])
            print("==========")
        counter=0

        your_card_2=draw_cards(card_list)

        your_string=""
        your_string=str(your_card)+str(' / ')+str(your_card_2)
        your_card_log.append(your_string)

        card_list=remove_card(card_list, your_card_2)
        print(f"1.{your_card}: {your_card.ability()}")
        print(f"2.{your_card_2}: {your_card_2.ability()}")
        answer=input("Which Card Would You Like To Play?")
        your_protection=False
        
        if answer=="1":
            if your_card.card_value()==1:
                temp_list=Resolve_Guard(computer_card, computer_protection)
                done=temp_list[0]

            if your_card.card_value()==2:
                temp_list=Resolve_Priest(computer_card, computer_protection)
                done=temp_list[0]

            if your_card.card_value()==3:
                temp_list=Resolve_Baron(your_card_2, computer_card, computer_protection)
                done=temp_list[0]

            if your_card.card_value()==4:
                temp_list=Resolve_Handmaid(your_protection)
                your_protection=temp_list[2]
                done=temp_list[0]

            if your_card.card_value()==5:
                temp_list=Resolve_Prince(your_card_2, your_card, computer_card, computer_protection, card_list)
                done=temp_list[0]
                your_card_2=temp_list[2]
                computer_card=temp_list[3]
                card_list=temp_list[4]

            if your_card.card_value()==6:
                temp_list=Resolve_King(your_card, your_card_2, computer_card, computer_protection)
                done=temp_list[0]
                your_card_2=temp_list[2]
                computer_card=temp_list[3]

            if your_card.card_value()==7:
                temp_list=Resolve_Countess()
                done=temp_list[0]

            if your_card.card_value()==8:
                temp_list=Resolve_Princess()
                done=temp_list[0]

            your_card=your_card_2

        if answer=="2":
            
            if your_card_2.card_value()==1:

                temp_list=Resolve_Guard(computer_card, computer_protection)
                done=temp_list[0]

            if your_card_2.card_value()==2:

                temp_list=Resolve_Priest(computer_card,computer_protection)
                done=temp_list[0]

            if your_card_2.card_value()==3:

                temp_list=Resolve_Baron(your_card, computer_card, computer_protection)
                done=temp_list[0]

            if your_card_2.card_value()==4:

                temp_list=Resolve_Handmaid(your_protection)
                done=temp_list[0]
                your_protection=temp_list[2]
            
            if your_card_2.card_value()==5:
                temp_list=Resolve_Prince(your_card,your_card_2,computer_card, computer_protection, card_list)
                done=temp_list[0]
                your_card=temp_list[2]
                computer_card=temp_list[3]
                card_list=temp_list[4]

            if your_card_2.card_value()==6:
                temp_list=Resolve_King(your_card, your_card_2, computer_card, computer_protection)
                done=temp_list[0]
                your_card=temp_list[2]
                computer_card=temp_list[3]

            if your_card_2.card_value()==7:
                temp_list=Resolve_Countess()
                done=temp_list[0]

            if your_card_2.card_value()==8:
                temp_list=Resolve_Princess()
                done=temp_list[0]

        if done==False:
            print("===============")
            print("Computer's Turn")
            print("===============")
            computer_protection=False
            computer_card_2=draw_cards(card_list)

            computer_string=""
            computer_string=str(computer_card)+ str(' / ')+str(computer_card_2)
            computer_card_log.append(computer_string)

            card_list=remove_card(card_list,computer_card_2)

            if computer_card.card_value()==8:
                answer=2
            elif computer_card_2.card_value()==8:
                answer=1
            elif computer_card.card_value()==3 and computer_card_2.card_value()>your_card.card_value():
                answer=1
            elif computer_card_2.card_value()==3 and computer_card.card_value()>your_card.card_value():
                answer=2
            elif computer_card_2.card_value()==4:
                answer=2
            elif computer_card.card_value()==4:
                answer=1
            elif computer_card.card_value()==6:
                answer=2
            elif computer_card_2.card_value()==6:
                answer=1
            elif computer_card.card_value()==3:
                answer=2
            elif computer_card_2.card_value()==3:
                answer=1
            else:
                answer=random.randint(1,2)

            if answer ==1:
                if computer_card.card_value()==1:

                    temp_list=Resolve_Guard_Computer_Extreme(your_card, your_protection)
                    done=temp_list[0]

                if computer_card.card_value()==2:

                    temp_list=Resolve_Priest_Computer_Extreme(your_card, your_protection)
                    done=temp_list[0]

                if computer_card.card_value()==3:

                    temp_list=Resolve_Baron_Computer_Extreme(computer_card_2, your_card, your_protection)
                    done=temp_list[0]

                if computer_card.card_value()==4:

                    temp_list=Resolve_Handmaid_Computer_Extreme(computer_protection)
                    done=temp_list[0]
                    computer_protection=temp_list[2]

                if computer_card.card_value()==5:
                    
                    temp_list=Resolve_Prince_Computer_Extreme(computer_card, computer_card_2, your_card, your_protection, card_list)
                    done=temp_list[0]
                    your_card=temp_list[3]
                    computer_card=temp_list[2]  
                    card_list=temp_list[4]              

                if computer_card.card_value()==6:
                    
                    temp_list=Resolve_King_Computer_Extreme(computer_card, computer_card_2,your_card,your_protection)
                    computer_card=temp_list[2]
                    your_card=temp_list[3]
                    done=temp_list[0]

                if computer_card.card_value()==7:
                    
                    temp_list=Resolve_Countess_Computer_Extreme()
                    done=temp_list[0]

                if computer_card.card_value()==8:
                    
                    temp_list=Resolve_Princess_Computer_Extreme()
                    done=temp_list[0]

                computer_card=computer_card_2
            if answer == 2:
                if computer_card_2.card_value()==1:
                    
                    temp_list=Resolve_Guard_Computer_Extreme(your_card,your_protection)
                    done=temp_list[0]

                if computer_card_2.card_value()==2:
                    
                    temp_list=Resolve_Priest_Computer_Extreme(your_card,your_protection)
                    done=temp_list[0]

                if computer_card_2.card_value()==3:
                    
                    temp_list=Resolve_Baron_Computer_Extreme(computer_card,your_card,your_protection)
                    done=temp_list[0]

                if computer_card_2.card_value()==4:
                    
                    temp_list=Resolve_Handmaid_Computer_Extreme(computer_protection)
                    done=temp_list[0]
                    computer_protection=temp_list[2]

                if computer_card_2.card_value()==5:
                    
                    temp_list=Resolve_Prince_Computer_Extreme(computer_card,computer_card_2,your_card, your_protection,card_list)
                    done=temp_list[0]
                    your_card=temp_list[3]
                    computer_card=temp_list[2]
                    card_list=temp_list[4]

                if computer_card_2.card_value()==6:

                    temp_list=Resolve_King_Computer_Extreme(computer_card,computer_card,your_card,your_protection)
                    done=temp_list[0]
                    computer_card=temp_list[2]
                    your_card=temp_list[3]

                if computer_card_2.card_value()==7:
                    temp_list=Resolve_Countess_Computer_Extreme()
                    done=temp_list[0]
                if computer_card_2.card_value()==8:
                    temp_list=Resolve_Princess_Computer_Extreme()
                    done=temp_list[0]
    log=[]
    log.append(your_card_log)
    log.append(computer_card_log)
    placeholder=input("")
    if placeholder==str("!log"):
        print(log)
    else:
        placeholder=placeholder

def princess2(cards):

    player_1_protection=False
    player_2_protection=False
    new_cards=[]
    print("==============")

    new_cards=cards
    card_list=[]
    player_1_card=draw_cards_original(new_cards)
    card_list=remove_card_original(new_cards,card_list,player_1_card)
    player_2_card=draw_cards(card_list)
    card_list=remove_card(card_list,player_2_card)
    done=False
    counter=1

    while not done:

        def Resolve_Guard(Opponent_Card, Opponent_Protection):
            temp_list=[]
            guess=int(input("Please Guess What Card You Think Your Opponent Has "))
            
            if Opponent_Protection == True:
                print("The Opponent Is Protected By Handmaid")
                result=False
                temp_list.append(result)
                outcome="The Opponent Played Guard"
                temp_list.append(outcome)
            
            else:
                if guess==1:
                    print("Incorrect")
                    result=False
                    temp_list.append(result)
                    outcome="The Opponent Played Guard And Guessed Incorrectly"
                    temp_list.append(outcome)

                elif guess==Opponent_Card.card_value():
                        print("The Opponent Discarded {}".format(Opponent_Card))
                        print("You win")
                        result=True
                        temp_list.append(result)
                else:
                    print("Incorrect")
                    result=False
                    temp_list.append(result)
                    if guess==2:
                        outcome="The Opponent Played Guard And Guessed You As Priest"
                    if guess==3:
                        outcome="The Opponent Played Guard And Guessed You As Baron"
                    if guess==4:
                        outcome="The Opponent Played Guard And Guessed You As Handmaid"
                    if guess==5:
                        outcome="The Opponent Played Guard And Guessed You As Prince"
                    if guess==6:
                        outcome="The Opponent Played Guard And Guessed You As King"
                    if guess==7:
                        outcome="The Opponent Played Guard And Guessed You As Countess"
                    if guess==8:
                        outcome="The Opponent Played Guard And Guessed You As Princess"
                    temp_list.append(outcome)
            
            return temp_list

        def Resolve_Priest(Opponent_Card, Opponent_Protection):
            
            temp_list=[]
            result=False
            temp_list.append(result)
            if Opponent_Protection == True:
                print("The Opponent Is Protected By Handmaid")
                outcome="The Opponent Played Priest and did not see your card"
                temp_list.append(outcome)
            
            else:
                print(f"The Opponent Has {Opponent_Card}")
                outcome="The Opponent Saw Your Card"
                temp_list.append(outcome)
            
            return temp_list

        def Resolve_Baron(Baron_Card, Opponent_Card, Opponent_Protection):
            temp_list=[]
            
            if Opponent_Protection == True:
                print("The Opponent is Protected By Handmaid")
                outcome="The Opponent Played Baron"
                result=False
            else:
                
                if Baron_Card.card_value()>Opponent_Card.card_value():
                    print("The Opponent Discarded {}".format(Opponent_Card))
                    print("You Win")
                    outcome=""
                    result=True
                
                elif Baron_Card.card_value()<Opponent_Card.card_value():
                    print("You Discarded {} As The Opponent Had {}".format(Baron_Card, Opponent_Card))
                    print("Opponent Wins")
                    outcome=""
                    result=True
                
                elif Baron_Card.card_value()==Opponent_Card.card_value():
                    print("It Is A Draw, You And Your Opponent Both Have {}".format(Baron_Card))
                    result=False
                    outcome="The Opponent Played Baron And It Was A Draw"
            
            temp_list.append(result)
            temp_list.append(outcome)
            return temp_list

        def Resolve_Handmaid(Your_Protection):
            temp_list=[]
            print("You Have Been Protected For 1 Turn")
            result=False
            outcome="The Opponent Played Handmaid"
            Your_Protection=True
            temp_list.append(result)
            temp_list.append(outcome)
            temp_list.append(Your_Protection)
            return temp_list

        def Resolve_Prince(Your_Card, Your_Other_Card, Opponent_Card, Opponent_Protection, card_list):
            
            temp_list=[]
            if Your_Card.card_value()==7:
                temp_list=Resolve_Countess()
                Your_Card=Your_Other_Card
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                temp_list.append(card_list)
                return temp_list
            
            else:
                if Opponent_Protection==True:
                    print("The opponent Is Protected By Handmaid")
                    ans=input("Do you want to discard yourself? (Y/N)")
                    if ans=="Y":
                        if Your_Card.card_value()==8:
                            print("You Lose")
                            outcome=""
                            result=True
                        else:
                            outcome="The Opponent Played Prince And Discarded: "+ str(Your_Card)
                            Your_Card=random.choice(card_list)
                            if len(card_list)!=0:
                                card_list=remove_card(card_list, Your_Card)
                            result=False
                            print("Your New Card Is {}".format(Your_Card))
                    else:
                        outcome="The Opponent Played Prince"

                else:
                    print("Do You Want To Discard Yourself (Y) Or Your Opponent (O)")
                    ans=str(input())
                    
                    if ans=="Y":
                    
                        if Your_Card.card_value()==8:
                            print("You Lose")
                            outcome=""
                            result=True
                    
                        else:
                            outcome="The Opponent Played Prince And Discarded: " + str(Your_Card)
                            Your_Card=random.choice(card_list)
                            if len(card_list)!=0:
                                card_list=remove_card(card_list, Your_Card)
                            print(f"Your New Card Is {Your_Card}")
                            result=False
                    
                    elif ans == "O":
                    
                        if Opponent_Card.card_value() == 8:
                            print("You Win")
                            outcome=""
                            result=True
                        else:
                            outcome="The Opponent Played Prince And Discarded Your Card: " + str(Opponent_Card)
                            Opponent_Card=random.choice(card_list)
                            if len(card_list)!=0:
                                card_list=remove_card(card_list, Opponent_Card)
                            result=False
                
                temp_list.append(result)
                temp_list.append(outcome)
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                temp_list.append(card_list)
                return temp_list
        
        def Resolve_King(Your_Card, Your_Other_Card, Opponent_Card, Opponent_Protection):
            
            temp_list=[]

            if Your_Card.card_value()==7:
                temp_list=Resolve_Countess()
                Your_Card=Your_Other_Card
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                return temp_list

            else:
                if Opponent_Protection == True:
                    print("The Opponent Is Protected By Handmaid")
                    temp_list=[]
                    result=False
                    outcome="The Opponent Played King"

                
                else:
                    temp=Your_Card
                    Your_Card=Opponent_Card
                    Opponent_Card=temp
                    print(f"Your New Card Is {Your_Card}")
                    temp_list=[]
                    result=False
                    outcome="The Opponent Played King"

                temp_list.append(result)
                temp_list.append(outcome)
                temp_list.append(Your_Card)
                temp_list.append(Opponent_Card)
                return temp_list

        def Resolve_Countess():
            temp_list=[]
            outcome="The Opponent Played Countess"
            result=False
            temp_list.append(result)
            temp_list.append(outcome)
            return temp_list

        def Resolve_Princess():
            temp_list=[]
            print("You Lose")
            result=True
            temp_list.append(result)
            outcome=""
            temp_list.append(outcome)
            return temp_list

                
        placeholder=input("")
        placeholder=placeholder
        print("")
        print("")
        print("")
        print("")
        print("===============")
        print("Player 1's Turn")
        print("===============")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")

        placeholder=input("")
        placeholder=placeholder
        
        if counter==0:
            print("========")
            print("Summary")
            print(temp_list[1])
            print("==========")
        counter=0

        player_1_card_2=draw_cards(card_list)
        card_list=remove_card(card_list,player_1_card_2)
        print(f"1.{player_1_card}: {player_1_card.ability()}")
        print(f"2.{player_1_card_2}: {player_1_card_2.ability()}")
        answer=input("Which Card Would You Like To Play?")
        player_1_protection=False

        if answer=="1":

            if player_1_card.card_value()==1:
                
                temp_list=Resolve_Guard(player_2_card, player_2_protection)
                done=temp_list[0]
    
            elif player_1_card.card_value()==2:
                
                temp_list=Resolve_Priest(player_2_card, player_2_protection)
                done=temp_list[0]
            
            elif player_1_card.card_value()==3:
                
                temp_list=Resolve_Baron(player_1_card_2, player_2_card, player_2_protection)
                done=temp_list[0]

            elif player_1_card.card_value()==4:
                
                temp_list=Resolve_Handmaid(player_1_protection)
                player_1_protection=temp_list[2]
                done=temp_list[0]
            
            elif player_1_card.card_value()==5:
                temp_list=Resolve_Prince(player_1_card_2, player_1_card, player_2_card, player_2_protection, card_list)
                done=temp_list[0]
                player_1_card_2=temp_list[2]
                player_2_card=temp_list[3]
                card_list=temp_list[4]

            elif player_1_card.card_value()==6:
            
                temp_list=Resolve_King(player_1_card_2, player_1_card, player_2_card, player_2_protection)
                player_1_card_2=temp_list[2]
                player_2_card=temp_list[3]
                done=temp_list[0]
        
            elif player_1_card.card_value()==7:
                
                temp_list=Resolve_Countess()
                done=temp_list[0]
                    
            elif player_1_card.card_value()==8:
                temp_list=Resolve_Princess()
                done=temp_list[0]

            player_1_card=player_1_card_2
        
        elif answer=="2":
            
            if player_1_card_2.card_value()==1:
                temp_list=Resolve_Guard(player_2_card, player_2_protection)
                done=temp_list[0]

            elif player_1_card_2.card_value()==2:
                temp_list=Resolve_Priest(player_2_card, player_2_protection)
                done=temp_list[0]

            elif player_1_card_2.card_value()==3:
                temp_list=Resolve_Baron(player_1_card, player_2_card, player_2_protection)
                done=temp_list[0]

            elif player_1_card_2.card_value()==4:
                temp_list=Resolve_Handmaid(player_1_protection)
                player_1_protection=temp_list[2]
                done=temp_list[0]
            
            elif player_1_card_2.card_value()==5:
                temp_list=Resolve_Prince(player_1_card, player_1_card_2, player_2_card, player_2_protection, card_list)
                player_1_card=temp_list[2]
                player_2_card=temp_list[3]
                card_list=temp_list[4]

            elif player_1_card_2.card_value()==6:

                temp_list=Resolve_King(player_1_card, player_1_card_2, player_2_card,player_2_protection)
                player_1_card=temp_list[2]
                player_2_card=temp_list[3]
                done=temp_list[0]
            
            elif player_1_card_2.card_value()==7:
                temp_list=Resolve_Countess()
                done=temp_list[0]
            
            elif player_1_card_2.card_value()==8:
                temp_list=Resolve_Princess()
                done=temp_list[0]
        
        if done==False:
            
            placeholder=input("")
            placeholder=placeholder
            print("")
            print("")
            print("")
            print("")
            print("===============")
            print("Player 2's Turn")
            print("===============")
            print("")
            print("")
            print("")
            print("")
            print("")
            placeholder=input("")
            placeholder=placeholder

            print("==================")
            print("Summary Of Last Turn")
            print(temp_list[1])
            player_2_card_2=draw_cards(card_list)
            card_list=remove_card(card_list,player_2_card_2)
            print("=====================================")
            print(f"Your Cards Are {player_2_card} And {player_2_card_2}")
            print(f"1.{player_2_card}: {player_2_card.ability()}")
            print(f"2.{player_2_card_2}: {player_2_card_2.ability()}")
            answer=input("Which Card Would You Like To Play?")
            player_2_protection=False
            
            if answer=="1":

                if player_2_card.card_value()==1:
                    temp_list=Resolve_Guard(player_1_card,player_1_protection)
                    done=temp_list[0]

                elif player_2_card.card_value()==2:
                    temp_list=Resolve_Priest(player_1_card,player_1_protection)
                    done=temp_list[0]

                elif player_2_card.card_value()==3:
                    temp_list=Resolve_Baron(player_2_card_2,player_1_card,player_1_protection)
                    done=temp_list[0]

                elif player_2_card.card_value()==4:
                    temp_list=Resolve_Handmaid(player_2_protection)
                    player_2_protection=temp_list[2]
                    done=temp_list[0]

                elif player_2_card.card_value()==5:
                    temp_list=Resolve_Prince(player_2_card_2, player_2_card, player_1_card,player_1_protection, card_list)                
                    done=temp_list[0]
                    player_2_card_2=temp_list[2]
                    player_1_card=temp_list[3]
                    card_list=temp_list[4]

                elif player_2_card.card_value()==6:
                    
                    temp_list=Resolve_King(player_2_card_2, player_2_card, player_1_card,player_1_protection)
                    player_2_card_2=temp_list[2]
                    player_1_card=temp_list[3]
                    done=temp_list[0]
                
                elif player_2_card.card_value()==7:
                    temp_list=Resolve_Countess()
                    done=temp_list[0]
                
                elif player_2_card.card_value()==8:
                    temp_list=Resolve_Princess()
                    done=temp_list[0]

                player_2_card=player_2_card_2
            
            elif answer=="2":
                
                if player_2_card_2.card_value()==1:
                    temp_list=Resolve_Guard(player_1_card,player_1_protection)
                    done=temp_list[0]
                
                elif player_2_card_2.card_value()==2:
                    temp_list=Resolve_Priest(player_1_card,player_1_protection)
                    done=temp_list[0]

                elif player_2_card_2.card_value()==3:
                    temp_list=Resolve_Baron(player_2_card,player_1_card,player_1_protection)
                    done=temp_list[0]

                elif player_2_card_2.card_value()==4:
                    temp_list=Resolve_Handmaid(player_2_protection)
                    player_2_protection=temp_list[2]
                    done=temp_list[0]
                
                elif player_2_card_2.card_value()==5:
                    temp_list=Resolve_Prince(player_2_card, player_2_card_2, player_1_card,player_1_protection, card_list)
                    done=temp_list[0]
                    player_1_card=temp_list[2]
                    player_2_card=temp_list[3]
                    card_list=temp_list[4]

                elif player_2_card_2.card_value()==6:
                    

                    temp_list=Resolve_King(player_2_card, player_2_card_2, player_1_card,player_1_protection)
                    player_2_card=temp_list[2]
                    player_1_card=temp_list[3]
                    done=temp_list[0]
                
                elif player_2_card_2.card_value()==7:
                    temp_list=Resolve_Countess()
                    done=temp_list[0]
                
                elif player_2_card_2.card_value()==8:
                    temp_list=Resolve_Princess()
                    done=temp_list[0]
    
        if len(card_list)==0:
            done=True
            if player_1_card.card_value()>player_2_card.card_value():
                print("You Win")
            elif player_1_card.card_value()<player_2_card.card_value():
                print("Opponent Wins")
            elif player_1_card.card_value()==player_2_card.card_value():
                print("Tie")

def Princess_Rules():
    print("========================")
    print("The rules are as follows")
    print("1. At any time, all players will have one card")
    print("2. On your turn, you will draw a card, then choose one of the two cards to play")
    print("3. At the end of the deck (if there are still people playing) then the highest card wins")
    print("========================")
    placeholder=input("")
    placeholder=placeholder

def Princess_Cards(cards):
    print("==============================")
    print("These are the cards in the deck")
    print(f"| # |     Card    | Frequency|")
    print(f"| 1 |     {cards[0]}   |     5    |")
    print(f"| 2 |    {cards[6]}   |     2    |")
    print(f"| 3 |     {cards[8]}   |     2    |")
    print(f"| 4 |  {cards[9]}   |     2    |")
    print(f"| 5 |     {cards[11]}  |     2    |")
    print(f"| 6 |       {cards[13]}  |     1    |")
    print(f"| 7 |   {cards[14]}  |     1    |")
    print(f"| 8 |   {cards[15]}  |     1    |")
    print("==============================")
    ans=int(input("Which card would you like to know more about?"))
    if ans <9:
        
        if ans==1:
            print("===============")
            print(f"{cards[0].ability()}")
            print("===========")

        elif ans == 2:
            print("==========")
            print(f"{cards[6].ability()}")
            print("===========")

        elif ans == 3:
            print("==============")
            print(f"{cards[8].ability()}")
            print("=============")

        elif ans == 4:
            print("===============")
            print(f"{cards[9].ability()}")
            print("===============")

        elif ans == 5:
            print("=============")
            print(f"{cards[11].ability()}")
            print("=============")

        elif ans == 6:
            print("===========")
            print(f"{cards[13].ability()}")
            print("=============")

        elif ans == 7:
            print("===========")
            print(f"{cards[14].ability()}")
            print("=============")

        elif ans == 8:
            print("===========")
            print(f"{cards[15].ability()}")
            print("=============")
        
        answer=input("Do you want to select another card? (Y/N)")
        
        if answer == "Y":
            Princess_Cards(cards)
        
        elif answer=="N":
            pass

    placeholder=input("")
    placeholder=placeholder
    
def princess_how_to(cards):
    print("=======-----------------")
    print("1. The rules of the game")
    print("2. The cards in the game")
    print("========================")
    ans=int(input(""))
    if ans==1:
        Princess_Rules()
    if ans==2:
        Princess_Cards(cards)

def princess():
    
    class guard:
        def __init__(self):
            self.__ability="Guess an opponents card"
            self.__card_value=1
            self.__name="Guard"
        def ability(self):
            return self.__ability
        def card_value(self):
            return self.__card_value
        def __repr__(self):
            return self.__name

    class priest:
        def __init__(self):
            self.__ability="Look at an opponents card"
            self.__card_value=2
            self.__name="Priest"
        def ability(self):
            return self.__ability
        def card_value(self):
            return self.__card_value
        def __repr__(self):
            return self.__name

    class baron:
        def __init__(self):
            self.__ability="Compare your card with the opponents card"
            self.__card_value=3
            self.__name="Baron"
        def ability(self):
            return self.__ability
        def card_value(self):
            return self.__card_value
        def __repr__(self):
            return self.__name

    class handmaid:
        def __init__(self):
            self.__ability="Protect yourself for 1 turn"
            self.__card_value=4
            self.__name="Handmaid"
        def ability(self):
            return self.__ability
        def card_value(self):
            return self.__card_value
        def __repr__(self):
            return self.__name

    class prince:
        def __init__(self):
            self.__ability="Your opponent discards their card and draws another"
            self.__card_value=5
            self.__name="Prince"
        def ability(self):
            return self.__ability
        def card_value(self):
            return self.__card_value
        def __repr__(self):
            return self.__name
    
    class king:
        def __init__(self):
            self.__ability="Swap your card with your opponents"
            self.__card_value=6
            self.__name="King"
        def ability(self):
            return self.__ability
        def card_value(self):
            return self.__card_value
        def __repr__(self):
            return self.__name

    class countess:
        def __init__(self):
            self.__ability="Immediately discard if with the prince or king"
            self.__card_value=7
            self.__name="Countess"
        def ability(self):
            return self.__ability
        def card_value(self):
            return self.__card_value
        def __repr__(self):
            return self.__name

    class princess:
        def __init__(self):
            self.__ability="If discarded, you lose"
            self.__card_value=8
            self.__name="Princess"
        def ability(self):
            return self.__ability
        def card_value(self):
            return self.__card_value
        def __repr__(self):
            return self.__name

    cards=[guard(),guard(),guard(),guard(),guard(),priest(),priest(),baron(),baron(),handmaid(),handmaid(),prince(),prince(),king(),countess(),princess()]
    
    print("========")
    print("1. One player")
    print("2. Two players")
    print("3. How To Play")
    print("========")
    answer=input("Please enter the desired option")
    if answer =="1":
        princess1(cards)
    if answer == "2":
        princess2(cards)
    if answer == "3":
        princess_how_to(cards)
    if answer == "9":
        pass

def Print_Card(player_card):
    count=""
    player_points=0
    if str(player_card[0])=="J":
        player_points+=11
    elif str(player_card[0])=="Q":
        player_points+=12
    elif str(player_card[0])=="K":
        player_points+=13
    elif str(player_card[0])=="0":
        player_points+=10
    elif str(player_card[0])=="A":
        player_points+=1
    else:
        player_points+=int(player_card[0])

    if player_points==1:
        count="Ace"
    elif player_points==2:
        count="Two"
    elif player_points==3:
        count="Three"
    elif player_points==4:
        count="Four"
    elif player_points==5:
        count="Five"
    elif player_points==6:
        count="Six"
    elif player_points==7:
        count="Seven"
    elif player_points==8:
        count="Eight"
    elif player_points==9:
        count="Nine"
    elif player_points==10:
        count="Ten"
    elif player_points==11:
        count="Jack"
    elif player_points==12:
        count="Queen"
    elif player_points==13:
        count="King"
    if player_points>10:
        player_points=10
    
    playing_card=""
    playing_card=playing_card + count
    playing_card=playing_card + " of "
    playing_card=playing_card + player_card[1:]
    info_list=[]
    info_list.append(player_points)
    info_list.append(count)
    info_list.append(playing_card)
    return info_list

def BlackJack_2():
    Deck=["ASpades","2Spades","3Spades","4Spades","5Spades","6Spades","7Spades","8Spades","9Spades","0Spades","JSpades","QSpades","KSpades","AClubs","2Clubs","3Clubs","4Clubs","5Clubs","6Clubs","7Clubs","8Clubs","9Clubs","0Clubs","JClubs","QClubs","KClubs","ADiamonds","2Diamonds","3Diamonds","4Diamonds","5Diamonds","6Diamonds","7Diamonds","8Diamodns","9Diamonds","0Diamonds","JDiamonds","QDiamonds","KDiamonds","AHearts","2Hearts","3Hearts","4Hearts","5Hearts","6Hearts","7Hearts","8Hearts","9Hearts","0Hearts","JHearts","QHearts","KHearts"]
    card_list=[]
    card_list=Deck
    player_2_points=0
    player_1_points=0
    player_1_cards=[]
    player_2_cards=[]
    winner=[]
    
    for _ in range(2):
        player_1_card=draw_cards(card_list)
        card_list=remove_card(card_list, player_1_card)
        info_list_1=Print_Card(player_1_card)
        player_1_points+=info_list_1[0]
        player_1_cards.append(info_list_1[2])


        player_2_card=draw_cards(card_list)
        card_list=remove_card(card_list, player_2_card)
        info_list_2=Print_Card(player_2_card)
        player_2_points+=info_list_2[0]
        player_2_cards.append(info_list_2[2])

    game_over=False
    stand_1=False
    stand_2=False
    while game_over==False:
        
        if player_1_points <22 and stand_1==False:

            print("========")
            print("Player 1")
            print("========")

            placeholder=input("")
            placeholder=placeholder

            print(f"Your cards")
            for item in player_1_cards:
                print(item)

            print("============================")
            answer=str(input("Do you want to hit or stand?"))
            print("===============================")
            if answer=="hit":
                
                stand_1=False
                player_1_card=draw_cards(card_list)
                card_list=remove_card(card_list, player_1_card)
                info_list_1=Print_Card(player_1_card)
                player_1_points+=info_list_1[0]
                player_1_cards.append(info_list_1[2])
                print(f"Your next card is: {info_list_1[2]}")
            else:
                stand_1=True

            if player_1_points>22:
                print("====")
                print("Bust: Your total was too high")
                print("====")
                stand_1=True
            elif player_1_points==21:
                stand_1=True


        if player_2_points <22 and stand_2==False:

            placeholder=input()
            placeholder=placeholder


            print("========")
            print("Player 2")
            print("========")

            placeholder=input()
            placeholder=placeholder

            print("============")
            print(f"Your cards")
            for item in player_2_cards:
                print(item)

            print("============================")
            answer=str(input("Do you want to hit or stand?"))
            print("===============================")
            if answer=="hit":
                
                stand_2=False
                player_2_card=draw_cards(card_list)
                card_list=remove_card(card_list, player_2_card)
                info_list_2=Print_Card(player_2_card)
                player_2_points+=info_list_2[0]
                player_2_cards.append(info_list_2[2])
                print(f"Your next card is: {info_list_2[2]}")
            else:
                stand_2=True

            if player_2_points>22:
                print("====")
                print("Bust: Your total was too high")
                print("====")
                stand_2=True
            if player_2_points==21:
                stand_2=True


        if stand_1==True and stand_2==True:
            game_over=True
            if player_1_points>21 and player_2_points>21:
                winner.append("Neither")
                ending_string=""
                ending_string="Both players went over 21"

            elif player_1_points>21:
                winner.append("Player 2")
                ending_string=""
                ending_string="Player One went over 21"
            elif player_2_points>21:
                winner.append("Player 1")
                ending_string=""
                ending_string="Player Two went over 21"
            else:
                if player_1_points==21 and player_2_points==21:
                    winner.append("Neither")
                    ending_string=""
                    ending_string="Both players reached 21 points"
                elif player_1_points==21:
                    winner.append("Player 1")
                    ending_string=""
                    ending_string="Player One reached 21 points"
                elif player_2_points==21:
                    winner.append("Player 2")
                    ending_string=""
                    ending_string="Player Two reached 21 points" 
                if player_1_points>player_2_points:
                    winner.append("Player 1")
                    ending_string=""
                    ending_string="Player One Scored "+str(player_1_points)+" Points, Player Two Scored"+str(player_2_points)+"points."
                else:
                    winner.append("Player 2")
                    ending_string=""
                    ending_string="Player Two Scored " +str(player_2_points)+ " Points, Player One Scored"+str(player_1_points)+"points."
                
                if player_1_points==player_2_points:
                    winner.append("Neither")
                    ending_string=""
                    ending_string="Both Players Have the Same Score" 
            winner.append(ending_string)
    print("=======")
    print("Results")
    print("=======")

    print(f"The Winner was {winner[0]}")
    print(f"Reason:{winner[1]}")
    print("====================")
    placeholder=input("")
    placeholder=placeholder

def Card_Percentage(card_list,percentile):
    card_totals=[0,0,0,0,0,0,0,0,0,0]
    total_number=0
    for card in card_list:
        card_points=0
        if str(card[0])=="J":
            card_points+=10
        elif str(card[0])=="Q":
            card_points+=10
        elif str(card[0])=="K":
            card_points+=10
        elif str(card[0])=="0":
            card_points+=10
        elif str(card[0])=="A":
            card_points+=1
        else:
            card_points+=int(card[0])
        total_number+=1
        card_totals[card_points-1]+=1
    count=0
    total=0
    while count!=int(percentile):
        total+=card_totals[count-1]
        count+=1
    divisor=100*total/total_number
    divisor=str(divisor)
    divisor=divisor[:2]
    return divisor

def BlackJack_Single():
    Deck=["ASpades","2Spades","3Spades","4Spades","5Spades","6Spades","7Spades","8Spades","9Spades","0Spades","JSpades","QSpades","KSpades","AClubs","2Clubs","3Clubs","4Clubs","5Clubs","6Clubs","7Clubs","8Clubs","9Clubs","0Clubs","JClubs","QClubs","KClubs","ADiamonds","2Diamonds","3Diamonds","4Diamonds","5Diamonds","6Diamonds","7Diamonds","8Diamodns","9Diamonds","0Diamonds","JDiamonds","QDiamonds","KDiamonds","AHearts","2Hearts","3Hearts","4Hearts","5Hearts","6Hearts","7Hearts","8Hearts","9Hearts","0Hearts","JHearts","QHearts","KHearts"]
    card_list=[]
    card_list=Deck
    computer_points=0
    player_1_points=0
    player_1_cards=[]
    computer_cards=[]
    winner=[]
    
    for _ in range(2):
        player_1_card=draw_cards(card_list)
        card_list=remove_card(card_list, player_1_card)
        info_list_1=Print_Card(player_1_card)
        player_1_points+=info_list_1[0]
        player_1_cards.append(info_list_1[2])


        computer_card=draw_cards(card_list)
        card_list=remove_card(card_list, computer_card)
        info_list_2=Print_Card(computer_card)
        computer_points+=info_list_2[0]
        computer_cards.append(info_list_2[2])

    game_over=False
    stand_1=False
    stand_2=False
    while game_over==False:
        
        if player_1_points <22 and stand_1==False:

            print("========")
            print("Player 1")
            print("========")

            placeholder=input("")
            placeholder=placeholder

            print("=================")
            print(f"Your cards")
            for item in player_1_cards:
                print(item)

            print("============================")
            answer=str(input("Do you want to hit or stand?"))
            print("===============================")
            if answer=="hit":
                
                stand_1=False
                player_1_card=draw_cards(card_list)
                card_list=remove_card(card_list, player_1_card)
                info_list_1=Print_Card(player_1_card)
                player_1_points+=info_list_1[0]
                player_1_cards.append(info_list_1[2])
                print(f"Your next card is: {info_list_1[2]}")
            else:
                stand_1=True

            if player_1_points>22:
                print("====")
                print("Bust: Your total was too high")
                print("====")
                stand_1=True
            elif player_1_points==21:
                stand_1=True


        if computer_points <22 and stand_2==False:

            percentile=21-computer_points
            percentage=Card_Percentage(card_list, percentile)
            chance=random.randint(1,100)
            if int(chance)<int(percentage):
                answer="hit"
            else:
                answer="stand"



            if answer=="hit":
                
                stand_2=False
                computer_card=draw_cards(card_list)
                card_list=remove_card(card_list, computer_card)
                info_list_2=Print_Card(computer_card)
                computer_points+=info_list_2[0]
                computer_cards.append(info_list_2[2])
            else:
                stand_2=True

            if computer_points>22:
                stand_2=True
            if computer_points==21:
                stand_2=True


        if stand_1==True and stand_2==True:
            game_over=True
            if player_1_points>21 and computer_points>21:
                winner.append("Neither")
                ending_string=""
                ending_string="Both players went over 21"

            elif player_1_points>21:
                winner.append("Computer")
                ending_string=""
                ending_string="You went over 21"
            elif computer_points>21:
                winner.append("You")
                ending_string=""
                ending_string="Computer went over 21"
            else:
                if player_1_points==21 and computer_points==21:
                    winner.append("Neither")
                    ending_string=""
                    ending_string="Both players reached 21 points"
                elif player_1_points==21:
                    winner.append("You")
                    ending_string=""
                    ending_string="You reached 21 points"
                elif computer_points==21:
                    winner.append("Computer")
                    ending_string=""
                    ending_string="The Computer reached 21 points" 
                if player_1_points>computer_points:
                    winner.append("You")
                    ending_string=""
                    ending_string="You Scored "+str(player_1_points)+" Points, The Computer Scored "+str(computer_points)+"points."
                else:
                    winner.append("Computer")
                    ending_string=""
                    ending_string="The Computer Scored " +str(computer_points)+ " Points, You Scored "+str(player_1_points)+"points."
            if player_1_points==computer_points:
                winner.append("neither")
                ending_string=""
                ending_string="You and the Computer have the same score"            
            winner.append(ending_string)
    print("=======")
    print("Results")
    print("=======")

    print(f"The Winner was {winner[0]}")
    print(f"Reason:{winner[1]}")
    print("====================")
    placeholder=input("")
    placeholder=placeholder

    Deck=["ASpades","2Spades","3Spades","4Spades","5Spades","6Spades","7Spades","8Spades","9Spades","0Spades","JSpades","QSpades","KSpades","AClubs","2Clubs","3Clubs","4Clubs","5Clubs","6Clubs","7Clubs","8Clubs","9Clubs","0Clubs","JClubs","QClubs","KClubs","ADiamonds","2Diamonds","3Diamonds","4Diamonds","5Diamonds","6Diamonds","7Diamonds","8Diamodns","9Diamonds","0Diamonds","JDiamonds","QDiamonds","KDiamonds","AHearts","2Hearts","3Hearts","4Hearts","5Hearts","6Hearts","7Hearts","8Hearts","9Hearts","0Hearts","JHearts","QHearts","KHearts"]


    for i in range(11):
        Card_Percentage(Deck,i)

def BlackJack_Rules():
    print("==========")
    print("1. All cards are worth points equal to their card number")
    print("2. Ace is equal to one point")
    print("3. Jack, Queen, King are all 10 points")
    print("4. The goal of the game is to reach 21 points but to not go over it")
    print("===================")

def BlackJack():
    answer=0
    while answer!=9:
        print("========")
        print("1. BlackJack Single")
        print("2. BlackJack Two Players")
        print("3. BlackJack Rules")
        print("=============")
        answer=str(input("Please enter the option that you desire "))
        if answer=="1":
            BlackJack_Single()
        elif answer=="2":
            BlackJack_2()
        elif answer=="3":
            BlackJack_Rules()
        elif answer=="9":
            pass

def Alpha_Counter(word, Counter):
    Alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    word_list=[]
    for char in word:
        word_list.append(char)

    for i in range(len(word_list)):
        for j in range(len(Alphabet)):
            if word_list[i]==Alphabet[j]:
                Counter[j]+=1
    return Counter

def Wordle_Sort():
    count=0
    f=open("Wordle_wordlist.txt", "r")
    file=open("allwords.txt","w")
    for line in f:
            file.write(line)
            count+=1
    print(count)
    file.write('\n')
    f.close()
    file.close()

def Wordle_Letter(Counter_list):
    letter_list=[]
    Alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(26):
        if Counter_list[i-1]==0:
            letter_list.append(Alphabet[i-1])
    print(letter_list)

def Wordle():
    Counter_list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    turns_taken=1
    line=random.randint(1,2315)
    f=open("allwords.txt","r")
    word_list=f.readlines()
    word=word_list[line]
    word=word.strip('\n')
    true_word=False

    correct_word=[]
    for char in word:
        correct_word.append(char)
    guess=input("Please input your word that is a total length of five letters ")
    
    
    if guess[0]=="!":
        if guess=="!help":
            print("Options for commands: !char !word !hint")
        elif guess=="!char":
            Wordle_Letter(Counter_list)
        elif guess=="!word":
            print(word)
        elif guess=="!hint":
            number=random.randint(0,4)
            print(word[number])
        else:
            print("Invalid command. Use !help for help")

    for i in range(len(word_list)):
        if guess==word_list[i].strip('\n'):
            true_word=True
    while len(guess) !=5 or true_word==False:
        guess=input("Please enter a word that is within five letters ")
        if guess[0]=="!":
            if guess=="!help":
                print("Options for commands: !char !word !hint")
            elif guess=="!char":
                Wordle_Letter(Counter_list)
            elif guess=="!word":
                print(word)
            elif guess=="!hint":
                number=random.randint(0,4)
                print(word[number])
            else:
                print("Invalid command. Use !help for help")
        for i in range(len(word_list)):
            if guess==word_list[i].strip('\n'):
                true_word=True
    Counter_list=Alpha_Counter(guess, Counter_list)
    
    while guess != str(word):
        for char in guess:
            print(char, end = "")
            print("", end=" ")
        print("")
        turns_taken+=1
        guess_word=[]
        accuracy=["X","X","X","X","X"]
        for char in guess:
            guess_word.append(char)

        for i in range(5):
            for j in range(5):
                if str(guess_word[i])==str(correct_word[j]):
                    accuracy[i]="O"
                if str(guess_word[i])==str(correct_word[i]):
                    accuracy[i]="‼"
        string=""
        for i in range(len(accuracy)):
            string=string+str(accuracy[i])
        for char in string:
            print(char, end= " ")
        print("")
        guess=input("Please input your next word that is a total length of five letters ")
        true_word=False
        if guess[0]=="!":
            if guess=="!help":
                print("Options for commands: !char !word !hint")
            elif guess=="!char":
                Wordle_Letter(Counter_list)
            elif guess=="!word":
                print(word)
            elif guess=="!hint":
                number=random.randint(0,4)
                print(word[number])
            else:
                print("Invalid command. Use !help for help")
        for i in range(len(word_list)):
            if guess==word_list[i].strip('\n'):
                true_word=True
        while len(guess) !=5 or true_word==False:
            guess=input("Please enter a word that is within five letters ")
            if guess[0]=="!":
                if guess=="!help":
                    print("Options for commands: !char !word !hint")
                elif guess=="!char":
                    Wordle_Letter(Counter_list)
                elif guess=="!word":
                    print(word)
                elif guess=="!hint":
                    number=random.randint(0,4)
                    print(word[number])
                else:
                    print("Invalid command. Use !help for help")
            for i in range(len(word_list)):
                if guess==word_list[i].strip('\n'):
                    true_word=True
        Counter_list=Alpha_Counter(guess,Counter_list)
        guess=guess.lower()
    print(f"Attempts taken: {turns_taken}")
    placeholder=input("")
    placeholder=placeholder
    return turns_taken

def Wordle_Challenge():
    
    turns_taken=1
    line=random.randint(1,2315)
    f=open("allwords.txt","r")
    word_list=f.readlines()
    word=word_list[line]
    word=word.strip('\n')
    true_word=False
    guess=input("Please input your word that is a total length of five letters ")
    for i in range(len(word_list)):
        if guess==word_list[i].strip('\n'):
            true_word=True
    while len(guess) !=5 or true_word==False:
        guess=input("Please enter a word that is within five letters ")
        for i in range(len(word_list)):
            if guess==word_list[i].strip('\n'):
                true_word=True

    correct_word=[]
    for char in word:
        correct_word.append(char)
    counter=0
    while guess != str(word) and counter<7:
        for char in guess:
            print(char, end = "")
            print("", end=" ")
        print("")
        turns_taken+=1
        guess_word=[]
        accuracy=["X","X","X","X","X"]
        for char in guess:
            guess_word.append(char)

        for i in range(5):
            for j in range(5):
                if str(guess_word[i])==str(correct_word[j]):
                    accuracy[i]="O"
                if str(guess_word[i])==str(correct_word[i]):
                    accuracy[i]="‼"
        string=""
        for i in range(len(accuracy)):
            string=string+str(accuracy[i])
        for char in string:
            print(char, end= " ")
        print("")
        guess=input("Please input your next word that is a total length of five letters ")
        true_word=False
        for i in range(len(word_list)):
            if guess==word_list[i].strip('\n'):
                true_word=True
        while len(guess) !=5 or true_word==False:
            guess=input("Please enter a word that is within five letters ")
            for i in range(len(word_list)):
                if guess==word_list[i].strip('\n'):
                    true_word=True
        guess=guess.lower()
        counter+=1
    if counter<7:
        print(f"Congratulations. You took {turns_taken}")
    else:
        print(f"Unfortunately you took {turns_taken} attempts, the word was {word}")
    placeholder=input("")
    placeholder=placeholder

def Wordle_Main():
    print("=========")
    print("1. Casual (infinite attempts and commands)")
    print("2. Challenge (6 attempts)")
    answer=""
    answer=input("Which option would you like? ")
    if answer=="1":
        turns_taken=Wordle()
        if int(turns_taken-1)<7:
            print("Congratulations")
        else:
            print("Unlucky")
    if answer=="2":
        Wordle_Challenge()

def guest():
    answer=""
    while answer !="9":
        print("=============")
        print("1. Add New Player")
        print("2. Play HiLo")
        print("3. Princess")
        print("4. Wordle")
        print("5. BlackJack")
        print("=============")
        answer=input("Please enter the desired choice ")
        if answer=="1":
            pass
        if answer == "2":
            hilo()
        if answer == "3":
            princess()
        if answer == "4":
            Wordle_Main()
        if answer == "5":
            BlackJack()
        if answer=="9":
            pass

def admin():
    answer=""
    while answer!=9:
        print("=========")
        print("1. Manage Accounts")
        print("=========")
    answer=input()

def main():
    answer=""
    while answer!="9":
        print("============")
        print("1. Add New Player")
        print("2. Guest")
        print("3. Log in")
        print("===========")
        answer=input("Please enter the desired choice ")
        if answer=="1":
            pass
        if answer=="2":
            guest()
        if answer=="3":
            pass
        if answer=="admin":
            admin()

main()