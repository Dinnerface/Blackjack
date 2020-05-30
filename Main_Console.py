import numpy as np
from Check_Conditions_File import checkconditions

number_of_decks = 6
number_of_cards_before_switch = 30
Total_player_cash = 0
Total_dealer_cash = 0
Total_player_wins = 0
Total_dealer_wins = 0
Total_ties = 0

Total_Player_Match_Victories = 0
Total_Dealer_Match_Victories = 0
Total_Match_Ties = 0

game = 0
number_of_games = 100
Total_splits = 0


def fullcards(number_of_decks):
    Ace = 11
    Jack = 10
    Queen = 10
    King = 10
    All_Cards = [Ace, Ace, Ace, Ace,
                 2, 2, 2, 2,
                 3, 3, 3, 3,
                 4, 4, 4, 4,
                 5, 5, 5, 5,
                 6, 6, 6, 6,
                 7, 7, 7, 7,
                 8, 8, 8, 8,
                 9, 9, 9, 9,
                 10, 10, 10, 10,
                 Jack, Jack, Jack, Jack,
                 Queen, Queen, Queen, Queen,
                 King, King, King, King]
    All_Cards = All_Cards*number_of_decks

    return(All_Cards)
def aceorone(current_hand):
    if (11 in current_hand) & (sum(current_hand) > 21):
        print("There's an 11.")
        i = 0
        finished = 0
        while (finished < 1):
            if (current_hand[i] != 11):
                i = i + 1
            else:
                current_hand[i] = 1
                finished = 1
    return (current_hand)
def initialdeal(All_Cards):

    current_card_count = len(All_Cards)
    r1 = np.random.randint(0, current_card_count, 1)
    player_card1 = All_Cards[r1[0]]
    All_Cards.pop(r1[0])
    current_card_count = len(All_Cards)
    r2 = np.random.randint(0, current_card_count, 1)
    player_card2 = All_Cards[r2[0]]
    All_Cards.pop(r2[0])
    player_initial_cards = [player_card1, player_card2]

    current_card_count = len(All_Cards)
    r3 = np.random.randint(0, current_card_count, 1)
    dealer_card1 = All_Cards[r3[0]]
    All_Cards.pop(r3[0])
    current_card_count = len(All_Cards)
    r4 = np.random.randint(0, current_card_count, 1)
    dealer_card2 = All_Cards[r4[0]]
    All_Cards.pop(r4[0])
    dealer_initial_cards = [dealer_card1, dealer_card2]


#    player_initial_cards = [6,10]
#    dealer_initial_cards = [10,6]
#    player_initial_cards = [10,10]

    ############Handles Case where either the player or dealer has [11,11]
#    if (player_initial_cards == [11,11]):
#        player_initial_cards = [1,11]

    if(dealer_initial_cards == [11,11]):
        dealer_initial_cards = [1,11]
        print("Two initial Aces for the dealer.")

    return(player_initial_cards,dealer_initial_cards,All_Cards)

def playerdraws(All_Cards,player_current_cards):
    doubledown = 0
    while ((sum(player_current_cards)) < 17):
        current_card_count = len(All_Cards)
        r_n = np.random.randint(0, current_card_count, 1)
        player_card_n = All_Cards[r_n[0]]
        All_Cards.pop(r_n[0])
        player_current_cards.extend([player_card_n])
        ###############################################################
        aceorone_2 = aceorone(player_current_cards)
        player_current_cards = aceorone_2
        ###############################################################
#        print(player_current_cards)

    if (sum(player_current_cards) > 21):
        print("playerdraws function: Busted Hand :(")

    return (All_Cards, player_current_cards, doubledown)
def dealerdraws(All_Cards,player_current_cards,dealer_initial_cards):
    dealer_current_cards = dealer_initial_cards

    while (sum(dealer_current_cards) <= min(16, sum(player_current_cards))): #changed from .. < min 17,..)
        current_card_count = len(All_Cards)
        r_n = np.random.randint(0, current_card_count, 1)
        dealer_card_n = All_Cards[r_n[0]]
        All_Cards.pop(r_n[0])
        dealer_current_cards.extend([dealer_card_n])
        #print(dealer_current_cards)
        ###############################################################
        aceorone_1 = aceorone(dealer_current_cards)
        dealer_current_cards = aceorone_1
        ###############################################################

    return (All_Cards, player_current_cards, dealer_current_cards)
