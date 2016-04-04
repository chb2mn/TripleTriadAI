#TripleTriadAI

###What is TripleTriad
This AI is based on TripleTriad as it is in Final Fantasy 8. [TripleTriad wiki](http://finalfantasy.wikia.com/wiki/Triple_Triad)

##How it works
The goal of this program is to determine which cards are better than others through a series of simulations.
Two AIs play each other and both take a greedy approach to playing always making the best move possible.
The AIs are both given a random set of cards based on defined values on min level and max level
(obviously a level 10 card is better than level 1 cards, but this is useful for figuring out in-rank which are better than others)

After the game concludes, the winning AI's hand is added back into the pool of random cards (making them more likely to appear again)
After 10 sets of 1000 games are concluded, we print the results.
