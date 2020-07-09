'''Esra GENECİ 041502020
Eyüp YASUNTİMUR 041502026
Rock Paper Scissors Game. 20.11.2019'''

from random import randint

def player1():
    print("-----------------------------------------")
    print("Please select: Rock, Scissors, Paper")
    choice=input()
    return choice;

def player2():
    player2=''
    choice = ["Rock", "Scissors", "Paper"]
    random_select = randint(0, 2)  # rolling random number for rates
    if (random_select == 0):
        player2 = choice[0]
    elif (random_select == 1):
        player2 = choice[1]
    elif (random_select== 2):
            player2 = choice[2]
    print("-----------------------------------------")
    print("please select: Rock, Scissors, Paper")
    print(player2)
    return player2;

def player3(ratePaper,rateRock,rateScissor):
    player3 = ' '
    choice = ["Rock", "Paper", "Scissors"]
    print("-----------------------------------------")
    print("please select: Rock, Scissors, Paper")
    if computerN <= ratePaper:
        player3 = choice[1]
    elif ratePaper < computerN < (ratePaper + rateRock):
        player3 = choice[0]
    elif (ratePaper + rateRock) <= computerN < (ratePaper + rateRock + rateScissor):
        player3 = choice[2]
    print(player3)
    return player3;

def player4(gamer_array):
    Scissors_counter=0
    Paper_counter = 0
    Rock_counter = 0

    if(len(gamer_array)<5):
        ratio_paper=1/3
        ratio_rock=1/3
        ratio_scissors=1/3
        choice = ["Rock", "Scissors", "Paper"]
        random_select = randint(0, 2)  # rolling random number for rates
        if (random_select == 0):
            player4 = choice[0]
        elif (random_select == 1):
            player4 = choice[1]
        elif (random_select == 2):
            player4 = choice[2]
        print("-----------------------------------------")
        print("please select: Rock, Scissors, Paper")
        print(player4)
        return player4;

    else:
        for i in gamer_array:
            if(i=='Rock'):
                Rock_counter=Rock_counter+1
            elif(i=='Paper'):
                Paper_counter = Paper_counter + 1
            elif(i=='Scissors'):
                Scissors_counter=Scissors_counter+1


        ratio_scissors=Scissors_counter/(len(gamer_array))
        ratio_rock=Rock_counter/(len(gamer_array))
        ratio_paper=Paper_counter/len(gamer_array)

        print("-----------------------------------------")
        print("please select: Rock, Scissors, Paper")


        if (ratio_rock >= ratio_paper and ratio_rock >= ratio_scissors):
            player4 = 'Paper'
        elif (ratio_scissors >= ratio_paper and ratio_scissors >= ratio_rock):
            player4 = 'Rock'
        elif (ratio_paper >= ratio_scissors and ratio_paper >= ratio_scissors):
            player4 = 'Scissors'

        print(player4)

    return player4;



    return gamer_array

def player5(gamer_array):

    Rock_counter=0
    Paper_counter = 0
    Scissors_counter = 0

    if(len(gamer_array)==0):
        player5='Rock'
        return player5

    else:

        for i in gamer_array:
            if (i == 'Rock'):
                Rock_counter = Rock_counter + 1
            elif (i == 'Paper'):
                Paper_counter = Paper_counter + 1
            elif (i == 'Scissors'):
                Scissors_counter = Scissors_counter + 1

        game_number=Rock_counter+Scissors_counter+Paper_counter



        if (Rock_counter == 0):
            rateRock = 0
        else:
            rateRock = ((Rock_counter * 1000) / game_number)
        if (Paper_counter == 0):
            ratePaper = 0
        else:
            ratePaper = ((Paper_counter * 1000) / game_number)
        if (Scissors_counter == 0):
            rateScissor = 0
        else:
            rateScissor = ((Scissors_counter * 1000) / game_number)

        choice = ["Rock", "Scissors", "Paper"]
        random_select = randint(0, 1000)  # rolling random number for rates
        choice = ["Rock", "Paper", "Scissors"]
        print("-----------------------------------------")
        print("please select: Rock, Scissors, Paper")
        if random_select <= ratePaper:
            player5 = choice[1]
        elif ratePaper < random_select < (ratePaper + rateRock):
            player5 = choice[0]
        elif (ratePaper + rateRock) <= random_select < (ratePaper + rateRock + rateScissor):
            player5 = choice[2]
        print(player5)
        return player5


def input_check(array,input):
    if(array.__contains__(input)):
        check=True
    else:
        check=False
    return check;

