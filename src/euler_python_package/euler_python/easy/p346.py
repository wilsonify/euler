
import itertools


# 1 is a strong repunit because in every base b >= 2, its representation is "1", which is a repunit.
# 2 is not a strong repunit because in base 2 it is "10", but in every base b >= 3 it is "2".
# 
# As for other numbers, first assume that n is an arbitrary integer at least 3.
# It is trivially a repunit in base b = n - 1 (which is at least 2), where its representation is "11".
# For this n to be a strong repunit, it needs to be a repunit in at least one other base.
# Obviously it can't be "11" in another base. So it must be {"111",
# "1111", "11111", or some longer string} in some base smaller than b.
# 
# Phrased differently, if an integer n >= 3 has the representation {"111", "1111", or some longer string}
# in some base b >= 2, then it is automatically a strong repunit because firstly, its value is
# at least 7 ("111" in base 2), and secondly it is equal to "11" in some base b' >= 2.
# 
# Hence all we need to do is for each repunit length 3, 4, 5, etc., we generate the string (e.g. "111"),
# then evaluate its value at base 2, 3, etc. as long as the value stays within the limit,
# and add these values to the set of known strong repunits (to catch possible duplicates).
# 
# Note that the longest repunit length we need to test is at most the bit length of the limit.
# For example, because the limit is 10^12 = 1110100011010100101001010001000000000000 (base 2),
# any repunit longer than "1111111111111111111111111111111111111111" is guaranteed
# to exceed the limit in every base.
def problem346():
    """


    The number 7 is special, because 7 is 111 written in base 2, and 11
       written in base 6
       (i.e. 7[10] = 11[6] = 111[2]). In other words, 7 is a repunit in at least
       two bases b > 1.

       We shall call a positive integer with this property a strong repunit. It
       can be verified that there are 8 strong repunits below 50:
       {1,7,13,15,21,31,40,43}.
       Furthermore, the sum of all strong repunits below 1000 equals 15864.

       Find the sum of all strong repunits below 10^12.
    """

    limit = 10 ** 12

    # Collect all generated numbers to eliminate duplicates
    strongrepunits = {1}  # Special case

    # For each possible length of strong repunits (ignoring the trivial length of 2)
    for length in range(3, limit.bit_length() + 1):

        # For each base to evaluate the repunit in, until the value exceeds the limit
        for base in itertools.count(2):

            # Evaluate value = base^(length-1) + base^(length-2) + ... + base^1 + base^0
            # Due to the geometric series, value = (base^length - 1) / (base - 1)
            value = (base ** length - 1) // (base - 1)
            if value >= limit:
                break
            strongrepunits.add(value)

    # Sum all the numbers generated
    ans = sum(strongrepunits)
    return ans


if __name__ == "__main__":
    print(problem346())
