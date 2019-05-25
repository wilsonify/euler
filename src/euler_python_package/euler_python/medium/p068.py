from euler_python.utils import eulerlib


def problem068():
    """


    Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
       and each line adding to nine.

       Working clockwise, and starting from the group of three with the
       numerically lowest external node (4,3,2 in this example), each solution
       can be described uniquely. For example, the above solution can be
       described by the set: 4,3,2; 6,2,1; 5,1,3.

       It is possible to complete the ring with four different totals: 9, 10, 11,
       and 12. There are eight solutions in total.

               Total          Solution Set
               9              4,2,3; 5,3,1; 6,1,2
               9              4,3,2; 6,2,1; 5,1,3
               10             2,3,5; 4,5,1; 6,1,3
               10             2,5,3; 6,3,1; 4,1,5
               11             1,4,6; 3,6,2; 5,2,4
               11             1,6,4; 5,4,2; 3,2,6
               12             1,5,6; 2,6,4; 3,4,5
               12             1,6,5; 3,5,4; 2,4,6

       By concatenating each group it is possible to form 9-digit strings; the
       maximum string for a 3-gon ring is 432621513.

       Using the numbers 1 to 10, and depending on arrangements, it is possible
       to form 16- and 17-digit strings. What is the maximum 16-digit string for
       a "magic" 5-gon ring?
    p_068_1.gif
       p_068_2.gif
    """
    state = list(range(1, 11))
    max = None
    while True:
        sum = state[0] + state[5] + state[6]
        if state[1] + state[6] + state[7] == sum and \
                state[2] + state[7] + state[8] == sum and \
                state[3] + state[8] + state[9] == sum and \
                state[4] + state[9] + state[5] == sum:

            minouterindex = 0
            minouter = state[0]
            for i in range(1, 5):
                if state[i] < minouter:
                    minouterindex = i
                    minouter = state[i]

            s = ""
            for i in range(5):
                s += str(state[(minouterindex + i) % 5])
                s += str(state[(minouterindex + i) % 5 + 5])
                s += str(state[(minouterindex + i + 1) % 5 + 5])
            if len(s) == 16 and (max is None or s > max):
                max = s

        if not eulerlib.next_permutation(state):
            break

    assert max is not None
    return int(max)


if __name__ == "__main__":
    print(problem068())
