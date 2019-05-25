# noinspection PyPackageRequirements
import pytest
from euler_python.medium import *


def test_smoke():
    print('is it on fire?')


def test_problem_66(answer):
    output = p066.problem066()
    expected_output = answer['Problem 066']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_68(answer):
    output = p068.problem068()
    expected_output = answer['Problem 068']
    assert output == expected_output


def test_problem_75(answer):
    output = p075.problem075()
    expected_output = answer['Problem 075']
    assert output == expected_output


def test_problem_77(answer):
    output = p077.problem077()
    expected_output = answer['Problem 077']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_78(answer):
    output = p078.problem078()
    expected_output = answer['Problem 078']
    assert output == expected_output


def test_problem_83(answer):
    output = p083.problem083()
    expected_output = answer['Problem 083']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_84(answer):
    output = p084.problem084()
    expected_output = answer['Problem 084']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_86(answer):
    output = p086.problem086()
    expected_output = answer['Problem 086']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_88(answer):
    output = p088.problem088()
    expected_output = answer['Problem 088']
    assert output == expected_output


def test_problem_90(answer):
    output = p090.problem090()
    expected_output = answer['Problem 090']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_91(answer):
    output = p091.problem091()
    expected_output = answer['Problem 091']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_93(answer):
    output = p093.problem093()
    expected_output = answer['Problem 093']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_94(answer):
    output = p094.problem094()
    expected_output = answer['Problem 094']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_95(answer):
    output = p095.problem095()
    expected_output = answer['Problem 095']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_96(answer):
    output = p096.problem096()
    expected_output = answer['Problem 096']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_98(answer):
    output = p098.problem098()
    expected_output = answer['Problem 098']
    assert output == expected_output


def test_problem_100(answer):
    output = p100.problem100()
    expected_output = answer['Problem 100']
    assert output == expected_output


def test_problem_101(answer):
    output = p101.problem101()
    expected_output = answer['Problem 101']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_103(answer):
    output = p103.problem103()
    expected_output = answer['Problem 103']
    assert output == expected_output


def test_problem_104(answer):
    output = p104.problem104()
    expected_output = answer['Problem 104']
    assert output == expected_output


def test_problem_105(answer):
    output = p105.problem105()
    expected_output = answer['Problem 105']
    assert output == expected_output


def test_problem_106(answer):
    output = p106.problem106()
    expected_output = answer['Problem 106']
    assert output == expected_output


"""


Let S(A) represent the sum of elements in set A of size n. We shall call
   it a special sum set if for any two non-empty disjoint subsets, B and C,
   the following properties are true:

   i. S(B) ≠ S(C); that is, sums of subsets cannot be equal.
   ii. If B contains more elements than C then S(B) > S(C).

   For this 
Problem we shall assume that a given set contains n strictly
   increasing elements and it already satisfies the second rule.

   Surprisingly, out of the 25 possible subset pairs that can be obtained
   from a set for which n = 4, only 1 of these pairs need to be tested for
   equality (first rule). Similarly, when n = 7, only 70 out of the 966
   subset pairs need to be tested.

   For n = 12, how many of the 261625 subset pairs that can be obtained need
   to be tested for equality?

   NOTE: This 
Problem is related to [1]
Problem 103 and [2]
Problem 105.
Visible links
   1. 
Problem=103
   2. 
Problem=105
"""


def test_problem_107(answer):
    output = p107.problem107()
    expected_output = answer['Problem 107']
    assert output == expected_output


"""


The following undirected network consists of seven vertices and twelve
   edges with a total weight of 243.

   The same network can be represented by the matrix below.

                  ┌──────┬────┬────┬────┬────┬────┬────┬────┐
                  │      │ A  │ B  │ C  │ D  │ E  │ F  │ G  │
                  ├──────┼────┼────┼────┼────┼────┼────┼────┤
                  │ A    │ -  │ 16 │ 12 │ 21 │ -  │ -  │ -  │
                  ├──────┼────┼────┼────┼────┼────┼────┼────┤
                  │ B    │ 16 │ -  │ -  │ 17 │ 20 │ -  │ -  │
                  ├──────┼────┼────┼────┼────┼────┼────┼────┤
                  │ C    │ 12 │ -  │ -  │ 28 │ -  │ 31 │ -  │
                  ├──────┼────┼────┼────┼────┼────┼────┼────┤
                  │ D    │ 21 │ 17 │ 28 │ -  │ 18 │ 19 │ 23 │
                  ├──────┼────┼────┼────┼────┼────┼────┼────┤
                  │ E    │ -  │ 20 │ -  │ 18 │ -  │ -  │ 11 │
                  ├──────┼────┼────┼────┼────┼────┼────┼────┤
                  │ F    │ -  │ -  │ 31 │ 19 │ -  │ -  │ 27 │
                  ├──────┼────┼────┼────┼────┼────┼────┼────┤
                  │ G    │ -  │ -  │ -  │ 23 │ 11 │ 27 │ -  │
                  └──────┴────┴────┴────┴────┴────┴────┴────┘

   However, it is possible to optimise the network by removing some edges and
   still ensure that all points on the network remain connected. The network
   which achieves the maximum saving is shown below. It has a weight of 93,
   representing a saving of 243 − 93 = 150 from the original network.

   Using [1]network.txt, a 6K text file containing a network with forty
   vertices, and given in matrix form, find the maximum saving which can be
   achieved by removing redundant edges whilst ensuring that the network
   remains connected.
Visible links
   1. network.txt
   p_107_1.gif
   p_107_2.gif
"""


@pytest.mark.skip(reason='too slow')
def test_problem_108(answer):
    output = p108.problem108()
    expected_output = answer['Problem 108']
    assert output == expected_output


"""


In the following equation x, y, and n are positive integers.

                                   1   1   1
                                   ─ + ─ = ─
                                   x   y   n

   For n = 4 there are exactly three distinct solutions:

                                   1   1    1
                                   ─ + ─  = ─
                                   5   20   4
                                   1   1    1
                                   ─ + ─  = ─
                                   6   12   4
                                   1   1    1
                                   ─ + ─  = ─
                                   8   8    4

   What is the least value of n for which the number of distinct solutions
   exceeds one-thousand?

   NOTE: This 
Problem is an easier version of [1]
Problem 110; it is strongly
   advised that you solve this one first.
Visible links
   1. 
Problem=110
"""


def test_problem_109(answer):
    output = p109.problem109()
    expected_output = answer['Problem 109']
    assert output == expected_output


"""


In the game of darts a player throws three darts at a target board which
   is split into twenty equal sized sections numbered one to twenty.

   The score of a dart is determined by the number of the region that the
   dart lands in. A dart landing outside the red/green outer ring scores
   zero. The black and cream regions inside this ring represent single
   scores. However, the red/green outer ring and middle ring score double and
   treble scores respectively.

   At the centre of the board are two concentric circles called the bull
   region, or bulls-eye. The outer bull is worth 25 points and the inner bull
   is a double, worth 50 points.

   There are many variations of rules but in the most popular game the
   players will begin with a score 301 or 501 and the first player to reduce
   their running total to zero is a winner. However, it is normal to play a
   "doubles out" system, which means that the player must land a double
   (including the double bulls-eye at the centre of the board) on their final
   dart to win; any other dart that would reduce their running total to one
   or lower means the score for that set of three darts is "bust".

   When a player is able to finish on their current score it is called a
   "checkout" and the highest checkout is 170: T20 T20 D25 (two treble 20s
   and double bull).

   There are exactly eleven distinct ways to checkout on a score of 6:

                                   ┌──┬──┬──┐
                                   │D3│  │  │
                                   ├──┼──┼──┤
                                   │D1│D2│  │
                                   ├──┼──┼──┤
                                   │S2│D2│  │
                                   ├──┼──┼──┤
                                   │D2│D1│  │
                                   ├──┼──┼──┤
                                   │S4│D1│  │
                                   ├──┼──┼──┤
                                   │S1│S1│D2│
                                   ├──┼──┼──┤
                                   │S1│T1│D1│
                                   ├──┼──┼──┤
                                   │S1│S3│D1│
                                   ├──┼──┼──┤
                                   │D1│D1│D1│
                                   ├──┼──┼──┤
                                   │D1│S2│D1│
                                   ├──┼──┼──┤
                                   │S2│S2│D1│
                                   └──┴──┴──┘

   Note that D1 D2 is considered different to D2 D1 as they finish on
   different doubles. However, the combination S1 T1 D1 is considered the
   same as T1 S1 D1.

   In addition we shall not include misses in considering combinations; for
   example, D3 is the same as 0 D3 and 0 0 D3.

   Incredibly there are 42336 distinct ways of checking out in total.

   How many distinct ways can a player checkout with a score less than 100?
p_109.gif
"""


def test_problem_110(answer):
    output = p110.problem110()
    expected_output = answer['Problem 110']
    assert output == expected_output


"""


In the following equation x, y, and n are positive integers.

                                   1   1   1
                                   ─ + ─ = ─
                                   x   y   n

   It can be verified that when n = 1260 there are 113 distinct solutions and
   this is the least value of n for which the total number of distinct
   solutions exceeds one hundred.

   What is the least value of n for which the number of distinct solutions
   exceeds four million?

   NOTE: This 
Problem is a much more difficult version of [1]
Problem 108 and
   as it is well beyond the limitations of a brute force approach it requires
   a clever implementation.
Visible links
   1. 
Problem=108
"""


def test_problem_111(answer):
    output = p111.problem111()
    expected_output = answer['Problem 111']
    assert output == expected_output


"""


Considering 4-digit primes containing repeated digits it is clear that
   they cannot all be the same: 1111 is divisible by 11, 2222 is divisible by
   22, and so on. But there are nine 4-digit primes containing three ones:

              1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

   We shall say that M(n, d) represents the maximum number of repeated digits
   for an n-digit prime where d is the repeated digit, N(n, d) represents the
   number of such primes, and S(n, d) represents the sum of these primes.

   So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit
   prime where one is the repeated digit, there are N(4, 1) = 9 such primes,
   and the sum of these primes is S(4, 1) = 22275. It turns out that for d =
   0, it is only possible to have M(4, 0) = 2 repeated digits, but there are
   N(4, 0) = 13 such cases.

   In the same way we obtain the following results for 4-digit primes.

                   ┌──────────┬─────────┬─────────┬─────────┐
                   │ Digit, d │ M(4, d) │ N(4, d) │ S(4, d) │
                   ├──────────┼─────────┼─────────┼─────────┤
                   │ 0        │ 2       │ 13      │ 67061   │
                   ├──────────┼─────────┼─────────┼─────────┤
                   │ 1        │ 3       │ 9       │ 22275   │
                   ├──────────┼─────────┼─────────┼─────────┤
                   │ 2        │ 3       │ 1       │ 2221    │
                   ├──────────┼─────────┼─────────┼─────────┤
                   │ 3        │ 3       │ 12      │ 46214   │
                   ├──────────┼─────────┼─────────┼─────────┤
                   │ 4        │ 3       │ 2       │ 8888    │
                   ├──────────┼─────────┼─────────┼─────────┤
                   │ 5        │ 3       │ 1       │ 5557    │
                   ├──────────┼─────────┼─────────┼─────────┤
                   │ 6        │ 3       │ 1       │ 6661    │
                   ├──────────┼─────────┼─────────┼─────────┤
                   │ 7        │ 3       │ 9       │ 57863   │
                   ├──────────┼─────────┼─────────┼─────────┤
                   │ 8        │ 3       │ 1       │ 8887    │
                   ├──────────┼─────────┼─────────┼─────────┤
                   │ 9        │ 3       │ 7       │ 48073   │
                   └──────────┴─────────┴─────────┴─────────┘

   For d = 0 to 9, the sum of all S(4, d) is 273700.

   Find the sum of all S(10, d).
"""


def test_problem_113(answer):
    output = p113.problem113()
    expected_output = answer['Problem 113']
    assert output == expected_output


"""


Working from left-to-right if no digit is exceeded by the digit to its
   left it is called an increasing number; for example, 134468.

   Similarly if no digit is exceeded by the digit to its right it is called a
   decreasing number; for example, 66420.

   We shall call a positive integer that is neither increasing nor decreasing
   a "bouncy" number; for example, 155349.

   As n increases, the proportion of bouncy numbers below n increases such
   that there are only 12951 numbers below one-million that are not bouncy
   and only 277032 non-bouncy numbers below 10^10.

   How many numbers below a googol (10^100) are not bouncy?
"""


def test_problem_114(answer):
    output = p114.problem114()
    expected_output = answer['Problem 114']
    assert output == expected_output


"""


A row measuring seven units in length has red blocks with a minimum length
   of three units placed on it, such that any two red blocks (which are
   allowed to be different lengths) are separated by at least one black
   square. There are exactly seventeen ways of doing this.

                          ┌┬┬┬┬┬┬┐  ┌──┬┬┬┬┐  ┌┬──┬┬┬┐
                          └┴┴┴┴┴┴┘  └──┴┴┴┴┘  └┴──┴┴┴┘
                          ┌┬┬──┬┬┐  ┌┬┬┬──┬┐  ┌┬┬┬┬──┐
                          └┴┴──┴┴┘  └┴┴┴──┴┘  └┴┴┴┴──┘
                          ┌──┬┬──┐  ┌───┬┬┬┐  ┌┬───┬┬┐
                          └──┴┴──┘  └───┴┴┴┘  └┴───┴┴┘
                          ┌┬┬───┬┐  ┌┬┬┬───┐  ┌────┬┬┐
                          └┴┴───┴┘  └┴┴┴───┘  └────┴┴┘
                          ┌┬────┬┐  ┌┬┬────┐  ┌─────┬┐
                          └┴────┴┘  └┴┴────┘  └─────┴┘
                          ┌┬─────┐  ┌──────┐   
                          └┴─────┘  └──────┘

   How many ways can a row measuring fifty units in length be filled?

   NOTE: Although the example above does not lend itself to the possibility,
   in general it is permitted to mix block sizes. For example, on a row
   measuring eight units in length you could use red (3), black (1), and red
   (4).
"""


def test_problem_115(answer):
    output = p115.problem115()
    expected_output = answer['Problem 115']
    assert output == expected_output


"""


NOTE: This is a more difficult version of [1]
Problem 114.

   A row measuring n units in length has red blocks with a minimum length of
   m units placed on it, such that any two red blocks (which are allowed to
   be different lengths) are separated by at least one black square.

   Let the fill-count function, F(m, n), represent the number of ways that a
   row can be filled.

   For example, F(3, 29) = 673135 and F(3, 30) = 1089155.

   That is, for m = 3, it can be seen that n = 30 is the smallest value for
   which the fill-count function first exceeds one million.

   In the same way, for m = 10, it can be verified that F(10, 56) = 880711
   and F(10, 57) = 1148904, so n = 57 is the least value for which the
   fill-count function first exceeds one million.

   For m = 50, find the least value of n for which the fill-count function
   first exceeds one million.
Visible links
   1. 
Problem=114
"""


def test_problem_116(answer):
    output = p116.problem116()
    expected_output = answer['Problem 116']
    assert output == expected_output


"""


A row of five black square tiles is to have a number of its tiles replaced
   with coloured oblong tiles chosen from red (length two), green (length
   three), or blue (length four).

   If red tiles are chosen there are exactly seven ways this can be done.

                         ┌─╥╥╥┐  ┌╥─╥╥┐  ┌╥╥─╥┐  ┌╥╥╥─┐
                         └─╨╨╨┘  └╨─╨╨┘  └╨╨─╨┘  └╨╨╨─┘

                         ┌─╥─╥┐  ┌─╥╥─┐  ┌╥─╥─┐   
                         └─╨─╨┘  └─╨╨─┘  └╨─╨─┘

   If green tiles are chosen there are three ways.

                           ┌──╥╥┐  ┌╥──╥┐  ┌╥╥──┐   
                           └──╨╨┘  └╨──╨┘  └╨╨──┘

   And if blue tiles are chosen there are two ways.

                                 ┌╥───┐  ┌───╥┐
                                 └╨───┘  └───╨┘

   Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of
   replacing the black tiles in a row measuring five units in length.

   How many different ways can the black tiles in a row measuring fifty units
   in length be replaced if colours cannot be mixed and at least one coloured
   tile must be used?

   NOTE: This is related to [1]
Problem 117.
Visible links
   1. 
Problem=117
"""


def test_problem_117(answer):
    output = p117.problem117()
    expected_output = answer['Problem 117']
    assert output == expected_output


"""


Using a combination of black square tiles and oblong tiles chosen from:
   red tiles measuring two units, green tiles measuring three units, and blue
   tiles measuring four units, it is possible to tile a row measuring five
   units in length in exactly fifteen different ways.

                         ┌╥╥╥╥┐  ┌─╥╥╥┐  ┌╥─╥╥┐  ┌╥╥─╥┐
                         └╨╨╨╨┘  └─╨╨╨┘  └╨─╨╨┘  └╨╨─╨┘

                         ┌╥╥╥─┐  ┌─╥─╥┐  ┌─╥╥─┐  ┌╥─╥─┐
                         └╨╨╨─┘  └─╨─╨┘  └─╨╨─┘  └╨─╨─┘

                         ┌──╥╥┐  ┌╥──╥┐  ┌╥╥──┐  ┌─╥──┐
                         └──╨╨┘  └╨──╨┘  └╨╨──┘  └─╨──┘

                         ┌──╥─┐  ┌───╥┐  ┌╥───┐   
                         └──╨─┘  └───╨┘  └╨───┘

   How many ways can a row measuring fifty units in length be tiled?

   NOTE: This is related to [1]
Problem 116.
Visible links
   1. 
Problem=116
"""


@pytest.mark.skip(reason='slow')
def test_problem_118(answer):
    output = p118.problem118()
    expected_output = answer['Problem 118']
    assert output == expected_output


"""


Using all of the digits 1 through 9 and concatenating them freely to form
   decimal integers, different sets can be formed. Interestingly with the set
   {2,5,47,89,631}, all of the elements belonging to it are prime.

   How many distinct sets containing each of the digits one through nine
   exactly once contain only prime elements?
"""


def test_problem_119(answer):
    output = p119.problem119()
    expected_output = answer['Problem 119']
    assert output == expected_output


"""


The number 512 is interesting because it is equal to the sum of its digits
   raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512. Another example of a
   number with this property is 614656 = 28^4.

   We shall define a[n] to be the nth term of this sequence and insist that a
   number must contain at least two digits to have a sum.

   You are given that a[2] = 512 and a[10] = 614656.

   Find a[30].
"""


def test_problem_120(answer):
    output = p120.problem120()
    expected_output = answer['Problem 120']
    assert output == expected_output


"""


Let r be the remainder when (a−1)^n + (a+1)^n is divided by a^2.

   For example, if a = 7 and n = 3, then r = 42: 6^3 + 8^3 = 728 ≡ 42 mod 49.
   And as n varies, so too will r, but for a = 7 it turns out that r[max] =
   42.

   For 3 ≤ a ≤ 1000, find ∑ r[max].
"""


def test_problem_121(answer):
    output = p121.problem121()
    expected_output = answer['Problem 121']
    assert output == expected_output


"""


A bag contains one red disc and one blue disc. In a game of chance a
   player takes a disc at random and its colour is noted. After each turn the
   disc is returned to the bag, an extra red disc is added, and another disc
   is taken at random.

   The player pays £1 to play and wins if they have taken more blue discs
   than red discs at the end of the game.

   If the game is played for four turns, the probability of a player winning
   is exactly 11/120, and so the maximum prize fund the banker should
   allocate for winning in this game would be £10 before they would expect to
   incur a loss. Note that any payout will be a whole number of pounds and
   also includes the original £1 paid to play the game, so in the example
   given the player actually wins £9.

   Find the maximum prize fund that should be allocated to a single game in
   which fifteen turns are played.
"""


@pytest.mark.skip(reason='too slow')
def test_problem_122(answer):
    output = p122.problem122()
    expected_output = answer['Problem 122']
    assert output == expected_output


"""


The most naive way of computing n^15 requires fourteen multiplications:

   n × n × ... × n = n^15

   But using a "binary" method you can compute it in six multiplications:

   n × n = n^2
   n^2 × n^2 = n^4
   n^4 × n^4 = n^8
   n^8 × n^4 = n^12
   n^12 × n^2 = n^14
   n^14 × n = n^15

   However it is yet possible to compute it in only five multiplications:

   n × n = n^2
   n^2 × n = n^3
   n^3 × n^3 = n^6
   n^6 × n^6 = n^12
   n^12 × n^3 = n^15

   We shall define m(k) to be the minimum number of multiplications to
   compute n^k; for example m(15) = 5.

   For 1 ≤ k ≤ 200, find ∑ m(k).
"""


def test_problem_123(answer):
    output = p123.problem123()
    expected_output = answer['Problem 123']
    assert output == expected_output


"""


Let p[n] be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder
   when (p[n]−1)^n + (p[n]+1)^n is divided by p[n]^2.

   For example, when n = 3, p[3] = 5, and 4^3 + 6^3 = 280 ≡ 5 mod 25.

   The least value of n for which the remainder first exceeds 10^9 is 7037.

   Find the least value of n for which the remainder first exceeds 10^10.
"""


def test_problem_124(answer):
    output = p124.problem124()
    expected_output = answer['Problem 124']
    assert output == expected_output


"""


The radical of n, rad(n), is the product of the distinct prime factors of
   n. For example, 504 = 2^3 × 3^2 × 7, so rad(504) = 2 × 3 × 7 = 42.

   If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and
   sorting on n if the radical values are equal, we get:

                            Unsorted       Sorted
                            n  rad(n)   n  rad(n) k
                            1    1      1    1    1
                            2    2      2    2    2
                            3    3      4    2    3
                            4    2      8    2    4
                            5    5      3    3    5
                            6    6      9    3    6
                            7    7      5    5    7
                            8    2      6    6    8
                            9    3      7    7    9
                            10   10     10   10   10

   Let E(k) be the kth element in the sorted n column; for example, E(4) = 8
   and E(6) = 9.

   If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).
"""


def test_problem_125(answer):
    output = p125.problem125()
    expected_output = answer['Problem 125']
    assert output == expected_output


"""


The palindromic number 595 is interesting because it can be written as the
   sum of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

   There are exactly eleven palindromes below one-thousand that can be
   written as consecutive square sums, and the sum of these palindromes is
   4164. Note that 1 = 0^2 + 1^2 has not been included as this 
Problem is
   concerned with the squares of positive integers.

   Find the sum of all the numbers less than 10^8 that are both palindromic
   and can be written as the sum of consecutive squares.
"""


def test_problem_126(answer):
    output = p126.problem126()
    expected_output = answer['Problem 126']
    assert output == expected_output


"""


The minimum number of cubes to cover every visible face on a cuboid
   measuring 3 x 2 x 1 is twenty-two.

   If we then add a second layer to this solid it would require forty-six
   cubes to cover every visible face, the third layer would require
   seventy-eight cubes, and the fourth layer would require one-hundred and
   eighteen cubes to cover every visible face.

   However, the first layer on a cuboid measuring 5 x 1 x 1 also requires
   twenty-two cubes; similarly the first layer on cuboids measuring
   5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain forty-six cubes.

   We shall define C(n) to represent the number of cuboids that contain n
   cubes in one of its layers. So C(22) = 2, C(46) = 4, C(78) = 5, and C(118)
   = 8.

   It turns out that 154 is the least value of n for which C(n) = 10.

   Find the least value of n for which C(n) = 1000.
p_126.gif
"""


@pytest.mark.skip(reason='too slow')
def test_problem_127(answer):
    output = p127.problem127()
    expected_output = answer['Problem 127']
    assert output == expected_output


"""


The radical of n, rad(n), is the product of distinct prime factors of n.
   For example, 504 = 2^3 × 3^2 × 7, so rad(504) = 2 × 3 × 7 = 42.

   We shall define the triplet of positive integers (a, b, c) to be an
   abc-hit if:

    1. GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
    2. a < b
    3. a + b = c
    4. rad(abc) < c

   For example, (5, 27, 32) is an abc-hit, because:

    1. GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
    2. 5 < 27
    3. 5 + 27 = 32
    4. rad(4320) = 30 < 32

   It turns out that abc-hits are quite rare and there are only thirty-one
   abc-hits for c < 1000, with ∑c = 12523.

   Find ∑c for c < 120000.
"""


def test_problem_128(answer):
    output = p128.problem128()
    expected_output = answer['Problem 128']
    assert output == expected_output


"""


A hexagonal tile with number 1 is surrounded by a ring of six hexagonal
   tiles, starting at "12 o'clock" and numbering the tiles 2 to 7 in an
   anti-clockwise direction.

   New rings are added in the same fashion, with the next rings being
   numbered 8 to 19, 20 to 37, 38 to 61, and so on. The diagram below shows
   the first three rings.

   By finding the difference between tile n and each its six neighbours we
   shall define PD(n) to be the number of those differences which are prime.

   For example, working clockwise around tile 8 the differences are 12, 29,
   11, 6, 1, and 13. So PD(8) = 3.

   In the same way, the differences around tile 17 are 1, 17, 16, 1, 11, and
   10, hence PD(17) = 2.

   It can be shown that the maximum value of PD(n) is 3.

   If all of the tiles for which PD(n) = 3 are listed in ascending order to
   form a sequence, the 10th tile would be 271.

   Find the 2000th tile in this sequence.
p_128.gif
"""


def test_problem_129(answer):
    output = p129.problem129()
    expected_output = answer['Problem 129']
    assert output == expected_output


"""


A number consisting entirely of ones is called a repunit. We shall define
   R(k) to be a repunit of length k; for example, R(6) = 111111.

   Given that n is a positive integer and GCD(n, 10) = 1, it can be shown
   that there always exists a value, k, for which R(k) is divisible by n, and
   let A(n) be the least such value of k; for example, A(7) = 6 and A(41) =
   5.

   The least value of n for which A(n) first exceeds ten is 17.

   Find the least value of n for which A(n) first exceeds one-million.
"""


def test_problem_130(answer):
    output = p130.problem130()
    expected_output = answer['Problem 130']
    assert output == expected_output


"""


A number consisting entirely of ones is called a repunit. We shall define
   R(k) to be a repunit of length k; for example, R(6) = 111111.

   Given that n is a positive integer and GCD(n, 10) = 1, it can be shown
   that there always exists a value, k, for which R(k) is divisible by n, and
   let A(n) be the least such value of k; for example, A(7) = 6 and A(41) =
   5.

   You are given that for all primes, p > 5, that p − 1 is divisible by A(p).
   For example, when p = 41, A(41) = 5, and 40 is divisible by 5.

   However, there are rare composite values for which this is also true; the
   first five examples being 91, 259, 451, 481, and 703.

   Find the sum of the first twenty-five composite values of n for which
   GCD(n, 10) = 1 and n − 1 is divisible by A(n).
"""


def test_problem_131(answer):
    output = p131.problem131()
    expected_output = answer['Problem 131']
    assert output == expected_output


"""


There are some prime values, p, for which there exists a positive integer,
   n, such that the expression n^3 + n^2p is a perfect cube.

   For example, when p = 19, 8^3 + 8^2×19 = 12^3.

   What is perhaps most surprising is that for each prime with this property
   the value of n is unique, and there are only four such primes below
   one-hundred.

   How many primes below one million have this remarkable property?
"""


def test_problem_132(answer):
    output = p132.problem132()
    expected_output = answer['Problem 132']
    assert output == expected_output


"""


A number consisting entirely of ones is called a repunit. We shall define
   R(k) to be a repunit of length k.

   For example, R(10) = 1111111111 = 11×41×271×9091, and the sum of these
   prime factors is 9414.

   Find the sum of the first forty prime factors of R(10^9).
"""


def test_problem_133(answer):
    output = p133.problem133()
    expected_output = answer['Problem 133']
    assert output == expected_output


"""


A number consisting entirely of ones is called a repunit. We shall define
   R(k) to be a repunit of length k; for example, R(6) = 111111.

   Let us consider repunits of the form R(10^n).

   Although R(10), R(100), or R(1000) are not divisible by 17, R(10000) is
   divisible by 17. Yet there is no value of n for which R(10^n) will divide
   by 19. In fact, it is remarkable that 11, 17, 41, and 73 are the only four
   primes below one-hundred that can be a factor of R(10^n).

   Find the sum of all the primes below one-hundred thousand that will never
   be a factor of R(10^n).
"""


def test_problem_134(answer):
    output = p134.problem134()
    expected_output = answer['Problem 134']
    assert output == expected_output


"""


Consider the consecutive primes p[1] = 19 and p[2] = 23. It can be
   verified that 1219 is the smallest number such that the last digits are
   formed by p[1] whilst also being divisible by p[2].

   In fact, with the exception of p[1] = 3 and p[2] = 5, for every pair of
   consecutive primes, p[2] > p[1], there exist values of n for which the
   last digits are formed by p[1] and n is divisible by p[2]. Let S be the
   smallest of these values of n.

   Find ∑ S for every pair of consecutive primes with 5 ≤ p[1] ≤ 1000000.
"""


def test_problem_135(answer):
    output = p135.problem135()
    expected_output = answer['Problem 135']
    assert output == expected_output


"""


Given the positive integers, x, y, and z, are consecutive terms of an
   arithmetic progression, the least value of the positive integer, n, for
   which the equation, x^2 − y^2 − z^2 = n, has exactly two solutions is n =
   27:

                   34^2 − 27^2 − 20^2 = 12^2 − 9^2 − 6^2 = 27

   It turns out that n = 1155 is the least value which has exactly ten
   solutions.

   How many values of n less than one million have exactly ten distinct
   solutions?
"""


def test_problem_136(answer):
    output = p136.problem136()
    expected_output = answer['Problem 136']
    assert output == expected_output


"""


The positive integers, x, y, and z, are consecutive terms of an arithmetic
   progression. Given that n is a positive integer, the equation, x^2 − y^2 −
   z^2 = n, has exactly one solution when n = 20:

                             13^2 − 10^2 − 7^2 = 20

   In fact there are twenty-five values of n below one hundred for which the
   equation has a unique solution.

   How many values of n less than fifty million have exactly one solution?
"""


def test_problem_137(answer):
    output = p137.problem137()
    expected_output = answer['Problem 137']
    assert output == expected_output


"""


Consider the infinite polynomial series A[F](x) = xF[1] + x^2F[2] +
   x^3F[3] + ..., where F[k] is the kth term in the Fibonacci sequence: 1, 1,
   2, 3, 5, 8, ... ; that is, F[k] = F[k−1] + F[k−2], F[1] = 1 and F[2] = 1.

   For this 
Problem we shall be interested in values of x for which A[F](x)
   is a positive integer.

   Surprisingly A[F](1/2)  =  (1/2).1 + (1/2)^2.1 + (1/2)^3.2 + (1/2)^4.3 +
                              (1/2)^5.5 + ...
                           =  1/2 + 1/4 + 2/8 + 3/16 + 5/32 + ...
                           =  2

   The corresponding values of x for the first five natural numbers are shown
   below.

                              ┌─────────┬───────┐
                              │x        │A[F](x)│
                              ├─────────┼───────┤
                              │√2−1     │1      │
                              ├─────────┼───────┤
                              │1/2      │2      │
                              ├─────────┼───────┤
                              │(√13−2)/3│3      │
                              ├─────────┼───────┤
                              │(√89−5)/8│4      │
                              ├─────────┼───────┤
                              │(√34−3)/5│5      │
                              └─────────┴───────┘

   We shall call A[F](x) a golden nugget if x is rational, because they
   become increasingly rarer; for example, the 10th golden nugget is
   74049690.

   Find the 15th golden nugget.
"""


def test_problem_138(answer):
    output = p138.problem138()
    expected_output = answer['Problem 138']
    assert output == expected_output


"""


Consider the isosceles triangle with base length, b = 16, and legs, L =
   17.

   By using the Pythagorean theorem it can be seen that the height of the
   triangle, h = √(17^2 − 8^2) = 15, which is one less than the base length.

   With b = 272 and L = 305, we get h = 273, which is one more than the base
   length, and this is the second smallest isosceles triangle with the
   property that h = b ± 1.

   Find ∑ L for the twelve smallest isosceles triangles for which h = b ± 1
   and b, L are positive integers.
p_138.gif
"""


@pytest.mark.skip(reason='too slow')
def test_problem_139(answer):
    output = p139.problem139()
    expected_output = answer['Problem 139']
    assert output == expected_output


"""


Let (a, b, c) represent the three sides of a right angle triangle with
   integral length sides. It is possible to place four such triangles
   together to form a square with length c.

   For example, (3, 4, 5) triangles can be placed together to form a 5 by 5
   square with a 1 by 1 hole in the middle and it can be seen that the 5 by 5
   square can be tiled with twenty-five 1 by 1 squares.

   However, if (5, 12, 13) triangles were used then the hole would measure 7
   by 7 and these could not be used to tile the 13 by 13 square.

   Given that the perimeter of the right triangle is less than one-hundred
   million, how many Pythagorean triangles would allow such a tiling to take
   place?
p_139.gif
"""


def test_problem_140(answer):
    output = p140.problem140()
    expected_output = answer['Problem 140']
    assert output == expected_output


"""


Consider the infinite polynomial series A[G](x) = xG[1] + x^2G[2] +
   x^3G[3] + ..., where G[k] is the kth term of the second order recurrence
   relation G[k] = G[k−1] + G[k−2], G[1] = 1 and G[2] = 4; that is, 1, 4, 5,
   9, 14, 23, ... .

   For this 
Problem we shall be concerned with values of x for which A[G](x)
   is a positive integer.

   The corresponding values of x for the first five natural numbers are shown
   below.

                             ┌───────────┬───────┐
                             │x          │A[G](x)│
                             ├───────────┼───────┤
                             │(√5−1)/4   │1      │
                             ├───────────┼───────┤
                             │2/5        │2      │
                             ├───────────┼───────┤
                             │(√22−2)/6  │3      │
                             ├───────────┼───────┤
                             │(√137−5)/14│4      │
                             ├───────────┼───────┤
                             │1/2        │5      │
                             └───────────┴───────┘

   We shall call A[G](x) a golden nugget if x is rational, because they
   become increasingly rarer; for example, the 20th golden nugget is
   211345365.

   Find the sum of the first thirty golden nuggets.
"""


def test_problem_141(answer):
    output = p141.problem141()
    expected_output = answer['Problem 141']
    assert output == expected_output


"""


A positive integer, n, is divided by d and the quotient and remainder are
   q and r respectively. In addition d, q, and r are consecutive positive
   integer terms in a geometric sequence, but not necessarily in that order.

   For example, 58 divided by 6 has quotient 9 and remainder 4. It can also
   be seen that 4, 6, 9 are consecutive terms in a geometric sequence (common
   ratio 3/2).
   We will call such numbers, n, progressive.

   Some progressive numbers, such as 9 and 10404 = 102^2, happen to also be
   perfect squares.
   The sum of all progressive perfect squares below one hundred thousand is
   124657.

   Find the sum of all progressive perfect squares below one trillion
   (10^12).
"""


@pytest.mark.skip(reason='too slow')
def test_problem_142(answer):
    output = p142.problem142()
    expected_output = answer['Problem 142']
    assert output == expected_output


"""


Find the smallest x + y + z with integers x > y > z > 0 such that x + y, x
   − y, x + z, x − z, y + z, y − z are all perfect squares.
"""


def test_problem_143(answer):
    output = p143.problem143()
    expected_output = answer['Problem 143']
    assert output == expected_output


"""


Let ABC be a triangle with all interior angles being less than 120
   degrees. Let X be any point inside the triangle and let XA = p, XC = q,
   and XB = r.

   Fermat challenged Torricelli to find the position of X such that p + q + r
   was minimised.

   Torricelli was able to prove that if equilateral triangles AOB, BNC and
   AMC are constructed on each side of triangle ABC, the circumscribed
   circles of AOB, BNC, and AMC will intersect at a single point, T, inside
   the triangle. Moreover he proved that T, called the Torricelli/Fermat
   point, minimises p + q + r. Even more remarkable, it can be shown that
   when the sum is minimised, AN = BM = CO = p + q + r and that AN, BM and CO
   also intersect at T.

   If the sum is minimised and a, b, c, p, q and r are all positive integers
   we shall call triangle ABC a Torricelli triangle. For example, a = 399, b
   = 455, c = 511 is an example of a Torricelli triangle, with p + q + r =
   784.

   Find the sum of all distinct values of p + q + r ≤ 120000 for Torricelli
   triangles.
p_143_torricelli.gif
"""


def test_problem_144(answer):
    output = p144.problem144()
    expected_output = answer['Problem 144']
    assert output == expected_output