def playerdoubledown(All_Cards,player_current_cards):
    double_down = 1

    current_card_count = len(All_Cards)
    r_n = np.random.randint(0, current_card_count, 1)
    player_card_n = All_Cards[r_n[0]]
    All_Cards.pop(r_n[0])
    player_current_cards.extend([player_card_n])
    ###############################################################
    aceorone_2 = aceorone(player_current_cards)
    player_current_cards = aceorone_2
    ###############################################################
#   print(player_current_cards)

    return (All_Cards, player_current_cards,double_down)

def splitting(All_Cards,player_initial_cards):

    current_card_count = len(All_Cards)
    r1 = np.random.randint(0, current_card_count, 1)
    player_card1 = All_Cards[r1[0]]
    All_Cards.pop(r1[0])
    current_card_count = len(All_Cards)
    r2 = np.random.randint(0, current_card_count, 1)
    player_card2 = All_Cards[r2[0]]
    All_Cards.pop(r2[0])

    hand_1 = [player_initial_cards[0], player_card1]
    hand_2 = [player_initial_cards[1], player_card2]
    arrayofsplithands = [hand_1,hand_2]

    return All_Cards,arrayofsplithands

All_Cards = fullcards(number_of_decks)


#############################################################################

while game < number_of_games:

    #########################################

    if (len(All_Cards) < number_of_cards_before_switch):
        print("Using New Deck+++++++++++++++++++++++++++++++++++++++++++")
        All_Cards = fullcards(number_of_decks)
    elif (len(All_Cards) >= number_of_cards_before_switch):
        print("Using Current Deck-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    else:
        print("Case not considered in Deck Reset")




    ######################### STEP 1: DRAW INITIAL CARDS ##########################
    terminate = 0
    surrender = 0
    player_wins = 0
    dealer_wins = 0
    ties = 0
    playerblackjack = 0 #may not need this
    bothblackjack = 0
    has_splitted = 0
    splitagain = 0
    player_cash = 0
    dealer_cash = 0

    InitialDeal = initialdeal(All_Cards)
    player_initial_cards = InitialDeal[0]
    dealer_initial_cards = InitialDeal[1]
    All_Cards = InitialDeal[2]
    dealer_face_card = dealer_initial_cards[1]
    print("The player initial cards are: " + str(player_initial_cards))
    print("The dealer initial cards are: " + str(dealer_initial_cards))
    print("The dealer's face card is: " + str(dealer_face_card))
    #################################################################################
    ########################### STEP 2: Late Surrender ############################
    #Final_Hand = []

    if (((sum(player_initial_cards) == 16) and (player_initial_cards != [8,8]))
            and (dealer_face_card >= 9)):
        Final_Hand = [player_initial_cards]
        surrender = 1
        terminate = 1
        dealer_current_cards = dealer_initial_cards
        print("Player Surrendered")
    elif((sum(player_initial_cards) == 15) and (dealer_face_card == 10)):
        Final_Hand = [player_initial_cards]
        surrender = 1
        terminate = 1
        dealer_current_cards = dealer_initial_cards
        print("Player Surrendered")
    else:
        print("No Surrender.")

    ########################### STEP 2: Blackjack Check ############################

    if((sum(player_initial_cards) == 21) and (sum(dealer_initial_cards) < 21)):
        playerblackjack = 1
        terminate = 1
    elif((sum(player_initial_cards) == 21) and (sum(dealer_initial_cards) == 21)):
        bothblackjack = 1

    ########################### STEP 3: ###########################################

    if ((player_initial_cards == [11,11]) or
            ((player_initial_cards == [9,9]) and (dealer_face_card != 7) and (dealer_face_card <= 9)) or
            (player_initial_cards == [8,8]) or
            ((player_initial_cards == [7, 7]) and (dealer_face_card <= 7)) or
            ((player_initial_cards == [6, 6]) and (dealer_face_card <= 6)) or
            ((player_initial_cards == [4, 4]) and ((dealer_face_card == 5) or (dealer_face_card == 6))) or
            ((player_initial_cards == [3, 3]) and (dealer_face_card <= 7)) or
            ((player_initial_cards == [2, 2]) and (dealer_face_card <= 7))
    ):

        Split = splitting(All_Cards, player_initial_cards)
        All_Cards = Split[0]
        Collection_of_Splits = Split[1]
        has_splitted = 1

        print("Split hands gives: " + str(Collection_of_Splits))
        print("--------------------------------------")

        Total_Resplit = []
        for s in Collection_of_Splits:
            if ((s == [s[0],s[0]]) and (s != [11,11])):  #need to modify s[0]I still need to convert [11,11] to [11,1]
                Split = splitting(All_Cards, s)
                All_Cards = Split[0]
                resplit = Split[1]
                splitagain = 1
                for s2 in resplit:
                    Total_Resplit.append(s2)
            else:
                Total_Resplit.append(s)
        Collection_of_Splits = Total_Resplit
        

    else:
        Collection_of_Splits = [player_initial_cards]
        has_splitted = 0

    print("Collection of Splits: " + str(Collection_of_Splits))
    #print(All_Cards)

    Final_Hand = []
    doubledown_array = []
    if (has_splitted == 1):
        for hand in Collection_of_Splits:
            if hand[0] == 11:
                doubledown_array = [0,0]
                ## considers the case
                Final_Hand.append(hand)
            else:
                Check_Conditions = checkconditions(All_Cards, hand, dealer_initial_cards, dealer_face_card)
                All_Cards = Check_Conditions[0]
                player_current_cards = Check_Conditions[1]
                doubledown_num = Check_Conditions[2]

                Final_Hand.append(player_current_cards)
                doubledown_array.append(doubledown_num)

    elif ((has_splitted != 1) and (terminate != 1)):
        for hand in Collection_of_Splits:
            Check_Conditions = checkconditions(All_Cards, hand, dealer_initial_cards, dealer_face_card)
            All_Cards = Check_Conditions[0]
            player_current_cards = Check_Conditions[1]
            doubledown_num = Check_Conditions[2]

            Final_Hand.append(player_current_cards)
            doubledown_array.append(doubledown_num)
    else:
        print("Something went wrong in has splitted conditions.")
        print("Possible Surrender")

    #print(All_Cards)
    #print("Final Hand: " + str(Final_Hand))
    print("Double Down Array: " + str(doubledown_array))

    ############################# STEP 4: Find the maximum of player hands #####################################

    if ((playerblackjack != 1) and (surrender != 1)):
        sums = []
        for hand in Final_Hand:
            if (sum(hand) <= 21):
                sums.append(sum(hand))
            else:
                sums.append(0)

        Max_sum_of_hands = max(sums)
        #print("The max sum value of the hands is: " + str(Max_sum_of_hands))
        ############################# STEP 5: Dealer Draw #####################################

        if (sum(dealer_initial_cards) > Max_sum_of_hands):
            dealer_current_cards = dealer_initial_cards
        elif ((sum(dealer_initial_cards) == Max_sum_of_hands) and (sum(dealer_initial_cards) >= 17)):
            dealer_current_cards = dealer_initial_cards
        elif ((sum(dealer_initial_cards) == Max_sum_of_hands) and (sum(dealer_initial_cards) < 17)):
            DealerDraws = dealerdraws(All_Cards, [Max_sum_of_hands], dealer_initial_cards)
            All_Cards = DealerDraws[0]
        #    player_current_cards = DealerDraws[1]
            dealer_current_cards = DealerDraws[2]
        elif ((sum(dealer_initial_cards) < Max_sum_of_hands) and (sum(dealer_initial_cards) >= 17)):
            dealer_current_cards = dealer_initial_cards
        elif ((sum(dealer_initial_cards) < Max_sum_of_hands) and (sum(dealer_initial_cards) < 17)):
            DealerDraws = dealerdraws(All_Cards, [Max_sum_of_hands], dealer_initial_cards)
            All_Cards = DealerDraws[0]
            #    player_current_cards = DealerDraws[1]
            dealer_current_cards = DealerDraws[2]
        else:
            print("Case not considered in dealer draw(step 5)")

    #print("Dealer (current)Cards after player: " + str(dealer_current_cards))

    ############################## STEP 6: Determine Winner ###############################

    ###### Check for surrender
    if (surrender == 1):
        dealer_wins = dealer_wins + 1
        dealer_game_victory = 1
        player_game_victory = 0
        match_tie = 0
        dealer_cash = dealer_cash + 0.5
        player_cash = player_cash - 0.5

    elif (playerblackjack == 1):
        player_wins = player_wins + 1
        player_game_victory = 1
        dealer_game_victory = 0
        match_tie = 0
        player_cash = player_cash + 1.5
        dealer_cash = dealer_cash - 1.5

    elif (bothblackjack == 1):
        ties = ties + 1
        match_tie = 1
        player_game_victory = 0
        dealer_game_victory = 0

    else:
        i = 0
        for hand in Final_Hand:
            if ((sum(hand) > 21) and (sum(dealer_current_cards) > 21)):
                print("")
                #ties = ties + 1
                print("Both the player and dealer bust, tie.")
            elif ((sum(hand) > 21) and (sum(dealer_current_cards) <= 21)):
                dealer_wins = dealer_wins + 1
                if (doubledown_array[i] == 1):
                    dealer_cash = dealer_cash + 2
                    player_cash = player_cash - 2
                else:
                    dealer_cash = dealer_cash + 1
                    player_cash = player_cash - 1
                print("The player busts, but not the dealer.")
            elif ((sum(hand) <= 21) and (sum(hand) > sum(dealer_current_cards))):
                #careful with this case may count blackjack
                player_wins = player_wins + 1
                if (doubledown_array[i] == 1):
                    player_cash = player_cash + 2
                    dealer_cash = dealer_cash - 2
                else:
                    player_cash = player_cash + 1
                    dealer_cash = dealer_cash - 1
            elif ((sum(hand) <= 21) and (sum(hand) == sum(dealer_current_cards))):
                print("")
                #ties = ties + 1
            elif (((sum(hand) <= 21) and (sum(hand) < sum(dealer_current_cards))) and (sum(dealer_current_cards) > 21)):
                player_wins = player_wins + 1
                if (doubledown_array[i] == 1):
                    player_cash = player_cash + 2
                    dealer_cash = dealer_cash - 2
                else:
                    player_cash = player_cash + 1
                    dealer_cash = dealer_cash - 1
            elif (((sum(hand) <= 21) and (sum(hand) < sum(dealer_current_cards))) and (sum(dealer_current_cards) <= 21)):
                dealer_wins = dealer_wins + 1
                if (doubledown_array[i] == 1):
                    dealer_cash = dealer_cash + 2
                    player_cash = player_cash - 2
                else:
                    dealer_cash = dealer_cash + 1
                    player_cash = player_cash - 1
            else:
                print("Case not considered in determining who wins.")

            i = i + 1

        if(player_wins == dealer_wins):
            player_wins = 0
            dealer_wins = 0
            ties = 1
            match_tie = 1
            player_game_victory = 0
            dealer_game_victory = 0
        elif(player_wins > dealer_wins):
            player_wins = player_wins - dealer_wins
            player_game_victory = 1
            dealer_game_victory = 0
            match_tie = 0
            dealer_wins = 0
            ties = 0
        elif(dealer_wins > player_wins):
            dealer_wins = dealer_wins - player_wins
            dealer_game_victory = 1
            player_game_victory = 0
            match_tie = 0
            player_wins = 0
            ties = 0
        else:
            print("There is an error in else, determining wins.")


    print("Player Final Hand(s): " + str(Final_Hand))
    print("Dealer Final Hand: " + str(dealer_current_cards))
    print("Player Wins Game, Dealer Wins Game, Tied Game: ")
    print(player_wins,dealer_wins,ties)
    print("Game Player Cash, Game Dealer Cash: ")
    print(player_cash,dealer_cash)
    if (player_game_victory == dealer_game_victory == match_tie):
        print("There's an error in match victories.")
        break

    print("Overall Game Victory: Player, Dealer, Tie")
    print(player_game_victory,dealer_game_victory,match_tie)


    number_of_aces = 0
    number_of_twos = 0
    number_of_threes = 0
    number_of_fours = 0
    number_of_fives = 0
    number_of_sixes = 0
    number_of_sevens = 0
    number_of_eights = 0
    number_of_nines = 0
    number_of_tens = 0

    for number in All_Cards:
        if number == 11:
            number_of_aces += 1
        elif number == 2:
            number_of_twos += 1
        elif number == 3:
            number_of_threes += 1
        elif number == 4:
            number_of_fours += 1
        elif number == 5:
            number_of_fives += 1
        elif number == 6:
            number_of_sixes += 1
        elif number == 7:
            number_of_sevens += 1
        elif number == 8:
            number_of_eights += 1
        elif number == 9:
            number_of_nines += 1
        elif number == 10:
            number_of_tens += 1
    print("Number of Cards: ")
    print(str([11,2,3,4,5,6,7,8,9,10]))
    print(str([number_of_aces,number_of_twos,number_of_threes,number_of_fours,number_of_fives,number_of_sixes,number_of_sevens,number_of_eights,number_of_nines,number_of_tens]) + " =  " + str(sum([number_of_aces,number_of_twos,number_of_threes,number_of_fours,number_of_fives,number_of_sixes,number_of_sevens,number_of_eights,number_of_nines,number_of_tens])))
    ##############################################################

    Total_player_cash = Total_player_cash + player_cash
    Total_dealer_cash = Total_dealer_cash + dealer_cash


    Total_player_wins = Total_player_wins + player_wins
    Total_dealer_wins = Total_dealer_wins + dealer_wins
    Total_ties = Total_ties + ties
    Total_splits = Total_splits + has_splitted + splitagain
#    if has_splitted == 1:
#        break
    Total_Player_Match_Victories = Total_Player_Match_Victories + player_game_victory
    Total_Dealer_Match_Victories = Total_Dealer_Match_Victories + dealer_game_victory
    Total_Match_Ties = Total_Match_Ties + match_tie

    print("Games played* :" + str(game + 1))
    print("ENDGAME-ENDGAME-ENDGAME-ENDGAME-ENDGAME-ENDGAME-ENDGAME-ENDGAME-ENDGAME-ENDGAME-ENDGAME")
    print("Running total of Player Wins, Dealer Wins, and Ties: ")
    print(Total_player_wins, Total_dealer_wins, Total_ties)
    print("_________________________________________________________")
    print("Running total of Player Cash and Dealer Cash: ")
    print(Total_player_cash, Total_dealer_cash)
    print("Running total of Player, Dealer Match Victories, and Ties: ")
    print(str([Total_Player_Match_Victories,Total_Dealer_Match_Victories,Total_Match_Ties]) + " =  " + str(sum([Total_Player_Match_Victories,Total_Dealer_Match_Victories,Total_Match_Ties])))


    print("")
    game = game + 1

print("")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("Total Player Wins, Total Dealer Wins, Total Ties: ")
print(Total_player_wins,Total_dealer_wins,Total_ties)
print("Complete total of Player, Dealer Match Victories, and Ties: ")
print(str([Total_Player_Match_Victories, Total_Dealer_Match_Victories, Total_Match_Ties]) + " =  " + str(
    sum([Total_Player_Match_Victories, Total_Dealer_Match_Victories, Total_Match_Ties])))
print("Total Player Cash, Total Dealer Cash: ")
print(Total_player_cash,Total_dealer_cash)
print("Total Splits and resplits: ")
print(Total_splits)
