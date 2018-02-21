import copy
import task6_deck as d

deck = d.Deck()
copy_deck = copy.copy(deck)

print(id(deck), id(copy_deck))
print(len(deck), len(copy_deck))

deck.shuffle()
print(len(deck), len(copy_deck))

copy_deck.shuffle()
print(len(deck), len(copy_deck))

c1 = deck.pick_from_top()
c2 = copy_deck.pick_from_top()

print(c1)
print(c2)