"""


In laser physics, a "white cell" is a mirror system that acts as a delay
   line for the laser beam. The beam enters the cell, bounces around on the
   mirrors, and eventually works its way back out.

   The specific white cell we will be considering is an ellipse with the
   equation 4x^2 + y^2 = 100

   The section corresponding to −0.01 ≤ x ≤ +0.01 at the top is missing,
   allowing the light to enter and exit through the hole.

   The light beam in this 
Problem starts at the point (0.0,10.1) just outside
   the white cell, and the beam first impacts the mirror at (1.4,-9.6).

   Each time the laser beam hits the surface of the ellipse, it follows the
   usual law of reflection "angle of incidence equals angle of reflection."
   That is, both the incident and reflected beams make the same angle with
   the normal line at the point of incidence.

   In the figure on the left, the red line shows the first two points of
   contact between the laser beam and the wall of the white cell; the blue
   line shows the line tangent to the ellipse at the point of incidence of
   the first bounce.

   The slope m of the tangent line at any point (x,y) of the given ellipse
   is: m = −4x/y

   The normal line is perpendicular to this tangent line at the point of
   incidence.

   The animation on the right shows the first 10 reflections of the beam.

   How many times does the beam hit the internal surface of the white cell
   before exiting?
p_144_1.gif
   p_144_2.gif
"""


@pytest.mark.skip(reason='too slow')
def test_problem_146(answer):
    output = p146.problem146()
    expected_output = answer['Problem 146']
    assert output == expected_output


"""

The smallest positive integer n for which the numbers n^2+1, n^2+3, n^2+7,
   n^2+9, n^2+13, and n^2+27 are consecutive primes is 10. The sum of all
   such integers n below one-million is 1242490.

   What is the sum of all such integers n below 150 million?
"""


def test_problem_147(answer):
    output = p147.problem147()
    expected_output = answer['Problem 147']
    assert output == expected_output


"""


In a 3x2 cross-hatched grid, a total of 37 different rectangles could be
   situated within that grid as indicated in the sketch.

   There are 5 grids smaller than 3x2, vertical and horizontal dimensions
   being important, i.e. 1x1, 2x1, 3x1, 1x2 and 2x2. If each of them is
   cross-hatched, the following number of different rectangles could be
   situated within those smaller grids:

   1x1: 1
   2x1: 4
   3x1: 8
   1x2: 4
   2x2: 18

   Adding those to the 37 of the 3x2 grid, a total of 72 different rectangles
   could be situated within 3x2 and smaller grids.

   How many different rectangles could be situated within 47x43 and smaller
   grids?
p_147.gif
"""


def test_problem_148(answer):
    output = p148.problem148()
    expected_output = answer['Problem 148']
    assert output == expected_output


"""


We can easily verify that none of the entries in the first seven rows of
   Pascal's triangle are divisible by 7:

                                       1
                                    1     1
                                 1     2     1
                              1     3     3     1
                           1     4     6     4     1
                        1     5    10    10     5     1
                     1     6    15    20    15     6     1

   However, if we check the first one hundred rows, we will find that only
   2361 of the 5050 entries are not divisible by 7.

   Find the number of entries which are not divisible by 7 in the first one
   billion (10^9) rows of Pascal's triangle.
"""


@pytest.mark.skip(reason='too slow')
def test_problem_149(answer):
    output = p149.problem149()
    expected_output = answer['Problem 149']
    assert output == expected_output


"""


Looking at the table below, it is easy to verify that the maximum possible
   sum of adjacent numbers in any direction (horizontal, vertical, diagonal
   or anti-diagonal) is 16 (= 8 + 7 + 1).

                             ┌────┬────┬────┬─────┐
                             │ −2 │ 5  │ 3  │ 2   │
                             ├────┼────┼────┼─────┤
                             │ 9  │ −6 │ 5  │ 1   │
                             ├────┼────┼────┼─────┤
                             │ 3  │ 2  │ 7  │ 3   │
                             ├────┼────┼────┼─────┤
                             │ −1 │ 8  │ −4 │   8 │
                             └────┴────┴────┴─────┘

   Now, let us repeat the search, but on a much larger scale:

   First, generate four million pseudo-random numbers using a specific form
   of what is known as a "Lagged Fibonacci Generator":

   For 1 ≤ k ≤ 55, s[k] = [100003 − 200003k + 300007k^3] (modulo 1000000) −
   500000.
   For 56 ≤ k ≤ 4000000, s[k] = [s[k−24] + s[k−55] + 1000000] (modulo
   1000000) − 500000.

   Thus, s[10] = −393027 and s[100] = 86613.

   The terms of s are then arranged in a 2000×2000 table, using the first
   2000 numbers to fill the first row (sequentially), the next 2000 numbers
   to fill the second row, and so on.

   Finally, find the greatest sum of (any number of) adjacent entries in any
   direction (horizontal, vertical, diagonal or anti-diagonal).
"""


@pytest.mark.skip(reason='too slow')
def test_problem_150(answer):
    output = p150.problem150()
    expected_output = answer['Problem 150']
    assert output == expected_output


"""


In a triangular array of positive and negative integers, we wish to find a
   sub-triangle such that the sum of the numbers it contains is the smallest
   possible.

   In the example below, it can be easily verified that the marked triangle
   satisfies this condition having a sum of −42.

   We wish to make such a triangular array with one thousand rows, so we
   generate 500500 pseudo-random numbers s[k] in the range ±2^19, using a
   type of random number generator (known as a Linear Congruential Generator)
   as follows:

   t := 0
   for k = 1 up to k = 500500:
       t := (615949*t + 797807) modulo 2^20
       s[k] := t−2^19

   Thus: s[1] = 273519, s[2] = −153582, s[3] = 450905 etc

   Our triangular array is then formed using the pseudo-random numbers thus:

                                      s[1]
                                   s[2]  s[3]
                               s[4]  s[5]  s[6] 
                            s[7]  s[8]  s[9]  s[10]
                                      ...

   Sub-triangles can start at any element of the array and extend down as far
   as we like (taking-in the two elements directly below it from the next
   row, the three elements directly below from the row after that, and so
   on).
   The "sum of a sub-triangle" is defined as the sum of all the elements it
   contains.
   Find the smallest possible sub-triangle sum.
p_150.gif
"""


def test_problem_151(answer):
    output = p151.problem151()
    expected_output = answer['Problem 151']
    assert output == expected_output


"""


A printing shop runs 16 batches (jobs) every week and each batch requires
   a sheet of special colour-proofing paper of size A5.

   Every Monday morning, the foreman opens a new envelope, containing a large
   sheet of the special paper with size A1.

   He proceeds to cut it in half, thus getting two sheets of size A2. Then he
   cuts one of them in half to get two sheets of size A3 and so on until he
   obtains the A5-size sheet needed for the first batch of the week.

   All the unused sheets are placed back in the envelope.

   At the beginning of each subsequent batch, he takes from the envelope one
   sheet of paper at random. If it is of size A5, he uses it. If it is
   larger, he repeats the 'cut-in-half' procedure until he has what he needs
   and any remaining sheets are always placed back in the envelope.

   Excluding the first and last batch of the week, find the expected number
   of times (during each week) that the foreman finds a single sheet of paper
   in the envelope.

   Give your answer rounded to six decimal places using the format x.xxxxxx .
p_151.gif
"""


def test_problem_152(answer):
    output = p152.problem152()
    expected_output = answer['Problem 152']
    assert output == expected_output


"""


There are several ways to write the number 1/2 as a sum of inverse squares
   using distinct integers.

   For instance, the numbers {2,3,4,5,7,12,15,20,28,35} can be used:

   In fact, only using integers between 2 and 45 inclusive, there are exactly
   three ways to do it, the remaining two being:
   {2,3,4,6,7,9,10,20,28,35,36,45} and {2,3,4,6,7,9,12,15,28,30,35,36,45}.

   How many ways are there to write the number 1/2 as a sum of inverse
   squares using distinct integers between 2 and 80 inclusive?
p_152_sum.gif
"""


def test_problem_153(answer):
    output = p153.problem153()
    expected_output = answer['Problem 153']
    assert output == expected_output


"""


As we all know the equation x^2=-1 has no solutions for real x.
   If we however introduce the imaginary number i this equation has two
   solutions: x=i and x=-i.
   If we go a step further the equation (x-3)^2=-4 has two complex solutions:
   x=3+2i and x=3-2i.
   x=3+2i and x=3-2i are called each others' complex conjugate.
   Numbers of the form a+bi are called complex numbers.
   In general a+bi and a−bi are each other's complex conjugate.

   A Gaussian Integer is a complex number a+bi such that both a and b are
   integers.
   The regular integers are also Gaussian integers (with b=0).
   To distinguish them from Gaussian integers with b ≠ 0 we call such
   integers "rational integers."
   A Gaussian integer is called a divisor of a rational integer n if the
   result is also a Gaussian integer.
   If for example we divide 5 by 1+2i we can simplify in the following
   manner:
   Multiply numerator and denominator by the complex conjugate of 1+2i: 1−2i.
   The result is .
   So 1+2i is a divisor of 5.
   Note that 1+i is not a divisor of 5 because .
   Note also that if the Gaussian Integer (a+bi) is a divisor of a rational
   integer n, then its complex conjugate (a−bi) is also a divisor of n.

   In fact, 5 has six divisors such that the real part is positive: {1, 1 +
   2i, 1 − 2i, 2 + i, 2 − i, 5}.
   The following is a table of all of the divisors for the first five
   positive rational integers:

              ┌───┬──────────────────────────────┬───────────────┐
              │ n │ Gaussian integer divisors    │ Sum s(n) of   │
              │   │ with positive real part      │ thesedivisors │
              ├───┼──────────────────────────────┼───────────────┤
              │ 1 │ 1                            │ 1             │
              ├───┼──────────────────────────────┼───────────────┤
              │ 2 │ 1, 1+i, 1-i, 2               │ 5             │
              ├───┼──────────────────────────────┼───────────────┤
              │ 3 │ 1, 3                         │ 4             │
              ├───┼──────────────────────────────┼───────────────┤
              │ 4 │ 1, 1+i, 1-i, 2, 2+2i, 2-2i,4 │ 13            │
              ├───┼──────────────────────────────┼───────────────┤
              │ 5 │ 1, 1+2i, 1-2i, 2+i, 2-i, 5   │ 12            │
              └───┴──────────────────────────────┴───────────────┘

   For divisors with positive real parts, then, we have: .

   For 1 ≤ n ≤ 10^5, ∑ s(n)=17924657155.

   What is ∑ s(n) for 1 ≤ n ≤ 10^8?
p_153_formule1.gif
   p_153_formule2.gif
   p_153_formule5.gif
   p_153_formule6.gif
"""


def test_problem_154(answer):
    output = p154.problem154()
    expected_output = answer['Problem 154']
    assert output == expected_output


"""


A triangular pyramid is constructed using spherical balls so that each
   ball rests on exactly three balls of the next lower level.

   Then, we calculate the number of paths leading from the apex to each
   position:

   A path starts at the apex and progresses downwards to any of the three
   spheres directly below the current position.

   Consequently, the number of paths to reach a certain position is the sum
   of the numbers immediately above it (depending on the position, there are
   up to three numbers above it).

   The result is Pascal's pyramid and the numbers at each level n are the
   coefficients of the trinomial expansion (x + y + z)^n.

   How many coefficients in the expansion of (x + y + z)^200000 are multiples
   of 10^12?
p_154_pyramid.gif
"""


@pytest.mark.skip(reason='too slow')
def test_problem_155(answer):
    output = p155.problem155()
    expected_output = answer['Problem 155']
    assert output == expected_output


"""


An electric circuit uses exclusively identical capacitors of the same
   value C.
   The capacitors can be connected in series or in parallel to form
   sub-units, which can then be connected in series or in parallel with other
   capacitors or other sub-units to form larger sub-units, and so on up to a
   final circuit.

   Using this simple procedure and up to n identical capacitors, we can make
   circuits having a range of different total capacitances. For example,
   using up to n=3 capacitors of 60 F each, we can obtain the following 7
   distinct total capacitance values:

   If we denote by D(n) the number of distinct total capacitance values we
   can obtain when using up to n equal-valued capacitors and the simple
   procedure described above, we have: D(1)=1, D(2)=3, D(3)=7 ...

   Find D(18).

   Reminder : When connecting capacitors C[1], C[2] etc in parallel, the
   total capacitance is C[T] = C[1] + C[2] +...,
   whereas when connecting them in series, the overall capacitance is given
   by:
p_155_capsmu.gif
   p_155_capacitors1.gif
   p_155_capsform.gif
"""


def test_problem_156(answer):
    output = p156.problem156()
    expected_output = answer['Problem 156']
    assert output == expected_output


"""


Starting from zero the natural numbers are written down in base 10 like
   this:
   0 1 2 3 4 5 6 7 8 9 10 11 12....

   Consider the digit d=1. After we write down each number n, we will update
   the number of ones that have occurred and call this number f(n,1). The
   first values for f(n,1), then, are as follows:

                                   n  f(n,1)
                                   0  0
                                   1  1
                                   2  1
                                   3  1
                                   4  1
                                   5  1
                                   6  1
                                   7  1
                                   8  1
                                   9  1
                                   10 2
                                   11 4
                                   12 5

   Note that f(n,1) never equals 3.
   So the first two solutions of the equation f(n,1)=n are n=0 and n=1. The
   next solution is n=199981.

   In the same manner the function f(n,d) gives the total number of digits d
   that have been written down after the number n has been written.
   In fact, for every digit d ≠ 0, 0 is the first solution of the equation
   f(n,d)=n.

   Let s(d) be the sum of all the solutions for which f(n,d)=n.
   You are given that s(1)=22786974071.

   Find ∑ s(d) for 1 ≤ d ≤ 9.

   Note: if, for some n, f(n,d)=n for more than one value of d this value of
   n is counted again for every value of d for which f(n,d)=n.
"""


def test_problem_157(answer):
    output = p157.problem157()
    expected_output = answer['Problem 157']
    assert output == expected_output


"""


Consider the diophantine equation ^1/[a]+^1/[b]= ^p/[10^n] with a, b, p, n
   positive integers and a ≤ b.
   For n=1 this equation has 20 solutions that are listed below:

1/1+1/1=20/10   1/1+1/2=15/10  1/1+1/5=12/10  1/1+1/10=11/10 1/2+1/2=10/10
1/2+1/5=7/10    1/2+1/10=6/10  1/3+1/6=5/10   1/3+1/15=4/10  1/4+1/4=5/10
1/4+1/20=3/10   1/5+1/5=4/10   1/5+1/10=3/10  1/6+1/30=2/10  1/10+1/10=2/10
1/11+1/110=1/10 1/12+1/60=1/10 1/14+1/35=1/10 1/15+1/30=1/10 1/20+1/20=1/10

   How many solutions has this equation for 1 ≤ n ≤ 9?
"""


def test_problem_158(answer):
    output = p158.problem158()
    expected_output = answer['Problem 158']
    assert output == expected_output


"""


Taking three different letters from the 26 letters of the alphabet,
   character strings of length three can be formed.
   Examples are 'abc', 'hat' and 'zyx'.
   When we study these three examples we see that for 'abc' two characters
   come lexicographically after its neighbour to the left.
   For 'hat' there is exactly one character that comes lexicographically
   after its neighbour to the left. For 'zyx' there are zero characters that
   come lexicographically after its neighbour to the left.
   In all there are 10400 strings of length 3 for which exactly one character
   comes lexicographically after its neighbour to the left.

   We now consider strings of n ≤ 26 different characters from the alphabet.
   For every n, p(n) is the number of strings of length n for which exactly
   one character comes lexicographically after its neighbour to the left.

   What is the maximum value of p(n)?
"""


def test_problem_159(answer):
    output = p159.problem159()
    expected_output = answer['Problem 159']
    assert output == expected_output


"""


A composite number can be factored many different ways. For instance, not
   including multiplication by one, 24 can be factored in 7 distinct ways:

   24 = 2x2x2x3
   24 = 2x3x4
   24 = 2x2x6
   24 = 4x6
   24 = 3x8
   24 = 2x12
   24 = 24

   Recall that the digital root of a number, in base 10, is found by adding
   together the digits of that number, and repeating that process until a
   number is arrived at that is less than 10. Thus the digital root of 467 is
   8.

   We shall call a Digital Root Sum (DRS) the sum of the digital roots of the
   individual factors of our number.
   The chart below demonstrates all of the DRS values for 24.

                        ┌─────────────┬────────────────┐
                        │Factorisation│Digital Root Sum│
                        ├─────────────┼────────────────┤
                        │2x2x2x3      │       9        │
                        ├─────────────┼────────────────┤
                        │2x3x4        │       9        │
                        ├─────────────┼────────────────┤
                        │2x2x6        │       10       │
                        ├─────────────┼────────────────┤
                        │4x6          │       10       │
                        ├─────────────┼────────────────┤
                        │3x8          │       11       │
                        ├─────────────┼────────────────┤
                        │2x12         │       5        │
                        ├─────────────┼────────────────┤
                        │24           │       6        │
                        └─────────────┴────────────────┘

   The maximum Digital Root Sum of 24 is 11.
   The function mdrs(n) gives the maximum Digital Root Sum of n. So
   mdrs(24)=11.
   Find ∑mdrs(n) for 1 < n < 1,000,000.
"""


def test_problem_160(answer):
    output = p160.problem160()
    expected_output = answer['Problem 160']
    assert output == expected_output


"""


For any N, let f(N) be the last five digits before the trailing zeroes in
   N!.
   For example,

   9! = 362880 so f(9)=36288
   10! = 3628800 so f(10)=36288
   20! = 2432902008176640000 so f(20)=17664

   Find f(1,000,000,000,000)
"""


def test_problem_161(answer):
    output = p161.problem161()
    expected_output = answer['Problem 161']
    assert output == expected_output


"""


A triomino is a shape consisting of three squares joined via the
   edges.There are two basic forms:

   If all possible orientations are taken into account there are six:

   Any n by m grid for which nxm is divisible by 3 can be tiled with
   triominoes.
   If we consider tilings that can be obtained by reflection or rotation from
   another tiling as different there are 41 ways a 2 by 9 grid can be tiled
   with triominoes:

   In how many ways can a 9 by 12 grid be tiled in this way by triominoes?
p_161_trio1.gif
   p_161_trio3.gif
   p_161_k9.gif
"""


def test_problem_162(answer):
    output = p162.problem162()
    expected_output = answer['Problem 162']
    assert output == expected_output


"""


In the hexadecimal number system numbers are represented using 16
   different digits:

                        0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F

   The hexadecimal number AF when written in the decimal number system equals
   10x16+15=175.

   In the 3-digit hexadecimal numbers 10A, 1A0, A10, and A01 the digits 0,1
   and A are all present.
   Like numbers written in base ten we write hexadecimal numbers without
   leading zeroes.

   How many hexadecimal numbers containing at most sixteen hexadecimal digits
   exist with all of the digits 0,1, and A present at least once?
   Give your answer as a hexadecimal number.

   (A,B,C,D,E and F in upper case, without any leading or trailing code that
   marks the number as hexadecimal and without leading zeroes , e.g. 1A3F and
   not: 1a3f and not 0x1a3f and not $1A3F and not #1A3F and not 0000001A3F)
"""


def test_problem_163(answer):
    output = p163.problem163()
    expected_output = answer['Problem 163']
    assert output == expected_output


"""


Consider an equilateral triangle in which straight lines are drawn from
   each vertex to the middle of the opposite side, such as in the size 1
   triangle in the sketch below.

   Sixteen triangles of either different shape or size or orientation or
   location can now be observed in that triangle. Using size 1 triangles as
   building blocks, larger triangles can be formed, such as the size 2
   triangle in the above sketch. One-hundred and four triangles of either
   different shape or size or orientation or location can now be observed in
   that size 2 triangle.

   It can be observed that the size 2 triangle contains 4 size 1 triangle
   building blocks. A size 3 triangle would contain 9 size 1 triangle
   building blocks and a size n triangle would thus contain n^2 size 1
   triangle building blocks.

   If we denote T(n) as the number of triangles present in a triangle of size
   n, then

   T(1) = 16
   T(2) = 104

   Find T(36).
p_163.gif
"""


def test_problem_164(answer):
    output = p164.problem164()
    expected_output = answer['Problem 164']
    assert output == expected_output


"""


How many 20 digit numbers n (without any leading zero) exist such that no
   three consecutive digits of n have a sum greater than 9?
"""


def test_problem_165(answer):
    output = p165.problem165()
    expected_output = answer['Problem 165']
    assert output == expected_output


"""


A segment is uniquely defined by its two endpoints.
   By considering two line segments in plane geometry there are three
   possibilities:
   the segments have zero points, one point, or infinitely many points in
   common.

   Moreover when two segments have exactly one point in common it might be
   the case that that common point is an endpoint of either one of the
   segments or of both. If a common point of two segments is not an endpoint
   of either of the segments it is an interior point of both segments.
   We will call a common point T of two segments L[1] and L[2] a true
   intersection point of L[1] and L[2] if T is the only common point of L[1]
   and L[2] and T is an interior point of both segments.

   Consider the three segments L[1], L[2], and L[3]:

   L[1]: (27, 44) to (12, 32)
   L[2]: (46, 53) to (17, 62)
   L[3]: (46, 70) to (22, 40)

   It can be verified that line segments L[2] and L[3] have a true
   intersection point. We note that as the one of the end points of L[3]:
   (22,40) lies on L[1] this is not considered to be a true point of
   intersection. L[1] and L[2] have no common point. So among the three line
   segments, we find one true intersection point.

   Now let us do the same for 5000 line segments. To this end, we generate
   20000 numbers using the so-called "Blum Blum Shub" pseudo-random number
   generator.

   s[0] = 290797

   s[n+1] = s[n]×s[n] (modulo 50515093)

   t[n] = s[n] (modulo 500)

   To create each line segment, we use four consecutive numbers t[n]. That
   is, the first line segment is given by:

   (t[1], t[2]) to (t[3], t[4])

   The first four numbers computed according to the above generator should
   be: 27, 144, 12 and 232. The first segment would thus be (27,144) to
   (12,232).

   How many distinct true intersection points are found among the 5000 line
   segments?
"""


@pytest.mark.skip(reason='too slow')
def test_problem_166(answer):
    output = p166.problem166()
    expected_output = answer['Problem 166']
    assert output == expected_output


"""


A 4x4 grid is filled with digits d, 0 ≤ d ≤ 9.

   It can be seen that in the grid

                                    6 3 3 0
                                    5 0 4 3
                                    0 7 1 4
                                    1 2 4 5

   the sum of each row and each column has the value 12. Moreover the sum of
   each diagonal is also 12.

   In how many ways can you fill a 4x4 grid with the digits d, 0 ≤ d ≤ 9 so
   that each row, each column, and both diagonals have the same sum?
"""


def test_problem_167(answer):
    output = p167.problem167()
    expected_output = answer['Problem 167']
    assert output == expected_output


"""


For two positive integers a and b, the Ulam sequence U(a,b) is defined by
   U(a,b)[1] = a, U(a,b)[2] = b and for k > 2,U(a,b)[k] is the smallest
   integer greater than U(a,b)[(k-1)] which can be written in exactly one way
   as the sum of two distinct previous members of U(a,b).

   For example, the sequence U(1,2) begins with
   1, 2, 3 = 1 + 2, 4 = 1 + 3, 6 = 2 + 4, 8 = 2 + 6, 11 = 3 + 8;
   5 does not belong to it because 5 = 1 + 4 = 2 + 3 has two representations
   as the sum of two previous members, likewise 7 = 1 + 6 = 3 + 4.

   Find ∑U(2,2n+1)[k] for 2 ≤ n ≤10, where k = 10^11.
"""


def test_problem_168(answer):
    output = p168.problem168()
    expected_output = answer['Problem 168']
    assert output == expected_output


"""


Consider the number 142857. We can right-rotate this number by moving the
   last digit (7) to the front of it, giving us 714285.
   It can be verified that 714285=5×142857.
   This demonstrates an unusual property of 142857: it is a divisor of its
   right-rotation.

   Find the last 5 digits of the sum of all integers n, 10 < n < 10^100, that
   have this property.
"""


def test_problem_169(answer):
    output = p169.problem169()
    expected_output = answer['Problem 169']
    assert output == expected_output


"""


Define f(0)=1 and f(n) to be the number of different ways n can be
   expressed as a sum of integer powers of 2 using each power no more than
   twice.

   For example, f(10)=5 since there are five different ways to express 10:

   1 + 1 + 8
   1 + 1 + 4 + 4
   1 + 1 + 2 + 2 + 4
   2 + 4 + 4
   2 + 8

   What is f(10^25)?
"""


def test_problem_170(answer):
    output = p170.problem170()
    expected_output = answer['Problem 170']
    assert output == expected_output


"""


Take the number 6 and multiply it by each of 1273 and 9854:

   6 × 1273 = 7638
   6 × 9854 = 59124

   By concatenating these products we get the 1 to 9 pandigital 763859124. We
   will call 763859124 the "concatenated product of 6 and (1273,9854)".
   Notice too, that the concatenation of the input numbers, 612739854, is
   also 1 to 9 pandigital.

   The same can be done for 0 to 9 pandigital numbers.

   What is the largest 0 to 9 pandigital 10-digit concatenated product of an
   integer with two or more other integers, such that the concatenation of
   the input numbers is also a 0 to 9 pandigital 10-digit number?
"""


def test_problem_171(answer):
    output = p171.problem171()
    expected_output = answer['Problem 171']
    assert output == expected_output


"""


For a positive integer n, let f(n) be the sum of the squares of the digits
   (in base 10) of n, e.g.

   f(3) = 3^2 = 9,
   f(25) = 2^2 + 5^2 = 4 + 25 = 29,
   f(442) = 4^2 + 4^2 + 2^2 = 16 + 16 + 4 = 36

   Find the last nine digits of the sum of all n, 0 < n < 10^20, such that
   f(n) is a perfect square.
"""


def test_problem_172(answer):
    output = p172.problem172()
    expected_output = answer['Problem 172']
    assert output == expected_output


"""


How many 18-digit numbers n (without leading zeros) are there such that no
   digit occurs more than three times in n?
"""


def test_problem_173(answer):
    output = p173.problem173()
    expected_output = answer['Problem 173']
    assert output == expected_output


"""


We shall define a square lamina to be a square outline with a square
   "hole" so that the shape possesses vertical and horizontal symmetry. For
   example, using exactly thirty-two square tiles we can form two different
   square laminae:

   With one-hundred tiles, and not necessarily using all of the tiles at one
   time, it is possible to form forty-one different square laminae.

   Using up to one million tiles how many different square laminae can be
   formed?
p_173_square_laminas.gif
"""


def test_problem_174(answer):
    output = p174.problem174()
    expected_output = answer['Problem 174']
    assert output == expected_output


"""


We shall define a square lamina to be a square outline with a square
   "hole" so that the shape possesses vertical and horizontal symmetry.

   Given eight tiles it is possible to form a lamina in only one way: 3x3
   square with a 1x1 hole in the middle. However, using thirty-two tiles it
   is possible to form two distinct laminae.

   If t represents the number of tiles used, we shall say that t = 8 is type
   L(1) and t = 32 is type L(2).

   Let N(n) be the number of t ≤ 1000000 such that t is type L(n); for
   example, N(15) = 832.

   What is ∑ N(n) for 1 ≤ n ≤ 10?
p_173_square_laminas.gif
"""


def test_problem_175(answer):
    output = p175.problem175()
    expected_output = answer['Problem 175']
    assert output == expected_output


"""



   Define f(0)=1 and f(n) to be the number of ways to write n as a sum of
   powers of 2 where no power occurs more than twice.

   For example, f(10)=5 since there are five different ways to express 10:
   10 = 8+2 = 8+1+1 = 4+4+2 = 4+2+2+1+1 = 4+4+1+1

   It can be shown that for every fraction p/q (p>0, q>0) there exists at
   least one integer n such that
   f(n)/f(n-1)=p/q.

   For instance, the smallest n for which f(n)/f(n-1)=13/17 is 241.
   The binary expansion of 241 is 11110001.
   Reading this binary number from the most significant bit to the least
   significant bit there are 4 one's, 3 zeroes and 1 one. We shall call the
   string 4,3,1 the Shortened Binary Expansion of 241.

   Find the Shortened Binary Expansion of the smallest n for which
   f(n)/f(n-1)=123456789/987654321.

   Give your answer as comma separated integers, without any whitespaces.
"""


def test_problem_176(answer):
    output = p176.problem176()
    expected_output = answer['Problem 176']
    assert output == expected_output


"""


The four right-angled triangles with sides (9,12,15), (12,16,20),
   (5,12,13) and (12,35,37) all have one of the shorter sides (catheti) equal
   to 12. It can be shown that no other integer sided right-angled triangle
   exists with one of the catheti equal to 12.

   Find the smallest integer that can be the length of a cathetus of exactly
   47547 different integer sided right-angled triangles.
"""


def test_problem_177(answer):
    output = p177.problem177()
    expected_output = answer['Problem 177']
    assert output == expected_output


"""


Let ABCD be a convex quadrilateral, with diagonals AC and BD. At each
   vertex the diagonal makes an angle with each of the two sides, creating
   eight corner angles.

   For example, at vertex A, the two angles are CAD, CAB.

   We call such a quadrilateral for which all eight corner angles have
   integer values when measured in degrees an "integer angled quadrilateral".
   An example of an integer angled quadrilateral is a square, where all eight
   corner angles are 45°. Another example is given by DAC = 20°, BAC = 60°,
   ABD = 50°, CBD = 30°, BCA = 40°, DCA = 30°, CDB = 80°, ADB = 50°.

   What is the total number of non-similar integer angled quadrilaterals?

   Note: In your calculations you may assume that a calculated angle is
   integral if it is within a tolerance of 10^-9 of an integer value.
p_177_quad.gif
"""


def test_problem_178(answer):
    output = p178.problem178()
    expected_output = answer['Problem 178']
    assert output == expected_output


"""



   Consider the number 45656.
   It can be seen that each pair of consecutive digits of 45656 has a
   difference of one.
   A number for which every pair of consecutive digits has a difference of
   one is called a step number.
   A pandigital number contains every decimal digit from 0 to 9 at least
   once.
   How many pandigital step numbers less than 10^40 are there?
"""


@pytest.mark.skip(reason='too slow')
def test_problem_179(answer):
    output = p179.problem179()
    expected_output = answer['Problem 179']
    assert output == expected_output


"""


Find the number of integers 1 < n < 10^7, for which n and n + 1 have the
   same number of positive divisors. For example, 14 has the positive
   divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
"""


def test_problem_180(answer):
    output = p180.problem180()
    expected_output = answer['Problem 180']
    assert output == expected_output


"""


For any integer n, consider the three functions

   f[1,n](x,y,z) = x^n+1 + y^n+1 − z^n+1
   f[2,n](x,y,z) = (xy + yz + zx)*(x^n-1 + y^n-1 − z^n-1)
   f[3,n](x,y,z) = xyz*(x^n-2 + y^n-2 − z^n-2)

   and their combination

   f[n](x,y,z) = f[1,n](x,y,z) + f[2,n](x,y,z) − f[3,n](x,y,z)

   We call (x,y,z) a golden triple of order k if x, y, and z are all rational
   numbers of the form a / b with
   0 < a < b ≤ k and there is (at least) one integer n, so that f[n](x,y,z) =
   0.

   Let s(x,y,z) = x + y + z.
   Let t = u / v be the sum of all distinct s(x,y,z) for all golden triples
   (x,y,z) of order 35.
   All the s(x,y,z) and t must be in reduced form.

   Find u + v.
"""


def test_problem_181(answer):
    output = p181.problem181()
    expected_output = answer['Problem 181']
    assert output == expected_output


"""


Having three black objects B and one white object W they can be grouped in
   7 ways like this:

        (BBBW)  (B,BBW)  (B,B,BW)  (B,B,B,W)  (B,BB,W)  (BBB,W)  (BB,BW)

   In how many ways can sixty black objects B and forty white objects W be
   thus grouped?
"""


@pytest.mark.skip(reason='too slow')
def test_problem_182(answer):
    output = p182.problem182()
    expected_output = answer['Problem 182']
    assert output == expected_output


"""


The RSA encryption is based on the following procedure:

   Generate two distinct primes p and q.
   Compute n=pq and φ=(p-1)(q-1).
   Find an integer e, 1<e<φ, such that gcd(e,φ)=1.

   A message in this system is a number in the interval [0,n-1].
   A text to be encrypted is then somehow converted to messages (numbers in
   the interval [0,n-1]).
   To encrypt the text, for each message, m, c=m^e mod n is calculated.

   To decrypt the text, the following procedure is needed: calculate d such
   that ed=1 mod φ, then for each encrypted message, c, calculate m=c^d mod
   n.

   There exist values of e and m such that m^e mod n=m.
   We call messages m for which m^e mod n=m unconcealed messages.

   An issue when choosing e is that there should not be too many unconcealed
   messages.
   For instance, let p=19 and q=37.
   Then n=19*37=703 and φ=18*36=648.
   If we choose e=181, then, although gcd(181,648)=1 it turns out that all
   possible messages
   m (0≤m≤n-1) are unconcealed when calculating m^e mod n.
   For any valid choice of e there exist some unconcealed messages.
   It's important that the number of unconcealed messages is at a minimum.

   Choose p=1009 and q=3643.
   Find the sum of all values of e, 1<e<φ(1009,3643) and gcd(e,φ)=1, so that
   the number of unconcealed messages for this value of e is at a minimum.
"""


def test_problem_183(answer):
    output = p183.problem183()
    expected_output = answer['Problem 183']
    assert output == expected_output


"""


Let N be a positive integer and let N be split into k equal parts, r =
   N/k, so that N = r + r + ... + r.
   Let P be the product of these parts, P = r × r × ... × r = r^k.

   For example, if 11 is split into five equal parts, 11 = 2.2 + 2.2 + 2.2 +
   2.2 + 2.2, then P = 2.2^5 = 51.53632.

   Let M(N) = P[max] for a given value of N.

   It turns out that the maximum for N = 11 is found by splitting eleven into
   four equal parts which leads to P[max] = (11/4)^4; that is, M(11) =
   14641/256 = 57.19140625, which is a terminating decimal.

   However, for N = 8 the maximum is achieved by splitting it into three
   equal parts, so M(8) = 512/27, which is a non-terminating decimal.

   Let D(N) = N if M(N) is a non-terminating decimal and D(N) = -N if M(N) is
   a terminating decimal.

   For example, ΣD(N) for 5 ≤ N ≤ 100 is 2438.

   Find ΣD(N) for 5 ≤ N ≤ 10000.
"""


def test_problem_184(answer):
    output = p184.problem184()
    expected_output = answer['Problem 184']
    assert output == expected_output


"""


Consider the set I[r] of points (x,y) with integer co-ordinates in the
   interior of the circle with radius r, centered at the origin, i.e. x^2 +
   y^2 < r^2.

   For a radius of 2, I[2] contains the nine points (0,0), (1,0), (1,1),
   (0,1), (-1,1), (-1,0), (-1,-1), (0,-1) and (1,-1). There are eight
   triangles having all three vertices in I[2] which contain the origin in
   the interior. Two of them are shown below, the others are obtained from
   these by rotation.

   For a radius of 3, there are 360 triangles containing the origin in the
   interior and having all vertices in I[3] and for I[5] the number is 10600.

   How many triangles are there containing the origin in the interior and
   having all three vertices in I[105]?
p_184.gif
"""


def test_problem_185(answer):
    output = p185.problem185()
    expected_output = answer['Problem 185']
    assert output == expected_output


"""


The game Number Mind is a variant of the well known game Master Mind.

   Instead of coloured pegs, you have to guess a secret sequence of digits.
   After each guess you're only told in how many places you've guessed the
   correct digit. So, if the sequence was 1234 and you guessed 2036, you'd be
   told that you have one correct digit; however, you would NOT be told that
   you also have another digit in the wrong place.

   For instance, given the following guesses for a 5-digit secret sequence,

   90342 ;2 correct
   70794 ;0 correct
   39458 ;2 correct
   34109 ;1 correct
   51545 ;2 correct
   12531 ;1 correct

   The correct sequence 39542 is unique.

   Based on the following guesses,

   5616185650518293 ;2 correct
   3847439647293047 ;1 correct
   5855462940810587 ;3 correct
   9742855507068353 ;3 correct
   4296849643607543 ;3 correct
   3174248439465858 ;1 correct
   4513559094146117 ;2 correct
   7890971548908067 ;3 correct
   8157356344118483 ;1 correct
   2615250744386899 ;2 correct
   8690095851526254 ;3 correct
   6375711915077050 ;1 correct
   6913859173121360 ;1 correct
   6442889055042768 ;2 correct
   2321386104303845 ;0 correct
   2326509471271448 ;2 correct
   5251583379644322 ;2 correct
   1748270476758276 ;3 correct
   4895722652190306 ;1 correct
   3041631117224635 ;3 correct
   1841236454324589 ;3 correct
   2659862637316867 ;2 correct

   Find the unique 16-digit secret sequence.
"""


