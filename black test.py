import random



class BlackJack:

    def randomizer_dealer_cards():
        
        card = ["Туз", "Король", "Дама","Валет", 6, 7, 8, 9, 10]*4
        card_suits = ["♠", "♥", "♣", "♦"]
        first_card = random.choice(card)
        second_card = random.choice(card)
        print(f'Карты диллера: {(first_card)}{random.choice(card_suits)} {second_card}{random.choice(card_suits)}')
        
        
        print(f'Сумма карт диллера: {str(first_card) + str(second_card)}')
    randomizer_dealer_cards()
    


class Player:
    def randomizer_player_cards():
        card = ["Туз", "Король", "Дама","Валет", 6, 7, 8, 9, 10]
        card_suits = ["♠", "♥", "♣", "♦"]
        first_card = random.choice(card)
        second_card = random.choice(card)
        return (f'{first_card}{random.choice(card_suits)} {second_card}{random.choice(card_suits)}')
    print(f'Ваши карты: {randomizer_player_cards()}')

    
   

