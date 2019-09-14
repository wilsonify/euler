def problem017():
    """
    If the numbers 1 to 5 are written out in words: one, two, three, four,
       five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

       If all the numbers from 1 to 1000 (one thousand) inclusive were written
       out in words, how many letters would be used?

       NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
       forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
       20 letters. The use of "and" when writing out numbers is in compliance
       with British usage.

    For the numbers 0 to 19, we write the single word:
    {zero, one, two, three, four, five, six, seven, eight, nine,
    ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen}.
    For the numbers 20 to 99, we write the word for the tens place:
    {twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety}.
    Subsequently if the last digit is not 0, then we write the word for the ones place (one to nine).
    For the numbers 100 to 999, we write the ones word for the hundreds place followed by "hundred":
    {one hundred, two hundred, three hundred, ..., eight hundred, nine hundred}.
    Subsequently if the last two digits are not 00, then we write the word "and"
    followed by the phrase for the last two digits (from 01 to 99).
    For the numbers 1000 to 999999, we write the word for the three digits starting at the
    thousands place and going leftward, followed by "thousand". Subsequently if the last three
    digits are not 000, then we write the phrase for the last three digits (from 001 to 999).


    """

    ans = sum(len(to_english(i)) for i in range(1, 1001))
    return ans


def to_english(n):
    if 0 <= n < 20:
        return ONES[n]
    elif 20 <= n < 100:
        return TENS[n // 10] + (ONES[n % 10] if (n % 10 != 0) else "")
    elif 100 <= n < 1000:
        return (
                ONES[n // 100]
                + "hundred"
                + (("and" + to_english(n % 100)) if (n % 100 != 0) else "")
        )
    elif 1000 <= n < 1000000:
        return (
                to_english(n // 1000)
                + "thousand"
                + (to_english(n % 1000) if (n % 1000 != 0) else "")
        )
    else:
        raise ValueError()


ONES = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
TENS = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

if __name__ == "__main__":
    print(problem017())