@pytest.mark.skip(reason='too slow')
def test_problem_186(answer):
    output = p186.problem186()
    expected_output = answer['Problem 186']
    assert output == expected_output


"""


Here are the records from a busy telephone system with one million users:

                    ┌─────────────────┬─────────┬─────────┐
                    │RecNr            │ Caller  │ Called  │
                    ├─────────────────┼─────────┼─────────┤
                    │        1        │ 200007  │ 100053  │
                    ├─────────────────┼─────────┼─────────┤
                    │        2        │ 600183  │ 500439  │
                    ├─────────────────┼─────────┼─────────┤
                    │        3        │ 600863  │ 701497  │
                    ├─────────────────┼─────────┼─────────┤
                    │       ...       │   ...   │   ...   │
                    └─────────────────┴─────────┴─────────┘

   The telephone number of the caller and the called number in record n are
   Caller(n) = S[2n-1] and Called(n) = S[2n] where S[1,2,3,...] come from the
   "Lagged Fibonacci Generator":

   For 1 ≤ k ≤ 55, S[k] = [100003 - 200003k + 300007k^3] (modulo 1000000)
   For 56 ≤ k, S[k] = [S[k-24] + S[k-55]] (modulo 1000000)

   If Caller(n) = Called(n) then the user is assumed to have misdialled and
   the call fails; otherwise the call is successful.

   From the start of the records, we say that any pair of users X and Y are
   friends if X calls Y or vice-versa. Similarly, X is a friend of a friend
   of Z if X is a friend of Y and Y is a friend of Z; and so on for longer
   chains.

   The Prime Minister's phone number is 524287. After how many successful
   calls, not counting misdials, will 99% of the users (including the PM) be
   a friend, or a friend of a friend etc., of the Prime Minister?
"""


@pytest.mark.skip(reason='too slow')
def test_problem_187(answer):
    output = p187.problem187()
    expected_output = answer['Problem 187']
    assert output == expected_output


"""


A composite is a number containing at least two prime factors. For
   example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

   There are ten composites below thirty containing precisely two, not
   necessarily distinct, prime factors:4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

   How many composite integers, n < 10^8, have precisely two, not necessarily
   distinct, prime factors?
"""


def test_problem_188(answer):
    output = p188.problem188()
    expected_output = answer['Problem 188']
    assert output == expected_output


"""


The hyperexponentiation or tetration of a number a by a positive integer
   b, denoted by a↑↑b or ^ba, is recursively defined by:

   a↑↑1 = a,
   a↑↑(k+1) = a^(a↑↑k).

   Thus we have e.g. 3↑↑2 = 3^3 = 27, hence 3↑↑3 = 3^27 = 7625597484987 and
   3↑↑4 is roughly 10^3.6383346400240996*10^12.

   Find the last 8 digits of 1777↑↑1855.
"""


def test_problem_189(answer):
    output = p189.problem189()
    expected_output = answer['Problem 189']
    assert output == expected_output


"""


Consider the following configuration of 64 triangles:

   We wish to colour the interior of each triangle with one of three colours:
   red, green or blue, so that no two neighbouring triangles have the same
   colour. Such a colouring shall be called valid. Here, two triangles are
   said to be neighbouring if they share an edge.
   Note: if they only share a vertex, then they are not neighbours.

   For example, here is a valid colouring of the above grid:

   A colouring C' which is obtained from a colouring C by rotation or
   reflection is considered distinct from C unless the two are identical.

   How many distinct valid colourings are there for the above configuration?
p_189_grid.gif
   p_189_colours.gif
"""


def test_problem_190(answer):
    output = p190.problem190()
    expected_output = answer['Problem 190']
    assert output == expected_output


"""


Let S[m] = (x[1], x[2], ... , x[m]) be the m-tuple of positive real
   numbers with x[1] + x[2] + ... + x[m] = m for which P[m] = x[1] * x[2]^2 *
   ... * x[m]^m is maximised.

   For example, it can be verified that [P[10]] = 4112 ([ ] is the integer
   part function).

   Find Σ[P[m]] for 2 ≤ m ≤ 15.
"""


def test_problem_191(answer):
    output = p191.problem191()
    expected_output = answer['Problem 191']
    assert output == expected_output


"""


A particular school offers cash rewards to children with good attendance
   and punctuality. If they are absent for three consecutive days or late on
   more than one occasion then they forfeit their prize.

   During an n-day period a trinary string is formed for each child
   consisting of L's (late), O's (on time), and A's (absent).

   Although there are eighty-one trinary strings for a 4-day period that can
   be formed, exactly forty-three strings would lead to a prize:

   OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
   OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
   AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
   AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
   LAOO LAOA LAAO

   How many "prize" strings exist over a 30-day period?
"""


def test_problem_192(answer):
    output = p192.problem192()
    expected_output = answer['Problem 192']
    assert output == expected_output


"""


Let x be a real number.
   A best approximation to x for the denominator bound d is a rational number
   r/s in reduced form, with s ≤ d, such that any rational number which is
   closer to x than r/s has a denominator larger than d:

                           |p/q-x| < |r/s-x| ⇒ q > d

   For example, the best approximation to √13 for the denominator bound 20 is
   18/5 and the best approximation to √13 for the denominator bound 30 is
   101/28.

   Find the sum of all denominators of the best approximations to √n for the
   denominator bound 10^12, where n is not a perfect square and 1 < n ≤
   100000.
"""


def test_problem_193(answer):
    output = p193.problem193()
    expected_output = answer['Problem 193']
    assert output == expected_output


"""


A positive integer n is called squarefree, if no square of a prime divides
   n, thus 1, 2, 3, 5, 6, 7, 10, 11 are squarefree, but not 4, 8, 9, 12.

   How many squarefree numbers are there below 2^50?
"""


def test_problem_194(answer):
    output = p194.problem194()
    expected_output = answer['Problem 194']
    assert output == expected_output


"""


Consider graphs built with the units A: and B: , where the units are glued
   alongthe vertical edges as in the graph .

   A configuration of type (a,b,c) is a graph thus built of a units A and b
   units B, where the graph's vertices are coloured using up to c colours, so
   that no two adjacent vertices have the same colour.
   The compound graph above is an example of a configuration of type (2,2,6),
   in fact of type (2,2,c) for all c ≥ 4.

   Let N(a,b,c) be the number of configurations of type (a,b,c).
   For example, N(1,0,3) = 24, N(0,2,4) = 92928 and N(2,2,3) = 20736.

   Find the last 8 digits of N(25,75,1984).
p_194_GraphA.png
   p_194_GraphB.png
   p_194_Fig.png
"""


def test_problem_195(answer):
    output = p195.problem195()
    expected_output = answer['Problem 195']
    assert output == expected_output


"""


Let's call an integer sided triangle with exactly one angle of 60 degrees
   a 60-degree triangle.
   Let r be the radius of the inscribed circle of such a 60-degree triangle.

   There are 1234 60-degree triangles for which r ≤ 100.
   Let T(n) be the number of 60-degree triangles for which r ≤ n, so
   T(100) = 1234,  T(1000) = 22767, and  T(10000) = 359912.

   Find T(1053779).
"""


def test_problem_196(answer):
    output = p196.problem196()
    expected_output = answer['Problem 196']
    assert output == expected_output


"""


Build a triangle from all positive integers in the following way:

    1
    2  3
    4  5  6
    7  8  9 10
   11 12 13 14 15
   16 17 18 19 20 21
   22 23 24 25 26 27 28
   29 30 31 32 33 34 35 36
   37 38 39 40 41 42 43 44 45
   46 47 48 49 50 51 52 53 54 55
   56 57 58 59 60 61 62 63 64 65 66
   . . .

   Each positive integer has up to eight neighbours in the triangle.

   A set of three primes is called a prime triplet if one of the three primes
   has the other two as neighbours in the triangle.

   For example, in the second row, the prime numbers 2 and 3 are elements of
   some prime triplet.

   If row 8 is considered, it contains two primes which are elements of some
   prime triplet, i.e. 29 and 31.
   If row 9 is considered, it contains only one prime which is an element of
   some prime triplet: 37.

   Define S(n) as the sum of the primes in row n which are elements of any
   prime triplet.
   Then S(8)=60 and S(9)=37.

   You are given that S(10000)=950007619.

   Find  S(5678027) + S(7208785).
"""


def test_problem_197(answer):
    output = p197.problem197()
    expected_output = answer['Problem 197']
    assert output == expected_output


"""


Given is the function f(x) = ⌊2^30.403243784-x^2⌋ × 10^-9 ( ⌊ ⌋ is the
   floor-function),
   the sequence u[n] is defined by u[0] = -1 and u[n+1] = f(u[n]).

   Find u[n] + u[n+1] for n = 10^12.
   Give your answer with 9 digits after the decimal point.
"""


def test_problem_198(answer):
    output = p198.problem198()
    expected_output = answer['Problem 198']
    assert output == expected_output


"""


A best approximation to a real number x for the denominator bound d is a
   rational number r/s (in reduced form) with s ≤ d, so that any rational
   number p/q which is closer to x than r/s has q > d.

   Usually the best approximation to a real number is uniquely determined for
   all denominator bounds. However, there are some exceptions, e.g. 9/40 has
   the two best approximations 1/4 and 1/5 for the denominator bound 6.We
   shall call a real number x ambiguous, if there is at least one denominator
   bound for which x possesses two best approximations. Clearly, an ambiguous
   number is necessarily rational.

   How many ambiguous numbers x = p/q,0 < x < 1/100, are there whose
   denominator q does not exceed 10^8?
"""


def test_problem_199(answer):
    output = p199.problem199()
    expected_output = answer['Problem 199']
    assert output == expected_output


"""


Three circles of equal radius are placed inside a larger circle such that
   each pair of circles is tangent to one another and the inner circles do
   not overlap. There are four uncovered "gaps" which are to be filled
   iteratively with more tangent circles.

   At each iteration, a maximally sized circle is placed in each gap, which
   creates more gaps for the next iteration. After 3 iterations (pictured),
   there are 108 gaps and the fraction of the area which is not covered by
   circles is 0.06790342, rounded to eight decimal places.

   What fraction of the area is not covered by circles after 10 iterations?
   Give your answer rounded to eight decimal places using the format
   x.xxxxxxxx .
p_199_circles_in_circles.gif
"""


def test_problem_200(answer):
    output = p200.problem200()
    expected_output = answer['Problem 200']
    assert output == expected_output


"""


We shall define a sqube to be a number of the form, p^2q^3, where p and q
   are distinct primes.
   For example, 200 = 5^22^3 or 120072949 = 23^261^3.

   The first five squbes are 72, 108, 200, 392, and 500.

   Interestingly, 200 is also the first number for which you cannot change
   any single digit to make a prime; we shall call such numbers, prime-proof.
   The next prime-proof sqube which contains the contiguous sub-string "200"
   is 1992008.

   Find the 200th prime-proof sqube containing the contiguous sub-string
   "200".
"""


def test_problem_201(answer):
    output = p201.problem201()
    expected_output = answer['Problem 201']
    assert output == expected_output


"""


For any set A of numbers, let sum(A) be the sum of the elements of A.
   Consider the set B = {1,3,6,8,10,11}.
   There are 20 subsets of B containing three elements, and their sums are:

   sum({1,3,6}) = 10,
   sum({1,3,8}) = 12,
   sum({1,3,10}) = 14,
   sum({1,3,11}) = 15,
   sum({1,6,8}) = 15,
   sum({1,6,10}) = 17,
   sum({1,6,11}) = 18,
   sum({1,8,10}) = 19,
   sum({1,8,11}) = 20,
   sum({1,10,11}) = 22,
   sum({3,6,8}) = 17,
   sum({3,6,10}) = 19,
   sum({3,6,11}) = 20,
   sum({3,8,10}) = 21,
   sum({3,8,11}) = 22,
   sum({3,10,11}) = 24,
   sum({6,8,10}) = 24,
   sum({6,8,11}) = 25,
   sum({6,10,11}) = 27,
   sum({8,10,11}) = 29.

   Some of these sums occur more than once, others are unique.
   For a set A, let U(A,k) be the set of unique sums of k-element subsets of
   A, in our example we find U(B,3) = {10,12,14,18,21,25,27,29} and
   sum(U(B,3)) = 156.

   Now consider the 100-element set S = {1^2, 2^2, ... , 100^2}.
   S has 100891344545564193334812497256 50-element subsets.

   Determine the sum of all integers which are the sum of exactly one of the
   50-element subsets of S, i.e. find sum(U(S,50)).
"""


def test_problem_202(answer):
    output = p202.problem202()
    expected_output = answer['Problem 202']
    assert output == expected_output


"""


Three mirrors are arranged in the shape of an equilateral triangle, with
   their reflective surfaces pointing inwards. There is an infinitesimal gap
   at each vertex of the triangle through which a laser beam may pass.

   Label the vertices A, B and C. There are 2 ways in which a laser beam may
   enter vertex C, bounce off 11 surfaces, then exit through the same vertex:
   one way is shown below; the other is the reverse of that.

   There are 80840 ways in which a laser beam may enter vertex C, bounce off
   1000001 surfaces, then exit through the same vertex.

   In how many ways can a laser beam enter at vertex C, bounce off
   12017639147 surfaces, then exit through the same vertex?
p_201_laserbeam.gif
"""


def test_problem_203(answer):
    output = p203.problem203()
    expected_output = answer['Problem 203']
    assert output == expected_output


"""


The binomial coefficients ^nC[k] can be arranged in triangular form,
   Pascal's triangle, like this:

                                       1
                                    1     1
                                 1     2     1
                              1     3     3     1
                            1    4     6     4     1
                          1   5     10    10    5    1
                        1   6    15    20    15    6   1
                      1   7   21    35    35    21   7   1

                                   .........

   It can be seen that the first eight rows of Pascal's triangle contain
   twelve distinct numbers: 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.

   A positive integer n is called squarefree if no square of a prime divides
   n.Of the twelve distinct numbers in the first eight rows of Pascal's
   triangle, all except 4 and 20 are squarefree.The sum of the distinct
   squarefree numbers in the first eight rows is 105.

   Find the sum of the distinct squarefree numbers in the first 51 rows of
   Pascal's triangle.
"""


@pytest.mark.skip(reason='too slow')
def test_problem_204(answer):
    output = p204.problem204()
    expected_output = answer['Problem 204']
    assert output == expected_output


"""


A Hamming number is a positive number which has no prime factor larger
   than 5.
   So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
   There are 1105 Hamming numbers not exceeding 10^8.

   We will call a positive number a generalised Hamming number of type n, if
   it has no prime factor larger than n.
   Hence the Hamming numbers are the generalised Hamming numbers of type 5.

   How many generalised Hamming numbers of type 100 are there which don't
   exceed 10^9?
"""


def test_problem_207(answer):
    output = p207.problem207()
    expected_output = answer['Problem 207']
    assert output == expected_output


"""


For some positive integers k, there exists an integer partition of the
   form   4^t = 2^t + k,
   where 4^t, 2^t, and k are all positive integers and t is a real number.

   The first two such partitions are 4^1 = 2^1 + 2 and 4^1.5849625... =
   2^1.5849625... + 6.

   Partitions where t is also an integer are called perfect.
   For any m ≥ 1 let P(m) be the proportion of such partitions that are
   perfect with k ≤ m.
   Thus P(6) = 1/2.

   In the following table are listed some values of P(m)

      P(5) = 1/1
      P(10) = 1/2
      P(15) = 2/3
      P(20) = 1/2
      P(25) = 1/2
      P(30) = 2/5
      ...
      P(180) = 1/4
      P(185) = 3/13

   Find the smallest m for which P(m) < 1/12345
"""


@pytest.mark.skip(reason='too slow')
def test_problem_208(answer):
    output = p208.problem208()
    expected_output = answer['Problem 208']
    assert output == expected_output


"""


A robot moves in a series of one-fifth circular arcs (72°), with a free
   choice of a clockwise or an anticlockwise arc for each step, but no
   turning on the spot.

   One of 70932 possible closed paths of 25 arcs starting northward is

   Given that the robot starts facing North, how many journeys of 70 arcs in
   length can it take that return it, after the final arc, to its starting
   position?
   (Any arc may be traversed multiple times.)
p_208_robotwalk.gif
"""


def test_problem_209(answer):
    output = p209.problem209()
    expected_output = answer['Problem 209']
    assert output == expected_output


"""


A k-input binary truth table is a map from k input bits(binary digits, 0
   [false] or 1 [true]) to 1 output bit. For example, the 2-input binary
   truth tables for the logical AND and XOR functions are:

   ┌────┬────┬─────────┐
   │ x  │ y  │x AND y  │
   ├────┼────┼─────────┤
   │ 0  │ 0  │    0    │
   ├────┼────┼─────────┤
   │ 0  │ 1  │    0    │
   ├────┼────┼─────────┤
   │ 1  │ 0  │    0    │
   ├────┼────┼─────────┤
   │ 1  │ 1  │    1    │
   └────┴────┴─────────┘

                                                        ┌────┬────┬─────────┐
                                                        │ x  │ y  │x XOR y  │
                                                        ├────┼────┼─────────┤
                                                        │ 0  │ 0  │    0    │
                                                        ├────┼────┼─────────┤
                                                        │ 0  │ 1  │    1    │
                                                        ├────┼────┼─────────┤
                                                        │ 1  │ 0  │    1    │
                                                        ├────┼────┼─────────┤
                                                        │ 1  │ 1  │    0    │
                                                        └────┴────┴─────────┘

   How many 6-input binary truth tables, τ, satisfy the formula

         τ(a, b, c, d, e, f) AND τ(b, c, d, e, f, a XOR (b AND c)) = 0
"""


def test_problem_210(answer):
    output = p210.problem210()
    expected_output = answer['Problem 210']
    assert output == expected_output


"""



   Consider the set S(r) of points (x,y) with integer coordinates satisfying
   |x| + |y| ≤ r.
   Let O be the point (0,0) and C the point (r/4,r/4).
   Let N(r) be the number of points B in S(r), so that the triangle OBC has
   an obtuse angle, i.e. the largest angle α satisfies 90°<α<180°.
   So, for example, N(4)=24 and N(8)=100.

   What is N(1,000,000,000)?
"""


@pytest.mark.skip(reason='too slow')
def test_problem_211(answer):
    output = p211.problem211()
    expected_output = answer['Problem 211']
    assert output == expected_output


"""


For a positive integer n, let σ[2](n) be the sum of the squares of its
   divisors. For example,

                       σ[2](10) = 1 + 4 + 25 + 100 = 130.

   Find the sum of all n, 0 < n < 64,000,000 such that σ[2](n) is a perfect
   square.
"""


def test_problem_212(answer):
    output = p212.problem212()
    expected_output = answer['Problem 212']
    assert output == expected_output


"""


An axis-aligned cuboid, specified by parameters { (x[0],y[0],z[0]),
   (dx,dy,dz) }, consists of all points (X,Y,Z) such that x[0] ≤ X ≤ x[0]+dx,
   y[0] ≤ Y ≤ y[0]+dy and z[0] ≤ Z ≤ z[0]+dz. The volume of the cuboid is the
   product, dx × dy × dz. The combined volume of a collection of cuboids is
   the volume of their union and will be less than the sum of the individual
   volumes if any cuboids overlap.

   Let C[1],...,C[50000] be a collection of 50000 axis-aligned cuboids such
   that C[n] has parameters

   x[0] = S[6n-5] modulo 10000
   y[0] = S[6n-4] modulo 10000
   z[0] = S[6n-3] modulo 10000
   dx = 1 + (S[6n-2] modulo 399)
   dy = 1 + (S[6n-1] modulo 399)
   dz = 1 + (S[6n] modulo 399)

   where S[1],...,S[300000] come from the "Lagged Fibonacci Generator":

   For 1 ≤ k ≤ 55, S[k] = [100003 - 200003k + 300007k^3]   (modulo 1000000)
   For 56 ≤ k, S[k] = [S[k-24] + S[k-55]]   (modulo 1000000)

   Thus, C[1] has parameters {(7,53,183),(94,369,56)}, C[2] has parameters
   {(2383,3563,5079),(42,212,344)}, and so on.

   The combined volume of the first 100 cuboids, C[1],...,C[100], is
   723581599.

   What is the combined volume of all 50000 cuboids, C[1],...,C[50000] ?
"""


def test_problem_213(answer):
    output = p213.problem213()
    expected_output = answer['Problem 213']
    assert output == expected_output


"""


A 30×30 grid of squares contains 900 fleas, initially one flea per square.
   When a bell is rung, each flea jumps to an adjacent square at random
   (usually 4 possibilities, except for fleas on the edge of the grid or at
   the corners).

   What is the expected number of unoccupied squares after 50 rings of the
   bell? Give your answer rounded to six decimal places.
"""


@pytest.mark.skip(reason='too slow')
def test_problem_214(answer):
    output = p214.problem214()
    expected_output = answer['Problem 214']
    assert output == expected_output


"""


Let φ be Euler's totient function, i.e. for a natural number n,φ(n) is the
   number of k, 1 ≤ k ≤ n, for which gcd(k,n) = 1.

   By iterating φ, each positive integer generates a decreasing chain of
   numbers ending in 1.
   E.g. if we start with 5 the sequence 5,4,2,1 is generated.
   Here is a listing of all chains with length 4:

                                                                      5,4,2,1
                                                                      7,6,2,1
                                                                      8,4,2,1
                                                                      9,6,2,1
                                                                     10,4,2,1
                                                                     12,4,2,1
                                                                     14,6,2,1
                                                                     18,6,2,1

   Only two of these chains start with a prime, their sum is 12.

   What is the sum of all primes less than 40000000 which generate a chain of
   length 25?
"""


def test_problem_215(answer):
    output = p215.problem215()
    expected_output = answer['Problem 215']
    assert output == expected_output


"""


Consider the 
Problem of building a wall out of 2×1 and 3×1 bricks
   (horizontal×vertical dimensions) such that, for extra strength, the gaps
   between horizontally-adjacent bricks never line up in consecutive layers,
   i.e. never form a "running crack".

   For example, the following 9×3 wall is not acceptable due to the running
   crack shown in red:

   There are eight ways of forming a crack-free 9×3 wall, written W(9,3) = 8.

   Calculate W(32,10).
p_215_crackfree.gif
"""


@pytest.mark.skip(reason='too slow')
def test_problem_216(answer):
    output = p216.problem216()
    expected_output = answer['Problem 216']
    assert output == expected_output


"""


Consider numbers t(n) of the form t(n) = 2n^2-1 with n > 1.
   The first such numbers are 7, 17, 31, 49, 71, 97, 127 and 161.
   It turns out that only 49 = 7*7 and 161 = 7*23 are not prime.
   For n ≤ 10000 there are 2202 numbers t(n) that are prime.

   How many numbers t(n) are prime for n ≤ 50,000,000 ?
"""


def test_problem_217(answer):
    output = p217.problem217()
    expected_output = answer['Problem 217']
    assert output == expected_output


"""


A positive integer with k (decimal) digits is called balanced if its first
   ⌈^k/[2]⌉ digits sum to the same value as its last ⌈^k/[2]⌉ digits, where
   ⌈x⌉, pronounced ceiling of x, is the smallest integer ≥ x, thus ⌈π⌉ = 4
   and ⌈5⌉ = 5.

   So, for example, all palindromes are balanced, as is 13722.

   Let T(n) be the sum of all balanced numbers less than 10^n.
   Thus: T(1) = 45, T(2) = 540 and T(5) = 334795890.

   Find T(47) mod 3^15
"""


def test_problem_218(answer):
    output = p218.problem218()
    expected_output = answer['Problem 218']
    assert output == expected_output


"""


Consider the right angled triangle with sides a=7, b=24 and c=25.The area
   of this triangle is 84, which is divisible by the perfect numbers 6 and
   28.
   Moreover it is a primitive right angled triangle as gcd(a,b)=1 and
   gcd(b,c)=1.
   Also c is a perfect square.

   We will call a right angled triangle perfect if
   -it is a primitive right angled triangle
   -its hypotenuse is a perfect square

   We will call a right angled triangle super-perfect if
   -it is a perfect right angled triangle and
   -its area is a multiple of the perfect numbers 6 and 28.

   How many perfect right-angled triangles with c≤10^16 exist that are not
   super-perfect?
"""


def test_problem_219(answer):
    output = p219.problem219()
    expected_output = answer['Problem 219']
    assert output == expected_output


"""


Let A and B be bit strings (sequences of 0's and 1's).
   If A is equal to the leftmost length(A) bits of B, then A is said to be a
   prefix of B.
   For example, 00110 is a prefix of 001101001, but not of 00111 or 100110.

   A prefix-free code of size n is a collection of n distinct bit strings
   such that no string is a prefix of any other. For example, this is a
   prefix-free code of size 6:

                          0000, 0001, 001, 01, 10, 11

   Now suppose that it costs one penny to transmit a '0' bit, but four pence
   to transmit a '1'.
   Then the total cost of the prefix-free code shown above is 35 pence, which
   happens to be the cheapest possible for the skewed pricing scheme in
   question.
   In short, we write Cost(6) = 35.

   What is Cost(10^9) ?
"""


def test_problem_220(answer):
    output = p220.problem220()
    expected_output = answer['Problem 220']
    assert output == expected_output


"""


Let D[0] be the two-letter string "Fa". For n≥1, derive D[n] from D[n-1]
   by the string-rewriting rules:

   "a" → "aRbFR"
   "b" → "LFaLb"

   Thus, D[0] = "Fa", D[1] = "FaRbFR", D[2] = "FaRbFRRLFaLbFR", and so on.

   These strings can be interpreted as instructions to a computer graphics
   program, with "F" meaning "draw forward one unit", "L" meaning "turn left
   90 degrees", "R" meaning "turn right 90 degrees", and "a" and "b" being
   ignored. The initial position of the computer cursor is (0,0), pointing up
   towards (0,1).

   Then D[n] is an exotic drawing known as the Heighway Dragon of order n.
   For example, D[10] is shown below; counting each "F" as one step, the
   highlighted spot at (18,16) is the position reached after 500 steps.

   What is the position of the cursor after 10^12 steps in D[50] ?
   Give your answer in the form x,y with no spaces.
p_220.gif
"""


def test_problem_221(answer):
    output = p221.problem221()
    expected_output = answer['Problem 221']
    assert output == expected_output


"""


We shall call a positive integer A an "Alexandrian integer", if there
   exist integers p, q, r such that:

   A = p · q · r    and   1 = 1 + 1 + 1
                          A   p   q   r

   For example, 630 is an Alexandrian integer (p = 5, q = −7, r = −18).In
   fact, 630 is the 6^th Alexandrian integer, the first 6 Alexandrian
   integers being: 6, 42, 120, 156, 420 and 630.

   Find the 150000^th Alexandrian integer.
"""


@pytest.mark.skip(reason='too slow')
def test_problem_222(answer):
    output = p222.problem222()
    expected_output = answer['Problem 222']
    assert output == expected_output


"""


What is the length of the shortest pipe, of internal radius 50mm, that can
   fully contain 21 balls of radii 30mm, 31mm, ..., 50mm?

   Give your answer in micrometres (10^-6 m) rounded to the nearest integer.
"""


def test_problem_223(answer):
    output = p223.problem223()
    expected_output = answer['Problem 223']
    assert output == expected_output


"""


Let us call an integer sided triangle with sides a ≤ b ≤ c barely acute if
   the sides satisfy
   a^2 + b^2 = c^2 + 1.

   How many barely acute triangles are there with perimeter ≤ 25,000,000?
"""


def test_problem_224(answer):
    output = p224.problem224()
    expected_output = answer['Problem 224']
    assert output == expected_output


"""


Let us call an integer sided triangle with sides a ≤ b ≤ c barely obtuse
   if the sides satisfy
   a^2 + b^2 = c^2 - 1.

   How many barely obtuse triangles are there with perimeter ≤ 75,000,000?
"""


def test_problem_225(answer):
    output = p225.problem225()
    expected_output = answer['Problem 225']
    assert output == expected_output


"""


The sequence 1, 1, 1, 3, 5, 9, 17, 31, 57, 105, 193, 355, 653, 1201 ...
   is defined by T[1] = T[2] = T[3] = 1 and T[n] = T[n-1] + T[n-2] + T[n-3].

   It can be shown that 27 does not divide any terms of this sequence.
   In fact, 27 is the first odd number with this property.

   Find the 124^th odd number that does not divide any terms of the above
   sequence.
"""


def test_problem_226(answer):
    output = p226.problem226()
    expected_output = answer['Problem 226']
    assert output == expected_output


"""


The blancmange curve is the set of points (x,y) such that 0 ≤ x ≤ 1 and ,
   where s(x) = the distance from x to the nearest integer.

   The area under the blancmange curve is equal to ½, shown in pink in the
   diagram below.

                              [1]blancmange curve

   Let C be the circle with centre (¼,½) and radius ¼, shown in black in the
   diagram.

   What area under the blancmange curve is enclosed by C?
   Give your answer rounded to eight decimal places in the form 0.abcdefgh
Visible links
   p_226_formula.gif
   p_226_scoop002.gif
"""


def test_problem_227(answer):
    output = p227.problem227()
    expected_output = answer['Problem 227']
    assert output == expected_output


"""


"The Chase" is a game played with two dice and an even number of players.

   The players sit around a table; the game begins with two opposite players
   having one die each. On each turn, the two players with a die roll it.
   If a player rolls a 1, he passes the die to his neighbour on the left; if
   he rolls a 6, he passes the die to his neighbour on the right; otherwise,
   he keeps the die for the next turn.
   The game ends when one player has both dice after they have been rolled
   and passed; that player has then lost.

   In a game with 100 players, what is the expected number of turns the game
   lasts?

   Give your answer rounded to ten significant digits.
"""


def test_problem_228(answer):
    output = p228.problem228()
    expected_output = answer['Problem 228']
    assert output == expected_output


"""


Let S[n] be the regular n-sided polygon – or shape – whose vertices v[k]
   (k = 1,2,…,n) have coordinates:

          x[k]   =   cos( ^2k-1/[n] ×180° )
          y[k]   =   sin( ^2k-1/[n] ×180° )

   Each S[n] is to be interpreted as a filled shape consisting of all points
   on the perimeter and in the interior.

   The Minkowski sum, S+T, of two shapes S and T is the result of adding
   every point in S to every point in T, where point addition is performed
   coordinate-wise: (u, v) + (x, y) = (u+x, v+y).

   For example, the sum of S[3] and S[4] is the six-sided shape shown in pink
   below:

                          [1]picture showing S_3 + S_4

   How many sides does S[1864] + S[1865] + … + S[1909] have?
Visible links
   p_228.png
"""


def test_problem_229(answer):
    output = p229.problem229()
    expected_output = answer['Problem 229']
    assert output == expected_output


"""


Consider the number 3600. It is very special, because

   3600 = 48^2 +     36^2

   3600 = 20^2 + 2×40^2

   3600 = 30^2 + 3×30^2

   3600 = 45^2 + 7×15^2

   Similarly, we find that 88201 = 99^2 + 280^2 = 287^2 + 2×54^2 = 283^2 +
   3×52^2 = 197^2 + 7×84^2.

   In 1747, Euler proved which numbers are representable as a sum of two
   squares.We are interested in the numbers n which admit representations of
   all of the following four types:

   n = a[1]^2 +   b[1]^2

   n = a[2]^2 + 2 b[2]^2

   n = a[3]^2 + 3 b[3]^2

   n = a[7]^2 + 7 b[7]^2,

   where the a[k] and b[k] are positive integers.

   There are 75373 such numbers that do not exceed 10^7.
   How many such numbers are there that do not exceed 2×10^9?
"""


def test_problem_230(answer):
    output = p230.problem230()
    expected_output = answer['Problem 230']
    assert output == expected_output


"""


For any two strings of digits, A and B, we define F[A,B] to be the
   sequence (A,B,AB,BAB,ABBAB,...) in which each term is the concatenation of
   the previous two.

   Further, we define D[A,B](n) to be the n^th digit in the first term of
   F[A,B] that contains at least n digits.

   Example:

   Let A=1415926535, B=8979323846. We wish to find D[A,B](35), say.

   The first few terms of F[A,B] are:
   1415926535
   8979323846
   14159265358979323846
   897932384614159265358979323846
   14159265358979323846897932384614159265358979323846

   Then D[A,B](35) is the 35^th digit in the fifth term, which is 9.

   Now we use for A the first 100 digits of π behind the decimal point:

   14159265358979323846264338327950288419716939937510
   58209749445923078164062862089986280348253421170679

   and for B the next hundred digits:

   82148086513282306647093844609550582231725359408128
   48111745028410270193852110555964462294895493038196 .

   Find ∑[n = 0,1,...,17]   10^n× D[A,B]((127+19n)×7^n) .
"""


@pytest.mark.skip(reason='slow')
def test_problem_231(answer):
    output = p231.problem231()
    expected_output = answer['Problem 231']
    assert output == expected_output


"""


The binomial coefficient ^10C[3] = 120.
   120 = 2^3 × 3 × 5 = 2 × 2 × 2 × 3 × 5, and 2 + 2 + 2 + 3 + 5 = 14.
   So the sum of the terms in the prime factorisation of ^10C[3] is 14.

   Find the sum of the terms in the prime factorisation of
   ^20000000C[15000000].
"""


def test_problem_232(answer):
    output = p232.problem232()
    expected_output = answer['Problem 232']
    assert output == expected_output


"""


Two players share an unbiased coin and take it in turns to play "The
   Race". On Player 1's turn, he tosses the coin once: if it comes up Heads,
   he scores one point; if it comes up Tails, he scores nothing. On Player
   2's turn, she chooses a positive integer T and tosses the coin T times: if
   it comes up all Heads, she scores 2^T-1 points; otherwise, she scores
   nothing. Player 1 goes first. The winner is the first to 100 or more
   points.

   On each turn Player 2 selects the number, T, of coin tosses that maximises
   the probability of her winning.

   What is the probability that Player 2 wins?

   Give your answer rounded to eight decimal places in the form 0.abcdefgh .
"""


def test_problem_233(answer):
    output = p233.problem233()
    expected_output = answer['Problem 233']
    assert output == expected_output


"""


Let f(N) be the number of points with integer coordinates that are on a
   circle passing through (0,0), (N,0),(0,N), and (N,N).

   It can be shown that f(10000) = 36.

   What is the sum of all positive integers N ≤ 10^11 such that f(N) = 420 ?
"""


def test_problem_234(answer):
    output = p234.problem234()
    expected_output = answer['Problem 234']
    assert output == expected_output


"""


For an integer n ≥ 4, we define the lower prime square root of n, denoted
   by lps(n), as the largest prime ≤ √n and the upper prime square root of n,
   ups(n), as the smallest prime ≥ √n.

   So, for example, lps(4) = 2 = ups(4), lps(1000) = 31, ups(1000) = 37.
   Let us call an integer n ≥ 4 semidivisible, if one of lps(n) and ups(n)
   divides n, but not both.

   The sum of the semidivisible numbers not exceeding 15 is 30, the numbers
   are 8, 10 and 12.
   15 is not semidivisible because it is a multiple of both lps(15) = 3 and
   ups(15) = 5.
   As a further example, the sum of the 92 semidivisible numbers up to 1000
   is 34825.

   What is the sum of all semidivisible numbers not exceeding 999966663333 ?
"""


def test_problem_235(answer):
    output = p235.problem235()
    expected_output = answer['Problem 235']
    assert output == expected_output


"""


Given is the arithmetic-geometric sequence u(k) = (900-3k)r^k-1.
   Let s(n) = Σ[k=1...n]u(k).

   Find the value of r for which s(5000) = -600,000,000,000.

   Give your answer rounded to 12 places behind the decimal point.
"""


def test_problem_236(answer):
    output = p236.problem236()
    expected_output = answer['Problem 236']
    assert output == expected_output


