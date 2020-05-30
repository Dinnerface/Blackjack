import numpy as np

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

    while (sum(dealer_current_cards) < min(17, sum(player_current_cards))):
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

    return All_Cards, player_current_cards, double_down


def checkconditions(All_Cards, player_initial_cards, dealer_initial_cards, dealer_face_card):

    doubledown_output = 0

    # Case 1: Player has 17 or greater, and not A,8|8,A or A,7|7,A or A,6|6,A
    if ((((sum(player_initial_cards) >= 17)) & (sum(dealer_initial_cards) <= 21))
            & ((player_initial_cards != [11,8]) or (player_initial_cards != [8,11]))
            & ((player_initial_cards != [11,7]) or (player_initial_cards != [7,11]))
            & ((player_initial_cards != [11,6]) or (player_initial_cards != [6,11]))):
        player_current_cards = player_initial_cards
        print("Case 1: The player stands on 17 or greater.")

    # Case 1.25: Player has A,8 or 8,A
    elif (((player_initial_cards == [11,8]) or (player_initial_cards == [8,11]))
          & (sum(dealer_initial_cards) <= 21)):
        print("Case 1.25: The player has A,8 or 8,A.")

        def A8soft(All_Cards, player_initial_cards, dealer_face_card):

            if (dealer_face_card == 6):
                DoubleDown = playerdoubledown(All_Cards, player_initial_cards)
                All_Cards = DoubleDown[0]
                player_current_cards = DoubleDown[1]
                doubledown_output = DoubleDown[2]
                print("(Single Case A-double)")
            elif ((dealer_face_card <= 5) or (dealer_face_card >= 7)):
                doubledown_output = 0
                player_current_cards = player_initial_cards
            else:
                print("Case not considered in 11,8/8,11 function.")
            return All_Cards, player_current_cards, doubledown_output

        A8_Soft = A8soft(All_Cards, player_initial_cards, dealer_face_card)
        All_Cards = A8_Soft[0]
        player_current_cards = A8_Soft[1]
        doubledown_output = A8_Soft[2]
        print(player_current_cards)

    # Case 1.5: Player has A,7 or 7,A
    elif (((player_initial_cards == [11, 7]) or (player_initial_cards == [7, 11]))
          & (sum(dealer_initial_cards) <= 21)):
        print("Case 1.5: The player has A,7 or 7,A.")

        def A7soft(All_Cards, player_initial_cards, dealer_face_card):

            if (dealer_face_card <= 6):
                DoubleDown = playerdoubledown(All_Cards, player_initial_cards)
                All_Cards = DoubleDown[0]
                player_current_cards = DoubleDown[1]
                doubledown_output = DoubleDown[2]
                print("(Single Case A-double)")
            elif (dealer_face_card >= 9):
                PlayerDraws = playerdraws(All_Cards, player_initial_cards)
                All_Cards = PlayerDraws[0]
                player_current_cards = PlayerDraws[1]
                doubledown_output = 0
            elif ((dealer_face_card == 7) or (dealer_face_card == 8)):
                doubledown_output = 0
                player_current_cards = player_initial_cards
            else:
                print("Case not considered in 11,8/8,11 function.")
            return All_Cards, player_current_cards, doubledown_output

        A7_Soft = A7soft(All_Cards, player_initial_cards, dealer_face_card)
        All_Cards = A7_Soft[0]
        player_current_cards = A7_Soft[1]
        doubledown_output = A7_Soft[2]
        print(player_current_cards)

    # Case 1.75: Player has A,6 or 6,A
    elif (((player_initial_cards == [11, 6]) or (player_initial_cards == [6, 11]))
          & (sum(dealer_initial_cards) <= 21)):
        print("Case 1.75: The player has A,6 or 6,A.")

        def A6soft(All_Cards, player_initial_cards, dealer_face_card):

            if ((dealer_face_card >= 3) or (dealer_face_card <= 6)):
                DoubleDown = playerdoubledown(All_Cards, player_initial_cards)
                All_Cards = DoubleDown[0]
                player_current_cards = DoubleDown[1]
                doubledown_output = DoubleDown[2]
                print("(Single Case A-double)")
            elif ((dealer_face_card <= 2) or (dealer_face_card >= 7)):
                PlayerDraws = playerdraws(All_Cards, player_initial_cards)
                All_Cards = PlayerDraws[0]
                player_current_cards = PlayerDraws[1]
                doubledown_output = 0
            else:
                print("Case not considered in 11,6/6,11 function.")
            return All_Cards, player_current_cards, doubledown_output

        A6_Soft = A6soft(All_Cards, player_initial_cards, dealer_face_card)
        All_Cards = A6_Soft[0]
        player_current_cards = A6_Soft[1]
        doubledown_output = A6_Soft[2]
        print(player_current_cards)


    # Case 2: Player has 13 to 16 and not A,5|5,A or A,4|4,A or A,3|3,A or A,2|2,A
    elif ((((sum(player_initial_cards) >= 13) & (sum(player_initial_cards) <= 16))
          & (sum(dealer_initial_cards) <= 21))
          & ((player_initial_cards != [11, 5]) or (player_initial_cards != [5, 11]))
          & ((player_initial_cards != [11, 4]) or (player_initial_cards != [4, 11]))
          & ((player_initial_cards != [11, 3]) or (player_initial_cards != [3, 11]))
          & ((player_initial_cards != [11, 2]) or (player_initial_cards != [2, 11]))):

        print("Case 2: The player has between 13 and 16.")
        def thirteentosixteen(All_Cards, player_initial_cards, dealer_face_card):
            if (dealer_face_card < 7):
                All_Cards = All_Cards
                player_current_cards = player_initial_cards
                print("(Case A)")
            elif (dealer_face_card >= 7):
                PlayerDraws = playerdraws(All_Cards, player_initial_cards)
                All_Cards = PlayerDraws[0]
                player_current_cards = PlayerDraws[1]
                print("(Case B)")
            else:
                print("Case not considered in 13 to 16 function.")

            return All_Cards, player_current_cards
        ThirteenToSixteen = thirteentosixteen(All_Cards, player_initial_cards, dealer_face_card)
        All_Cards = ThirteenToSixteen[0]
        player_current_cards = ThirteenToSixteen[1]
        print(player_current_cards)


    # Case 2.33: Player has A,5 or 5,A   or   A,4 or 4,A
    elif ((((player_initial_cards == [11, 5]) or (player_initial_cards == [5, 11])) or
          ((player_initial_cards == [11, 4]) or (player_initial_cards == [4, 11])))
          & (sum(dealer_initial_cards) <= 21)):
        print("Case 2.33: The player has A,5 or 5,A  or  A,4 or 4,A.")

        def A54soft(All_Cards, player_initial_cards, dealer_face_card):

            if ((dealer_face_card >= 4) or (dealer_face_card <= 6)):
                DoubleDown = playerdoubledown(All_Cards, player_initial_cards)
                All_Cards = DoubleDown[0]
                player_current_cards = DoubleDown[1]
                doubledown_output = DoubleDown[2]
                print("(Single Case A-double)")
            elif ((dealer_face_card <= 3) or (dealer_face_card >= 7)):
                PlayerDraws = playerdraws(All_Cards, player_initial_cards)
                All_Cards = PlayerDraws[0]
                player_current_cards = PlayerDraws[1]
                doubledown_output = 0
            else:
                print("Case not considered in 11,54/54,11 function.")
            return All_Cards, player_current_cards, doubledown_output

        A54_Soft = A54soft(All_Cards, player_initial_cards, dealer_face_card)
        All_Cards = A54_Soft[0]
        player_current_cards = A54_Soft[1]
        doubledown_output = A54_Soft[2]
        print(player_current_cards)


    # Case 2.66: Player has A,3 or 3,A   or   A,2 or 2,A
    elif ((((player_initial_cards == [11, 3]) or (player_initial_cards == [3, 11])) or
          ((player_initial_cards == [11, 2]) or (player_initial_cards == [2, 11])))
          & (sum(dealer_initial_cards) <= 21)):
        print("Case 2.66: The player has A,3 or 3,A  or  A,2 or 2,A.")

        def A32soft(All_Cards, player_initial_cards, dealer_face_card):

            if ((dealer_face_card >= 5) or (dealer_face_card <= 6)):
                DoubleDown = playerdoubledown(All_Cards, player_initial_cards)
                All_Cards = DoubleDown[0]
                player_current_cards = DoubleDown[1]
                doubledown_output = DoubleDown[2]
                print("(Single Case A-double)")
            elif ((dealer_face_card <= 4) or (dealer_face_card >= 7)):
                PlayerDraws = playerdraws(All_Cards, player_initial_cards)
                All_Cards = PlayerDraws[0]
                player_current_cards = PlayerDraws[1]
                doubledown_output = 0
            else:
                print("Case not considered in 11,32/32,11 function.")
            return All_Cards, player_current_cards, doubledown_output

        A32_Soft = A32soft(All_Cards, player_initial_cards, dealer_face_card)
        All_Cards = A32_Soft[0]
        player_current_cards = A32_Soft[1]
        doubledown_output = A32_Soft[2]
        print(player_current_cards)


    # Case 3: Player has 12
    elif ((sum(player_initial_cards) == 12) & (sum(dealer_initial_cards) <= 21)):
        print("Case 3: The player has 12.")

        def twelve(All_Cards ,player_initial_cards ,dealer_face_card):

            if ((dealer_face_card <= 3) or (dealer_face_card >= 7)):
                PlayerDraws = playerdraws(All_Cards, player_initial_cards)
                All_Cards = PlayerDraws[0]
                player_current_cards = PlayerDraws[1]
                print("(Case A/C)")
            elif ((dealer_face_card >= 4) and (dealer_face_card <= 6)):
                All_Cards = All_Cards
                player_current_cards = player_initial_cards
                print("(Case B)")
            else:
                print("Case not considered in 12 function.")

            return All_Cards, player_current_cards
        Twelve = twelve(All_Cards, player_initial_cards, dealer_face_card)
        All_Cards = Twelve[0]
        player_current_cards = Twelve[1]
        print(player_current_cards)

    # Case 4: Player has 11
    elif ((sum(player_initial_cards) == 11) & (sum(dealer_initial_cards) <= 21)):
        print("Case 4: The player has 11.")

        def eleven(All_Cards, player_initial_cards, dealer_face_card):

            if (dealer_face_card <= 11):
                DoubleDown = playerdoubledown(All_Cards, player_initial_cards)
                All_Cards = DoubleDown[0]
                player_current_cards = DoubleDown[1]
                doubledown_output = DoubleDown[2]
                print("(Single Case A-double)")
            else:
                print("Case not considered in 11 function.")

            return All_Cards, player_current_cards, doubledown_output
        Eleven = eleven(All_Cards, player_initial_cards, dealer_face_card)
        All_Cards = Eleven[0]
        player_current_cards = Eleven[1]
        doubledown_output = Eleven[2]
        print(player_current_cards)

    # Case 5: Player has 10
    elif ((sum(player_initial_cards) == 10) & (sum(dealer_initial_cards) <= 21)):
        print("Case 5: The player has 10.")

        def ten(All_Cards, player_initial_cards, dealer_face_card):

            if (dealer_face_card <= 9):
                DoubleDown = playerdoubledown(All_Cards, player_initial_cards)
                All_Cards = DoubleDown[0]
                player_current_cards = DoubleDown[1]
                doubledown_output = DoubleDown[2]
                print("(Case A-double)")
            elif (dealer_face_card >= 10):
                PlayerDraws = playerdraws(All_Cards, player_initial_cards)
                All_Cards = PlayerDraws[0]
                player_current_cards = PlayerDraws[1]
                doubledown_output = 0
                print("(Case B-only hit)")
            else:
                print("Case not considered in 10 function.")

            return All_Cards, player_current_cards, doubledown_output
        Ten = ten(All_Cards, player_initial_cards, dealer_face_card)
        All_Cards = Ten[0]
        player_current_cards = Ten[1]
        doubledown_output = Ten[2]
        print(player_current_cards)

    # Case 6: Player has 9
    elif ((sum(player_initial_cards) == 9) & (sum(dealer_initial_cards) <= 21)):
        print("Case 9: The player has 9.")

        def nine(All_Cards ,player_initial_cards ,dealer_face_card):

            if ((dealer_face_card <= 2) or (dealer_face_card >= 7)):
                PlayerDraws = playerdraws(All_Cards, player_initial_cards)
                All_Cards = PlayerDraws[0]
                player_current_cards = PlayerDraws[1]
                doubledown_output = 0

                print("(Case A/C-only hit)")
            elif ((dealer_face_card >= 3) & (dealer_face_card <= 6)):
                DoubleDown = playerdoubledown(All_Cards, player_initial_cards)
                All_Cards = DoubleDown[0]
                player_current_cards = DoubleDown[1]
                doubledown_output = DoubleDown[2]
                print("(Case A-double)")
            else:
                print("Case not considered in 9 function.")

            return All_Cards, player_current_cards, doubledown_output
        Nine = nine(All_Cards, player_initial_cards, dealer_face_card)
        All_Cards = Nine[0]
        player_current_cards = Nine[1]
        doubledown_output = Nine[2]
        print(player_current_cards)

    # Case 7: Player has 8 or less
    elif ((sum(player_initial_cards) <= 8) & (sum(dealer_initial_cards) <= 21)):
        print("Case 7: The player has 8.")

        def eightorless(All_Cards ,player_initial_cards ,dealer_face_card):

            if (dealer_face_card <= 11):
                PlayerDraws = playerdraws(All_Cards ,player_initial_cards)
                All_Cards = PlayerDraws[0]
                player_current_cards = PlayerDraws[1]
                print("(Single Case A-just hit)")
            else:
                print("Case not considered in 8 or less function.")

            return All_Cards, player_current_cards
        EightOrLess = eightorless(All_Cards, player_initial_cards, dealer_face_card)
        All_Cards = EightOrLess[0]
        player_current_cards = EightOrLess[1]
        print(player_current_cards)

    else:
        print("Case not considered for Player: Global(game)")



    return All_Cards, player_current_cards, doubledown_output