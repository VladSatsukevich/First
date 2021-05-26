import random

class BlackJack:

    def randomizer_dealer_cards():
        
        card = ['Туз', 'Король', 'Дама', 'Валет', 2, 3, 4, 5, 6, 7, 8, 9, 10]*4
        card_suits = ['♠', '♥', '♣', '♦'] * 4
        first_card = random.choice(card)
        second_card = random.choice(card)
        res = (f'Карты диллера: {(first_card)}{random.choice(card_suits)} {second_card}{random.choice(card_suits)}')
        print(res)
        if first_card == 'Туз':
            first_card = 1
        elif second_card == 'Туз':
            second_card = 1
        elif first_card == 'Король':
            first_card = 10
        elif second_card == 'Король':
            second_card = 10
        elif first_card == 'Дама':
            first_card = 10
        elif second_card == 'Дама':
            second_card = 10
        elif first_card == 'Валет':
            first_card = 10
        elif second_card == 'Валет':
            second_card = 10
        print(f'Сумма карт диллера: {first_card + second_card}')
        
rdc = BlackJack
rdc.randomizer_dealer_cards()    


class Player:

    def randomizer_player_cards():

        card = ["Туз", "Король", "Дама","Валет", 2, 3, 4, 5, 6, 7, 8, 9, 10]*4
        card_suits = ["♠", "♥", "♣", "♦"]*4
        first_card = random.choice(card)
        second_card = random.choice(card)
        res = (f'Ваши карты: {first_card}{random.choice(card_suits)} {second_card}{random.choice(card_suits)}')
        print(res)
        if first_card == 'Туз':
            first_card = 1
        elif second_card == 'Туз':
            second_card = 1
        elif first_card == 'Король':
            first_card = 10
        elif second_card == 'Король':
            second_card = 10
        elif first_card == 'Дама':
            first_card = 10
        elif second_card == 'Дама':
            second_card = 10
        elif first_card == 'Валет':
            first_card = 10
        elif second_card == 'Валет':
            second_card = 10
        print(f'Сумма ваших карт: {first_card + second_card}')

rpc = Player
rpc.randomizer_player_cards()
    

   