"""


Suppliers 'A' and 'B' provided the following numbers of products for the
   luxury hamper market:

                                                         Product       'A'  'B'
                                                    Beluga Caviar      5248 640
                                                    Christmas Cake     1312 1888
                                                    Gammon Joint       2624 3776
                                                    Vintage Port       5760 3776
                                                    Champagne Truffles 3936 5664

   Although the suppliers try very hard to ship their goods in perfect
   condition, there is inevitably some spoilage - i.e. products gone bad.

   The suppliers compare their performance using two types of statistic:

     • The five per-product spoilage rates for each supplier are equal to the
       number of products gone bad divided by the number of products
       supplied, for each of the five products in turn.
     • The overall spoilage rate for each supplier is equal to the total
       number of products gone bad divided by the total number of products
       provided by that supplier.

   To their surprise, the suppliers found that each of the five per-product
   spoilage rates was worse (higher) for 'B' than for 'A' by the same factor
   (ratio of spoilage rates), m>1; and yet, paradoxically, the overall
   spoilage rate was worse for 'A' than for 'B', also by a factor of m.

   There are thirty-five m>1 for which this surprising result could have
   occurred, the smallest of which is 1476/1475.

   What's the largest possible value of m?
   Give your answer as a fraction reduced to its lowest terms, in the form
   u/v.
"""


def test_problem_237(answer):
    output = p237.problem237()
    expected_output = answer['Problem 237']
    assert output == expected_output


"""


Let T(n) be the number of tours over a 4 × n playing board such that:

     • The tour starts in the top left corner.
     • The tour consists of moves that are up, down, left, or right one
       square.
     • The tour visits each square exactly once.
     • The tour ends in the bottom left corner.

   The diagram shows one tour over a 4 × 10 board:

   T(10) is 2329. What is T(10^12) modulo 10^8?
p_237.gif
"""


def test_problem_238(answer):
    output = p238.problem238()
    expected_output = answer['Problem 238']
    assert output == expected_output


"""


Create a sequence of numbers using the "Blum Blum Shub" pseudo-random
   number generator:

                          s[0]   = 14025256
                          s[n+1] = s[n]^2 mod 20300713

   Concatenate these numbers  s[0]s[1]s[2]… to create a string w of infinite
   length.
   Then, w = 14025256741014958470038053646…

   For a positive integer k, if no substring of w exists with a sum of digits
   equal to k, p(k) is defined to be zero. If at least one substring of w
   exists with a sum of digits equal to k, we define p(k) = z, where z is the
   starting position of the earliest such substring.

   For instance:

   The substrings 1, 14, 1402, …
   with respective sums of digits equal to 1, 5, 7, …
   start at position 1, hence p(1) = p(5) = p(7) = … = 1.

   The substrings 4, 402, 4025, …
   with respective sums of digits equal to 4, 6, 11, …
   start at position 2, hence p(4) = p(6) = p(11) = … = 2.

   The substrings 02, 0252, …
   with respective sums of digits equal to 2, 9, …
   start at position 3, hence p(2) = p(9) = … = 3.

   Note that substring 025 starting at position 3, has a sum of digits equal
   to 7, but there was an earlier substring (starting at position 1) with a
   sum of digits equal to 7, so p(7) = 1, not 3.

   We can verify that, for 0 < k ≤ 10^3, ∑ p(k) = 4742.

   Find ∑ p(k), for 0 < k ≤ 2·10^15.
"""


def test_problem_239(answer):
    output = p239.problem239()
    expected_output = answer['Problem 239']
    assert output == expected_output


"""


A set of disks numbered 1 through 100 are placed in a line in random
   order.

   What is the probability that we have a partial derangement such that
   exactly 22 prime number discs are found away from their natural positions?
   (Any number of non-prime disks may also be found in or out of their
   natural positions.)

   Give your answer rounded to 12 places behind the decimal point in the form
   0.abcdefghijkl.
"""


def test_problem_240(answer):
    output = p240.problem240()
    expected_output = answer['Problem 240']
    assert output == expected_output


"""


There are 1111 ways in which five 6-sided dice (sides numbered 1 to 6) can
   be rolled so that the top three sum to 15. Some examples are:

   D[1],D[2],D[3],D[4],D[5] = 4,3,6,3,5
   D[1],D[2],D[3],D[4],D[5] = 4,3,3,5,6
   D[1],D[2],D[3],D[4],D[5] = 3,3,3,6,6
   D[1],D[2],D[3],D[4],D[5] = 6,6,3,3,3

   In how many ways can twenty 12-sided dice (sides numbered 1 to 12) be
   rolled so that the top ten sum to 70?
"""


def test_problem_241(answer):
    output = p241.problem241()
    expected_output = answer['Problem 241']
    assert output == expected_output


"""


For a positive integer n, let σ(n) be the sum of all divisors of n, so
   e.g. σ(6) = 1 + 2 + 3 + 6 = 12.

   A perfect number, as you probably know, is a number with σ(n) = 2n.

   Let us define the perfection quotient of a positive integer p(n) =  σ(n) .
   as                                                                   n

   Find the sum of all positive integers n ≤ 10^18 for which p(n) has the
   form k + ^1⁄[2], where k is an integer.
"""


def test_problem_242(answer):
    output = p242.problem242()
    expected_output = answer['Problem 242']
    assert output == expected_output


"""


Given the set {1,2,...,n}, we define f(n,k) as the number of its k-element
   subsets with an odd sum of elements. For example, f(5,3) = 4, since the
   set {1,2,3,4,5} has four 3-element subsets having an odd sum of elements,
   i.e.: {1,2,4}, {1,3,5}, {2,3,4} and {2,4,5}.

   When all three values n, k and f(n,k) are odd, we say that they make
   an odd-triplet [n,k,f(n,k)].

   There are exactly five odd-triplets with n ≤ 10, namely:
   [1,1,f(1,1) = 1], [5,1,f(5,1) = 3], [5,5,f(5,5) = 1], [9,1,f(9,1) = 5] and
   [9,9,f(9,9) = 1].

   How many odd-triplets are there with n ≤ 10^12 ?
"""


def test_problem_243(answer):
    output = p243.problem243()
    expected_output = answer['Problem 243']
    assert output == expected_output


"""


A positive fraction whose numerator is less than its denominator is called
   a proper fraction.
   For any denominator, d, there will be d−1 proper fractions; for example,
   with d = 12:
   1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 ,
   8/12 , 9/12 , 10/12 , 11/12 .

   We shall call a fraction that cannot be cancelled down a resilient
   fraction.
   Furthermore we shall define the resilience of a denominator, R(d), to be
   the ratio of its proper fractions that are resilient; for example, R(12) =
   4/11 .
   In fact, d = 12 is the smallest denominator having a resilience R(d) <
   4/10 .

   Find the smallest denominator d, having a resilience R(d) < 15499/94744
   .
"""


def test_problem_244(answer):
    output = p244.problem244()
    expected_output = answer['Problem 244']
    assert output == expected_output


"""


You probably know the game Fifteen Puzzle. Here, instead of numbered
   tiles, we have seven red tiles and eight blue tiles.

   A move is denoted by the uppercase initial of the direction (Left, Right,
   Up, Down) in which the tile is slid, e.g. starting from configuration (S),
   by the sequence LULUR we reach the configuration (E):

                  (S)                   , (E)

   For each path, its checksum is calculated by (pseudocode):
   checksum = 0
   checksum = (checksum × 243 + m[1]) mod 100 000 007
   checksum = (checksum × 243 + m[2]) mod 100 000 007
      …
   checksum = (checksum × 243 + m[n]) mod 100 000 007
   where m[k] is the ASCII value of the k^th letter in the move sequence and
                      the ASCII values for the moves are:

                                 ┌──────┬─────┐
                                 │L     │76   │
                                 ├──────┼─────┤
                                 │R     │82   │
                                 ├──────┼─────┤
                                 │U     │85   │
                                 ├──────┼─────┤
                                 │D     │68   │
                                 └──────┴─────┘

   For the sequence LULUR given above, the checksum would be 19761398.

   Now, starting from configuration (S),find all shortest ways to reach
   configuration (T).

                  (S)                   , (T)

   What is the sum of all checksums for the paths having the minimal length?
p_244_start.gif
   p_244_example.gif
   p_244_start.gif
   p_244_target.gif
"""


def test_problem_245(answer):
    output = p245.problem245()
    expected_output = answer['Problem 245']
    assert output == expected_output


"""


We shall call a fraction that cannot be cancelled down a resilient
   fraction.
   Furthermore we shall define the resilience of a denominator, R(d), to be
   the ratio of its proper fractions that are resilient; for example, R(12) =
   ^4⁄[11].

   The resilience of a number d > 1 is     φ(d)  , where φ is Euler's totient
   then                                    d - 1 function.

   We further define the coresilience of a number n > 1 as C(n) =  n - φ(n) .
                                                                    n - 1

   The coresilience of a prime p is C(p) =    1   .
                                            p - 1

   Find the sum of all composite integers 1 < n ≤ 2×10^11, for which C(n) is
   a unit fraction.
"""


def test_problem_246(answer):
    output = p246.problem246()
    expected_output = answer['Problem 246']
    assert output == expected_output


"""


A definition for an ellipse is:
   Given a circle c with centre M and radius r and a point G such that
   d(G,M)<r, the locus of the points that are equidistant from c and G form
   an ellipse.

         The construction of the points of the ellipse is shown below.

   Given are the points M(-2000,1500) and G(8000,1500).
   Given is also the circle c with centre M and radius 15000.
   The locus of the points that are equidistant from G and c form an ellipse
   e.
   From a point P outside e the two tangents t[1] and t[2] to the ellipse are
   drawn.
   Let the points where t[1] and t[2] touch the ellipse be R and S.

   For how many lattice points P is angle RPS greater than 45 degrees?
p_246_anim.gif
   p_246_ellipse.gif
"""


def test_problem_247(answer):
    output = p247.problem247()
    expected_output = answer['Problem 247']
    assert output == expected_output


"""


Consider the region constrained by 1 ≤ x and 0 ≤ y ≤ ^1/[x].

   Let S[1] be the largest square that can fit under the curve.
   Let S[2] be the largest square that fits in the remaining area, and so on.
   Let the index of S[n] be the pair (left, below) indicating the number of
   squares to the left of S[n] and the number of squares below S[n].

   The diagram shows some such squares labelled by number.
   S[2] has one square to its left and none below, so the index of S[2] is
   (1,0).
   It can be seen that the index of S[32] is (1,1) as is the index of S[50].
   50 is the largest n for which the index of S[n] is (1,1).

   What is the largest n for which the index of S[n] is (3,3)?
p_247_hypersquares.gif
"""


def test_problem_248(answer):
    output = p248.problem248()
    expected_output = answer['Problem 248']
    assert output == expected_output


"""


The first number n for which φ(n)=13! is 6227180929.

   Find the 150,000^th such number.
"""


@pytest.mark.skip(reason='slow')
def test_problem_249(answer):
    output = p249.problem249()
    expected_output = answer['Problem 249']
    assert output == expected_output


"""


Let S = {2, 3, 5, ..., 4999} be the set of prime numbers less than 5000.

   Find the number of subsets of S, the sum of whose elements is a prime
   number.
   Enter the rightmost 16 digits as your answer.
"""


@pytest.mark.skip(reason='slow')
def test_problem_250(answer):
    output = p250.problem250()
    expected_output = answer['Problem 250']
    assert output == expected_output


"""


Find the number of non-empty subsets of {1^1, 2^2, 3^3,...,
   250250^250250}, the sum of whose elements is divisible by 250. Enter the
   rightmost 16 digits as your answer.
"""


def test_problem_251(answer):
    output = p251.problem251()
    expected_output = answer['Problem 251']
    assert output == expected_output


"""


A triplet of positive integers (a,b,c) is called a Cardano Triplet if it
   satisfies the condition:

   For example, (2,1,5) is a Cardano Triplet.

   There exist 149 Cardano Triplets for which a+b+c ≤ 1000.

   Find how many Cardano Triplets exist such that a+b+c ≤ 110,000,000.
p_251_cardano.gif
"""


def test_problem_252(answer):
    output = p252.problem252()
    expected_output = answer['Problem 252']
    assert output == expected_output


"""


Given a set of points on a plane, we define a convex hole to be a convex
   polygon having as vertices any of the given points and not containing any
   of the given points in its interior (in addition to the vertices, other
   given points may lie on the perimeter of the polygon).

   As an example, the image below shows a set of twenty points and a few such
   convex holes. The convex hole shown as a red heptagon has an area equal to
   1049694.5 square units, which is the highest possible area for a convex
   hole on the given set of points.

   For our example, we used the first 20 points (T[2k−1], T[2k]), for
   k = 1,2,…,20, produced with the pseudo-random number generator:

                     S[0]   =[ ] 290797[ ]
                     S[n+1] =[ ] S[n]^2 mod 50515093
                     T[n]   =[ ] ( S[n] mod 2000 ) − 1000^ 

   i.e. (527, 144), (−488, 732), (−454, −947), …

   What is the maximum area for a convex hole on the set containing the first
   500 points in the pseudo-random sequence?
   Specify your answer including one digit after the decimal point.
p_252_convexhole.gif
"""


def test_problem_253(answer):
    output = p253.problem253()
    expected_output = answer['Problem 253']
    assert output == expected_output


"""


A small child has a “number caterpillar” consisting of forty jigsaw
   pieces, each with one number on it, which, when connected together in a
   line, reveal the numbers 1 to 40 in order.

   Every night, the child's father has to pick up the pieces of the
   caterpillar that have been scattered across the play room. He picks up the
   pieces at random and places them in the correct order.
   As the caterpillar is built up in this way, it forms distinct segments
   that gradually merge together.
   The number of segments starts at zero (no pieces placed), generally
   increases up to about eleven or twelve, then tends to drop again before
   finishing at a single segment (all pieces placed).

   For example:

                         ┌────────────┬───────────────┐
                         │Piece Placed│Segments So Far│
                         ├────────────┼───────────────┤
                         │     12     │       1       │
                         ├────────────┼───────────────┤
                         │     4      │       2       │
                         ├────────────┼───────────────┤
                         │     29     │       3       │
                         ├────────────┼───────────────┤
                         │     6      │       4       │
                         ├────────────┼───────────────┤
                         │     34     │       5       │
                         ├────────────┼───────────────┤
                         │     5      │       4       │
                         ├────────────┼───────────────┤
                         │     35     │       4       │
                         ├────────────┼───────────────┤
                         │     …      │       …       │
                         └────────────┴───────────────┘

   Let M be the maximum number of segments encountered during a random
   tidy-up of the caterpillar.
   For a caterpillar of ten pieces, the number of possibilities for each M is

                            ┌────────┬─────────────┐
                            │   M    │Possibilities│
                            ├────────┼─────────────┤
                            │   1    │    512      │
                            ├────────┼─────────────┤
                            │   2    │ 250912      │
                            ├────────┼─────────────┤
                            │   3    │1815264      │
                            ├────────┼─────────────┤
                            │   4    │1418112      │
                            ├────────┼─────────────┤
                            │   5    │ 144000      │
                            └────────┴─────────────┘

   so the most likely value of M is 3 and the average value is
   ^385643⁄[113400] = 3.400732, rounded to six decimal places.

   The most likely value of M for a forty-piece caterpillar is 11; but what
   is the average value of M?

   Give your answer rounded to six decimal places.
"""


def test_problem_254(answer):
    output = p254.problem254()
    expected_output = answer['Problem 254']
    assert output == expected_output


"""


Define f(n) as the sum of the factorials of the digits of n. For example,
   f(342) = 3! + 4! + 2! = 32.

   Define sf(n) as the sum of the digits of f(n). So sf(342) = 3 + 2 = 5.

   Define g(i) to be the smallest positive integer n such that sf(n) = i.
   Though sf(342) is 5, sf(25) is also 5, and it can be verified that g(5) is
   25.

   Define sg(i) as the sum of the digits of g(i). So sg(5) = 2 + 5 = 7.

   Further, it can be verified that g(20) is 267 and ∑ sg(i) for 1 ≤ i ≤ 20
   is 156.

   What is ∑ sg(i) for 1 ≤ i ≤ 150?
"""


def test_problem_255(answer):
    output = p255.problem255()
    expected_output = answer['Problem 255']
    assert output == expected_output


"""


We define the rounded-square-root of a positive integer n as the square
   root of n rounded to the nearest integer.

   The following procedure (essentially Heron's method adapted to integer
   arithmetic) finds the rounded-square-root of n:

   Let d be the number of digits of the number n.
   If d is odd, set x[0] = 2×10^(d-1)⁄2.
   If d is even, set x[0] = 7×10^(d-2)⁄2.
   Repeat:

   until x[k+1] = x[k].

   As an example, let us find the rounded-square-root of n = 4321.
   n has 4 digits, so x[0] = 7×10^(4-2)⁄2 = 70.
   Since x[2] = x[1], we stop here.
   So, after just two iterations, we have found that the rounded-square-root
   of 4321 is 66 (the actual square root is 65.7343137…).

   The number of iterations required when using this method is surprisingly
   low.
   For example, we can find the rounded-square-root of a 5-digit integer
   (10,000 ≤ n ≤ 99,999) with an average of 3.2102888889 iterations (the
   average value was rounded to 10 decimal places).

   Using the procedure described above, what is the average number of
   iterations required to find the rounded-square-root of a 14-digit number
   (10^13 ≤ n < 10^14)?
   Give your answer rounded to 10 decimal places.

   Note: The symbols ⌊x⌋ and ⌈x⌉ represent the floor function and ceiling
   function respectively.
p_255_Heron.gif
   p_255_Example.gif
"""


def test_problem_256(answer):
    output = p256.problem256()
    expected_output = answer['Problem 256']
    assert output == expected_output


"""


Tatami are rectangular mats, used to completely cover the floor of a room,
   without overlap.

   Assuming that the only type of available tatami has dimensions 1×2, there
   are obviously some limitations for the shape and size of the rooms that
   can be covered.

   For this 
Problem, we consider only rectangular rooms with integer
   dimensions a, b and even size s = a·b.
   We use the term 'size' to denote the floor surface area of the room, and —
   without loss of generality — we add the condition a ≤ b.

   There is one rule to follow when laying out tatami: there must be no
   points where corners of four different mats meet.
   For example, consider the two arrangements below for a 4×4 room:

   The arrangement on the left is acceptable, whereas the one on the right is
   not: a red "X" in the middle, marks the point where four tatami meet.

   Because of this rule, certain even-sized rooms cannot be covered with
   tatami: we call them tatami-free rooms.
   Further, we define T(s) as the number of tatami-free rooms of size s.

   The smallest tatami-free room has size s = 70 and dimensions 7×10.
   All the other rooms of size s = 70 can be covered with tatami; they are:
   1×70, 2×35 and 5×14.
   Hence, T(70) = 1.

   Similarly, we can verify that T(1320) = 5 because there are exactly 5
   tatami-free rooms of size s = 1320:
   20×66, 22×60, 24×55, 30×44 and 33×40.
   In fact, s = 1320 is the smallest room-size s for which T(s) = 5.

   Find the smallest room-size s for which T(s) = 200.
p_256_tatami3.gif
"""


def test_problem_257(answer):
    output = p257.problem257()
    expected_output = answer['Problem 257']
    assert output == expected_output


"""


Given is an integer sided triangle ABC with sides a ≤ b ≤ c. (AB = c, BC =
   a and AC = b).
   The angular bisectors of the triangle intersect the sides at points E, F
   and G (see picture below).

   The segments EF, EG and FG partition the triangle ABC into four smaller
   triangles: AEG, BFE, CGF and EFG.
   It can be proven that for each of these four triangles the ratio
   area(ABC)/area(subtriangle) is rational.
   However, there exist triangles for which some or all of these ratios are
   integral.

   How many triangles ABC with perimeter≤100,000,000 exist so that the ratio
   area(ABC)/area(AEG) is integral?
p_257_bisector.gif
"""


def test_problem_258(answer):
    output = p258.problem258()
    expected_output = answer['Problem 258']
    assert output == expected_output


"""


A sequence is defined as:

     • g[k] = 1, for 0 ≤ k ≤ 1999
     • g[k] = g[k-2000] + g[k-1999], for k ≥ 2000.

   Find g[k] mod 20092010 for k = 10^18.
"""


def test_problem_259(answer):
    output = p259.problem259()
    expected_output = answer['Problem 259']
    assert output == expected_output


"""


A positive integer will be called reachable if it can result from an
   arithmetic expression obeying the following rules:

     • Uses the digits 1 through 9, in that order and exactly once each.
     • Any successive digits can be concatenated (for example, using the
       digits 2, 3 and 4 we obtain the number 234).
     • Only the four usual binary arithmetic operations (addition,
       subtraction, multiplication and division) are allowed.
     • Each operation can be used any number of times, or not at all.
     • Unary minus is not allowed.
     • Any number of (possibly nested) parentheses may be used to define the
       order of operations.

   For example, 42 is reachable, since (1/23) * ((4*5)-6) * (78-9) = 42.

   What is the sum of all positive reachable integers?
"""


def test_problem_260(answer):
    output = p260.problem260()
    expected_output = answer['Problem 260']
    assert output == expected_output


"""


A game is played with three piles of stones and two players.
   At her turn, a player removes one or more stones from the piles. However,
   if she takes stones from more than one pile, she must remove the same
   number of stones from each of the selected piles.

   In other words, the player chooses some N>0 and removes:

     • N stones from any single pile; or
     • N stones from each of any two piles (2N total); or
     • N stones from each of the three piles (3N total).

   The player taking the last stone(s) wins the game.

   A winning configuration is one where the first player can force a win.
   For example, (0,0,13), (0,11,11) and (5,5,5) are winning configurations
   because the first player can immediately remove all stones.

   A losing configuration is one where the second player can force a win, no
   matter what the first player does.
   For example, (0,1,2) and (1,3,3) are losing configurations: any legal move
   leaves a winning configuration for the second player.

   Consider all losing configurations (x[i],y[i],z[i]) where x[i] ≤ y[i] ≤
   z[i] ≤ 100.
   We can verify that Σ(x[i]+y[i]+z[i]) = 173895 for these.

   Find Σ(x[i]+y[i]+z[i]) where (x[i],y[i],z[i]) ranges over the losing
   configurations
   with x[i] ≤ y[i] ≤ z[i] ≤ 1000.
"""


def test_problem_261(answer):
    output = p261.problem261()
    expected_output = answer['Problem 261']
    assert output == expected_output


"""


Let us call a positive integer k a square-pivot, if there is a pair of
   integers m > 0 and n ≥ k, such that the sum of the (m+1) consecutive
   squares up to k equals the sum of the m consecutive squares from (n+1) on:

                 (k-m)^2 + ... + k^2 = (n+1)^2 + ... + (n+m)^2.

   Some small square-pivots are

     • 4: 3^2 + 4^2 = 5^2
     • 21: 20^2 + 21^2 = 29^2
     • 24: 21^2 + 22^2 + 23^2 + 24^2 = 25^2 + 26^2 + 27^2
     • 110: 108^2 + 109^2 + 110^2 = 133^2 + 134^2

   Find the sum of all distinct square-pivots ≤ 10^10.
"""


def test_problem_262(answer):
    output = p262.problem262()
    expected_output = answer['Problem 262']
    assert output == expected_output


"""


The following equation represents the continuous topography of a
   mountainous region, giving the elevation h at any point (x,y):

   A mosquito intends to fly from A(200,200) to B(1400,1400), without leaving
   the area given by 0 ≤ x, y ≤ 1600.

   Because of the intervening mountains, it first rises straight up to a
   point A', having elevation f. Then, while remaining at the same elevation
   f, it flies around any obstacles until it arrives at a point B' directly
   above B.

   First, determine f[min] which is the minimum constant elevation allowing
   such a trip from A to B, while remaining in the specified area.
   Then, find the length of the shortest path between A' and B', while flying
   at that constant elevation f[min].

   Give that length as your answer, rounded to three decimal places.

   Note: For convenience, the elevation function shown above is repeated
   below, in a form suitable for most programming languages:
   h=( 5000-0.005*(x*x+y*y+x*y)+12.5*(x+y) ) * exp(
   -abs(0.000001*(x*x+y*y)-0.0015*(x+y)+0.7) )
p_262_formula1.gif
"""


def test_problem_263(answer):
    output = p263.problem263()
    expected_output = answer['Problem 263']
    assert output == expected_output


"""


Consider the number 6. The divisors of 6 are: 1,2,3 and 6.
   Every number from 1 up to and including 6 can be written as a sum of
   distinct divisors of 6:
   1=1, 2=2, 3=1+2, 4=1+3, 5=2+3, 6=6.
   A number n is called a practical number if every number from 1 up to and
   including n can be expressed as a sum of distinct divisors of n.

   A pair of consecutive prime numbers with a difference of six is called a
   sexy pair (since "sex" is the Latin word for "six"). The first sexy pair
   is (23, 29).

   We may occasionally find a triple-pair, which means three consecutive sexy
   prime pairs, such that the second member of each pair is the first member
   of the next pair.

   We shall call a number n such that :

     • (n-9, n-3), (n-3,n+3), (n+3, n+9) form a triple-pair, and
     • the numbers n-8, n-4, n, n+4 and n+8 are all practical,

   an engineers’ paradise.

   Find the sum of the first four engineers’ paradises.
"""


def test_problem_264(answer):
    output = p264.problem264()
    expected_output = answer['Problem 264']
    assert output == expected_output


"""


Consider all the triangles having:

     • All their vertices on lattice points.
     • Circumcentre at the origin O.
     • Orthocentre at the point H(5, 0).

   There are nine such triangles having a perimeter ≤ 50.
   Listed and shown in ascending order of their perimeter, they are:

   A(-4, 3), B(5, 0), C(4, -3)
   A(4, 3), B(5, 0), C(-4, -3)
   A(-3, 4), B(5, 0), C(3, -4)

   A(3, 4), B(5, 0), C(-3, -4)
   A(0, 5), B(5, 0), C(0, -5)
   A(1, 8), B(8, -1), C(-4, -7)

   A(8, 1), B(1, -8), C(-4, 7)
   A(2, 9), B(9, -2), C(-6, -7)
   A(9, 2), B(2, -9), C(-6, 7)

   The sum of their perimeters, rounded to four decimal places, is 291.0089.

   Find all such triangles with a perimeter ≤ 10^5.
   Enter as your answer the sum of their perimeters rounded to four decimal
   places.
p_264_TriangleCentres.gif
"""


@pytest.mark.skip(reason='slow')
def test_problem_265(answer):
    output = p265.problem265()
    expected_output = answer['Problem 265']
    assert output == expected_output


"""


2^N binary digits can be placed in a circle so that all the N-digit
   clockwise subsequences are distinct.

   For N=3, two such circular arrangements are possible, ignoring rotations:

   For the first arrangement, the 3-digit subsequences, in clockwise order,
   are:
   000, 001, 010, 101, 011, 111, 110 and 100.

   Each circular arrangement can be encoded as a number by concatenating the
   binary digits starting with the subsequence of all zeros as the most
   significant bits and proceeding clockwise. The two arrangements for N=3
   are thus represented as 23 and 29:
                               00010111 [2] = 23
                               00011101 [2] = 29

   Calling S(N) the sum of the unique numeric representations, we can see
   that S(3) = 23 + 29 = 52.

   Find S(5).
p_265_BinaryCircles.gif
"""


def test_problem_266(answer):
    output = p266.problem266()
    expected_output = answer['Problem 266']
    assert output == expected_output


"""


The divisors of 12 are: 1,2,3,4,6 and 12.
   The largest divisor of 12 that does not exceed the square root of 12 is 3.
   We shall call the largest divisor of an integer n that does not exceed the
   square root of n the pseudo square root (PSR) of n.
   It can be seen that PSR(3102)=47.

   Let p be the product of the primes below 190.
   Find PSR(p) mod 10^16.
"""


def test_problem_267(answer):
    output = p267.problem267()
    expected_output = answer['Problem 267']
    assert output == expected_output


"""


You are given a unique investment opportunity.

   Starting with £1 of capital, you can choose a fixed proportion, f, of your
   capital to bet on a fair coin toss repeatedly for 1000 tosses.

   Your return is double your bet for heads and you lose your bet for tails.

   For example, if f = 1/4, for the first toss you bet £0.25, and if heads
   comes up you win £0.5 and so then have £1.5. You then bet £0.375 and if
   the second toss is tails, you have £1.125.

   Choosing f to maximize your chances of having at least £1,000,000,000
   after 1,000 flips, what is the chance that you become a billionaire?

   All computations are assumed to be exact (no rounding), but give your
   answer rounded to 12 digits behind the decimal point in the form
   0.abcdefghijkl.
"""


def test_problem_268(answer):
    output = p268.problem268()
    expected_output = answer['Problem 268']
    assert output == expected_output


"""


It can be verified that there are 23 positive integers less than 1000 that
   are divisible by at least four distinct primes less than 100.

   Find how many positive integers less than 10^16 are divisible by at least
   four distinct primes less than 100.
"""


def test_problem_269(answer):
    output = p269.problem269()
    expected_output = answer['Problem 269']
    assert output == expected_output


"""


A root or zero of a polynomial P(x) is a solution to the equation P(x) =
   0.
   Define P[n] as the polynomial whose coefficients are the digits of n.
   For example, P[5703](x) = 5x^3 + 7x^2 + 3.

   We can see that:

     • P[n](0) is the last digit of n,
     • P[n](1) is the sum of the digits of n,
     • P[n](10) is n itself.

   Define Z(k) as the number of positive integers, n, not exceeding k for
   which the polynomial P[n] has at least one integer root.

   It can be verified that Z(100 000) is 14696.

   What is Z(10^16)?
"""


def test_problem_270(answer):
    output = p270.problem270()
    expected_output = answer['Problem 270']
    assert output == expected_output


"""


A square piece of paper with integer dimensions N×N is placed with a
   corner at the origin and two of its sides along the x- and y-axes. Then,
   we cut it up respecting the following rules:

     • We only make straight cuts between two points lying on different sides
       of the square, and having integer coordinates.
     • Two cuts cannot cross, but several cuts can meet at the same border
       point.
     • Proceed until no more legal cuts can be made.

   Counting any reflections or rotations as distinct, we call C(N) the number
   of ways to cut an N×N square. For example, C(1) = 2 and C(2) = 30 (shown
   below).

   What is C(30) mod 10^8 ?
p_270_CutSquare.gif
"""


def test_problem_271(answer):
    output = p271.problem271()
    expected_output = answer['Problem 271']
    assert output == expected_output


"""


For a positive number n, define S(n) as the sum of the integers x, for
   which 1<x<n and
   x^3≡1 mod n.

   When n=91, there are 8 possible values for x, namely : 9, 16, 22, 29, 53,
   74, 79, 81.
   Thus, S(91)=9+16+22+29+53+74+79+81=363.

   Find S(13082761331670030).
"""


def test_problem_272(answer):
    output = p272.problem272()
    expected_output = answer['Problem 272']
    assert output == expected_output


"""


For a positive number n, define C(n) as the number of the integers x, for
   which 1<x<n and
   x^3≡1 mod n.

   When n=91, there are 8 possible values for x, namely : 9, 16, 22, 29, 53,
   74, 79, 81.
   Thus, C(91)=8.

   Find the sum of the positive numbers n≤10^11 for which C(n)=242.
"""


def test_problem_273(answer):
    output = p273.problem273()
    expected_output = answer['Problem 273']
    assert output == expected_output


"""


Consider equations of the form: a^2 + b^2 = N, 0 ≤ a ≤ b, a, b and N
   integer.

   For N=65 there are two solutions:

   a=1, b=8 and a=4, b=7.

   We call S(N) the sum of the values of a of all solutions of a^2 + b^2 = N,
   0 ≤ a ≤ b, a, b and N integer.

   Thus S(65) = 1 + 4 = 5.

   Find ∑S(N), for all squarefree N only divisible by primes of the form 4k+1
   with 4k+1 < 150.
"""


def test_problem_274(answer):
    output = p274.problem274()
    expected_output = answer['Problem 274']
    assert output == expected_output


"""


For each integer p > 1 coprime to 10 there is a positive divisibility
   multiplier m < p which preserves divisibility by p for the following
   function on any positive integer, n:

   f(n) = (all but the last digit of n) + (the last digit of n) * m

   That is, if m is the divisibility multiplier for p, then f(n) is divisible
   by p if and only if n is divisible by p.

   (When n is much larger than p, f(n) will be less than n and repeated
   application of f provides a multiplicative divisibility test for p.)

   For example, the divisibility multiplier for 113 is 34.

   f(76275) = 7627 + 5 * 34 = 7797 : 76275 and 7797 are both divisible by 113
   f(12345) = 1234 + 5 * 34 = 1404 : 12345 and 1404 are both not divisible by
   113

   The sum of the divisibility multipliers for the primes that are coprime to
   10 and less than 1000 is 39517. What is the sum of the divisibility
   multipliers for the primes that are coprime to 10 and less than 10^7?
"""


def test_problem_275(answer):
    output = p275.problem275()
    expected_output = answer['Problem 275']
    assert output == expected_output


"""


Let us define a balanced sculpture of order n as follows:

     • A polyomino made up of n+1 tiles known as the blocks (n tiles)
       and the plinth (remaining tile);
     • the plinth has its centre at position (x = 0, y = 0);
     • the blocks have y-coordinates greater than zero (so the plinth is the
       unique lowest tile);
     • the centre of mass of all the blocks, combined, has x-coordinate equal
       to zero.

   When counting the sculptures, any arrangements which are simply
   reflections about the y-axis, are not counted as distinct. For example,
   the 18 balanced sculptures of order 6 are shown below; note that each pair
   of mirror images (about the y-axis) is counted as one sculpture:

   There are 964 balanced sculptures of order 10 and 360505 of order 15.
   How many balanced sculptures are there of order 18?
p_275_sculptures2.gif
"""


def test_problem_276(answer):
    output = p276.problem276()
    expected_output = answer['Problem 276']
    assert output == expected_output


"""


Consider the triangles with integer sides a, b and c with a ≤ b ≤ c.
   An integer sided triangle (a,b,c) is called primitive if gcd(a,b,c)=1.
   How many primitive integer sided triangles exist with a perimeter not
   exceeding 10 000 000?
"""


def test_problem_277(answer):
    output = p277.problem277()
    expected_output = answer['Problem 277']
    assert output == expected_output


"""


A modified Collatz sequence of integers is obtained from a starting value
   a[1] in the following way:

   a[n+1] = a[n]/3 if a[n] is divisible by 3. We shall denote this as a large
   downward step, "D".

   a[n+1] = (4a[n] + 2)/3 if a[n] divided by 3 gives a remainder of 1. We
   shall denote this as an upward step, "U".

   a[n+1] = (2a[n] - 1)/3 if a[n] divided by 3 gives a remainder of 2. We
   shall denote this as a small downward step, "d".

   The sequence terminates when some a[n] = 1.

   Given any integer, we can list out the sequence of steps.
   For instance if a[1]=231, then the sequence
   {a[n]}={231,77,51,17,11,7,10,14,9,3,1} corresponds to the steps
   "DdDddUUdDD".

   Of course, there are other sequences that begin with that same sequence
   "DdDddUUdDD....".
   For instance, if a[1]=1004064, then the sequence is
   DdDddUUdDDDdUDUUUdDdUUDDDUdDD.
   In fact, 1004064 is the smallest possible a[1] > 10^6 that begins with the
   sequence DdDddUUdDD.

   What is the smallest a[1] > 10^15 that begins with the sequence
   "UDDDUdddDDUDDddDdDddDDUDDdUUDd"?
"""


def test_problem_278(answer):
    output = p278.problem278()
    expected_output = answer['Problem 278']
    assert output == expected_output


"""


Given the values of integers 1 < a[1] < a[2] <... < a[n], consider the
   linear combination
   q[1]a[1] + q[2]a[2] + ... + q[n]a[n] = b, using only integer values q[k] ≥
   0.

   Note that for a given set of a[k], it may be that not all values of b are
   possible.
   For instance, if a[1] = 5 and a[2] = 7, there are no q[1] ≥ 0 and q[2] ≥ 0
   such that b could be
   1, 2, 3, 4, 6, 8, 9, 11, 13, 16, 18 or 23.
   In fact, 23 is the largest impossible value of b for a[1] = 5 and a[2] =
   7.
   We therefore call f(5, 7) = 23.
   Similarly, it can be shown that f(6, 10, 15)=29 and f(14, 22, 77) = 195.

   Find ∑ f(p*q,p*r,q*r), where p, q and r are prime numbers and p < q < r <
   5000.
"""


