
import random


# This is a statistical sampling approximation algorithm that simply simulates the game for a fixed number of dice rolls.
# An exact algorithm would involve calculating the eigenvector of the largest eigenvalue of the transition matrix (which is practical),
# but averaging over all possible permutations of both the Chance and Community Chest decks (which is computationally infeasible).
def problem084():
    """


    In the game, Monopoly, the standard board is set up in the following way:

                    GO   A1  CC1  A2  T1  R1  B1  CH1  B2   B3  JAIL
                    H2                                          C1
                    T2                                          U1
                    H1                                          C2
                    CH3                                         C3
                    R4                                          R2
                    G3                                          D1
                    CC3                                         CC2
                    G2                                          D2
                    G1                                          D3
                    G2J  F3  U2   F2  F1  R3  E3  E2   CH2  E1  FP

       A player starts on the GO square and adds the scores on two 6-sided dice
       to determine the number of squares they advance in a clockwise direction.
       Without any further rules we would expect to visit each square with equal
       probability: 2.5%. However, landing on G2J (Go To Jail), CC (community
       chest), and CH (chance) changes this distribution.

       In addition to G2J, and one card from each of CC and CH, that orders the
       player to go directly to jail, if a player rolls three consecutive
       doubles, they do not advance the result of their 3rd roll. Instead they
       proceed directly to jail.

       At the beginning of the game, the CC and CH cards are shuffled. When a
       player lands on CC or CH they take a card from the top of the respective
       pile and, after following the instructions, it is returned to the bottom
       of the pile. There are sixteen cards in each pile, but for the purpose of
       this
    Problem we are only concerned with cards that order a movement; any
       instruction not concerned with movement will be ignored and the player
       will remain on the CC/CH square.

         • Community Chest (2/16 cards):

             1. Advance to GO
             2. Go to JAIL

         • Chance (10/16 cards):

             1. Advance to GO
             2. Go to JAIL
             3. Go to C1
             4. Go to E3
             5. Go to H2
             6. Go to R1
             7. Go to next R (railway company)
             8. Go to next R
             9. Go to next U (utility company)
            10. Go back 3 squares.

       The heart of this
    Problem concerns the likelihood of visiting a particular
       square. That is, the probability of finishing at that square after a roll.
       For this reason it should be clear that, with the exception of G2J for
       which the probability of finishing on it is zero, the CH squares will have
       the lowest probabilities, as 5/8 request a movement to another square, and
       it is the final square that the player finishes at on each roll that we
       are interested in. We shall make no distinction between "Just Visiting"
       and being sent to JAIL, and we shall also ignore the rule about requiring
       a double to "get out of jail", assuming that they pay to get out on their
       next turn.

       By starting at GO and numbering the squares sequentially from 00 to 39 we
       can concatenate these two-digit numbers to produce strings that correspond
       with sets of squares.

       Statistically it can be shown that the three most popular squares, in
       order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO
       (3.09%) = Square 00. So these three most popular squares can be listed
       with the six-digit modal string: 102400.

       If, instead of using two 6-sided dice, two 4-sided dice are used, find the
       six-digit modal string.
    """
    TRIALS = 10 ** 7

    visitcounts = [0] * 40

    chance = CardDeck(16)
    communitychest = CardDeck(16)
    consecutivedoubles = 0
    location = 0

    for i in range(TRIALS):
        # Roll tetrahedral dice
        die0 = random.randint(1, 4)
        die1 = random.randint(1, 4)
        consecutivedoubles = (consecutivedoubles + 1) if (die0 == die1) else 0
        if consecutivedoubles < 3:
            location = (location + die0 + die1) % 40
        else:
            location = 30
            consecutivedoubles = 0

        # Process actions for some locations
        if location in (7, 22, 36):  # Chance
            card = chance.next_card()
            if card == 0:
                location = 0
            elif card == 1:
                location = 10
            elif card == 2:
                location = 11
            elif card == 3:
                location = 24
            elif card == 4:
                location = 39
            elif card == 5:
                location = 5
            elif card in (6, 7):  # Next railway
                location = (location + 5) // 10 % 4 * 10 + 5
            elif card == 8:  # Next utility
                location = 28 if (12 < location < 28) else 12
            elif card == 9:
                location -= 3
            else:
                pass
        elif location == 30:  # Go to jail
            location = 10
        else:
            pass

        if location in (2, 17, 33):  # Community chest
            card = communitychest.next_card()
            if card == 0:
                location = 0
            elif card == 1:
                location = 10

        visitcounts[location] += 1

    temp = sorted(enumerate(visitcounts), key=(lambda ic: -ic[1]))
    ans = "".join("{:02d}".format(i) for (i, c) in temp[: 3])
    return int(ans)


class CardDeck(object):

    def __init__(self, size):
        self.cards = list(range(size))
        self.index = size

    def next_card(self):
        if self.index == len(self.cards):
            random.shuffle(self.cards)
            self.index = 0
        result = self.cards[self.index]
        self.index += 1
        return result


if __name__ == "__main__":
    print(problem084())
