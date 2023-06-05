from _08_Milestone_Project_2.War_Game.Card import Card
from _08_Milestone_Project_2.War_Game.Deck import Deck
from _08_Milestone_Project_2.War_Game.Player import Player

player_one = Player("One")
player_two = Player("Two")

new_Deck = Deck()
new_Deck.shuffle()

for x in range(26):
    player_one.add_cards(new_Deck.deal_one())
    player_two.add_cards(new_Deck.deal_one())

print(len(new_Deck.all_cards))
print(len(player_two.all_cards))
print(len(player_one.all_cards))

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")
    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:
        print(player_one)
        print(player_two)
        if player_one_cards[-1].values > player_two_cards[-1].values:
            # Player One gets the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            # No Longer at "war" , time for next round
            at_war = False
        elif player_one_cards[-1].values < player_two_cards[-1].values:

            # Player Two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            # No Longer at "war" , time for next round
            at_war = False
        else:
            print('WAR!')
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.

            # First check to see if player has enough cards

            # Check to see if a player is out of cards:
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
