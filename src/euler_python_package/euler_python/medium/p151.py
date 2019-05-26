
from euler_python.utils import eulerlib


def problem151():
    ans = get_expected_singles((1,)) - 2
    return "{:.6f}".format(ans)


@eulerlib.Memoize
def get_expected_singles(state):
    result = 0.0
    if len(state) > 0:
        for i in range(len(state)):
            tempstate = list(state)
            sheet = state[i]
            del tempstate[i]
            for j in range(sheet + 1, 6):
                tempstate.append(j)
            tempstate.sort()
            result += get_expected_singles(tuple(tempstate))
        result /= len(state)
        if len(state) == 1:
            result += 1.0
    return result


if __name__ == "__main__":
    print(problem151())
