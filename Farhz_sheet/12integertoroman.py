dct = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
}

ndct = {v: k for k, v in dct.items()}
values = list(dct.values())
keys = list(dct.keys())


class Solution:
    def intToRoman(self, num: int) -> str:
        # first set keys and values 2 list with possible values
        ans = ""
        # iterate the values
        for i in range(13):
            # subtract that value until its less than i  then move to next loop
            while(num >= values[i]):
                print(num)
                ans += keys[i]
                num -= values[i]

        return ans