def test_problem_279(answer):
    output = p279.problem279()
    expected_output = answer['Problem 279']
    assert output == expected_output


"""


How many triangles are there with integral sides, at least one integral
   angle (measured in degrees), and a perimeter that does not exceed 10^8?
"""


@pytest.mark.skip(reason='slow')
def test_problem_280(answer):
    output = p280.problem280()
    expected_output = answer['Problem 280']
    assert output == expected_output


"""


A laborious ant walks randomly on a 5x5 grid. The walk starts from the
   central square. At each step, the ant moves to an adjacent square at
   random, without leaving the grid; thus there are 2, 3 or 4 possible moves
   at each step depending on the ant's position.

   At the start of the walk, a seed is placed on each square of the lower
   row. When the ant isn't carrying a seed and reaches a square of the lower
   row containing a seed, it will start to carry the seed. The ant will drop
   the seed on the first empty square of the upper row it eventually reaches.

   What's the expected number of steps until all seeds have been dropped in
   the top row?
   Give your answer rounded to 6 decimal places.
"""


def test_problem_281(answer):
    output = p281.problem281()
    expected_output = answer['Problem 281']
    assert output == expected_output


"""


You are given a pizza (perfect circle) that has been cut into m·n equal
   pieces and you want to have exactly one topping on each slice.

   Let f(m,n) denote the number of ways you can have toppings on the pizza
   with m different toppings (m ≥ 2), using each topping on exactly n slices
   (n ≥ 1).
   Reflections are considered distinct, rotations are not.

   Thus, for instance, f(2,1) = 1, f(2,2) = f(3,1) = 2 and f(3,2) = 16.
   f(3,2) is shown below:

   Find the sum of all f(m,n) such that f(m,n) ≤ 10^15.
p_281_pizza.gif
"""


def test_problem_282(answer):
    output = p282.problem282()
    expected_output = answer['Problem 282']
    assert output == expected_output


"""


For non-negative integers m, n, the Ackermann function A(m, n) is defined
   as follows:

   For example A(1, 0) = 2, A(2, 2) = 7 and A(3, 4) = 125.

   Find A(n, n) and give your answer mod 14^8.
p_282_formula.gif
"""


def test_problem_283(answer):
    output = p283.problem283()
    expected_output = answer['Problem 283']
    assert output == expected_output


"""


Consider the triangle with sides 6, 8 and 10. It can be seen that the
   perimeter and the area are both equal to 24. So the area/perimeter ratio
   is equal to 1.
   Consider also the triangle with sides 13, 14 and 15. The perimeter equals
   42 while the area is equal to 84. So for this triangle the area/perimeter
   ratio is equal to 2.

   Find the sum of the perimeters of all integer sided triangles for which
   the area/perimeter ratios are equal to positive integers not exceeding
   1000.
"""


def test_problem_284(answer):
    output = p284.problem284()
    expected_output = answer['Problem 284']
    assert output == expected_output


"""


The 3-digit number 376 in the decimal numbering system is an example of
   numbers with the special property that its square ends with the same
   digits: 376^2 = 141376. Let's call a number with this property a steady
   square.

   Steady squares can also be observed in other numbering systems. In the
   base 14 numbering system, the 3-digit number c37 is also a steady square:
   c37^2 = aa0c37, and the sum of its digits is c+3+7=18 in the same
   numbering system. The letters a, b, c and d are used for the 10, 11, 12
   and 13 digits respectively, in a manner similar to the hexadecimal
   numbering system.

   For 1 ≤ n ≤ 9, the sum of the digits of all the n-digit steady squares in
   the base 14 numbering system is 2d8 (582 decimal). Steady squares with
   leading 0's are not allowed.

   Find the sum of the digits of all the n-digit steady squares in the base
   14 numbering system for
   1 ≤ n ≤ 10000 (decimal) and give your answer in the base 14 system using
   lower case letters where necessary.
"""


def test_problem_285(answer):
    output = p285.problem285()
    expected_output = answer['Problem 285']
    assert output == expected_output


"""


Albert chooses a positive integer k, then two real numbers a, b are
   randomly chosen in the interval [0,1] with uniform distribution.
   The square root of the sum (k·a+1)^2 + (k·b+1)^2 is then computed and
   rounded to the nearest integer. If the result is equal to k, he scores k
   points; otherwise he scores nothing.

   For example, if k = 6, a = 0.2 and b = 0.85, then
   (k·a+1)^2 + (k·b+1)^2 = 42.05.
   The square root of 42.05 is 6.484... and when rounded to the nearest
   integer, it becomes 6.
   This is equal to k, so he scores 6 points.

   It can be shown that if he plays 10 turns with k = 1, k = 2, ..., k = 10,
   the expected value of his total score, rounded to five decimal places, is
   10.20914.

   If he plays 10^5 turns with k = 1, k = 2, k = 3, ..., k = 10^5, what is
   the expected value of his total score, rounded to five decimal places?
"""


def test_problem_286(answer):
    output = p286.problem286()
    expected_output = answer['Problem 286']
    assert output == expected_output


"""


Barbara is a mathematician and a basketball player. She has found that the
   probability of scoring a point when shooting from a distance x is exactly
   (1 - ^x/[q]), where q is a real constant greater than 50.

   During each practice run, she takes shots from distances x = 1, x = 2,
   ..., x = 50 and, according to her records, she has precisely a 2 % chance
   to score a total of exactly 20 points.

   Find q and give your answer rounded to 10 decimal places.
"""


@pytest.mark.skip(reason='slow')
def test_problem_287(answer):
    output = p287.problem287()
    expected_output = answer['Problem 287']
    assert output == expected_output


"""


The quadtree encoding allows us to describe a 2^N×2^N black and white
   image as a sequence of bits (0 and 1). Those sequences are to be read from
   left to right like this:

     • the first bit deals with the complete 2^N×2^N region;
     • "0" denotes a split:
       the current 2^n×2^n region is divided into 4 sub-regions of dimension
       2^n-1×2^n-1,
       the next bits contains the description of the top left, top right,
       bottom left and bottom right sub-regions - in that order;
     • "10" indicates that the current region contains only black pixels;
     • "11" indicates that the current region contains only white pixels.

   Consider the following 4×4 image (colored marks denote places where a
   split can occur):

   This image can be described by several sequences, for example
   :"001010101001011111011010101010", of length 30, or
   "0100101111101110", of length 16, which is the minimal sequence for this
   image.

   For a positive integer N, define D[N] as the 2^N×2^N image with the
   following coloring scheme:

     • the pixel with coordinates x = 0, y = 0 corresponds to the bottom left
       pixel,
     • if (x - 2^N-1)^2 + (y - 2^N-1)^2 ≤ 2^2N-2 then the pixel is black,
     • otherwise the pixel is white.

   What is the length of the minimal sequence describing D[24] ?
p_287_quadtree.gif
"""


def test_problem_288(answer):
    output = p288.problem288()
    expected_output = answer['Problem 288']
    assert output == expected_output


"""


For any prime p the number N(p,q) is defined byN(p,q) = ∑[n=0 to q]
   T[n]*p^n
   with T[n] generated by the following random number generator:

   S[0] = 290797
   S[n+1] = S[n]^2 mod 50515093
   T[n] = S[n] mod p

   Let Nfac(p,q) be the factorial of N(p,q).
   Let NF(p,q) be the number of factors p in Nfac(p,q).

   You are given that NF(3,10000) mod 3^20=624955285.

   Find NF(61,10^7) mod 61^10
"""


def test_problem_289(answer):
    output = p289.problem289()
    expected_output = answer['Problem 289']
    assert output == expected_output


"""


Let C(x,y) be a circle passing through the points (x, y), (x, y+1),
   (x+1, y) and (x+1, y+1).

   For positive integers m and n, let E(m,n) be a configuration which
   consists of the m·n circles:
   { C(x,y): 0 ≤ x < m, 0 ≤ y < n, x and y are integers }

   An Eulerian cycle on E(m,n) is a closed path that passes through each arc
   exactly once.
   Many such paths are possible on E(m,n), but we are only interested in
   those which are not self-crossing: A non-crossing path just touches itself
   at lattice points, but it never crosses itself.

   The image below shows E(3,3) and an example of an Eulerian non-crossing
   path.

   Let L(m,n) be the number of Eulerian non-crossing paths on E(m,n).
   For example, L(1,2) = 2, L(2,2) = 37 and L(3,3) = 104290.

   Find L(6,10) mod 10^10.
p_289_euler.gif
"""


def test_problem_290(answer):
    output = p290.problem290()
    expected_output = answer['Problem 290']
    assert output == expected_output


"""


How many integers 0 ≤ n < 10^18 have the property that the sum of the
   digits of n equals the sum of digits of 137n?
"""


def test_problem_291(answer):
    output = p291.problem291()
    expected_output = answer['Problem 291']
    assert output == expected_output


"""


A prime number p is called a Panaitopol prime if for some positive
   integers
   x and y.

   Find how many Panaitopol primes are less than 5×10^15.
p_291_formula.gif
"""


def test_problem_292(answer):
    output = p292.problem292()
    expected_output = answer['Problem 292']
    assert output == expected_output


"""


We shall define a pythagorean polygon to be a convex polygon with the
   following properties:

     • there are at least three vertices,
     • no three vertices are aligned,
     • each vertex has integer coordinates,
     • each edge has integer length.

   For a given integer n, define P(n) as the number of distinct pythagorean
   polygons for which the perimeter is ≤ n.
   Pythagorean polygons should be considered distinct as long as none is a
   translation of another.

   You are given that P(4) = 1, P(30) = 3655 and P(60) = 891045.
   Find P(120).
"""


def test_problem_293(answer):
    output = p293.problem293()
    expected_output = answer['Problem 293']
    assert output == expected_output


"""


An even positive integer N will be called admissible, if it is a power of
   2 or its distinct prime factors are consecutive primes.
   The first twelve admissible numbers are 2,4,6,8,12,16,18,24,30,32,36,48.

   If N is admissible, the smallest integer M > 1 such that N+M is prime,
   will be called the pseudo-Fortunate number for N.

   For example, N=630 is admissible since it is even and its distinct prime
   factors are the consecutive primes 2,3,5 and 7.
   The next prime number after 631 is 641; hence, the pseudo-Fortunate number
   for 630 is M=11.
   It can also be seen that the pseudo-Fortunate number for 16 is 3.

   Find the sum of all distinct pseudo-Fortunate numbers for admissible
   numbers N less than 10^9.
"""


def test_problem_294(answer):
    output = p294.problem294()
    expected_output = answer['Problem 294']
    assert output == expected_output


"""


For a positive integer k, define d(k) as the sum of the digits of k in its
   usual decimal representation.Thus d(42) = 4+2 = 6.

   For a positive integer n, define S(n) as the number of positive integers k
   < 10^n with the following properties :

     • k is divisible by 23 and
     • d(k) = 23.

   You are given that S(9) = 263626 and S(42) = 6377168878570056.

   Find S(11^12) and give your answer mod 10^9.
"""


def test_problem_295(answer):
    output = p295.problem295()
    expected_output = answer['Problem 295']
    assert output == expected_output


"""


We call the convex area enclosed by two circles a lenticular hole if:

     • The centres of both circles are on lattice points.
     • The two circles intersect at two distinct lattice points.
     • The interior of the convex area enclosed by both circles does not
       contain any lattice points.

   Consider the circles:
   C[0]: x^2+y^2=25
   C[1]: (x+4)^2+(y-4)^2=1
   C[2]: (x-12)^2+(y-4)^2=65

   The circles C[0], C[1] and C[2] are drawn in the picture below.

   C[0] and C[1] form a lenticular hole, as well as C[0] and C[2].

   We call an ordered pair of positive real numbers (r[1], r[2]) a lenticular
   pair if there exist two circles with radii r[1] and r[2] that form a
   lenticular hole.We can verify that (1, 5) and (5, √65) are the lenticular
   pairs of the example above.

   Let L(N) be the number of distinct lenticular pairs (r[1], r[2]) for which
   0 < r[1] ≤ r[2] ≤ N.
   We can verify that L(10) = 30 and L(100) = 3442.

   Find L(100 000).
"""


def test_problem_296(answer):
    output = p296.problem296()
    expected_output = answer['Problem 296']
    assert output == expected_output


"""


Given is an integer sided triangle ABC with BC ≤ AC ≤ AB.
   k is the angular bisector of angle ACB.
   m is the tangent at C to the circumscribed circle of ABC.
   n is a line parallel to m through B.
   The intersection of n and k is called E.

   How many triangles ABC with a perimeter not exceeding 100 000 exist such
   that BE has integral length?
"""


def test_problem_297(answer):
    output = p297.problem297()
    expected_output = answer['Problem 297']
    assert output == expected_output


"""


Each new term in the Fibonacci sequence is generated by adding the
   previous two terms.
   Starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21,
   34, 55, 89.

   Every positive integer can be uniquely written as a sum of nonconsecutive
   terms of the Fibonacci sequence. For example, 100 = 3 + 8 + 89.
   Such a sum is called the Zeckendorf representation of the number.

   For any integer n>0, let z(n) be the number of terms in the Zeckendorf
   representation of n.
   Thus, z(5) = 1, z(14) = 2, z(100) = 3 etc.
   Also, for 0<n<10^6, ∑ z(n) = 7894453.

   Find ∑ z(n) for 0<n<10^17.
"""


def test_problem_298(answer):
    output = p298.problem298()
    expected_output = answer['Problem 298']
    assert output == expected_output


"""


Larry and Robin play a memory game involving of a sequence of random
   numbers between 1 and 10, inclusive, that are called out one at a time.
   Each player can remember up to 5 previous numbers. When the called number
   is in a player's memory, that player is awarded a point. If it's not, the
   player adds the called number to his memory, removing another number if
   his memory is full.

   Both players start with empty memories. Both players always add new missed
   numbers to their memory but use a different strategy in deciding which
   number to remove:
   Larry's strategy is to remove the number that hasn't been called in the
   longest time.
   Robin's strategy is to remove the number that's been in the memory the
   longest time.

   Example game:

               Turn Called  Larry's   Larry's  Robin's   Robin's
                    number   memory    score    memory    score
               1    1      1          0       1          0
               2    2      1,2        0       1,2        0
               3    4      1,2,4      0       1,2,4      0
               4    6      1,2,4,6    0       1,2,4,6    0
               5    1      1,2,4,6    1       1,2,4,6    1
               6    8      1,2,4,6,8  1       1,2,4,6,8  1
               7    10     1,4,6,8,10 1       2,4,6,8,10 1
               8    2      1,2,6,8,10 1       2,4,6,8,10 2
               9    4      1,2,4,8,10 1       2,4,6,8,10 3
               10   1      1,2,4,8,10 2       1,4,6,8,10 3

   Denoting Larry's score by L and Robin's score by R, what is the expected
   value of |L-R| after 50 turns? Give your answer rounded to eight decimal
   places using the format x.xxxxxxxx .
"""


def test_problem_299(answer):
    output = p299.problem299()
    expected_output = answer['Problem 299']
    assert output == expected_output


"""


Four points with integer coordinates are selected:
   A(a, 0), B(b, 0), C(0, c) and D(0, d), with 0 < a < b and 0 < c < d.
   Point P, also with integer coordinates, is chosen on the line AC so that
   the three triangles ABP, CDP and BDP are all similar.

   It is easy to prove that the three triangles can be similar, only if a=c.

   So, given that a=c, we are looking for triplets (a,b,d) such that at least
   one point P (with integer coordinates) exists on AC, making the three
   triangles ABP, CDP and BDP all similar.

   For example, if (a,b,d)=(2,3,4), it can be easily verified that point
   P(1,1) satisfies the above condition. Note that the triplets (2,3,4) and
   (2,4,3) are considered as distinct, although point P(1,1) is common for
   both.

   If b+d < 100, there are 92 distinct triplets (a,b,d) such that point P
   exists.
   If b+d < 100 000, there are 320471 distinct triplets (a,b,d) such that
   point P exists.

   If b+d < 100 000 000, how many distinct triplets (a,b,d) are there such
   that point P exists?
p_299_ThreeSimTri.gif
"""


def test_problem_300(answer):
    output = p300.problem300()
    expected_output = answer['Problem 300']
    assert output == expected_output


"""


In a very simplified form, we can consider proteins as strings consisting
   of hydrophobic (H) and polar (P) elements, e.g. HHPPHHHPHHPH.
   For this 
Problem, the orientation of a protein is important; e.g. HPP is
   considered distinct from PPH. Thus, there are 2^n distinct proteins
   consisting of n elements.

   When one encounters these strings in nature, they are always folded in
   such a way that the number of H-H contact points is as large as possible,
   since this is energetically advantageous.
   As a result, the H-elements tend to accumulate in the inner part, with the
   P-elements on the outside.
   Natural proteins are folded in three dimensions of course, but we will
   only consider protein folding in two dimensions.

   The figure below shows two possible ways that our example protein could be
   folded (H-H contact points are shown with red dots).

   The folding on the left has only six H-H contact points, thus it would
   never occur naturally.
   On the other hand, the folding on the right has nine H-H contact points,
   which is optimal for this string.

   Assuming that H and P elements are equally likely to occur in any position
   along the string, the average number of H-H contact points in an optimal
   folding of a random protein string of length 8 turns out to be
   850 / 2^8=3.3203125.

   What is the average number of H-H contact points in an optimal folding of
   a random protein string of length 15?
   Give your answer using as many decimal places as necessary for an exact
   result.
p_300_protein.gif
"""


def test_problem_302(answer):
    output = p302.problem302()
    expected_output = answer['Problem 302']
    assert output == expected_output


"""


A positive integer n is powerful if p^2 is a divisor of n for every prime
   factor p in n.

   A positive integer n is a perfect power if n can be expressed as a power
   of another positive integer.

   A positive integer n is an Achilles number if n is powerful but not a
   perfect power. For example, 864 and 1800 are Achilles numbers: 864 =
   2^5·3^3 and 1800 = 2^3·3^2·5^2.

   We shall call a positive integer S a Strong Achilles number if both S and
   φ(S) are Achilles numbers.^1
   For example, 864 is a Strong Achilles number: φ(864) = 288 = 2^5·3^2.
   However, 1800 isn't a Strong Achilles number because: φ(1800) = 480 =
   2^5·3^1·5^1.

   There are 7 Strong Achilles numbers below 10^4 and 656 below 10^8.

   How many Strong Achilles numbers are there below 10^18?

   ^1 φ denotes Euler's totient function.
"""


@pytest.mark.skip(reason='slow')
def test_problem_303(answer):
    output = p303.problem303()
    expected_output = answer['Problem 303']
    assert output == expected_output


"""


For a positive integer n, define f(n) as the least positive multiple of n
   that, written in base 10, uses only digits ≤ 2.

   Thus f(2)=2, f(3)=12, f(7)=21, f(42)=210, f(89)=1121222.

   Also, .

   Find .
"""


def test_problem_304(answer):
    output = p304.problem304()
    expected_output = answer['Problem 304']
    assert output == expected_output


"""


For any positive integer n the function next_prime(n) returns the smallest
   prime p
   such that p>n.

   The sequence a(n) is defined by:
   a(1)=next_prime(10^14) and a(n)=next_prime(a(n-1)) for n>1.

   The fibonacci sequence f(n) is defined by:f(0)=0, f(1)=1 and
   f(n)=f(n-1)+f(n-2) for n>1.

   The sequence b(n) is defined as f(a(n)).

   Find ∑b(n) for 1≤n≤100 000. Give your answer mod 1234567891011.
"""


def test_problem_305(answer):
    output = p305.problem305()
    expected_output = answer['Problem 305']
    assert output == expected_output


"""


Let's call S the (infinite) string that is made by concatenating the
   consecutive positive integers (starting from 1) written down in base 10.
   Thus, S = 1234567891011121314151617181920212223242...

   It's easy to see that any number will show up an infinite number of times
   in S.

   Let's call f(n) the starting position of the n^th occurrence of n in S.
   For example, f(1)=1, f(5)=81, f(12)=271 and f(7780)=111111365.

   Find ∑f(3^k) for 1≤k≤13.
"""


def test_problem_306(answer):
    output = p306.problem306()
    expected_output = answer['Problem 306']
    assert output == expected_output


"""


The following game is a classic example of Combinatorial Game Theory:

   Two players start with a strip of n white squares and they take alternate
   turns.
   On each turn, a player picks two contiguous white squares and paints them
   black.
   The first player who cannot make a move loses.

     • If n = 1, there are no valid moves, so the first player loses
       automatically.
     • If n = 2, there is only one valid move, after which the second player
       loses.
     • If n = 3, there are two valid moves, but both leave a situation where
       the second player loses.
     • If n = 4, there are three valid moves for the first player; she can
       win the game by painting the two middle squares.
     • If n = 5, there are four valid moves for the first player (shown below
       in red); but no matter what she does, the second player (blue) wins.

   So, for 1 ≤ n ≤ 5, there are 3 values of n for which the first player can
   force a win.
   Similarly, for 1 ≤ n ≤ 50, there are 40 values of n for which the first
   player can force a win.

   For 1 ≤ n ≤ 1 000 000, how many values of n are there for which the first
   player can force a win?
p_306_pstrip.gif
"""


def test_problem_307(answer):
    output = p307.problem307()
    expected_output = answer['Problem 307']
    assert output == expected_output


"""


k defects are randomly distributed amongst n integrated-circuit chips
   produced by a factory (any number of defects may be found on a chip and
   each defect is independent of the other defects).

   Let p(k,n) represent the probability that there is a chip with at least 3
   defects.
   For instance p(3,7) ≈ 0.0204081633.

   Find p(20 000, 1 000 000) and give your answer rounded to 10 decimal
   places in the form 0.abcdefghij
"""


def test_problem_308(answer):
    output = p308.problem308()
    expected_output = answer['Problem 308']
    assert output == expected_output


"""


A program written in the programming language Fractran consists of a list
   of fractions.

   The internal state of the Fractran Virtual Machine is a positive integer,
   which is initially set to a seed value. Each iteration of a Fractran
   program multiplies the state integer by the first fraction in the list
   which will leave it an integer.

   For example, one of the Fractran programs that John Horton Conway wrote
   for prime-generation consists of the following 14 fractions:

   17 , 78 , 19 , 23 , 29 , 77 , 95 , 77 , 1  , 11 , 13 , 15 , 1 , 55 .
   91   85   51   38   33   29   23   19   17   13   11   2    7   1

   Starting with the seed integer 2, successive iterations of the program
   produce the sequence:
   15, 825, 725, 1925, 2275, 425, ..., 68, 4, 30, ..., 136, 8, 60, ..., 544,
   32, 240, ...

   The powers of 2 that appear in this sequence are 2^2, 2^3, 2^5, ...
   It can be shown that all the powers of 2 in this sequence have prime
   exponents and that all the primes appear as exponents of powers of 2, in
   proper order!

   If someone uses the above Fractran program to solve Project Euler 
Problem
   7 (find the 10001^st prime), how many iterations would be needed until the
   program produces 2^10001st prime ?
"""


def test_problem_309(answer):
    output = p309.problem309()
    expected_output = answer['Problem 309']
    assert output == expected_output


"""


In the classic "Crossing Ladders" 
Problem, we are given the lengths x and
   y of two ladders resting on the opposite walls of a narrow, level street.
   We are also given the height h above the street where the two ladders
   cross and we are asked to find the width of the street (w).

   Here, we are only concerned with instances where all four variables are
   positive integers.
   For example, if x = 70, y = 119 and h = 30, we can calculate that w = 56.

   In fact, for integer values x, y, h and 0 < x < y < 200, there are only
   five triplets (x,y,h) producing integer solutions for w:
   (70, 119, 30), (74, 182, 21), (87, 105, 35), (100, 116, 35) and (119, 175,
   40).

   For integer values x, y, h and 0 < x < y < 1 000 000, how many triplets
   (x,y,h) produce integer solutions for w?
p_309_ladders.gif
"""


def test_problem_310(answer):
    output = p310.problem310()
    expected_output = answer['Problem 310']
    assert output == expected_output


"""


Alice and Bob play the game Nim Square.
   Nim Square is just like ordinary three-heap normal play Nim, but the
   players may only remove a square number of stones from a heap.
   The number of stones in the three heaps is represented by the ordered
   triple (a,b,c).
   If 0≤a≤b≤c≤29 then the number of losing positions for the next player is
   1160.

   Find the number of losing positions for the next player if 0≤a≤b≤c≤100
   000.
"""


def test_problem_311(answer):
    output = p311.problem311()
    expected_output = answer['Problem 311']
    assert output == expected_output


"""


ABCD is a convex, integer sided quadrilateral with 1 ≤ AB < BC < CD < AD.
   BD has integer length. O is the midpoint of BD. AO has integer length.
   We'll call ABCD a biclinic integral quadrilateral if AO = CO ≤ BO = DO.

   For example, the following quadrilateral is a biclinic integral
   quadrilateral:
   AB = 19, BC = 29, CD = 37, AD = 43, BD = 48 and AO = CO = 23.

   Let B(N) be the number of distinct biclinic integral quadrilaterals ABCD
   that satisfy AB^2+BC^2+CD^2+AD^2 ≤ N.
   We can verify that B(10 000) = 49 and B(1 000 000) = 38239.

   Find B(10 000 000 000).
p_311_biclinic.gif
"""


def test_problem_312(answer):
    output = p312.problem312()
    expected_output = answer['Problem 312']
    assert output == expected_output


"""


- A Sierpiński graph of order-1 (S[1]) is an equilateral triangle.
   - S[n+1] is obtained from S[n] by positioning three copies of S[n] so that
   every pair of copies has one common corner.

   Let C(n) be the number of cycles that pass exactly once through all the
   vertices of S[n].
   For example, C(3) = 8 because eight such cycles can be drawn on S[3], as
   shown below:

   It can also be verified that :
   C(1) = C(2) = 1
   C(5) = 71328803586048
   C(10 000) mod 10^8 = 37652224
   C(10 000) mod 13^8 = 617720485

   Find C(C(C(10 000))) mod 13^8.
p_312_sierpinskyAt.gif
   p_312_sierpinsky8t.gif
"""


def test_problem_313(answer):
    output = p313.problem313()
    expected_output = answer['Problem 313']
    assert output == expected_output


"""


In a sliding game a counter may slide horizontally or vertically into an
   empty space. The objective of the game is to move the red counter from the
   top left corner of a grid to the bottom right corner; the space always
   starts in the bottom right corner. For example, the following sequence of
   pictures show how the game can be completed in five moves on a 2 by 2
   grid.

   Let S(m,n) represent the minimum number of moves to complete the game on
   an m by n grid. For example, it can be verified that S(5,4) = 25.

   There are exactly 5482 grids for which S(m,n) = p^2, where p < 100 is
   prime.

   How many grids does S(m,n) = p^2, where p < 10^6 is prime?
p_313_sliding_game_1.gif
   p_313_sliding_game_2.gif
"""


def test_problem_314(answer):
    output = p314.problem314()
    expected_output = answer['Problem 314']
    assert output == expected_output


"""


The moon has been opened up, and land can be obtained for free, but there
   is a catch. You have to build a wall around the land that you stake out,
   and building a wall on the moon is expensive. Every country has been
   allotted a 500 m by 500 m square area, but they will possess only that
   area which they wall in. 251001 posts have been placed in a rectangular
   grid with 1 meter spacing. The wall must be a closed series of straight
   lines, each line running from post to post.

   The bigger countries of course have built a 2000 m wall enclosing the
   entire 250 000 m^2 area. The [1]Duchy of Grand Fenwick, has a tighter
   budget, and has asked you (their Royal Programmer) to compute what shape
   would get best maximum enclosed-area/wall-length ratio.

   You have done some preliminary calculations on a sheet of paper.For a 2000
   meter wall enclosing the 250 000 m^2 area theenclosed-area/wall-length
   ratio is 125.
   Although not allowed , but to get an idea if this is anything better: if
   you place a circle inside the square area touching the four sides the area
   will be equal to π*250^2 m^2 and the perimeter will be π*500 m, so the
   enclosed-area/wall-length ratio will also be 125.

   However, if you cut off from the square four triangles with sides 75 m, 75
   m and 75√2 m the total area becomes 238750 m^2 and the perimeter becomes
   1400+300√2 m. So this gives an enclosed-area/wall-length ratio of 130.87,
   which is significantly better.

   Find the maximum enclosed-area/wall-length ratio.
   Give your answer rounded to 8 places behind the decimal point in the form
   abc.defghijk.
Visible links
   1. http://en.wikipedia.org/wiki/Grand_Fenwick
   p_314_landgrab.gif
"""


@pytest.mark.skip(reason='slow')
def test_problem_315(answer):
    output = p315.problem315()
    expected_output = answer['Problem 315']
    assert output == expected_output


"""


Sam and Max are asked to transform two digital clocks into two "digital
   root" clocks.
   A digital root clock is a digital clock that calculates digital roots step
   by step.

   When a clock is fed a number, it will show it and then it will start the
   calculation, showing all the intermediate values until it gets to the
   result.
   For example, if the clock is fed the number 137, it will show: "137" →
   "11" → "2" and then it will go black, waiting for the next number.

   Every digital number consists of some light segments: three horizontal
   (top, middle, bottom) and four vertical (top-left, top-right, bottom-left,
   bottom-right).
   Number "1" is made of vertical top-right and bottom-right, number "4" is
   made by middle horizontal and vertical top-left, top-right and
   bottom-right. Number "8" lights them all.

   The clocks consume energy only when segments are turned on/off.
   To turn on a "2" will cost 5 transitions, while a "7" will cost only 4
   transitions.

   Sam and Max built two different clocks.

   Sam's clock is fed e.g. number 137: the clock shows "137", then the panel
   is turned off, then the next number ("11") is turned on, then the panel is
   turned off again and finally the last number ("2") is turned on and, after
   some time, off.
   For the example, with number 137, Sam's clock requires:

   "137" : (2 + 5 + 4) × 2 = 22 transitions ("137" on/off).
   "11"  : (2 + 2) × 2 = 8 transitions ("11" on/off).
   "2"   : (5) × 2 = 10 transitions ("2" on/off).

   For a grand total of 40 transitions.

   Max's clock works differently. Instead of turning off the whole panel, it
   is smart enough to turn off only those segments that won't be needed for
   the next number.
   For number 137, Max's clock requires:

           2 + 5 + 4 = 11 transitions ("137" on)
   "137" : 7 transitions (to turn off the segments that are not needed for
           number "11").
           0 transitions (number "11" is already turned on correctly)
   "11"  : 3 transitions (to turn off the first "1" and the bottom part of
           the second "1";
           the top part is common with number "2").
           4 tansitions (to turn on the remaining segments in order to get a
   "2"   : "2")
           5 transitions (to turn off number "2").

   For a grand total of 30 transitions.

   Of course, Max's clock consumes less power than Sam's one.
   The two clocks are fed all the prime numbers between A = 10^7 and B =
   2×10^7.
   Find the difference between the total number of transitions needed by
   Sam's clock and that needed by Max's one.
p_315_clocks.gif
"""


def test_problem_316(answer):
    output = p316.problem316()
    expected_output = answer['Problem 316']
    assert output == expected_output


"""


Let p = p[1] p[2] p[3] ... be an infinite sequence of random digits,
   selected from {0,1,2,3,4,5,6,7,8,9} with equal probability.
   It can be seen that p corresponds to the real number 0.p[1] p[2] p[3] ....
   It can also be seen that choosing a random real number from the interval
   [0,1) is equivalent to choosing an infinite sequence of random digits
   selected from {0,1,2,3,4,5,6,7,8,9} with equal probability.

   For any positive integer n with d decimal digits, let k be the smallest
   index such that
   p[k, ]p[k+1], ...p[k+d-1] are the decimal digits of n, in the same order.
   Also, let g(n) be the expected value of k; it can be proven that g(n) is
   always finite and, interestingly, always an integer number.

   For example, if n = 535, then
   for p = 31415926535897...., we get k = 9
   for p = 355287143650049560000490848764084685354..., we get k = 36
   etc and we find that g(535) = 1008.

   Given that , find

   Note: represents the floor function.

   p_316_decexp001.gif
   p_316_decexp002.gif
   p_316_decexp3.gif
"""


def test_problem_317(answer):
    output = p317.problem317()
    expected_output = answer['Problem 317']
    assert output == expected_output


"""


A firecracker explodes at a height of 100 m above level ground. It breaks
   into a large number of very small fragments, which move in every
   direction; all of them have the same initial velocity of 20 m/s.

   We assume that the fragments move without air resistance, in a uniform
   gravitational field with g=9.81 m/s^2.

   Find the volume (in m^3) of the region through which the fragments move
   before reaching the ground. Give your answer rounded to four decimal
   places.
"""


def test_problem_318(answer):
    output = p318.problem318()
    expected_output = answer['Problem 318']
    assert output == expected_output


"""


Consider the real number √2+√3.
   When we calculate the even powers of √2+√3we get:
   (√2+√3)^2 = 9.898979485566356...
   (√2+√3)^4 = 97.98979485566356...
   (√2+√3)^6 = 969.998969071069263...
   (√2+√3)^8 = 9601.99989585502907...
   (√2+√3)^10 = 95049.999989479221...
   (√2+√3)^12 = 940897.9999989371855...
   (√2+√3)^14 = 9313929.99999989263...
   (√2+√3)^16 = 92198401.99999998915...

   It looks like that the number of consecutive nines at the beginning of the
   fractional part of these powers is non-decreasing.
   In fact it can be proven that the fractional part of (√2+√3)^2n approaches
   1 for large n.

   Consider all real numbers of the form √p+√q with p and q positive integers
   and p<q, such that the fractional part of (√p+√q)^2n approaches 1 for
   large n.

   Let C(p,q,n) be the number of consecutive nines at the beginning of the
   fractional part of
   (√p+√q)^2n.

   Let N(p,q) be the minimal value of n such that C(p,q,n) ≥ 2011.

   Find ∑N(p,q) for p+q ≤ 2011.
"""


def test_problem_319(answer):
    output = p319.problem319()
    expected_output = answer['Problem 319']
    assert output == expected_output


"""


Let x[1], x[2],..., x[n] be a sequence of length n such that:

     • x[1] = 2
     • for all 1 < i ≤ n : x[i-1] < x[i]
     • for all i and j with 1 ≤ i, j ≤ n : (x[i]) ^ j < (x[j] + 1)^i

   There are only five such sequences of length 2, namely:{2,4}, {2,5},
   {2,6}, {2,7} and {2,8}.
   There are 293 such sequences of length 5; three examples are given below:
   {2,5,11,25,55}, {2,6,14,36,88}, {2,8,22,64,181}.

   Let t(n) denote the number of such sequences of length n.
   You are given that t(10) = 86195 and t(20) = 5227991891.

   Find t(10^10) and give your answer modulo 10^9.
"""


def test_problem_320(answer):
    output = p320.problem320()
    expected_output = answer['Problem 320']
    assert output == expected_output


"""


Let N(i) be the smallest integer n such that n! is divisible by
   (i!)^1234567890

   Let S(u)=∑N(i) for 10 ≤ i ≤ u.

   S(1000)=614538266565663.

   Find S(1 000 000) mod 10^18.
"""


def test_problem_321(answer):
    output = p321.problem321()
    expected_output = answer['Problem 321']
    assert output == expected_output


"""


A horizontal row comprising of 2n + 1 squares has n red counters placed at
   one end and n blue counters at the other end, being separated by a single
   empty square in the centre. For example, when n = 3.

   A counter can move from one square to the next (slide) or can jump over
   another counter (hop) as long as the square next to that counter is
   unoccupied.

   Let M(n) represent the minimum number of moves/actions to completely
   reverse the positions of the coloured counters; that is, move all the red
   counters to the right and all the blue counters to the left.

   It can be verified M(3) = 15, which also happens to be a triangle number.

   If we create a sequence based on the values of n for which M(n) is a
   triangle number then the first five terms would be:
   1, 3, 10, 22, and 63, and their sum would be 99.

   Find the sum of the first forty terms of this sequence.
p_321_swapping_counters_1.gif
   p_321_swapping_counters_2.gif
"""


def test_problem_322(answer):
    output = p322.problem322()
    expected_output = answer['Problem 322']
    assert output == expected_output


"""


Let T(m, n) be the number of the binomial coefficients ^iC[n] that are
   divisible by 10 for n ≤ i < m(i, m and n are positive integers).
   You are given that T(10^9, 10^7-10) = 989697000.

   Find T(10^18, 10^12-10).
"""


def test_problem_323(answer):
    output = p323.problem323()
    expected_output = answer['Problem 323']
    assert output == expected_output