def game(player1,player2,game_array):
    choice_array = ["Rock", "Scissors", "Paper"]
    print("-----------------------------------------")
    if (input_check(choice_array, player1) and input_check(choice_array, player2)):
        if(player1 == player2):
            game_array[0]=game_array[0]+1
            print("Tie...\n", player1, "=", player2)
            print("Tie:", game_array[0], "\nWin:", game_array[1], "\nLose:", game_array[2])
            print("**********************************")
            return game_array;
        elif(player1=="Rock"):
            if(player2=="Scissors"):
                game_array[1]=game_array[1]+1
                print("Player1 win...\n", player1, "smashes", player2)
                print("**********************************")
                return print("Tie:",game_array[0],"\nWin:",game_array[1],"\nLose:", game_array[2])
            elif(player2=="Paper"):
                game_array[2]=game_array[2]+1
                print("Player1 lose...\n", player2, "covers", player1)
                print("Tie:", game_array[0], "\nWin:", game_array[1], "\nLose:", game_array[2])
                print("**********************************")
                return game_array
        elif(player1=="Scissors"):
            if(player2=="Paper"):
                game_array[1] = game_array[1] + 1
                print("Player1 win...\n", player1, "cut", player2)
                print("Tie:", game_array[0], "\nWin:", game_array[1], "\nLose:", game_array[2])
                print("**********************************")
                return game_array
            elif(player2=="Rock"):
                game_array[2]=game_array[2]+1
                print("Player1 lose...\n", player2, "smashes", player1)
                print("Tie:", game_array[0], "\nWin:", game_array[1], "\nLose:", game_array[2])
                print("**********************************")
                return game_array
        elif(player1=="Paper"):
            if (player2 == "Rock"):
                game_array[1]=game_array[1]+1
                print("Player1 win...\n", player1, "covers", player2)
                print("Tie:", game_array[0], "\nWin:", game_array[1], "\nLose:", game_array[2])
                print("**********************************")
                return game_array
            elif (player2 == "Scissors"):
                game_array[2]=game_array[2]+1
                print("Player1 lose...\n", player2, "cuts", player1)
                print("Tie:", game_array[0], "\nWin:", game_array[1], "\nLose:", game_array[2])
                print("**********************************")
                return game_array
    else:
        return print("One of players do not play")

##MAIN PART

