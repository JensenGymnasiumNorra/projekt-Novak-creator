import random

#Deck

suits = ["Diamond", "Spade", "Heart", "Club" ]
cards = ["2","3","4","5","6","7","8","9","10","Ace", "Jack", "Queen", "King"]




#values

values = {
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "Jack" : 10,
    "Queen" : 10,
    "King" : 10,
    "Ace" : 11
}



#Visar värden

def calculate_value(list):
    total = 0
    aces = 0
    for y in list:
        rank = y.split(" ")[0]
        
        total += values[rank]
        if rank == "Ace":
            aces += 1
    
    #Kollar om aces ska vara värd 1 eller 11.
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
        


    return total

def can_split_cards():
    #Kollar om man kan splitta korten genom att kolla på första och andra korten i handen.
    rank1 = player_hand[0].split(" ")[0]
    rank2 = player_hand[1].split(" ")[0]
    return rank1 == rank2

def get_results(list1, list2):
    #Räknar pengarna och listar ut vem vinner.
    global player_saldo, player_bet_choice


    list1 = calculate_value(list1)
    list2 = calculate_value(list2)

    print(f"Your total: {list1} : Dealer total: {list2}")

    if list1 > 21:
        print("Loss")
        player_saldo -= player_bet_choice
    elif list2 > 21 or list1 > list2:
        print("\nYou win")
        player_saldo += player_bet_choice
    elif list1 == list2:
        print("\ntie")
    else:
        print("\nDealer wins!")
        player_saldo -= player_bet_choice


    
player_saldo = 1000


while True:
    #Skapar decken.
    deck = []

    for suit in suits:
        for card in cards:
            deck.append(card + " of " + suit + " ")        
    random.shuffle(deck)    

    player_hand = []
    dealer_hand = []

    # Om spelaren bestämmer sig att splitta.
    hand1 = []
    hand2 = []

    #Starting hand
    for x in range(2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())


    #Player turns.

    turn = 0
    BlackJack = False
    
    #Kollar om man satsar på mer pengar än man har.
    while True:
        print(f"Your saldo: {player_saldo}")
        player_bet_choice = int(input("What do you want to bet?: "))
        if player_bet_choice > player_saldo:
            print("You dont have that much money")
        else:
            break

   #Game loop.
    while True:
        print(*player_hand)
        print(calculate_value(player_hand))
        
        #Checks for blackjack
        if calculate_value(player_hand) == 21 and turn == 0:
            print("Blackjack!!!!!")
            BlackJack = True

            break

        
        
        if can_split_cards() and turn == 0:
            player_choice = input("Choose your action\n 1. Draw \n 2. Stand \n 3. Split ")
        else:
            player_choice = input("Choose your action\n 1. Draw\n 2. Stand ")
        
        if player_choice == "1":
            player_hand.append(deck.pop())
            turn +=1
            #Checks for bust
            if calculate_value(player_hand) > 21:
                print(calculate_value(player_hand))
                break

        elif player_choice == "2":
            break

        elif player_choice == "3" and turn == 0 and can_split_cards():
            hand1.append(player_hand.pop())
            hand2.append(player_hand.pop())

            #Kollar om de splitta korten är Ace eller inte.
            aces = hand1[0].split(" ")[0] == "Ace"
            #First hand game-loop om man splittar korten.
            while True:
                
                if aces:
                    hand1.append(deck.pop())
                    print("Only one card for aces, your first hand:")
                    print(*hand1)
                    print(calculate_value(hand1))
                    break
            

                print(*hand1)
                print(calculate_value(hand1))
                
                player_choice_split = input("Choose your input for your first hand:\n 1. Draw\n 2. Stand")
                if player_choice_split == "1":
                    hand1.append(deck.pop())
                    turn +=1
                    if calculate_value(hand1) > 21:
                      print(calculate_value(hand1))
                      break

                elif player_choice_split == "2":
                    break
            
            #Second hand game loop om man splittar
            while True:
            
                if aces:
                    hand2.append(deck.pop())
                    print("Only one card for aces, your second hand:")
                    print(*hand2)
                    print(calculate_value(hand2))
                    break
                
                print(*hand2)
                print(calculate_value(hand2))
            
                player_choice_split = input("Choose your input for your second hand: \n 1. Draw\n 2. Stand")
                if player_choice_split == "1":
                    hand2.append(deck.pop())
                    turn +=1
                    if calculate_value(hand2) > 21:
                      print(calculate_value(hand2))
                      break
                elif player_choice_split == "2":
                    break
            break
        
    while calculate_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    

    #Om hand1 är tom, så vet programmet att spelaren har inte splittat, so den tar värden av korten i player hand.
    if hand1 == []:
        get_results(player_hand, dealer_hand)
    else:
        print("First hand")
        get_results(hand1, dealer_hand)
        print("Second hand")
        get_results(hand2, dealer_hand)

    print(f"Final saldo: \n {player_saldo}")

    #Frågar om man vill köra igen.
    player_play_again_choice = input("Do you want to play again, Yes or No?").lower()
    if player_play_again_choice == "no":
        print("goodbye")
        break
    else:
        print("\n\n\nnew game started\n\n\n")
        