"""


Let y[0], y[1], y[2],... be a sequence of random unsigned 32 bit integers
   (i.e. 0 ≤ y[i] < 2^32, every value equally likely).

   For the sequence x[i] the following recursion is given:

     • x[0] = 0 and
     • x[i] = x[i-1] | y[i-1], for i > 0. ( | is the bitwise-OR operator)

   It can be seen that eventually there will be an index N such that x[i] =
   2^32 -1 (a bit-pattern of all ones) for all i ≥ N.

   Find the expected value of N.
   Give your answer rounded to 10 digits after the decimal point.
"""


def test_problem_324(answer):
    output = p324.problem324()
    expected_output = answer['Problem 324']
    assert output == expected_output


"""


Let f(n) represent the number of ways one can fill a 3×3×n tower with
   blocks of 2×1×1.
   You're allowed to rotate the blocks in any way you like; however,
   rotations, reflections etc of the tower itself are counted as distinct.

   For example (with q = 100000007) :
   f(2) = 229,
   f(4) = 117805,
   f(10) mod q = 96149360,
   f(10^3) mod q = 24806056,
   f(10^6) mod q = 30808124.

   Find f(10^10000) mod 100000007.
"""


def test_problem_325(answer):
    output = p325.problem325()
    expected_output = answer['Problem 325']
    assert output == expected_output


"""


A game is played with two piles of stones and two players. At her turn, a
   player removes a number of stones from the larger pile. The number of
   stones she removes must be a positive multiple of the number of stones in
   the smaller pile.

   E.g., let the ordered pair(6,14) describe a configuration with 6 stones in
   the smaller pile and 14 stones in the larger pile, then the first player
   can remove 6 or 12 stones from the larger pile.

   The player taking all the stones from a pile wins the game.

   A winning configuration is one where the first player can force a win. For
   example, (1,5), (2,6) and (3,12) are winning configurations because the
   first player can immediately remove all stones in the second pile.

   A losing configuration is one where the second player can force a win, no
   matter what the first player does. For example, (2,3) and (3,4) are losing
   configurations: any legal move leaves a winning configuration for the
   second player.

   Define S(N) as the sum of (x[i]+y[i]) for all losing configurations
   (x[i],y[i]), 0 < x[i] < y[i] ≤ N. We can verify that S(10) = 211 and
   S(10^4) = 230312207313.

   Find S(10^16) mod 7^10.
"""


def test_problem_326(answer):
    output = p326.problem326()
    expected_output = answer['Problem 326']
    assert output == expected_output


"""


Let a[n] be a sequence recursively defined by: .

   So the first 10 elements of a[n] are: 1,1,0,3,0,3,5,4,1,9.

   Let f(N,M) represent the number of pairs (p,q) such that:

   It can be seen that f(10,10)=4 with the pairs (3,3), (5,5), (7,9) and
   (9,10).

   You are also given that f(10^4,10^3)=97158.

   Find f(10^12,10^6).
p_326_formula1.gif
   p_326_formula2.gif
"""


def test_problem_327(answer):
    output = p327.problem327()
    expected_output = answer['Problem 327']
    assert output == expected_output


"""


A series of three rooms are connected to each other by automatic doors.

   Each door is operated by a security card. Once you enter a room the door
   automatically closes and that security card cannot be used again. A
   machine at the start will dispense an unlimited number of cards, but each
   room (including the starting room) contains scanners and if they detect
   that you are holding more than three security cards or if they detect an
   unattended security card on the floor, then all the doors will become
   permanently locked. However, each room contains a box where you may safely
   store any number of security cards for use at a later stage.

   If you simply tried to travel through the rooms one at a time then as you
   entered room 3 you would have used all three cards and would be trapped in
   that room forever!

   However, if you make use of the storage boxes, then escape is possible.
   For example, you could enter room 1 using your first card, place one card
   in the storage box, and use your third card to exit the room back to the
   start. Then after collecting three more cards from the dispensing machine
   you could use one to enter room 1 and collect the card you placed in the
   box a moment ago. You now have three cards again and will be able to
   travel through the remaining three doors. This method allows you to travel
   through all three rooms using six security cards in total.

   It is possible to travel through six rooms using a total of 123 security
   cards while carrying a maximum of 3 cards.

   Let C be the maximum number of cards which can be carried at any time.

   Let R be the number of rooms to travel through.

   Let M(C,R) be the minimum number of cards required from the dispensing
   machine to travel through R rooms carrying up to a maximum of C cards at
   any time.

   For example, M(3,6)=123 and M(4,6)=23.
   And, ΣM(C,6)=146 for 3 ≤ C ≤ 4.

   You are given that ΣM(C,10)=10382 for 3 ≤ C ≤ 10.

   Find ΣM(C,30) for 3 ≤ C ≤ 40.
p_327_rooms_of_doom.gif
"""


def test_problem_328(answer):
    output = p328.problem328()
    expected_output = answer['Problem 328']
    assert output == expected_output


"""


We are trying to find a hidden number selected from the set of integers
   {1, 2, ..., n} by asking questions. Each number (question) we ask, has a
   cost equal to the number asked and we get one of three possible answers:

     • "Your guess is lower than the hidden number", or
     • "Yes, that's it!", or
     • "Your guess is higher than the hidden number".

   Given the value of n, an optimal strategy minimizes the total cost (i.e.
   the sum of all the questions asked) for the worst possible case. E.g.

   If n=3, the best we can do is obviously to ask the number "2". The answer
   will immediately lead us to find the hidden number (at a total cost = 2).

   If n=8, we might decide to use a "binary search" type of strategy: Our
   first question would be "4" and if the hidden number is higher than 4 we
   will need one or two additional questions.
   Let our second question be "6". If the hidden number is still higher than
   6, we will need a third question in order to discriminate between 7 and 8.
   Thus, our third question will be "7" and the total cost for this
   worst-case scenario will be 4+6+7=17.

   We can improve considerably the worst-case cost for n=8, by asking "5" as
   our first question.
   If we are told that the hidden number is higher than 5, our second
   question will be "7", then we'll know for certain what the hidden number
   is (for a total cost of 5+7=12).
   If we are told that the hidden number is lower than 5, our second question
   will be "3" and if the hidden number is lower than 3 our third question
   will be "1", giving a total cost of 5+3+1=9.
   Since 12>9, the worst-case cost for this strategy is 12. That's better
   than what we achieved previously with the "binary search" strategy; it is
   also better than or equal to any other strategy.
   So, in fact, we have just described an optimal strategy for n=8.

   Let C(n) be the worst-case cost achieved by an optimal strategy for n, as
   described above.
   Thus C(1) = 0, C(2) = 1, C(3) = 2 and C(8) = 12.
   Similarly, C(100) = 400 and C(n) = 17575.

   Find C(n).
p_328_sum1.gif
   p_328_sum2.gif
"""


@pytest.mark.skip(reason='slow')
def test_problem_329(answer):
    output = p329.problem329()
    expected_output = answer['Problem 329']
    assert output == expected_output


"""


Susan has a prime frog.
   Her frog is jumping around over 500 squares numbered 1 to 500.He can only
   jump one square to the left or to the right, with equal probability, and
   he cannot jump outside the range [1;500].
   (if it lands at either end, it automatically jumps to the only available
   square on the next move.)

   When he is on a square with a prime number on it, he croaks 'P' (PRIME)
   with probability 2/3 or 'N' (NOT PRIME) with probability 1/3 just before
   jumping to the next square.
   When he is on a square with a number on it that is not a prime he croaks
   'P' with probability 1/3 or 'N' with probability 2/3 just before jumping
   to the next square.

   Given that the frog's starting position is random with the same
   probability for every square, and given that she listens to his first 15
   croaks, what is the probability that she hears the sequence
   PPPPNNPPPNPPNPN?

   Give your answer as a fraction p/q in reduced form.
"""


def test_problem_330(answer):
    output = p330.problem330()
    expected_output = answer['Problem 330']
    assert output == expected_output


"""



   An infinite sequence of real numbers a(n) is defined for all integers n as
   follows:

   For example,

   a(0) = 1  + 1  + 1  + ... = e − 1
          1!   2!   3!

   a(1) = e − 1 + 1  + 1  + ... = 2e − 3
          1!      2!   3!

   a(2) = 2e − 3 + e − 1 + 1  + ... = 7 e − 6
          1!       2!      3!         2

   with e = 2.7182818... being Euler's constant.

   It can be shown that a(n) is of  A(n) e + B(n) for integers A(n) and B(n).
   the form                         n!

   For example a(10) = 328161643 e − 652694486 .
                       10!

   Find A(10^9) + B(10^9) and give your answer mod 77 777 777.
p_330_formula.gif
"""


def test_problem_332(answer):
    output = p332.problem332()
    expected_output = answer['Problem 332']
    assert output == expected_output


"""


A spherical triangle is a figure formed on the surface of a sphere by
   three great circular arcs intersecting pairwise in three vertices.

   Let C(r) be the sphere with the centre (0,0,0) and radius r.
   Let Z(r) be the set of points on the surface of C(r) with integer
   coordinates.
   Let T(r) be the set of spherical triangles with vertices in
   Z(r).Degenerate spherical triangles, formed by three points on the same
   great arc, are not included in T(r).
   Let A(r) be the area of the smallest spherical triangle in T(r).

   For example A(14) is 3.294040 rounded to six decimal places.

   Find A(r). Give your answer rounded to six decimal places.
p_332_spherical.jpg
   p_332_sum.gif
"""


def test_problem_333(answer):
    output = p333.problem333()
    expected_output = answer['Problem 333']
    assert output == expected_output


"""


All positive integers can be partitioned in such a way that each and every
   term of the partition can be expressed as 2^ix3^j, where i,j ≥ 0.

   Let's consider only those such partitions where none of the terms can
   divide any of the other terms.
   For example, the partition of 17 = 2 + 6 + 9 = (2^1x3^0 + 2^1x3^1 +
   2^0x3^2) would not be valid since 2 can divide 6. Neither would the
   partition 17 = 16 + 1 = (2^4x3^0 + 2^0x3^0) since 1 can divide 16. The
   only valid partition of 17 would be 8 + 9 = (2^3x3^0 + 2^0x3^2).

   Many integers have more than one valid partition, the first being 11
   having the following two partitions.
   11 = 2 + 9 = (2^1x3^0 + 2^0x3^2)
   11 = 8 + 3 = (2^3x3^0 + 2^0x3^1)

   Let's define P(n) as the number of valid partitions of n. For example,
   P(11) = 2.

   Let's consider only the prime integers q which would have a single valid
   partition such as P(17).

   The sum of the primes q <100 such that P(q)=1 equals 233.

   Find the sum of the primes q <1000000 such that P(q)=1.
"""


def test_problem_334(answer):
    output = p334.problem334()
    expected_output = answer['Problem 334']
    assert output == expected_output


"""


In Plato's heaven, there exist an infinite number of bowls in a straight
   line.
   Each bowl either contains some or none of a finite number of beans.
   A child plays a game, which allows only one kind of move: removing two
   beans from any bowl, and putting one in each of the two adjacent bowls.
   The game ends when each bowl contains either one or no beans.

   For example, consider two adjacent bowls containing 2 and 3 beans
   respectively, all other bowls being empty. The following eight moves will
   finish the game:

   You are given the following sequences:

   t[0] = 123456.

            t[i-1] ,         if t[i-1] is even
   t[i] =   2
            t[i-1]   926252, if t[i-1] is odd
            2
           where ⌊x⌋ is the floor function
           and is the bitwise XOR operator.

   b[i] = ( t[i] mod 2^11) + 1.

   The first two terms of the last sequence are b[1] = 289 and b[2] = 145.
   If we start with b[1] and b[2] beans in two adjacent bowls, 3419100 moves
   would be required to finish the game.

   Consider now 1500 adjacent bowls containing b[1], b[2],..., b[1500] beans
   respectively, all other bowls being empty. Find how many moves it takes
   before the game ends.
p_334_beans.gif
   p_334_cases.gif
   p_334_lfloor.gif
   p_334_rfloor.gif
   p_334_oplus.gif
"""


def test_problem_335(answer):
    output = p335.problem335()
    expected_output = answer['Problem 335']
    assert output == expected_output


"""


Whenever Peter feels bored, he places some bowls, containing one bean
   each, in a circle. After this, he takes all the beans out of a certain
   bowl and drops them one by one in the bowls going clockwise. He repeats
   this, starting from the bowl he dropped the last bean in, until the
   initial situation appears again. For example with 5 bowls he acts as
   follows:

   So with 5 bowls it takes Peter 15 moves to return to the initial
   situation.

   Let M(x) represent the number of moves required to return to the initial
   situation, starting with x bowls. Thus, M(5) = 15. It can also be verified
   that M(100) = 10920.

   Find M(2^k+1). Give your answer modulo 7^9.
p_335_mancala.gif
   p_335_sum.gif
"""


def test_problem_336(answer):
    output = p336.problem336()
    expected_output = answer['Problem 336']
    assert output == expected_output


"""


A train is used to transport four carriages in the order: ABCD. However,
   sometimes when the train arrives to collect the carriages they are not in
   the correct order.
   To rearrange the carriages they are all shunted on to a large rotating
   turntable. After the carriages are uncoupled at a specific point the train
   moves off the turntable pulling the carriages still attached with it. The
   remaining carriages are rotated 180 degrees. All of the carriages are then
   rejoined and this process is repeated as often as necessary in order to
   obtain the least number of uses of the turntable.
   Some arrangements, such as ADCB, can be solved easily: the carriages are
   separated between A and D, and after DCB are rotated the correct order has
   been achieved.

   However, Simple Simon, the train driver, is not known for his efficiency,
   so he always solves the 
Problem by initially getting carriage A in the
   correct place, then carriage B, and so on.

   Using four carriages, the worst possible arrangements for Simon, which we
   shall call maximix arrangements, are DACB and DBAC; each requiring him
   five rotations (although, using the most efficient approach, they could be
   solved using just three rotations). The process he uses for DACB is shown
   below.

   It can be verified that there are 24 maximix arrangements for six
   carriages, of which the tenth lexicographic maximix arrangement is DFAECB.

   Find the 2011^th lexicographic maximix arrangement for eleven carriages.
p_336_maximix.gif
"""


def test_problem_337(answer):
    output = p337.problem337()
    expected_output = answer['Problem 337']
    assert output == expected_output


"""


Let {a[1], a[2],..., a[n]} be an integer sequence of length n such that:

     • a[1] = 6
     • for all 1 ≤ i < n : φ(a[i]) < φ(a[i+1]) < a[i] < a[i+1] ^1

   Let S(N) be the number of such sequences with a[n] ≤ N.
   For example, S(10) = 4: {6}, {6, 8}, {6, 8, 9} and {6, 10}.
   We can verify that S(100) = 482073668 and S(10 000) mod 10^8 = 73808307.

   Find S(20 000 000) mod 10^8.

   ^1 φ denotes Euler's totient function.
"""


def test_problem_338(answer):
    output = p338.problem338()
    expected_output = answer['Problem 338']
    assert output == expected_output


"""


A rectangular sheet of grid paper with integer dimensions w × h is given.
   Its grid spacing is 1.
   When we cut the sheet along the grid lines into two pieces and rearrange
   those pieces without overlap, we can make new rectangles with different
   dimensions.

   For example, from a sheet with dimensions 9 × 4 , we can make rectangles
   with dimensions 18 × 2, 12 × 3 and 6 × 6 by cutting and rearranging as
   below:

   Similarly, from a sheet with dimensions 9 × 8 , we can make rectangles
   with dimensions 18 × 4 and 12 × 6 .

   For a pair w and h, let F(w,h) be the number of distinct rectangles that
   can be made from a sheet with dimensions w × h .
   For example, F(2,1) = 0, F(2,2) = 1, F(9,4) = 3 and F(9,8) = 2.
   Note that rectangles congruent to the initial one are not counted in
   F(w,h).
   Note also that rectangles with dimensions w × h and dimensions h × w are
   not considered distinct.

   For an integer N, let G(N) be the sum of F(w,h) for all pairs w and h
   which satisfy 0 < h ≤ w ≤ N.
   We can verify that G(10) = 55, G(10^3) = 971745 and G(10^5) = 9992617687.

   Find G(10^12). Give your answer modulo 10^8.
p_338_gridpaper.gif
"""


def test_problem_339(answer):
    output = p339.problem339()
    expected_output = answer['Problem 339']
    assert output == expected_output


"""


"And he came towards a valley, through which ran a river; and the borders
   of the valley were wooded, and on each side of the river were level
   meadows. And on one side of the river he saw a flock of white sheep, and
   on the other a flock of black sheep. And whenever one of the white sheep
   bleated, one of the black sheep would cross over and become white; and
   when one of the black sheep bleated, one of the white sheep would cross
   over and become black."
   [1]en.wikisource.org

   Initially each flock consists of n sheep. Each sheep (regardless of
   colour) is equally likely to be the next sheep to bleat. After a sheep has
   bleated and a sheep from the other flock has crossed over, Peredur may
   remove a number of white sheep in order to maximize the expected final
   number of black sheep. Let E(n) be the expected final number of black
   sheep if Peredur uses an optimal strategy.

   You are given that E(5) = 6.871346 rounded to 6 places behind the decimal
   point.
   Find E(10 000) and give your answer rounded to 6 places behind the decimal
   point.
Visible links
   1. http://en.wikisource.org/wiki/The_Mabinogion/Peredur_the_Son_of_Evrawc
"""


def test_problem_340(answer):
    output = p340.problem340()
    expected_output = answer['Problem 340']
    assert output == expected_output


"""


For fixed integers a, b, c, define the crazy function F(n) as follows:
   F(n) = n - c for all n > b
   F(n) = F(a + F(a + F(a + F(a + n)))) for all n ≤ b.

   Also, define S(a, b, c) = .

   For example, if a = 50, b = 2000 and c = 40, then F(0) = 3240 and F(2000)
   = 2040.
   Also, S(50, 2000, 40) = 5204240.

   Find the last 9 digits of S(21^7, 7^21, 12^7).
p_340_formula.gif
"""


def test_problem_341(answer):
    output = p341.problem341()
    expected_output = answer['Problem 341']
    assert output == expected_output


"""


The Golomb's self-describing sequence {G(n)} is the only nondecreasing
   sequence of natural numbers such that n appears exactly G(n) times in the
   sequence. The values of G(n) for the first few n are

           n     1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  …
           G(n)  1  2  2  3  3  4  4  4  5  5   5   6   6   6   6   …

   You are given that G(10^3) = 86, G(10^6) = 6137.
   You are also given that ΣG(n^3) = 153506976 for 1 ≤ n < 10^3.

   Find ΣG(n^3) for 1 ≤ n < 10^6.
"""


def test_problem_342(answer):
    output = p342.problem342()
    expected_output = answer['Problem 342']
    assert output == expected_output


"""


Consider the number 50.
   50^2 = 2500 = 2^2 × 5^4, so φ(2500) = 2 × 4 × 5^3 = 8 × 5^3 = 2^3 × 5^3.
   ^1
   So 2500 is a square and φ(2500) is a cube.

   Find the sum of all numbers n, 1 < n < 10^10 such that φ(n^2) is a cube.

   ^1 φ denotes Euler's totient function.
"""


def test_problem_343(answer):
    output = p343.problem343()
    expected_output = answer['Problem 343']
    assert output == expected_output


"""


For any positive integer k, a finite sequence a[i] of fractions x[i]/y[i]
   is defined by:
   a[1] = 1/k and
   a[i] = (x[i-1]+1)/(y[i-1]-1) reduced to lowest terms for i>1.
   When a[i] reaches some integer n, the sequence stops. (That is, when
   y[i]=1.)
   Define f(k) = n.
   For example, for k = 20:

   1/20 → 2/19 → 3/18 = 1/6 → 2/5 → 3/4 → 4/3 → 5/2 → 6/1 = 6

   So f(20) = 6.

   Also f(1) = 1, f(2) = 2, f(3) = 1 and Σf(k^3) = 118937 for 1 ≤ k ≤ 100.

   Find Σf(k^3) for 1 ≤ k ≤ 2×10^6.
"""


def test_problem_344(answer):
    output = p344.problem344()
    expected_output = answer['Problem 344']
    assert output == expected_output


"""


One variant of N.G. de Bruijn's silver dollar game can be described as
   follows:

   On a strip of squares a number of coins are placed, at most one coin per
   square. Only one coin, called the silver dollar, has any value. Two
   players take turns making moves. At each turn a player must make either a
   regular or a special move.

   A regular move consists of selecting one coin and moving it one or more
   squares to the left. The coin cannot move out of the strip or jump on or
   over another coin.

   Alternatively, the player can choose to make the special move of pocketing
   the leftmost coin rather than making a regular move. If no regular moves
   are possible, the player is forced to pocket the leftmost coin.

   The winner is the player who pockets the silver dollar.

   A winning configuration is an arrangement of coins on the strip where the
   first player can force a win no matter what the second player does.

   Let W(n,c) be the number of winning configurations for a strip of n
   squares, c worthless coins and one silver dollar.

   You are given that W(10,2) = 324 and W(100,10) = 1514704946113500.

   Find W(1 000 000, 100) modulo the semiprime 1000 036 000 099 (= 1 000 003
   · 1 000 033).
p_344_silverdollar.gif
"""


@pytest.mark.skip(reason='slow')
def test_problem_348(answer):
    output = p348.problem348()
    expected_output = answer['Problem 348']
    assert output == expected_output


"""


Many numbers can be expressed as the sum of a square and a cube. Some of
   them in more than one way.

   Consider the palindromic numbers that can be expressed as the sum of a
   square and a cube, both greater than 1, in exactly 4 different ways.
   For example, 5229225 is a palindromic number and it can be expressed in
   exactly 4 different ways:

   2285^2 + 20^3
   2223^2 + 66^3
   1810^2 + 125^3
   1197^2 + 156^3

   Find the sum of the five smallest such palindromic numbers.
"""


def test_problem_349(answer):
    output = p349.problem349()
    expected_output = answer['Problem 349']
    assert output == expected_output


"""


An ant moves on a regular grid of squares that are coloured either black
   or white.
   The ant is always oriented in one of the cardinal directions (left, right,
   up or down) and moves from square to adjacent square according to the
   following rules:
   - if it is on a black square, it flips the color of the square to white,
   rotates 90 degrees counterclockwise and moves forward one square.
   - if it is on a white square, it flips the color of the square to black,
   rotates 90 degrees clockwise and moves forward one square.

   Starting with a grid that is entirely white, how many squares are black
   after 10^18 moves of the ant?
"""


def test_problem_350(answer):
    output = p350.problem350()
    expected_output = answer['Problem 350']
    assert output == expected_output


"""


A list of size n is a sequence of n natural numbers.
   Examples are (2,4,6), (2,6,4), (10,6,15,6), and (11).

   The greatest common divisor, or gcd, of a list is the largest natural
   number that divides all entries of the list.
   Examples: gcd(2,6,4) = 2, gcd(10,6,15,6) = 1 and gcd(11) = 11.

   The least common multiple, or lcm, of a list is the smallest natural
   number divisible by each entry of the list.
   Examples: lcm(2,6,4) = 12, lcm(10,6,15,6) = 30 and lcm(11) = 11.

   Let f(G, L, N) be the number of lists of size N with gcd ≥ G and lcm ≤ L.
   For example:

   f(10, 100, 1) = 91.
   f(10, 100, 2) = 327.
   f(10, 100, 3) = 1135.
   f(10, 100, 1000) mod 101^4 = 3286053.

   Find f(10^6, 10^12, 10^18) mod 101^4.
"""


def test_problem_351(answer):
    output = p351.problem351()
    expected_output = answer['Problem 351']
    assert output == expected_output


"""


A hexagonal orchard of order n is a triangular lattice made up of points
   within a regular hexagon with side n. The following is an example of a
   hexagonal orchard of order 5:

   Highlighted in green are the points which are hidden from the center by a
   point closer to it. It can be seen that for a hexagonal orchard of order
   5, 30 points are hidden from the center.

   Let H(n) be the number of points hidden from the center in a hexagonal
   orchard of order n.

   H(5) = 30. H(10) = 138. H(1 000) = 1177848.

   Find H(100 000 000).
p_351_hexorchard.png
"""


def test_problem_352(answer):
    output = p352.problem352()
    expected_output = answer['Problem 352']
    assert output == expected_output


"""


Each one of the 25 sheep in a flock must be tested for a rare virus, known
   to affect 2% of the sheep population.An accurate and extremely sensitive
   PCR test exists for blood samples, producing a clear positive / negative
   result, but it is very time-consuming and expensive.

   Because of the high cost, the vet-in-charge suggests that instead of
   performing 25 separate tests, the following procedure can be used instead:

   The sheep are split into 5 groups of 5 sheep in each group. For each
   group, the 5 samples are mixed together and a single test is performed.
   Then,

     • If the result is negative, all the sheep in that group are deemed to
       be virus-free.
     • If the result is positive, 5 additional tests will be performed (a
       separate test for each animal) to determine the affected
       individual(s).

   Since the probability of infection for any specific animal is only 0.02,
   the first test (on the pooled samples) for each group will be:

     • Negative (and no more tests needed) with probability 0.98^5 =
       0.9039207968.
     • Positive (5 additional tests needed) with probability 1 - 0.9039207968
       = 0.0960792032.

   Thus, the expected number of tests for each group is 1 + 0.0960792032 × 5
   = 1.480396016.
   Consequently, all 5 groups can be screened using an average of only
   1.480396016 × 5 = 7.40198008 tests, which represents a huge saving of more
   than 70% !

   Although the scheme we have just described seems to be very efficient, it
   can still be improved considerably (always assuming that the test is
   sufficiently sensitive and that there are no adverse effects caused by
   mixing different samples). E.g.:

     • We may start by running a test on a mixture of all the 25 samples. It
       can be verified that in about 60.35% of the cases this test will be
       negative, thus no more tests will be needed. Further testing will only
       be required for the remaining 39.65% of the cases.
     • If we know that at least one animal in a group of 5 is infected and
       the first 4 individual tests come out negative, there is no need to
       run a test on the fifth animal (we know that it must be infected).
     • We can try a different number of groups / different number of animals
       in each group, adjusting those numbers at each level so that the total
       expected number of tests will be minimised.

   To simplify the very wide range of possibilities, there is one restriction
   we place when devising the most cost-efficient testing scheme: whenever we
   start with a mixed sample, all the sheep contributing to that sample must
   be fully screened (i.e. a verdict of infected / virus-free must be reached
   for all of them) before we start examining any other animals.

   For the current example, it turns out that the most cost-efficient testing
   scheme (we'll call it the optimal strategy) requires an average of just
   4.155452 tests!

   Using the optimal strategy, let T(s,p) represent the average number of
   tests needed to screen a flock of s sheep for a virus having probability p
   to be present in any individual.
   Thus, rounded to six decimal places, T(25, 0.02) = 4.155452 and T(25,
   0.10) = 12.702124.

   Find ΣT(10000, p) for p=0.01, 0.02, 0.03, ... 0.50.
   Give your answer rounded to six decimal places.
"""


def test_problem_353(answer):
    output = p353.problem353()
    expected_output = answer['Problem 353']
    assert output == expected_output


"""


A moon could be described by the sphere C(r) with centre (0,0,0) and
   radius r.

   There are stations on the moon at the points on the surface of C(r) with
   integer coordinates. The station at (0,0,r) is called North Pole station,
   the station at (0,0,-r) is called South Pole station.

   All stations are connected with each other via the shortest road on the
   great arc through the stations. A journey between two stations is risky.
   If d is the length of the road between two stations, (d/(π r))^2 is a
   measure for the risk of the journey (let us call it the risk of the road).
   If the journey includes more than two stations, the risk of the journey is
   the sum of risks of the used roads.

   A direct journey from the North Pole station to the South Pole station has
   the length πr and risk 1. The journey from the North Pole station to the
   South Pole station via (0,r,0) has the same length, but a smaller risk:
   (½πr/(πr))^2+(½πr/(πr))^2=0.5.

   The minimal risk of a journey from the North Pole station to the South
   Pole station on C(r) is M(r).

   You are given that M(7)=0.1784943998 rounded to 10 digits behind the
   decimal point.

   Find ∑M(2^n-1) for 1≤n≤15.

   Give your answer rounded to 10 digits behind the decimal point in the form
   a.bcdefghijk.
"""


def test_problem_354(answer):
    output = p354.problem354()
    expected_output = answer['Problem 354']
    assert output == expected_output


"""


Consider a honey bee's honeycomb where each cell is a perfect regular
   hexagon with side length 1.

   One particular cell is occupied by the queen bee.
   For a positive real number L, let B(L) count the cells with distance L
   from the queen bee cell (all distances are measured from centre to
   centre); you may assume that the honeycomb is large enough to accommodate
   for any distance we wish to consider.
   For example, B(√3) = 6, B(√21) = 12 and B(111 111 111) = 54.

   Find the number of L ≤ 5·10^11 such that B(L) = 450.
p_354_bee_honeycomb.png
"""


def test_problem_355(answer):
    output = p355.problem355()
    expected_output = answer['Problem 355']
    assert output == expected_output


"""


Define Co(n) to be the maximal possible sum of a set of mutually co-prime
   elements from {1, 2, ..., n}.
   For example Co(10) is 30 and hits that maximum on the subset
   {1, 5, 7, 8, 9}.

   You are given that Co(30) = 193 and Co(100) = 1356.

   Find Co(200000).
"""


def test_problem_356(answer):
    output = p356.problem356()
    expected_output = answer['Problem 356']
    assert output == expected_output


"""


Let a[n] be the largest real root of a polynomial g(x) = x^3 - 2^n·x^2 +
   n.
   For example, a[2] = 3.86619826...

   Find the last eight digits of.

   Note: represents the floor function.
p_356_cubicpoly1.gif
   p_356_cubicpoly2.gif
"""


def test_problem_358(answer):
    output = p358.problem358()
    expected_output = answer['Problem 358']
    assert output == expected_output


"""


A cyclic number with n digits has a very interesting property:
   When it is multiplied by 1, 2, 3, 4, ... n, all the products have exactly
   the same digits, in the same order, but rotated in a circular fashion!

   The smallest cyclic number is the 6-digit number 142857 :
   142857 × 1 = 142857
   142857 × 2 = 285714
   142857 × 3 = 428571
   142857 × 4 = 571428
   142857 × 5 = 714285
   142857 × 6 = 857142

   The next cyclic number is 0588235294117647 with 16 digits :
   0588235294117647 × 1 = 0588235294117647
   0588235294117647 × 2 = 1176470588235294
   0588235294117647 × 3 = 1764705882352941
   ...
   0588235294117647 × 16 = 9411764705882352

   Note that for cyclic numbers, leading zeros are important.

   There is only one cyclic number for which, the eleven leftmost digits are
   00000000137 and the five rightmost digits are 56789 (i.e., it has the form
   00000000137...56789 with an unknown number of digits in the middle). Find
   the sum of all its digits.
"""


def test_problem_359(answer):
    output = p359.problem359()
    expected_output = answer['Problem 359']
    assert output == expected_output


"""


An infinite number of people (numbered 1, 2, 3, etc.) are lined up to get
   a room at Hilbert's newest infinite hotel. The hotel contains an infinite
   number of floors (numbered 1, 2, 3, etc.), and each floor contains an
   infinite number of rooms (numbered 1, 2, 3, etc.).

   Initially the hotel is empty. Hilbert declares a rule on how the n^th
   person is assigned a room: person n gets the first vacant room in the
   lowest numbered floor satisfying either of the following:

     • the floor is empty
     • the floor is not empty, and if the latest person taking a room in that
       floor is person m, then m + n is a perfect square

   Person 1 gets room 1 in floor 1 since floor 1 is empty.
   Person 2 does not get room 2 in floor 1 since 1 + 2 = 3 is not a perfect
   square.
   Person 2 instead gets room 1 in floor 2 since floor 2 is empty.
   Person 3 gets room 2 in floor 1 since 1 + 3 = 4 is a perfect square.

   Eventually, every person in the line gets a room in the hotel.

   Define P(f, r) to be n if person n occupies room r in floor f, and 0 if no
   person occupies the room. Here are a few examples:
   P(1, 1) = 1
   P(1, 2) = 3
   P(2, 1) = 2
   P(10, 20) = 440
   P(25, 75) = 4863
   P(99, 100) = 19454

   Find the sum of all P(f, r) for all positive f and r such that f × r =
   71328803586048 and give the last 8 digits as your answer.
"""


def test_problem_360(answer):
    output = p360.problem360()
    expected_output = answer['Problem 360']
    assert output == expected_output


"""


Given two points (x[1],y[1],z[1]) and (x[2],y[2],z[2]) in three
   dimensional space, the Manhattan distance between those points is defined
   as
   |x[1]-x[2]|+|y[1]-y[2]|+|z[1]-z[2]|.

   Let C(r) be a sphere with radius r and center in the origin O(0,0,0).
   Let I(r) be the set of all points with integer coordinates on the surface
   of C(r).
   Let S(r) be the sum of the Manhattan distances of all elements of I(r) to
   the origin O.

   E.g. S(45)=34518.

   Find S(10^10).
"""


def test_problem_361(answer):
    output = p361.problem361()
    expected_output = answer['Problem 361']
    assert output == expected_output


"""


The Thue-Morse sequence {T[n]} is a binary sequence satisfying:

     • T[0] = 0
     • T[2n] = T[n]
     • T[2n+1] = 1 - T[n]

   The first several terms of {T[n]} are given as follows:
   01101001100101101001011001101001....

   We define {A[n]} as the sorted sequence of integers such that the binary
   expression of each element appears as a subsequence in {T[n]}.
   For example, the decimal number 18 is expressed as 10010 in binary. 10010
   appears in {T[n]} (T[8] to T[12]), so 18 is an element of {A[n]}.
   The decimal number 14 is expressed as 1110 in binary. 1110 never appears
   in {T[n]}, so 14 is not an element of {A[n]}.

   The first several terms of A[n] are given as follows:

              n     0  1  2  3  4  5  6  7  8   9   10  11  12  …
              A[n]  0  1  2  3  4  5  6  9  10  11  12  13  18  …

   We can also verify that A[100] = 3251 and A[1000] = 80852364498.

   Find the last 9 digits of .
p_361_Thue-Morse1.gif
"""


def test_problem_362(answer):
    output = p362.problem362()
    expected_output = answer['Problem 362']
    assert output == expected_output


"""


Consider the number 54.
   54 can be factored in 7 distinct ways into one or more factors larger than
   1:
   54, 2×27, 3×18, 6×9, 3×3×6, 2×3×9 and 2×3×3×3.
   If we require that the factors are all squarefree only two ways remain:
   3×3×6 and 2×3×3×3.

   Let's call Fsf(n) the number of ways n can be factored into one or more
   squarefree factors larger than 1, soFsf(54)=2.

   Let S(n) be ∑Fsf(k) for k=2 to n.

   S(100)=193.

   Find S(10 000 000 000).
"""


def test_problem_363(answer):
    output = p363.problem363()
    expected_output = answer['Problem 363']
    assert output == expected_output


"""



   A cubic Bézier curve is defined by four points: P[0], P[1], P[2] and P[3].

   The curve is constructed as follows:
   On the segments P[0]P[1], P[1]P[2] and P[2]P[3] the points Q[0],Q[1] and
   Q[2] are drawn such that
   P[0]Q[0]/P[0]P[1]=P[1]Q[1]/P[1]P[2]=P[2]Q[2]/P[2]P[3]=t (t in [0,1]).
   On the segments Q[0]Q[1] and Q[1]Q[2] the points R[0] and R[1] are drawn
   such thatQ[0]R[0]/Q[0]Q[1]=Q[1]R[1]/Q[1]Q[2]=t for the same value of t.
   On the segment R[0]R[1] the point B is drawn such that R[0]B/R[0]R[1]=t
   for the same value of t.The Bézier curve defined by the points P[0], P[1],
   P[2], P[3] is the locus of B as Q[0] takes all possible positions on the
   segment P[0]P[1]. (Please note that for all points the value of t is the
   same.)

   [1]Applet

   In the applet to the right you can drag the points P[0], P[1], P[2] and
   P[3] to see what the Bézier curve (green curve) defined by those points
   looks like. You can also drag the point Q[0] along the segment P[0]P[1].

   From the construction it is clear that the Bézier curve will be tangent to
   the segments P[0]P[1] in P[0] and P[2]P[3] in P[3].

   A cubic Bézier curve with P[0]=(1,0), P[1]=(1,v), P[2]=(v,1) and
   P[3]=(0,1) is used to approximate a quarter circle.
   The value v>0 is chosen such that the area enclosed by the lines OP[0],
   OP[3] and the curve is equal to ^π/[4] (the area of the quarter circle).

   By how many percent does the length of the curve differ from the length of
   the quarter circle?
   That is, if L is the length of the curve, calculate 100*^(L-π/2)/[(π/2)].
   Give your answer rounded to 10 digits behind the decimal point.
Visible links
   1. CabriJava.class
"""