print("please enter : \n Start(1)  Exit(9)")
game_quit=int(input())
gamer1_array = []
gamer2_array = []
while(game_quit!=9):



    mode_array=['P1','P2','P3','P4','P5']
    print("please select player one:\n P1,P2,P3,P4,P5")
    player1_type=input()

    print("please select player two:\n P1,P2,P3,P4,P5")
    player2_type=input()

    if(input_check(mode_array,player1_type) and input_check(mode_array,player2_type)):


        print("please enter game number:")
        game_number=int(input())
        game_counter=0
        computerN = randint(0, 1000)
        rateRock = 342
        rateScissor = 358
        ratePaper = 300
        rateRock1 = 342
        rateScissor1 = 358
        ratePaper1 = 300
        game_array=[0,0,0] #0.index tie, 1. index win, 2. index lose sayıları tuttuyor



        while(game_counter<game_number):

            game_counter = game_counter + 1

            if(player1_type=='P1' and player2_type=='P1' ):

                gamer1=player1();
                gamer2=player1();
                #print(gamer1, gamer2)
                game(gamer1,gamer2,game_array)

            elif(player1_type=='P1' and player2_type=='P2'):

                gamer1 = player1();
                gamer2 = player2();
                #print(gamer1, gamer2)
                game(gamer1,gamer2,game_array)

            elif(player1_type =='P1' and player2_type =='P3'):

                gamer1 = player1()
                gamer2 = player3(ratePaper, rateRock, rateScissor)
                game(gamer1, gamer2,game_array)

                if gamer1 == "Rock":  # in case of rock increase the paper rate
                    if gamer2 == "Paper":
                        rateRock = rateRock - rateRock
                        rateScissor = rateScissor - rateScissor
                        ratePaper = ratePaper + 700
                    else:
                        rateRock = rateRock - rateRock
                        rateScissor = rateScissor - rateScissor
                        ratePaper = ratePaper + 700
                elif gamer1 == "Paper":  # in case of paper increase scissors rate
                    if gamer2 == "Scissors":
                        rateScissor = rateScissor + 642
                        rateRock = rateRock - rateRock
                        ratePaper = ratePaper - ratePaper
                    else:
                        rateScissor = rateScissor + 642
                        rateRock = rateRock - rateRock
                        ratePaper = ratePaper - ratePaper
                elif gamer1 == "Scissors":  # in case of scissors increase rock rate
                    if gamer2 == "Rock":
                        rateScissor = rateScissor - rateScissor
                        rateRock = rateRock + 658
                        ratePaper = ratePaper - ratePaper
                    else:
                        rateScissor = rateScissor - rateScissor
                        rateRock = rateRock + 658
                        ratePaper = ratePaper - ratePaper

                print("paper rate", ratePaper, "rock rate", rateRock, "Scissors rate", rateScissor)

            elif(player1_type=='P2' and player2_type=='P2'):

                gamer1 = player2();
                gamer2 = player2();
               # print(gamer1, gamer2)
                game(gamer1, gamer2,game_array)

            elif(player1_type == 'P2' and player2_type =='P3'):

                gamer1=player2()
                gamer2=player3(ratePaper, rateRock, rateScissor)
                game(gamer1,gamer2,game_array)

                if gamer1 == "Rock":  # in case of rock increase the paper rate
                    if gamer2 == "Paper":
                        rateRock = rateRock - rateRock
                        rateScissor = rateScissor - rateScissor
                        ratePaper = ratePaper + 700
                    else:
                        rateRock = rateRock - rateRock
                        rateScissor = rateScissor - rateScissor
                        ratePaper = ratePaper + 700
                elif gamer1 == "Paper":  # in case of paper increase scissors rate
                    if gamer2 == "Scissors":
                        rateScissor = rateScissor + 642
                        rateRock = rateRock - rateRock
                        ratePaper = ratePaper - ratePaper
                    else:
                        rateScissor = rateScissor + 642
                        rateRock = rateRock - rateRock
                        ratePaper = ratePaper - ratePaper
                elif gamer1 == "Scissors":  # in case of scissors increase rock rate
                    if gamer2 == "Rock":
                        rateScissor = rateScissor - rateScissor
                        rateRock = rateRock + 658
                        ratePaper = ratePaper - ratePaper
                    else:
                        rateScissor = rateScissor - rateScissor
                        rateRock = rateRock + 658
                        ratePaper = ratePaper - ratePaper

                print("paper rate",ratePaper,"rock rate",rateRock, "Scissors rate",rateScissor)

            elif (player1_type == 'P1' and player2_type == 'P4'):
                gamer1 = player1()
                gamer1_array.append(gamer1)
                gamer2 = player4(gamer1_array)
                gamer2_array.append(gamer2)
                game(gamer1, gamer2, game_array)

            elif(player1_type == 'P2' and player2_type =='P4'):
                gamer1 = player2()
                gamer1_array.append(gamer1)
                gamer2 = player4(gamer1_array)
                gamer2_array.append(gamer2)
                game(gamer1, gamer2, game_array)

            elif (player1_type == 'P3' and player2_type == 'P4'):
                gamer1 = player4(gamer1_array)
                gamer2 = player3(ratePaper, rateRock, rateScissor)
                game(gamer2, gamer1, game_array)
                gamer1_array.append(gamer2)
                gamer2_array.append(gamer1)

                if gamer1 == "Rock":  # in case of rock increase the paper rate
                    if gamer2 == "Paper":
                        rateRock = rateRock - rateRock
                        rateScissor = rateScissor - rateScissor
                        ratePaper = ratePaper + 700
                    else:
                        rateRock = rateRock - rateRock
                        rateScissor = rateScissor - rateScissor
                        ratePaper = ratePaper + 700
                elif gamer1 == "Paper":  # in case of paper increase scissors rate
                    if gamer2 == "Scissors":
                        rateScissor = rateScissor + 642
                        rateRock = rateRock - rateRock
                        ratePaper = ratePaper - ratePaper
                    else:
                        rateScissor = rateScissor + 642
                        rateRock = rateRock - rateRock
                        ratePaper = ratePaper - ratePaper
                elif gamer1 == "Scissors":  # in case of scissors increase rock rate
                    if gamer2 == "Rock":
                        rateScissor = rateScissor - rateScissor
                        rateRock = rateRock + 658
                        ratePaper = ratePaper - ratePaper
                    else:
                        rateScissor = rateScissor - rateScissor
                        rateRock = rateRock + 658
                        ratePaper = ratePaper - ratePaper

                print("paper rate", ratePaper, "rock rate", rateRock, "Scissors rate", rateScissor)

            elif (player1_type == 'P3' and player2_type == 'P3'):
                gamer1 = player3(ratePaper1, rateRock1, rateScissor1)
                gamer2 = player3(ratePaper, rateRock, rateScissor)
                game(gamer2, gamer1, game_array)
                gamer1_array.append(gamer1)
                gamer2_array.append(gamer2)


                if gamer2 == "Rock":  # in case of rock increase the paper rate
                    if gamer1 == "Paper":
                        rateRock1 = rateRock1 - rateRock1
                        rateScissor1 = rateScissor1 - rateScissor1
                        ratePaper1 = ratePaper1 + 700
                    else:
                        rateRock1 = rateRock1 - rateRock1
                        rateScissor1 = rateScissor1 - rateScissor1
                        ratePaper1 = ratePaper1 + 700
                elif gamer2 == "Paper":  # in case of paper increase scissors rate
                    if gamer1 == "Scissors":
                        rateScissor1 = rateScissor1 + 642
                        rateRock1 = rateRock1 - rateRock1
                        ratePaper1 = ratePaper1 - ratePaper1
                    else:
                        rateScissor1 = rateScissor1 + 642
                        rateRock1 = rateRock1 - rateRock1
                        ratePaper1 = ratePaper1 - ratePaper1
                elif gamer2 == "Scissors":  # in case of scissors increase rock rate
                    if gamer1 == "Rock":
                        rateScissor1 = rateScissor1 - rateScissor1
                        rateRock1 = rateRock1 + 658
                        ratePaper1 = ratePaper1 - ratePaper1
                    else:
                        rateScissor1 = rateScissor1 - rateScissor1
                        rateRock1 = rateRock1 + 658
                        ratePaper1 = ratePaper1 - ratePaper1

                if gamer1 == "Rock":  # in case of rock increase the paper rate
                    if gamer2 == "Paper":
                        rateRock = rateRock - rateRock
                        rateScissor = rateScissor - rateScissor
                        ratePaper = ratePaper + 700
                    else:
                        rateRock = rateRock - rateRock
                        rateScissor = rateScissor - rateScissor
                        ratePaper = ratePaper + 700
                elif gamer1 == "Paper":  # in case of paper increase scissors rate
                    if gamer2 == "Scissors":
                        rateScissor = rateScissor + 642
                        rateRock = rateRock - rateRock
                        ratePaper = ratePaper - ratePaper
                    else:
                        rateScissor = rateScissor + 642
                        rateRock = rateRock - rateRock
                        ratePaper = ratePaper - ratePaper
                elif gamer1 == "Scissors":  # in case of scissors increase rock rate
                    if gamer2 == "Rock":
                        rateScissor = rateScissor - rateScissor
                        rateRock = rateRock + 658
                        ratePaper = ratePaper - ratePaper
                    else:
                        rateScissor = rateScissor - rateScissor
                        rateRock = rateRock + 658
                        ratePaper = ratePaper - ratePaper

            elif (player1_type == 'P4' and player2_type == 'P4'):
                gamer1 = player4(gamer2_array)
                gamer1_array.append(gamer1)
                gamer2 = player4(gamer1_array)
                gamer2_array.append(gamer2)
                game(gamer1, gamer2, game_array)

            elif (player1_type == 'P2' and player2_type == 'P5'):
                gamer1 = player2()
                gamer1_array.append(gamer1)
                gamer2 = player5(gamer1_array)
                gamer2_array.append(gamer2)
                game(gamer1, gamer2, game_array)

            elif (player1_type == 'P1' and player2_type == 'P5'):
                gamer1 = player1()
                gamer1_array.append(gamer1)
                gamer2 = player5(gamer1_array)
                gamer2_array.append(gamer2)
                game(gamer1, gamer2, game_array)

            elif (player1_type == 'P3' and player2_type == 'P5'):
                gamer1 = player3(ratePaper, rateRock, rateScissor)
                gamer1_array.append(gamer1)
                gamer2 = player5(gamer1_array)
                gamer2_array.append(gamer2)
                game(gamer1, gamer2, game_array)

                if gamer1 == "Rock":  # in case of rock increase the paper rate
                    if gamer2 == "Paper":
                        rateRock = rateRock - rateRock
                        rateScissor = rateScissor - rateScissor
                        ratePaper = ratePaper + 700
                    else:
                        rateRock = rateRock - rateRock
                        rateScissor = rateScissor - rateScissor
                        ratePaper = ratePaper + 700
                elif gamer1 == "Paper":  # in case of paper increase scissors rate
                    if gamer2 == "Scissors":
                        rateScissor = rateScissor + 642
                        rateRock = rateRock - rateRock
                        ratePaper = ratePaper - ratePaper
                    else:
                        rateScissor = rateScissor + 642
                        rateRock = rateRock - rateRock
                        ratePaper = ratePaper - ratePaper
                elif gamer1 == "Scissors":  # in case of scissors increase rock rate
                    if gamer2 == "Rock":
                        rateScissor = rateScissor - rateScissor
                        rateRock = rateRock + 658
                        ratePaper = ratePaper - ratePaper
                    else:
                        rateScissor = rateScissor - rateScissor
                        rateRock = rateRock + 658
                        ratePaper = ratePaper - ratePaper

            elif (player1_type == 'P4' and player2_type == 'P5'):
                gamer1 = player4(gamer2_array)
                gamer1_array.append(gamer1)
                gamer2 = player5(gamer1_array)
                gamer2_array.append(gamer2)
                game(gamer1, gamer2, game_array)

    else:
        print("We don't have player mode. Please start again.")


    print("#########################")
    print("please enter : \n Start(1)  Exit(9)")
    game_quit = int(input())
    print("#########################")

print("See you later :)")




