def test_problem_364(answer):
    output = p364.problem364()
    expected_output = answer['Problem 364']
    assert output == expected_output


"""


There are N seats in a row. N people come after each other to fill the
   seats according to the following rules:

    1. If there is any seat whose adjacent seat(s) are not occupied take such
       a seat.
    2. If there is no such seat and there is any seat for which only one
       adjacent seat is occupied take such a seat.
    3. Otherwise take one of the remaining available seats.

   Let T(N) be the number of possibilities that N seats are occupied by N
   people with the given rules.
   The following figure shows T(4)=8.

   We can verify that T(10) = 61632 and T(1 000) mod 100 000 007 = 47255094.

   Find T(1 000 000) mod 100 000 007.
p_364_comf_dist.gif
"""


def test_problem_365(answer):
    output = p365.problem365()
    expected_output = answer['Problem 365']
    assert output == expected_output


"""


The binomial coeffient C(10^18,10^9) is a number with more than 9 billion
   (9×10^9) digits.

   Let M(n,k,m) denote the binomial coefficient C(n,k) modulo m.

   Calculate ∑M(10^18,10^9,p*q*r) for 1000<p<q<r<5000 and p,q,r prime.
"""


def test_problem_366(answer):
    output = p366.problem366()
    expected_output = answer['Problem 366']
    assert output == expected_output


"""


Two players, Anton and Bernhard, are playing the following game.
   There is one pile of n stones.
   The first player may remove any positive number of stones, but not the
   whole pile.
   Thereafter, each player may remove at most twice the number of stones his
   opponent took on the previous move.
   The player who removes the last stone wins.

   E.g. n=5
   If the first player takes anything more than one stone the next player
   will be able to take all remaining stones.
   If the first player takes one stone, leaving four, his opponent will take
   also one stone, leaving three stones.
   The first player cannot take all three because he may take at most 2x1=2
   stones. So let's say he takes also one stone, leaving 2. The second player
   can take the two remaining stones and wins.
   So 5 is a losing position for the first player.
   For some winning positions there is more than one possible move for the
   first player.
   E.g. when n=17 the first player can remove one or four stones.

   Let M(n) be the maximum number of stones the first player can take from a
   winning position at his first turn and M(n)=0 for any other position.

   ∑M(n) for n≤100 is 728.

   Find ∑M(n) for n≤10^18.Give your answer modulo 10^8.
"""


def test_problem_367(answer):
    output = p367.problem367()
    expected_output = answer['Problem 367']
    assert output == expected_output


"""


Bozo sort, not to be confused with the slightly less efficient bogo sort,
   consists out of checking if the input sequence is sorted and if not
   swapping randomly two elements. This is repeated until eventually the
   sequence is sorted.

   If we consider all permutations of the first 4 natural numbers as input
   the expectation value of the number of swaps, averaged over all 4! input
   sequences is 24.75.
   The already sorted sequence takes 0 steps.

   In this 
Problem we consider the following variant on bozo sort.
   If the sequence is not in order we pick three elements at random and
   shuffle these three elements randomly.
   All 3!=6 permutations of those three elements are equally likely.
   The already sorted sequence will take 0 steps.
   If we consider all permutations of the first 4 natural numbers as input
   the expectation value of the number of shuffles, averaged over all 4!
   input sequences is 27.5.
   Consider as input sequences the permutations of the first 11 natural
   numbers.
   Averaged over all 11! input sequences, what is the expected number of
   shuffles this sorting algorithm will perform?

   Give your answer rounded to the nearest integer.
"""


def test_problem_368(answer):
    output = p368.problem368()
    expected_output = answer['Problem 368']
    assert output == expected_output


"""


The harmonic series 1 + 1 + 1 + 1 + ... is well known to be divergent.
                           2   3   4

   If we however omit from this series every term where the denominator has a
   9 in it, the series remarkably enough converges to approximately
   22.9206766193.
   This modified harmonic series is called the Kempner series.

   Let us now consider another modified harmonic series by omitting from the
   harmonic series every term where the denominator has 3 or more equal
   consecutive digits.One can verify that out of the first 1200 terms of the
   harmonic series, only 20 terms will be omitted.
   These 20 omitted terms are:

   1   , 1   , 1   , 1   , 1   , 1   , 1   , 1   , 1   , 1    , 1    ,
   111   222   333   444   555   666   777   888   999   1000   1110

   1    , 1    , 1    , 1    , 1    , 1    , 1    , 1    and 1    .
   1111   1112   1113   1114   1115   1116   1117   1118     1119

   This series converges as well.

   Find the value the series converges to.
   Give your answer rounded to 10 digits behind the decimal point.
"""


def test_problem_369(answer):
    output = p369.problem369()
    expected_output = answer['Problem 369']
    assert output == expected_output


"""


In a standard 52 card deck of playing cards, a set of 4 cards is a Badugi
   if it contains 4 cards with no pairs and no two cards of the same suit.

   Let f(n) be the number of ways to choose n cards with a 4 card subset that
   is a Badugi. For example, there are 2598960 ways to choose five cards from
   a standard 52 card deck, of which 514800 contain a 4 card subset that is a
   Badugi, so f(5) = 514800.

   Find ∑f(n) for 4 ≤ n ≤ 13.
"""


def test_problem_370(answer):
    output = p370.problem370()
    expected_output = answer['Problem 370']
    assert output == expected_output


"""


Let us define a geometric triangle as an integer sided triangle with sides
   a ≤ b ≤ c so that its sides form a geometric progression, i.e.
   b^2 = a · c . 

   An example of such a geometric triangle is the triangle with sides a =
   144, b = 156 and c = 169.

   There are 861805 geometric triangles with perimeter ≤ 10^6 .

   How many geometric triangles exist with perimeter ≤ 2.5·10^13 ?
"""


def test_problem_371(answer):
    output = p371.problem371()
    expected_output = answer['Problem 371']
    assert output == expected_output


"""


Oregon licence plates consist of three letters followed by a three digit
   number (each digit can be from [0..9]).
   While driving to work Seth plays the following game:
   Whenever the numbers of two licence plates seen on his trip add to 1000
   that's a win.

   E.g. MIC-012 and HAN-988 is a win and RYU-500 and SET-500 too. (as long as
   he sees them in the same trip).

   Find the expected number of plates he needs to see for a win.
   Give your answer rounded to 8 decimal places behind the decimal point.

   Note: We assume that each licence plate seen is equally likely to have any
   three digit number on it.
"""


def test_problem_372(answer):
    output = p372.problem372()
    expected_output = answer['Problem 372']
    assert output == expected_output


"""


Let R(M, N) be the number of lattice points (x, y) which satisfy M<x≤N,
   M<y≤N and is odd.
   We can verify that R(0, 100) = 3019 and R(100, 10000) = 29750422.
   Find R(2·10^6, 10^9).

   Note: represents the floor function.
p_372_pencilray1.jpg
   p_372_pencilray2.gif
"""


def test_problem_373(answer):
    output = p373.problem373()
    expected_output = answer['Problem 373']
    assert output == expected_output


"""


Every triangle has a circumscribed circle that goes through the three
   vertices.Consider all integer sided triangles for which the radius of the
   circumscribed circle is integral as well.

   Let S(n) be the sum of the radii of the circumscribed circles of all such
   triangles for which the radius does not exceed n.

   S(100)=4950 and S(1200)=1653605.

   Find S(10^7).
"""


def test_problem_374(answer):
    output = p374.problem374()
    expected_output = answer['Problem 374']
    assert output == expected_output


"""


An integer partition of a number n is a way of writing n as a sum of
   positive integers.

   Partitions that differ only in the order of their summands are considered
   the same.A partition of n into distinct parts is a partition of n in which
   every part occurs at most once.

   The partitions of 5 into distinct parts are:
   5, 4+1 and 3+2.

   Let f(n) be the maximum product of the parts of any such partition of n
   into distinct parts and let m(n) be the number of elements of any such
   partition of n with that product.

   So f(5)=6 and m(5)=2.

   For n=10 the partition with the largest product is 10=2+3+5, which gives
   f(10)=30 and m(10)=3.
   And their product, f(10)·m(10) = 30·3 = 90

   It can be verified that
   ∑f(n)·m(n) for 1 ≤ n ≤ 100 = 1683550844462.

   Find ∑f(n)·m(n) for 1 ≤ n ≤ 10^14.
   Give your answer modulo 982451653, the 50 millionth prime.
"""


def test_problem_375(answer):
    output = p375.problem375()
    expected_output = answer['Problem 375']
    assert output == expected_output


"""


Let S[n] be an integer sequence produced with the following pseudo-random
   number generator:

                        S[0]   =[ ] 290797[ ]
                        S[n+1] =[ ] S[n]^2 mod 50515093

   Let A(i, j) be the minimum of the numbers S[i], S[i+1], ... , S[j] for i ≤
   j.
   Let M(N) = ΣA(i, j) for 1 ≤ i ≤ j ≤ N.
   We can verify that M(10) = 432256955 and M(10 000) = 3264567774119.

   Find M(2 000 000 000).
"""


def test_problem_376(answer):
    output = p376.problem376()
    expected_output = answer['Problem 376']
    assert output == expected_output


"""


Consider the following set of dice with nonstandard pips:

   Die A: 1 4 4 4 4 4
   Die B: 2 2 2 5 5 5
   Die C: 3 3 3 3 3 6

   A game is played by two players picking a die in turn and rolling it. The
   player who rolls the highest value wins.

   If the first player picks die A and the second player picks die B we get
   P(second player wins) = 7/12 > 1/2

   If the first player picks die B and the second player picks die C we get
   P(second player wins) = 7/12 > 1/2

   If the first player picks die C and the second player picks die A we get
   P(second player wins) = 25/36 > 1/2

   So whatever die the first player picks, the second player can pick another
   die and have a larger than 50% chance of winning.
   A set of dice having this property is called a nontransitive set of dice.

   We wish to investigate how many sets of nontransitive dice exist. We will
   assume the following conditions:

     • There are three six-sided dice with each side having between 1 and N
       pips, inclusive.
     • Dice with the same set of pips are equal, regardless of which side on
       the die the pips are located.
     • The same pip value may appear on multiple dice; if both players roll
       the same value neither player wins.
     • The sets of dice {A,B,C}, {B,C,A} and {C,A,B} are the same set.

   For N = 7 we find there are 9780 such sets.
   How many are there for N = 30 ?
"""


def test_problem_377(answer):
    output = p377.problem377()
    expected_output = answer['Problem 377']
    assert output == expected_output


"""


There are 16 positive integers that do not have a zero in their digits and
   that have a digital sum equal to 5, namely:
   5, 14, 23, 32, 41, 113, 122, 131, 212, 221, 311, 1112, 1121, 1211, 2111
   and 11111.
   Their sum is 17891.

   Let f(n) be the sum of all positive integers that do not have a zero in
   their digits and have a digital sum equal to n.

   Find .
   Give the last 9 digits as your answer.
"""


def test_problem_378(answer):
    output = p378.problem378()
    expected_output = answer['Problem 378']
    assert output == expected_output


"""


Let T(n) be the n^th triangle number, so T(n) = n (n+1) .
                                                   2

   Let dT(n) be the number of divisors of T(n).
   E.g.:T(7) = 28 and dT(7) = 6.

   Let Tr(n) be the number of triples (i, j, k) such that 1 ≤ i < j < k ≤ n
   and dT(i) > dT(j) > dT(k).
   Tr(20) = 14, Tr(100) = 5772 and Tr(1000) = 11174776.

   Find Tr(60 000 000).
   Give the last 18 digits of your answer.
"""


def test_problem_379(answer):
    output = p379.problem379()
    expected_output = answer['Problem 379']
    assert output == expected_output


"""


Let f(n) be the number of couples (x,y) with x and y positive integers, x
   ≤ y and the least common multiple of x and y equal to n.

   Let g be the summatory function of f, i.e.: g(n) = ∑ f(i) for 1 ≤ i ≤ n.

   You are given that g(10^6) = 37429395.

   Find g(10^12).
"""


def test_problem_380(answer):
    output = p380.problem380()
    expected_output = answer['Problem 380']
    assert output == expected_output


"""


An m×n maze is an m×n rectangular grid with walls placed between grid
   cells such that there is exactly one path from the top-left square to any
   other square.
   The following are examples of a 9×12 maze and a 15×20 maze:

   Let C(m,n) be the number of distinct m×n mazes. Mazes which can be formed
   by rotation and reflection from another maze are considered distinct.

   It can be verified that C(1,1) = 1, C(2,2) = 4, C(3,4) = 2415, and C(9,12)
   = 2.5720e46 (in scientific notation rounded to 5 significant digits).
   Find C(100,500) and write your answer in scientific notation rounded to 5
   significant digits.

   When giving your answer, use a lowercase e to separate mantissa and
   exponent.E.g. if the answer is 1234567891011 then the answer format would
   be 1.2346e12.
"""


def test_problem_382(answer):
    output = p382.problem382()
    expected_output = answer['Problem 382']
    assert output == expected_output


"""


A polygon is a flat shape consisting of straight line segments that are
   joined to form a closed chain or circuit. A polygon consists of at least
   three sides and does not self-intersect.

   A set S of positive numbers is said to generate a polygon P if:

     • no two sides of P are the same length,
     • the length of every side of P is in S, and
     • S contains no other value.

   For example:
   The set {3, 4, 5} generates a polygon with sides 3, 4, and 5 (a triangle).
   The set {6, 9, 11, 24} generates a polygon with sides 6, 9, 11, and 24 (a
   quadrilateral).
   The sets {1, 2, 3} and {2, 3, 4, 9} do not generate any polygon at all.

   Consider the sequence s, defined as follows:

     • s[1] = 1, s[2] = 2, s[3] = 3
     • s[n] = s[n-1] + s[n-3] for n > 3.

   Let U[n] be the set {s[1], s[2], ..., s[n]}. For example, U[10] = {1, 2,
   3, 4, 6, 9, 13, 19, 28, 41}.
   Let f(n) be the number of subsets of U[n] which generate at least one
   polygon.
   For example, f(5) = 7, f(10) = 501 and f(25) = 18635853.

   Find the last 9 digits of f(10^18).
"""


def test_problem_383(answer):
    output = p383.problem383()
    expected_output = answer['Problem 383']
    assert output == expected_output


"""


Let f[5](n) be the largest integer x for which 5^x divides n.
   For example, f[5](625000) = 7.

   Let T[5](n) be the number of integers i which satisfy f[5]((2·i-1)!) <
   2·f[5](i!) and 1 ≤ i ≤ n.
   It can be verified that T[5](10^3) = 68 and T[5](10^9) = 2408210.

   Find T[5](10^18).
"""


def test_problem_384(answer):
    output = p384.problem384()
    expected_output = answer['Problem 384']
    assert output == expected_output


"""


Define the sequence a(n) as the number of adjacent pairs of ones in the
   binary expansion of n (possibly overlapping).
   E.g.: a(5) = a(101[2]) = 0, a(6) = a(110[2]) = 1, a(7) = a(111[2]) = 2

   Define the sequence b(n) = (-1)^a(n).
   This sequence is called the Rudin-Shapiro sequence.

   Also consider the summatory sequence of b(n): .

   The first couple of values of these sequences are:
   n        0     1     2     3     4     5     6     7
   a(n)     0     0     0     1     0     0     1     2
   b(n)     1     1     1    -1     1     1    -1     1
   s(n)     1     2     3     2     3     4     3     4

   The sequence s(n) has the remarkable property that all elements are
   positive and every positive integer k occurs exactly k times.

   Define g(t,c), with 1 ≤ c ≤ t, as the index in s(n) for which t occurs for
   the c'th time in s(n).
   E.g.: g(3,3) = 6, g(4,2) = 7 and g(54321,12345) = 1220847710.

   Let F(n) be the fibonacci sequence defined by:
   F(0)=F(1)=1 and
   F(n)=F(n-1)+F(n-2) for n>1.

   Define GF(t)=g(F(t),F(t-1)).

   Find ΣGF(t) for 2≤t≤45.
"""


def test_problem_385(answer):
    output = p385.problem385()
    expected_output = answer['Problem 385']
    assert output == expected_output


"""


For any triangle T in the plane, it can be shown that there is a unique
   ellipse with largest area that is completely inside T.

   For a given n, consider triangles T such that:
   - the vertices of T have integer coordinates with absolute value ≤ n, and
   - the foci^1 of the largest-area ellipse inside T are (√13,0) and
   (-√13,0).
   Let A(n) be the sum of the areas of all such triangles.

   For example, if n = 8, there are two such triangles. Their vertices are
   (-4,-3),(-4,3),(8,0) and (4,3),(4,-3),(-8,0), and the area of each
   triangle is 36. Thus A(8) = 36 + 36 = 72.

   It can be verified that A(10) = 252, A(100) = 34632 and A(1000) = 3529008.

   Find A(1 000 000 000).

   ^1The foci (plural of focus) of an ellipse are two points A and B such
   that for every point P on the boundary of the ellipse, AP + PB is
   constant.
"""


def test_problem_386(answer):
    output = p386.problem386()
    expected_output = answer['Problem 386']
    assert output == expected_output


"""


Let n be an integer and S(n) be the set of factors of n.

   A subset A of S(n) is called an antichain of S(n) if A contains only one
   element or if none of the elements of A divides any of the other elements
   of A.

   For example: S(30) = {1, 2, 3, 5, 6, 10, 15, 30}
   {2, 5, 6} is not an antichain of S(30).
   {2, 3, 5} is an antichain of S(30).

   Let N(n) be the maximum length of an antichain of S(n).

   Find ΣN(n) for 1 ≤ n ≤ 10^8
"""


def test_problem_388(answer):
    output = p388.problem388()
    expected_output = answer['Problem 388']
    assert output == expected_output


"""


Consider all lattice points (a,b,c) with 0 ≤ a,b,c ≤ N.

   From the origin O(0,0,0) all lines are drawn to the other lattice points.
   Let D(N) be the number of distinct such lines.

   You are given that D(1 000 000) = 831909254469114121.

   Find D(10^10). Give as your answer the first nine digits followed by the
   last nine digits.
"""


def test_problem_389(answer):
    output = p389.problem389()
    expected_output = answer['Problem 389']
    assert output == expected_output


"""


An unbiased single 4-sided die is thrown and its value, T, is noted.
   T unbiased 6-sided dice are thrown and their scores are added together.
   The sum, C, is noted.
   C unbiased 8-sided dice are thrown and their scores are added together.
   The sum, O, is noted.
   O unbiased 12-sided dice are thrown and their scores are added together.
   The sum, D, is noted.
   D unbiased 20-sided dice are thrown and their scores are added together.
   The sum, I, is noted.
   Find the variance of I, and give your answer rounded to 4 decimal places.
"""


def test_problem_390(answer):
    output = p390.problem390()
    expected_output = answer['Problem 390']
    assert output == expected_output


"""


Consider the triangle with sides √5, √65 and √68.It can be shown that this
   triangle has area 9.

   S(n) is the sum of the areas of all triangles with sides √(1+b^2),
   √(1+c^2) and √(b^2+c^2) (for positive integers b and c ) that have an
   integral area not exceeding n.

   The example triangle has b=2 and c=8.

   S(10^6)=18018206.

   Find S(10^10).
"""


def test_problem_391(answer):
    output = p391.problem391()
    expected_output = answer['Problem 391']
    assert output == expected_output


"""


Let s[k] be the number of 1’s when writing the numbers from 0 to k in
   binary.
   For example, writing 0 to 5 in binary, we have 0, 1, 10, 11, 100, 101.
   There are seven 1’s, so s[5] = 7.
   The sequence S = {s[k] : k ≥ 0} starts {0, 1, 2, 4, 5, 7, 9, 12, ...}.

   A game is played by two players. Before the game starts, a number n is
   chosen. A counter c starts at 0. At each turn, the player chooses a number
   from 1 to n (inclusive) and increases c by that number. The resulting
   value of c must be a member of S. If there are no more valid moves, the
   player loses.

   For example:
   Let n = 5. c starts at 0.
   Player 1 chooses 4, so c becomes 0 + 4 = 4.
   Player 2 chooses 5, so c becomes 4 + 5 = 9.
   Player 1 chooses 3, so c becomes 9 + 3 = 12.
   etc.
   Note that c must always belong to S, and each player can increase c by at
   most n.

   Let M(n) be the highest number the first player can choose at her first
   turn to force a win, and M(n) = 0 if there is no such move. For example,
   M(2) = 2, M(7) = 1 and M(20) = 4.

   Given Σ(M(n))^3 = 8150 for 1 ≤ n ≤ 20.

   Find Σ(M(n))^3 for 1 ≤ n ≤ 1000.
"""


def test_problem_392(answer):
    output = p392.problem392()
    expected_output = answer['Problem 392']
    assert output == expected_output


"""


A rectilinear grid is an orthogonal grid where the spacing between the
   gridlines does not have to be equidistant.
   An example of such grid is logarithmic graph paper.

   Consider rectilinear grids in the Cartesian coordinate system with the
   following properties:

     • The gridlines are parallel to the axes of the Cartesian coordinate
       system.
     • There are N+2 vertical and N+2 horizontal gridlines. Hence there are
       (N+1) x (N+1) rectangular cells.
     • The equations of the two outer vertical gridlines are x = -1 and x =
       1.
     • The equations of the two outer horizontal gridlines are y = -1 and y =
       1.
     • The grid cells are colored red if they overlap with the unit circle,
       black otherwise.

   For this 
Problem we would like you to find the postions of the remaining N
   inner horizontal and N inner vertical gridlines so that the area occupied
   by the red cells is minimized.

   E.g. here is a picture of the solution for N = 10:

   The area occupied by the red cells for N = 10 rounded to 10 digits behind
   the decimal point is 3.3469640797.

   Find the positions for N = 400.
   Give as your answer the area occupied by the red cells rounded to 10
   digits behind the decimal point.
"""


def test_problem_393(answer):
    output = p393.problem393()
    expected_output = answer['Problem 393']
    assert output == expected_output


"""


An n×n grid of squares contains n^2 ants, one ant per square.
   All ants decide to move simultaneously to an adjacent square (usually 4
   possibilities, except for ants on the edge of the grid or at the corners).
   We define f(n) to be the number of ways this can happen without any ants
   ending on the same square and without any two ants crossing the same edge
   between two squares.

   You are given that f(4) = 88.
   Find f(10).
"""


def test_problem_394(answer):
    output = p394.problem394()
    expected_output = answer['Problem 394']
    assert output == expected_output


"""


Jeff eats a pie in an unusual way.
   The pie is circular. He starts with slicing an initial cut in the pie
   along a radius.
   While there is at least a given fraction F of pie left, he performs the
   following procedure:
   - He makes two slices from the pie centre to any point of what is
   remaining of the pie border, any point on the remaining pie border equally
   likely. This will divide the remaining pie into three pieces.
   - Going counterclockwise from the initial cut, he takes the first two pie
   pieces and eats them.
   When less than a fraction F of pie remains, he does not repeat this
   procedure. Instead, he eats all of the remaining pie.

   For x ≥ 1, let E(x) be the expected number of times Jeff repeats the
   procedure above with F = ^1/[x].
   It can be verified that E(1) = 1, E(2) ≈ 1.2676536759, and E(7.5) ≈
   2.1215732071.

   Find E(40) rounded to 10 decimal places behind the decimal point.
"""


def test_problem_395(answer):
    output = p395.problem395()
    expected_output = answer['Problem 395']
    assert output == expected_output


"""


The Pythagorean tree is a fractal generated by the following procedure:

   Start with a unit square. Then, calling one of the sides its base (in the
   animation, the bottom side is the base):

    1. Attach a right triangle to the side opposite the base, with the
       hypotenuse coinciding with that side and with the sides in a 3-4-5
       ratio. Note that the smaller side of the triangle must be on the
       'right' side with respect to the base (see animation).
    2. Attach a square to each leg of the right triangle, with one of its
       sides coinciding with that leg.
    3. Repeat this procedure for both squares, considering as their bases the
       sides touching the triangle.

   The resulting figure, after an infinite number of iterations, is the
   Pythagorean tree.

   It can be shown that there exists at least one rectangle, whose sides are
   parallel to the largest square of the Pythagorean tree, which encloses the
   Pythagorean tree completely.

   Find the smallest area possible for such a bounding rectangle, and give
   your answer rounded to 10 decimal places.
p_395_pythagorean.gif
"""


def test_problem_396(answer):
    output = p396.problem396()
    expected_output = answer['Problem 396']
    assert output == expected_output


"""


For any positive integer n, the nth weak Goodstein sequence {g[1], g[2],
   g[3], ...} is defined as:

     • g[1] = n
     • for k > 1, g[k] is obtained by writing g[k-1] in base k, interpreting
       it as a base k + 1 number, and subtracting 1.

   The sequence terminates when g[k] becomes 0.

   For example, the 6th weak Goodstein sequence is {6, 11, 17, 25, ...}:

     • g[1] = 6.
     • g[2] = 11 since 6 = 110[2], 110[3] = 12, and 12 - 1 = 11.
     • g[3] = 17 since 11 = 102[3], 102[4] = 18, and 18 - 1 = 17.
     • g[4] = 25 since 17 = 101[4], 101[5] = 26, and 26 - 1 = 25.

   and so on.

   It can be shown that every weak Goodstein sequence terminates.

   Let G(n) be the number of nonzero elements in the nth weak Goodstein
   sequence.
   It can be verified that G(2) = 3, G(4) = 21 and G(6) = 381.
   It can also be verified that ΣG(n) = 2517 for 1 ≤ n < 8.

   Find the last 9 digits of ΣG(n) for 1 ≤ n < 16.
"""


def test_problem_397(answer):
    output = p397.problem397()
    expected_output = answer['Problem 397']
    assert output == expected_output


"""


On the parabola y = x^2/k, three points A(a, a^2/k), B(b, b^2/k) and C(c,
   c^2/k) are chosen.

   Let F(K, X) be the number of the integer quadruplets (k, a, b, c) such
   that at least one angle of the triangle ABC is 45-degree, with 1 ≤ k ≤ K
   and -X ≤ a < b < c ≤ X.

   For example, F(1, 10) = 41 and F(10, 100) = 12492.
   Find F(10^6, 10^9).
"""


def test_problem_398(answer):
    output = p398.problem398()
    expected_output = answer['Problem 398']
    assert output == expected_output


"""


Inside a rope of length n, n-1 points are placed with distance 1 from each
   other and from the endpoints. Among these points, we choose m-1 points at
   random and cut the rope at these points to create m segments.

   Let E(n, m) be the expected length of the second-shortest segment.For
   example, E(3, 2) = 2 and E(8, 3) = 16/7.Note that if multiple segments
   have the same shortest length the length of the second-shortest segment is
   defined as the same as the shortest length.

   Find E(10^7, 100).Give your answer rounded to 5 decimal places behind the
   decimal point.
"""


def test_problem_399(answer):
    output = p399.problem399()
    expected_output = answer['Problem 399']
    assert output == expected_output


"""


The first 15 fibonacci numbers are:
   1,1,2,3,5,8,13,21,34,55,89,144,233,377,610.
   It can be seen that 8 and 144 are not squarefree: 8 is divisible by 4 and
   144 is divisible by 4 and by 9.
   So the first 13 squarefree fibonacci numbers are:
   1,1,2,3,5,13,21,34,55,89,233,377 and 610.

   The 200th squarefree fibonacci number
   is:971183874599339129547649988289594072811608739584170445.
   The last sixteen digits of this number are: 1608739584170445 and in
   scientific notation this number can be written as 9.7e53.

   Find the 100 000 000th squarefree fibonacci number.
   Give as your answer its last sixteen digits followed by a comma followed
   by the number in scientific notation (rounded to one digit after the
   decimal point).
   For the 200th squarefree number the answer would have been:
   1608739584170445,9.7e53

   Note:
   For this 
Problem, assume that for every prime p, the first fibonacci
   number divisible by p is not divisible by p^2 (this is part of Wall's
   conjecture). This has been verified for primes ≤ 3·10^15, but has not been
   proven in general.
   If it happens that the conjecture is false, then the accepted answer to
   this 
Problem isn't guaranteed to be the 100 000 000th squarefree fibonacci
   number, rather it represents only a lower bound for that number.
"""


def test_problem_400(answer):
    output = p400.problem400()
    expected_output = answer['Problem 400']
    assert output == expected_output


"""


A Fibonacci tree is a binary tree recursively defined as:

     • T(0) is the empty tree.
     • T(1) is the binary tree with only one node.
     • T(k) consists of a root node that has T(k-1) and T(k-2) as children.

   On such a tree two players play a take-away game. On each turn a player
   selects a node and removes that node along with the subtree rooted at that
   node.
   The player who is forced to take the root node of the entire tree loses.

   Here are the winning moves of the first player on the first turn for T(k)
   from k=1 to k=6.

   Let f(k) be the number of winning moves of the first player (i.e. the
   moves for which the second player has no winning strategy) on the first
   turn of the game when this game is played on T(k).

   For example, f(5) = 1 and f(10) = 17.

   Find f(10000). Give the last 18 digits of your answer.
"""


@pytest.mark.skip(reason='slow')
def test_problem_401(answer):
    output = p401.problem401()
    expected_output = answer['Problem 401']
    assert output == expected_output


"""


The divisors of 6 are 1,2,3 and 6.
   The sum of the squares of these numbers is 1+4+9+36=50.

   Let sigma2(n) represent the sum of the squares of the divisors of n.Thus
   sigma2(6)=50.

   Let SIGMA2 represent the summatory function of sigma2, that is
   SIGMA2(n)=∑sigma2(i) for i=1 to n.
   The first 6 values of SIGMA2 are: 1,6,16,37,63 and 113.

   Find SIGMA2(10^15) modulo 10^9.
"""


def test_problem_402(answer):
    output = p402.problem402()
    expected_output = answer['Problem 402']
    assert output == expected_output


"""


It can be shown that the polynomial n^4 + 4n^3 + 2n^2 + 5n is a multiple
   of 6 for every integer n. It can also be shown that 6 is the largest
   integer satisfying this property.

   Define M(a, b, c) as the maximum m such that n^4 + an^3 + bn^2 + cn is a
   multiple of m for all integers n. For example, M(4, 2, 5) = 6.

   Also, define S(N) as the sum of M(a, b, c) for all 0 < a, b, c ≤ N.

   We can verify that S(10) = 1972 and S(10000) = 2024258331114.

   Let F[k] be the Fibonacci sequence:
   F[0] = 0, F[1] = 1 and
   F[k] = F[k-1] + F[k-2] for k ≥ 2.

   Find the last 9 digits of Σ S(F[k]) for 2 ≤ k ≤ 1234567890123.
"""


def test_problem_403(answer):
    output = p403.problem403()
    expected_output = answer['Problem 403']
    assert output == expected_output


"""


For integers a and b, we define D(a, b) as the domain enclosed by the
   parabola y = x^2 and the line y = a·x + b:
   D(a, b) = { (x, y) | x^2 ≤ y ≤ a·x + b }.

   L(a, b) is defined as the number of lattice points contained in D(a, b).
   For example, L(1, 2) = 8 and L(2, -1) = 1.

   We also define S(N) as the sum of L(a, b) for all the pairs (a, b) such
   that the area of D(a, b) is a rational number and |a|,|b| ≤ N.
   We can verify that S(5) = 344 and S(100) = 26709528.

   Find S(10^12). Give your answer mod 10^8.
"""


def test_problem_404(answer):
    output = p404.problem404()
    expected_output = answer['Problem 404']
    assert output == expected_output


"""


E[a] is an ellipse with an equation of the form x^2 + 4y^2 = 4a^2.
   E[a]' is the rotated image of E[a] by θ degrees counterclockwise around
   the origin O(0, 0) for 0° < θ < 90°.

   b is the distance to the origin of the two intersection points closest to
   the origin and c is the distance of the two other intersection points.
   We call an ordered triplet (a, b, c) a canonical ellipsoidal triplet if a,
   b and c are positive integers.
   For example, (209, 247, 286) is a canonical ellipsoidal triplet.

   Let C(N) be the number of distinct canonical ellipsoidal triplets (a, b,
   c) for a ≤ N.
   It can be verified that C(10^3) = 7, C(10^4) = 106 and C(10^6) = 11845.

   Find C(10^17).
p_404_c_ellipse.gif
"""


def test_problem_405(answer):
    output = p405.problem405()
    expected_output = answer['Problem 405']
    assert output == expected_output


"""


We wish to tile a rectangle whose length is twice its width.
   Let T(0) be the tiling consisting of a single rectangle.
   For n > 0, let T(n) be obtained from T(n-1) by replacing all tiles in the
   following manner:

   The following animation demonstrates the tilings T(n) for n from 0 to 5:

   Let f(n) be the number of points where four tiles meet in T(n).
   For example, f(1) = 0, f(4) = 82 and f(10^9) mod 17^7 = 126897180.

   Find f(10^k) for k = 10^18, give your answer modulo 17^7.
p_405_tile1.png
   p_405_tile2.gif
"""


def test_problem_406(answer):
    output = p406.problem406()
    expected_output = answer['Problem 406']
    assert output == expected_output


"""


We are trying to find a hidden number selected from the set of integers
   {1, 2, ..., n} by asking questions. Each number (question) we ask, we get
   one of three possible answers:

     • "Your guess is lower than the hidden number" (and you incur a cost of
       a), or
     • "Your guess is higher than the hidden number" (and you incur a cost of
       b), or
     • "Yes, that's it!" (and the game ends).

   Given the value of n, a, and b, an optimal strategy minimizes the total
   cost for the worst possible case.

   For example, if n = 5, a = 2, and b = 3, then we may begin by asking "2"
   as our first question.

   If we are told that 2 is higher than the hidden number (for a cost of
   b=3), then we are sure that "1" is the hidden number (for a total cost of
   3).
   If we are told that 2 is lower than the hidden number (for a cost of a=2),
   then our next question will be "4".
   If we are told that 4 is higher than the hidden number (for a cost of
   b=3), then we are sure that "3" is the hidden number (for a total cost of
   2+3=5).
   If we are told that 4 is lower than the hidden number (for a cost of a=2),
   then we are sure that "5" is the hidden number (for a total cost of
   2+2=4).
   Thus, the worst-case cost achieved by this strategy is 5. It can also be
   shown that this is the lowest worst-case cost that can be achieved. So, in
   fact, we have just described an optimal strategy for the given values of
   n, a, and b.

   Let C(n, a, b) be the worst-case cost achieved by an optimal strategy for
   the given values of n, a, and b.

   Here are a few examples:
   C(5, 2, 3) = 5
   C(500, √2, √3) = 13.22073197...
   C(20000, 5, 7) = 82
   C(2000000, √5, √7) = 49.63755955...

   Let F[k] be the Fibonacci numbers: F[k] = F[k-1] + F[k-2] with base cases
   F[1] = F[2] = 1.
   Find ∑[1≤k≤30] C(10^12, √k, √F[k]), and give your answer rounded to 8
   decimal places behind the decimal point.
"""


@pytest.mark.skip(reason='slow')
def test_problem_407(answer):
    output = p407.problem407()
    expected_output = answer['Problem 407']
    assert output == expected_output


"""


If we calculate a^2 mod 6 for 0 ≤ a ≤ 5 we get: 0,1,4,3,4,1.

   The largest value of a such that a^2 ≡ a mod 6 is 4.
   Let's call M(n) the largest value of a < n such that a^2 ≡ a (mod n).
   So M(6) = 4.

   Find ∑M(n) for 1 ≤ n ≤ 10^7.
"""


def test_problem_408(answer):
    output = p408.problem408()
    expected_output = answer['Problem 408']
    assert output == expected_output


"""


Let's call a lattice point (x, y) inadmissible if x, y and x + y are all
   positive perfect squares.
   For example, (9, 16) is inadmissible, while (0, 4), (3, 1) and (9, 4) are
   not.

   Consider a path from point (x[1], y[1]) to point (x[2], y[2]) using only
   unit steps north or east.
   Let's call such a path admissible if none of its intermediate points are
   inadmissible.

   Let P(n) be the number of admissible paths from (0, 0) to (n, n).
   It can be verified that P(5) = 252, P(16) = 596994440 and P(1000) mod
   1 000 000 007 = 341920854.

   Find P(10 000 000) mod 1 000 000 007.
"""


def test_problem_409(answer):
    output = p409.problem409()
    expected_output = answer['Problem 409']
    assert output == expected_output


"""


Let n be a positive integer. Consider nim positions where:

     • There are n non-empty piles.
     • Each pile has size less than 2^n.
     • No two piles have the same size.

   Let W(n) be the number of winning nim positions satisfying the
   aboveconditions (a position is winning if the first player has a winning
   strategy). For example, W(1) = 1, W(2) = 6, W(3) = 168, W(5) = 19764360
   and W(100) mod 1 000 000 007 = 384777056.

   Find W(10 000 000) mod 1 000 000 007.
"""


def test_problem_410(answer):
    output = p410.problem410()
    expected_output = answer['Problem 410']
    assert output == expected_output


"""


Let C be the circle with radius r, x^2 + y^2 = r^2. We choose two points
   P(a, b) and Q(-a, c) so that the line passing through P and Q is tangent
   to C.

   For example, the quadruplet (r, a, b, c) = (2, 6, 2, -7) satisfies this
   property.

   Let F(R, X) be the number of the integer quadruplets (r, a, b, c) with
   this property, and with 0 < r ≤ R and 0 < a ≤ X.

   We can verify that F(1, 5) = 10, F(2, 10) = 52 and F(10, 100) = 3384.
   Find F(10^8, 10^9) + F(10^9, 10^8).
"""


def test_problem_411(answer):
    output = p411.problem411()
    expected_output = answer['Problem 411']
    assert output == expected_output


"""


Let n be a positive integer. Suppose there are stations at the coordinates
   (x, y) = (2^i mod n, 3^i mod n) for 0 ≤ i ≤ 2n. We will consider stations
   with the same coordinates as the same station.

   We wish to form a path from (0, 0) to (n, n) such that the x and y
   coordinates never decrease.
   Let S(n) be the maximum number of stations such a path can pass through.

   For example, if n = 22, there are 11 distinct stations, and a valid path
   can pass through at most 5 stations. Therefore, S(22) = 5.The case is
   illustrated below, with an example of an optimal path:

   It can also be verified that S(123) = 14 and S(10000) = 48.

   Find ∑ S(k^5) for 1 ≤ k ≤ 30.
"""


def test_problem_412(answer):
    output = p412.problem412()
    expected_output = answer['Problem 412']
    assert output == expected_output


"""


For integers m, n (0 ≤ n < m), let L(m, n) be an m×m grid with the
   top-right n×n grid removed.

   For example, L(5, 3) looks like this:

   We want to number each cell of L(m, n) with consecutive integers 1, 2, 3,
   ... such that the number in every cell is smaller than the number below it
   and to the left of it.

   For example, here are two valid numberings of L(5, 3):

   Let LC(m, n) be the number of valid numberings of L(m, n).
   It can be verified that LC(3, 0) = 42, LC(5, 3) = 250250, LC(6, 3) =
   406029023400 and LC(10, 5) mod 76543217 = 61251715.

   Find LC(10000, 5000) mod 76543217.
"""


def test_problem_413(answer):
    output = p413.problem413()
    expected_output = answer['Problem 413']
    assert output == expected_output


"""


We say that a d-digit positive number (no leading zeros) is a one-child
   number if exactly one of its sub-strings is divisible by d.

   For example, 5671 is a 4-digit one-child number. Among all its sub-strings
   5, 6, 7, 1, 56, 67, 71, 567, 671 and 5671, only 56 is divisible by 4.
   Similarly, 104 is a 3-digit one-child number because only 0 is divisible
   by 3.
   1132451 is a 7-digit one-child number because only 245 is divisible by 7.

   Let F(N) be the number of the one-child numbers less than N.
   We can verify that F(10) = 9, F(10^3) = 389 and F(10^7) = 277674.

   Find F(10^19).
"""


def test_problem_414(answer):
    output = p414.problem414()
    expected_output = answer['Problem 414']
    assert output == expected_output


"""


6174 is a remarkable number; if we sort its digits in increasing order and
   subtract that number from the number you get when you sort the digits in
   decreasing order, we get 7641-1467=6174.
   Even more remarkable is that if we start from any 4 digit number and
   repeat this process of sorting and subtracting, we'll eventually end up
   with 6174 or immediately with 0 if all digits are equal.
   This also works with numbers that have less than 4 digits if we pad the
   number with leading zeroes until we have 4 digits.
   E.g. let's start with the number 0837:
   8730-0378=8352
   8532-2358=6174

   6174 is called the Kaprekar constant. The process of sorting and
   subtracting and repeating this until either 0 or the Kaprekar constant is
   reached is called the Kaprekar routine.

   We can consider the Kaprekar routine for other bases and number of digits.
   Unfortunately, it is not guaranteed a Kaprekar constant exists in all
   cases; either the routine can end up in a cycle for some input numbers or
   the constant the routine arrives at can be different for different input
   numbers.
   However, it can be shown that for 5 digits and a base b = 6t+3≠9, a
   Kaprekar constant exists.
   E.g. base 15: (10,4,14,9,5)[15]
   base 21: (14,6,20,13,7)[21]

   Define C[b] to be the Kaprekar constant in base b for 5 digits.Define the
   function sb(i) to be

     • 0 if i = C[b] or if i written in base b consists of 5 identical digits
     • the number of iterations it takes the Kaprekar routine in base b to
       arrive at C[b], otherwise

   Note that we can define sb(i) for all integers i < b^5. If i written in
   base b takes less than 5 digits, the number is padded with leading zero
   digits until we have 5 digits before applying the Kaprekar routine.

   Define S(b) as the sum of sb(i) for 0 < i < b^5.
   E.g. S(15) = 5274369
   S(111) = 400668930299

   Find the sum of S(6k+3) for 2 ≤ k ≤ 300.
   Give the last 18 digits as your answer.
"""


def test_problem_415(answer):
    output = p415.problem415()
    expected_output = answer['Problem 415']
    assert output == expected_output


"""


A set of lattice points S is called a titanic set if there exists a line
   passing through exactly two points in S.

   An example of a titanic set is S = {(0, 0), (0, 1), (0, 2), (1, 1), (2,
   0), (1, 0)}, where the line passing through (0, 1) and (2, 0) does not
   pass through any other point in S.

   On the other hand, the set {(0, 0), (1, 1), (2, 2), (4, 4)} is not a
   titanic set since the line passing through any two points in the set also
   passes through the other two.

   For any positive integer N, let T(N) be the number of titanic sets S whose
   every point (x, y) satisfies 0 ≤ x, y ≤ N.It can be verified that T(1) =
   11, T(2) = 494, T(4) = 33554178, T(111) mod 10^8 = 13500401 and
   T(10^5) mod 10^8 = 63259062.

   Find T(10^11) mod 10^8.
"""


def test_problem_416(answer):
    output = p416.problem416()
    expected_output = answer['Problem 416']
    assert output == expected_output


"""


A row of n squares contains a frog in the leftmost square. By successive
   jumps the frog goes to the rightmost square and then back to the leftmost
   square. On the outward trip he jumps one, two or three squares to the
   right, and on the homeward trip he jumps to the left in a similar manner.
   He cannot jump outside the squares. He repeats the round-trip travel m
   times.

   Let F(m, n) be the number of the ways the frog can travel so that at most
   one square remains unvisited.
   For example, F(1, 3) = 4, F(1, 4) = 15, F(1, 5) = 46, F(2, 3) = 16 and
   F(2, 100) mod 10^9 = 429619151.

   Find the last 9 digits of F(10, 10^12).
"""


def test_problem_417(answer):
    output = p417.problem417()
    expected_output = answer['Problem 417']
    assert output == expected_output


"""


A unit fraction contains 1 in the numerator. The decimal representation of
   the unit fractions with denominators 2 to 10 are given:

     1/2  =  0.5
     1/3  =  0.(3)
     1/4  =  0.25
     1/5  =  0.2
     1/6  =  0.1(6)
     1/7  =  0.(142857)
     1/8  =  0.125
     1/9  =  0.(1)
     1/10 =  0.1

   Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
   be seen that 1/7 has a 6-digit recurring cycle.

   Unit fractions whose denominator has no other prime factors than 2 and/or
   5 are not considered to have a recurring cycle.
   We define the length of the recurring cycle of those unit fractions as 0.

   Let L(n) denote the length of the recurring cycle of 1/n.You are given
   that ∑L(n) for 3 ≤ n ≤ 1 000 000 equals 55535191115.

   Find ∑L(n) for 3 ≤ n ≤ 100 000 000
"""


def test_problem_418(answer):
    output = p418.problem418()
    expected_output = answer['Problem 418']
    assert output == expected_output


"""


Let n be a positive integer. An integer triple (a, b, c) is called a
   factorisation triple of n if:

     • 1 ≤ a ≤ b ≤ c
     • a·b·c = n.

   Define f(n) to be a + b + c for the factorisation triple (a, b, c) of n
   which minimises c / a. One can show that this triple is unique.

   For example, f(165) = 19, f(100100) = 142 and f(20!) = 4034872.

   Find f(43!).
"""


def test_problem_419(answer):
    output = p419.problem419()
    expected_output = answer['Problem 419']
    assert output == expected_output


"""


The look and say sequence goes 1, 11, 21, 1211, 111221, 312211, 13112221,
   1113213211, ...
   The sequence starts with 1 and all other members are obtained by
   describing the previous member in terms of consecutive digits.
   It helps to do this out loud:
   1 is 'one one' → 11
   11 is 'two ones' → 21
   21 is 'one two and one one' → 1211
   1211 is 'one one, one two and two ones' → 111221
   111221 is 'three ones, two twos and one one' → 312211
   ...

   Define A(n), B(n) and C(n) as the number of ones, twos and threes in the
   n'th element of the sequence respectively.
   One can verify that A(40) = 31254, B(40) = 20259 and C(40) = 11625.

   Find A(n), B(n) and C(n) for n = 10^12.
   Give your answer modulo 2^30 and separate your values for A, B and C by a
   comma.
   E.g. for n = 40 the answer would be 31254,20259,11625
"""


def test_problem_420(answer):
    output = p420.problem420()
    expected_output = answer['Problem 420']
    assert output == expected_output


"""


A positive integer matrix is a matrix whose elements are all positive
   integers.
   Some positive integer matrices can be expressed as a square of a positive
   integer matrix in two different ways. Here is an example:

   We define F(N) as the number of the 2x2 positive integer matrices which
   have a trace less than N and which can be expressed as a square of a
   positive integer matrix in two different ways.
   We can verify that F(50) = 7 and F(1000) = 1019.

   Find F(10^7).
p_420_matrix.gif
"""


def test_problem_421(answer):
    output = p421.problem421()
    expected_output = answer['Problem 421']
    assert output == expected_output


"""


Numbers of the form n^15+1 are composite for every integer n > 1.
   For positive integers n and m let s(n,m) be defined as the sum of the
   distinct prime factors of n^15+1 not exceeding m.

   E.g. 2^15+1 = 3×3×11×331.
   So s(2,10) = 3 and s(2,1000) = 3+11+331 = 345.

   Also 10^15+1 = 7×11×13×211×241×2161×9091.
   So s(10,100) = 31 and s(10,1000) = 483.

   Find &Sum; s(n,10^8) for 1 ≤ n ≤ 10^11.
"""


def test_problem_422(answer):
    output = p422.problem422()
    expected_output = answer['Problem 422']
    assert output == expected_output


"""


Let H be the hyperbola defined by the equation 12x^2 + 7xy - 12y^2 = 625.

   Next, define X as the point (7, 1). It can be seen that X is in H.

   Now we define a sequence of points in H, {P[i] : i ≥ 1}, as:

     • P[1] = (13, 61/4).
     • P[2] = (-43/6, -4).
     • For i > 2, P[i] is the unique point in H that is different from P[i-1]
       and such that line P[i]P[i-1] is parallel to line P[i-2]X. It can be
       shown that P[i] is well-defined, and that its coordinates are always
       rational.

   You are given that P[3] = (-19/2, -229/24), P[4] = (1267/144, -37/12) and
   P[7] = (17194218091/143327232, 274748766781/1719926784).

   Find P[n] for n = 11^14 in the following format:
   If P[n] = (a/b, c/d) where the fractions are in lowest terms and the
   denominators are positive, then the answer is (a + b + c + d) mod
   1 000 000 007.

   For n = 7, the answer would have been: 806236837.
"""


def test_problem_423(answer):
    output = p423.problem423()
    expected_output = answer['Problem 423']
    assert output == expected_output


"""


Let n be a positive integer.
   A 6-sided die is thrown n times. Let c be the number of pairs of
   consecutive throws that give the same value.

   For example, if n = 7 and the values of the die throws are
   (1,1,5,6,6,6,3), then the following pairs of consecutive throws give the
   same value:
   (1,1,5,6,6,6,3)
   (1,1,5,6,6,6,3)
   (1,1,5,6,6,6,3)
   Therefore, c = 3 for (1,1,5,6,6,6,3).

   Define C(n) as the number of outcomes of throwing a 6-sided die n times
   such that c does not exceed π(n).^1
   For example, C(3) = 216, C(4) = 1290, C(11) = 361912500 and C(24) =
   4727547363281250000.

   Define S(L) as ∑ C(n) for 1 ≤ n ≤ L.
   For example, S(50) mod 1 000 000 007 = 832833871.

   Find S(50 000 000) mod 1 000 000 007.

   ^1 π denotes the prime-counting function, i.e. π(n) is the number of
   primes ≤ n.
"""


def test_problem_424(answer):
    output = p424.problem424()
    expected_output = answer['Problem 424']
    assert output == expected_output


"""


The above is an example of a cryptic kakuro (also known as cross sums, or
   even sums cross) puzzle, with its final solution on the right. (The common
   rules of kakuro puzzles can be found easily on numerous internet sites.
   Other related information can also be currently found at [1]krazydad.com
   whose author has provided the puzzle data for this challenge.)

   The downloadable text file ([2]kakuro200.txt) contains the description of
   200 such puzzles, a mix of 5x5 and 6x6 types. The first puzzle in the file
   is the above example which is coded as follows:

   6,X,X,(vCC),(vI),X,X,X,(hH),B,O,(vCA),(vJE),X,(hFE,vD),O,O,O,O,(hA),O,I,(hJC,vB),O,O,(hJC),H,O,O,O,X,X,X,(hJE),O,O,X

   The first character is a numerical digit indicating the size of the
   information grid. It would be either a 6 (for a 5x5 kakuro puzzle) or a 7
   (for a 6x6 puzzle) followed by a comma (,). The extra top line and left
   column are needed to insert information.

   The content of each cell is then described and followed by a comma, going
   left to right and starting with the top line.
   X = Gray cell, not required to be filled by a digit.
   O (upper case letter)= White empty cell to be filled by a digit.
   A = Or any one of the upper case letters from A to J to be replaced by its
   equivalent digit in the solved puzzle.
   ( ) = Location of the encrypted sums. Horizontal sums are preceded by a
   lower case "h" and vertical sums are preceded by a lower case "v". Those
   are followed by one or two upper case letters depending if the sum is a
   single digit or double digit one. For double digit sums, the first letter
   would be for the "tens" and the second one for the "units". When the cell
   must contain information for both a horizontal and a vertical sum, the
   first one is always for the horizontal sum and the two are separated by a
   comma within the same set of brackets, ex.: (hFE,vD). Each set of brackets
   is also immediately followed by a comma.

   The description of the last cell is followed by a Carriage Return/Line
   Feed (CRLF) instead of a comma.

   The required answer to each puzzle is based on the value of each letter
   necessary to arrive at the solution and according to the alphabetical
   order. As indicated under the example puzzle, its answer would be
   8426039571. At least 9 out of the 10 encrypting letters are always part of
   the 
Problem description. When only 9 are given, the missing one must be
   assigned the remaining digit.

   You are given that the sum of the answers for the first 10 puzzles in the
   file is 64414157580.

   Find the sum of the answers for the 200 puzzles.
Visible links
   1. http://krazydad.com/
   2. kakuro200.txt
"""


@pytest.mark.skip(reason='slow')
def test_problem_425(answer):
    output = p425.problem425()
    expected_output = answer['Problem 425']
    assert output == expected_output


"""


Two positive numbers A and B are said to be connected (denoted by "A ↔ B")
   if one of these conditions holds:
   (1) A and B have the same length and differ in exactly one digit; for
   example, 123 ↔ 173.
   (2) Adding one digit to the left of A (or B) makes B (or A); for example,
   23 ↔ 223 and 123 ↔ 23.

   We call a prime P a 2's relative if there exists a chain of connected
   primes between 2 and P and no prime in the chain exceeds P.

   For example, 127 is a 2's relative. One of the possible chains is shown
   below:
   2 ↔ 3 ↔ 13 ↔ 113 ↔ 103 ↔ 107 ↔ 127
   However, 11 and 103 are not 2's relatives.

   Let F(N) be the sum of the primes ≤ N which are not 2's relatives.
   We can verify that F(10^3) = 431 and F(10^4) = 78728.

   Find F(10^7).
"""


def test_problem_426(answer):
    output = p426.problem426()
    expected_output = answer['Problem 426']
    assert output == expected_output


"""


Consider an infinite row of boxes. Some of the boxes contain a ball. For
   example, an initial configuration of 2 consecutive occupied boxes followed
   by 2 empty boxes, 2 occupied boxes, 1 empty box, and 2 occupied boxes can
   be denoted by the sequence (2, 2, 2, 1, 2), in which the number of
   consecutive occupied and empty boxes appear alternately.

   A turn consists of moving each ball exactly once according to the
   following rule: Transfer the leftmost ball which has not been moved to the
   nearest empty box to its right.

   After one turn the sequence (2, 2, 2, 1, 2) becomes (2, 2, 1, 2, 3) as can
   be seen below; note that we begin the new sequence starting at the first
   occupied box.

   A system like this is called a Box-Ball System or BBS for short.

   It can be shown that after a sufficient number of turns, the system
   evolves to a state where the consecutive numbers of occupied boxes is
   invariant. In the example below, the consecutive numbers of occupied boxes
   evolves to [1, 2, 3]; we shall call this the final state.

   We define the sequence {t[i]}:

     • s[0] = 290797
     • s[k+1] = s[k]^2 mod 50515093
     • t[k] = (s[k] mod 64) + 1

   Starting from the initial configuration (t[0], t[1], …, t[10]), the final
   state becomes [1, 3, 10, 24, 51, 75].
   Starting from the initial configuration (t[0], t[1], …, t[10 000 000]),
   find the final state.
   Give as your answer the sum of the squares of the elements of the final
   state. For example, if the final state is [1, 2, 3] then 14 ( = 1^2 + 2^2
   + 3^2) is your answer.
p_426_baxball1.gif
   p_426_baxball2.gif
"""


def test_problem_427(answer):
    output = p427.problem427()
    expected_output = answer['Problem 427']
    assert output == expected_output


"""


A sequence of integers S = {s[i]} is called an n-sequence if it has n
   elements and each element s[i] satisfies 1 ≤ s[i] ≤ n. Thus there are n^n
   distinct n-sequences in total.For example, the sequence S = {1, 5, 5, 10,
   7, 7, 7, 2, 3, 7} is a 10-sequence.

   For any sequence S, let L(S) be the length of the longest contiguous
   subsequence of S with the same value.For example, for the given sequence S
   above, L(S) = 3, because of the three consecutive 7's.

   Let f(n) = ∑ L(S) for all n-sequences S.

   For example, f(3) = 45, f(7) = 1403689 and f(11) = 481496895121.

   Find f(7 500 000) mod 1 000 000 009.
"""


def test_problem_428(answer):
    output = p428.problem428()
    expected_output = answer['Problem 428']
    assert output == expected_output


"""


Let a, b and c be positive numbers.
   Let W, X, Y, Z be four collinear points where |WX| = a, |XY| = b, |YZ| = c
   and |WZ| = a + b + c.
   Let C[in] be the circle having the diameter XY.
   Let C[out] be the circle having the diameter WZ.

   The triplet (a, b, c) is called a necklace triplet if you can place k ≥ 3
   distinct circles C[1], C[2], ..., C[k] such that:

     • C[i] has no common interior points with any C[j] for 1 ≤ i, j ≤ k and
       i ≠ j,
     • C[i] is tangent to both C[in] and C[out] for 1 ≤ i ≤ k,
     • C[i] is tangent to C[i+1] for 1 ≤ i < k, and
     • C[k] is tangent to C[1].

   For example, (5, 5, 5) and (4, 3, 21) are necklace triplets, while it can
   be shown that (2, 2, 5) is not.

   Let T(n) be the number of necklace triplets (a, b, c) such that a, b and c
   are positive integers, and b ≤ n.For example, T(1) = 9, T(20) = 732 and
   T(3000) = 438106.

   Find T(1 000 000 000).
"""


@pytest.mark.skip(reason='slow')
def test_problem_429(answer):
    output = p429.problem429()
    expected_output = answer['Problem 429']
    assert output == expected_output


"""


A unitary divisor d of a number n is a divisor of n that has the property
   gcd(d, n/d) = 1.
   The unitary divisors of 4! = 24 are 1, 3, 8 and 24.
   The sum of their squares is 1^2 + 3^2 + 8^2 + 24^2 = 650.

   Let S(n) represent the sum of the squares of the unitary divisors of n.
   Thus S(4!)=650.

   Find S(100 000 000!) modulo 1 000 000 009.
"""


def test_problem_430(answer):
    output = p430.problem430()
    expected_output = answer['Problem 430']
    assert output == expected_output


"""


N disks are placed in a row, indexed 1 to N from left to right.
   Each disk has a black side and white side. Initially all disks show their
   white side.

   At each turn, two, not necessarily distinct, integers A and B between 1
   and N (inclusive) are chosen uniformly at random.
   All disks with an index from A to B (inclusive) are flipped.

   The following example shows the case N = 8. At the first turn A = 5 and B
   = 2, and at the second turn A = 4 and B = 6.

   Let E(N, M) be the expected number of disks that show their white side
   after M turns.
   We can verify that E(3, 1) = 10/9, E(3, 2) = 5/3, E(10, 4) ≈ 5.157 and
   E(100, 10) ≈ 51.893.

   Find E(10^10, 4000).
   Give your answer rounded to 2 decimal places behind the decimal point.
p_430_flips.gif
"""


def test_problem_431(answer):
    output = p431.problem431()
    expected_output = answer['Problem 431']
    assert output == expected_output


"""


Fred the farmer arranges to have a new storage silo installed on his farm
   and having an obsession for all things square he is absolutely devastated
   when he discovers that it is circular. Quentin, the representative from
   the company that installed the silo, explains that they only manufacture
   cylindrical silos, but he points out that it is resting on a square base.
   Fred is not amused and insists that it is removed from his property.

   Quick thinking Quentin explains that when granular materials are delivered
   from above a conical slope is formed and the natural angle made with the
   horizontal is called the angle of repose. For example if the angle of
   repose, $\\alpha = 30$ degrees, and grain is delivered at the centre of the
   silo then a perfect cone will form towards the top of the cylinder. In the
   case of this silo, which has a diameter of 6m, the amount of space wasted
   would be approximately 32.648388556 m^3. However, if grain is delivered at
   a point on the top which has a horizontal distance of $x$ metres from the
   centre then a cone with a strangely curved and sloping base is formed. He
   shows Fred a picture.

   We shall let the amount of space wasted in cubic metres be given by
   $V(x)$. If $x = 1.114785284$, which happens to have three squared decimal
   places, then the amount of space wasted, $V(1.114785284) \\approx 36$.
   Given the range of possible solutions to this 
Problem there is exactly one
   other option: $V(2.511167869) \\approx 49$. It would be like knowing that
   the square is king of the silo, sitting in splendid glory on top of your
   grain.

   Fred's eyes light up with delight at this elegant resolution, but on
   closer inspection of Quentin's drawings and calculations his happiness
   turns to despondency once more. Fred points out to Quentin that it's the
   radius of the silo that is 6 metres, not the diameter, and the angle of
   repose for his grain is 40 degrees. However, if Quentin can find a set of
   solutions for this particular silo then he will be more than happy to keep
   it.

   If Quick thinking Quentin is to satisfy frustratingly fussy Fred the
   farmer's appetite for all things square then determine the values of $x$
   for all possible square space wastage options and calculate $\\sum x$
   correct to 9 decimal places.
p_431_grain_silo.png
"""


def test_problem_432(answer):
    output = p432.problem432()
    expected_output = answer['Problem 432']
    assert output == expected_output


"""


Let S(n,m) = ∑φ(n × i) for 1 ≤ i ≤ m. (φ is Euler's totient function)
   You are given that S(510510,10^6 )= 45480596821125120.

   Find S(510510,10^11).
   Give the last 9 digits of your answer.
"""


def test_problem_433(answer):
    output = p433.problem433()
    expected_output = answer['Problem 433']
    assert output == expected_output


"""


Let E(x[0], y[0]) be the number of steps it takes to determine the
   greatest common divisor of x[0] and y[0] with Euclid's algorithm. More
   formally:
   x[1] = y[0], y[1] = x[0] mod y[0]
   x[n] = y[n-1], y[n] = x[n-1] mod y[n-1]
   E(x[0], y[0]) is the smallest n such that y[n] = 0.

   We have E(1,1) = 1, E(10,6) = 3 and E(6,10) = 4.

   Define S(N) as the sum of E(x,y) for 1 ≤ x,y ≤ N.
   We have S(1) = 1, S(10) = 221 and S(100) = 39826.

   Find S(5·10^6).
"""


def test_problem_434(answer):
    output = p434.problem434()
    expected_output = answer['Problem 434']
    assert output == expected_output


"""


Recall that a graph is a collection of vertices and edges connecting the
   vertices, and that two vertices connected by an edge are called adjacent.
   Graphs can be embedded in Euclidean space by associating each vertex with
   a point in the Euclidean space.
   A flexible graph is an embedding of a graph where it is possible to move
   one or more vertices continuously so that the distance between at least
   two nonadjacent vertices is altered while the distances between each pair
   of adjacent vertices is kept constant.
   A rigid graph is an embedding of a graph which is not flexible.
   Informally, a graph is rigid if by replacing the vertices with fully
   rotating hinges and the edges with rods that are unbending and inelastic,
   no parts of the graph can be moved independently from the rest of the
   graph.

   The grid graphs embedded in the Euclidean plane are not rigid, as the
   following animation demonstrates:

   However, one can make them rigid by adding diagonal edges to the cells.
   For example, for the 2x3 grid graph, there are 19 ways to make the graph
   rigid:

   Note that for the purposes of this 
Problem, we do not consider changing
   the orientation of a diagonal edge or adding both diagonal edges to a cell
   as a different way of making a grid graph rigid.

   Let R(m,n) be the number of ways to make the m × n grid graph rigid.
   E.g. R(2,3) = 19 and R(5,5) = 23679901

   Define S(N) as ∑R(i,j) for 1 ≤ i, j ≤ N.
   E.g. S(5) = 25021721.
   Find S(100), give your answer modulo 1000000033
"""


def test_problem_435(answer):
    output = p435.problem435()
    expected_output = answer['Problem 435']
    assert output == expected_output


"""


The Fibonacci numbers {f[n], n ≥ 0} are defined recursively as f[n] =
   f[n-1] + f[n-2] with base cases f[0] = 0 and f[1] = 1.

   Define the polynomials {F[n], n ≥ 0} as F[n](x) = ∑f[i]x^i for 0 ≤ i ≤ n.

   For example, F[7](x) = x + x^2 + 2x^3 + 3x^4 + 5x^5 + 8x^6 + 13x^7, and
   F[7](11) = 268357683.

   Let n = 10^15. Find the sum [∑[0≤x≤100] F[n](x)] mod 1307674368000 (=
   15!).
"""


def test_problem_436(answer):
    output = p436.problem436()
    expected_output = answer['Problem 436']
    assert output == expected_output


"""


Julie proposes the following wager to her sister Louise.
   She suggests they play a game of chance to determine who will wash the
   dishes.
   For this game, they shall use a generator of independent random numbers
   uniformly distributed between 0 and 1.
   The game starts with S = 0.
   The first player, Louise, adds to S different random numbers from the
   generator until S > 1 and records her last random number 'x'.
   The second player, Julie, continues adding to S different random numbers
   from the generator until S > 2 and records her last random number 'y'.
   The player with the highest number wins and the loser washes the dishes,
   i.e. if y > x the second player wins.

   For example, if the first player draws 0.62 and 0.44, the first player
   turn ends since 0.62+0.44 > 1 and x = 0.44.
   If the second players draws 0.1, 0.27 and 0.91, the second player turn
   ends since 0.62+0.44+0.1+0.27+0.91 > 2 and y = 0.91.Since y > x, the
   second player wins.

   Louise thinks about it for a second, and objects: "That's not fair".
   What is the probability that the second player wins?
   Give your answer rounded to 10 places behind the decimal point in the form
   0.abcdefghij
"""


def test_problem_437(answer):
    output = p437.problem437()
    expected_output = answer['Problem 437']
    assert output == expected_output


"""


When we calculate 8^n modulo 11 for n=0 to 9 we get: 1, 8, 9, 6, 4, 10, 3,
   2, 5, 7.
   As we see all possible values from 1 to 10 occur. So 8 is a primitive root
   of 11.
   But there is more:
   If we take a closer look we see:
   1+8=9
   8+9=17≡6 mod 11
   9+6=15≡4 mod 11
   6+4=10
   4+10=14≡3 mod 11
   10+3=13≡2 mod 11
   3+2=5
   2+5=7
   5+7=12≡1 mod 11.

   So the powers of 8 mod 11 are cyclic with period 10, and 8^n + 8^n+1 ≡
   8^n+2 (mod 11).
   8 is called a Fibonacci primitive root of 11.
   Not every prime has a Fibonacci primitive root.
   There are 323 primes less than 10000 with one or more Fibonacci primitive
   roots and the sum of these primes is 1480491.
   Find the sum of the primes less than 100,000,000 with at least one
   Fibonacci primitive root.
"""


def test_problem_438(answer):
    output = p438.problem438()
    expected_output = answer['Problem 438']
    assert output == expected_output


"""


For an n-tuple of integers t = (a[1], ..., a[n]), let (x[1], ..., x[n]) be
   the solutions of the polynomial equation x^n + a[1]x^n-1 + a[2]x^n-2 + ...
   + a[n-1]x + a[n] = 0.

   Consider the following two conditions:

     • x[1], ..., x[n] are all real.
     • If x[1], ..., x[n] are sorted, ⌊x[i]⌋ = i for 1 ≤ i ≤ n. (⌊·⌋: floor
       function.)

   In the case of n = 4, there are 12 n-tuples of integers which satisfy both
   conditions.
   We define S(t) as the sum of the absolute values of the integers in t.
   For n = 4 we can verify that ∑S(t) = 2087 for all n-tuples t which satisfy
   both conditions.

   Find ∑S(t) for n = 7.
"""


def test_problem_439(answer):
    output = p439.problem439()
    expected_output = answer['Problem 439']
    assert output == expected_output


"""


Let d(k) be the sum of all divisors of k.
   We define the function S(N) = ∑[1≤i≤N] ∑[1≤j≤N] d(i·j).
   For example, S(3) = d(1) + d(2) + d(3) + d(2) + d(4) + d(6) + d(3) + d(6)
   + d(9) = 59.

   You are given that S(10^3) = 563576517282 and S(10^5) mod 10^9 =
   215766508.
   Find S(10^11) mod 10^9.
"""


def test_problem_440(answer):
    output = p440.problem440()
    expected_output = answer['Problem 440']
    assert output == expected_output


"""


We want to tile a board of length n and height 1 completely, with either 1
   × 2 blocks or 1 × 1 blocks with a single decimal digit on top:

   For example, here are some of the ways to tile a board of length n = 8:

   Let T(n) be the number of ways to tile a board of length n as described
   above.

   For example, T(1) = 10 and T(2) = 101.

   Let S(L) be the triple sum ∑[a,b,c] gcd(T(c^a), T(c^b)) for 1 ≤ a, b, c ≤
   L.
   For example:
   S(2) = 10444
   S(3) = 1292115238446807016106539989
   S(4) mod 987 898 789 = 670616280.

   Find S(2000) mod 987 898 789.
"""


def test_problem_441(answer):
    output = p441.problem441()
    expected_output = answer['Problem 441']
    assert output == expected_output


def test_problem_442(answer):
    output = p442.problem442()
    expected_output = answer['Problem 442']
    assert output == expected_output


def test_problem_443(answer):
    output = p443.problem443()
    expected_output = answer['Problem 443']
    assert output == expected_output


def test_problem_444(answer):
    output = p444.problem444()
    expected_output = answer['Problem 444']
    assert output == expected_output


def test_problem_445(answer):
    output = p445.problem445()
    expected_output = answer['Problem 445']
    assert output == expected_output


def test_problem_446(answer):
    output = p446.problem446()
    expected_output = answer['Problem 446']
    assert output == expected_output


def test_problem_447(answer):
    output = p447.problem447()
    expected_output = answer['Problem 447']
    assert output == expected_output


def test_problem_448(answer):
    output = p448.problem448()
    expected_output = answer['Problem 448']
    assert output == expected_output


def test_problem_449(answer):
    output = p449.problem449()
    expected_output = answer['Problem 449']
    assert output == expected_output


def test_problem_450(answer):
    output = p450.problem450()
    expected_output = answer['Problem 450']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_451(answer):
    output = p451.problem451()
    expected_output = answer['Problem 451']
    assert output == expected_output


def test_problem_452(answer):
    output = p452.problem452()
    expected_output = answer['Problem 452']
    assert output == expected_output


def test_problem_453(answer):
    output = p453.problem453()
    expected_output = answer['Problem 453']
    assert output == expected_output


def test_problem_454(answer):
    output = p454.problem454()
    expected_output = answer['Problem 454']
    assert output == expected_output


def test_problem_455(answer):
    output = p455.problem455()
    expected_output = answer['Problem 455']
    assert output == expected_output


def test_problem_456(answer):
    output = p456.problem456()
    expected_output = answer['Problem 456']
    assert output == expected_output


def test_problem_457(answer):
    output = p457.problem457()
    expected_output = answer['Problem 457']
    assert output == expected_output


def test_problem_458(answer):
    output = p458.problem458()
    expected_output = answer['Problem 458']
    assert output == expected_output


def test_problem_459(answer):
    output = p459.problem459()
    expected_output = answer['Problem 459']
    assert output == expected_output


def test_problem_460(answer):
    output = p460.problem460()
    expected_output = answer['Problem 460']
    assert output == expected_output


def test_problem_461(answer):
    output = p461.problem461()
    expected_output = answer['Problem 461']
    assert output == expected_output


def test_problem_462(answer):
    output = p462.problem462()
    expected_output = answer['Problem 462']
    assert output == expected_output


def test_problem_463(answer):
    output = p463.problem463()
    expected_output = answer['Problem 463']
    assert output == expected_output


def test_problem_464(answer):
    output = p464.problem464()
    expected_output = answer['Problem 464']
    assert output == expected_output


def test_problem_465(answer):
    output = p465.problem465()
    expected_output = answer['Problem 465']
    assert output == expected_output


def test_problem_466(answer):
    output = p466.problem_466()
    expected_output = answer['Problem 466']
    assert output == expected_output


def test_problem_467(answer):
    output = p467.problem467()
    expected_output = answer['Problem 467']
    assert output == expected_output


def test_problem_468(answer):
    output = p468.problem468()
    expected_output = answer['Problem 468']
    assert output == expected_output


def test_problem_469(answer):
    output = p469.problem469()
    expected_output = answer['Problem 469']
    assert output == expected_output


def test_problem_470(answer):
    output = p470.problem470()
    expected_output = answer['Problem 470']
    assert output == expected_output


def test_problem_471(answer):
    output = p471.problem471()
    expected_output = answer['Problem 471']
    assert output == expected_output


def test_problem_472(answer):
    output = p472.problem472()
    expected_output = answer['Problem 472']
    assert output == expected_output


def test_problem_473(answer):
    output = p473.problem473()
    expected_output = answer['Problem 473']
    assert output == expected_output


def test_problem_474(answer):
    output = p474.problem474()
    expected_output = answer['Problem 474']
    assert output == expected_output


def test_problem_475(answer):
    output = p475.problem475()
    expected_output = answer['Problem 475']
    assert output == expected_output


def test_problem_476(answer):
    output = p476.problem476()
    expected_output = answer['Problem 476']
    assert output == expected_output
