class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0
        for numeral_index in range(0, len(s)):
            if numeral_index == len(s) - 1:
                if s[numeral_index] == "I":
                    integer = integer + 1
                elif s[numeral_index] == "X":
                    if s[numeral_index - 1] == "I":
                        return integer
                    else:
                        integer = integer + 10
                elif s[numeral_index] == "V":
                    if s[numeral_index - 1] == "I":
                        return integer
                    else:
                        integer = integer + 5
                elif s[numeral_index] == "L":
                    if s[numeral_index - 1] == "X":
                        return integer
                    else:
                        integer = integer + 50
                elif s[numeral_index] == "C":
                    if s[numeral_index - 1] == "X":
                        return integer
                    else:
                        integer = integer + 100
                elif s[numeral_index] == "D":
                    if s[numeral_index - 1] == "C":
                        return integer
                    else:
                        integer = integer + 500
                elif s[numeral_index] == "M":
                    if s[numeral_index - 1] == "C":
                        return integer
                    else:
                        integer = integer + 1000
            elif s[numeral_index] == "I":
                if s[numeral_index + 1] == "V" :
                    integer = integer + 4
                elif s[numeral_index + 1] == "X":
                    integer = integer + 9
                else:
                    integer = integer + 1
            elif s[numeral_index] == "V":
                if numeral_index == 0:
                    integer = integer + 5
                elif numeral_index > 0:
                    if s[numeral_index - 1] != "I":
                        integer = integer + 5
            elif s[numeral_index] == "X":
                if s[numeral_index + 1] == "L":
                    integer = integer + 40
                elif s[numeral_index + 1] == "C":
                    integer = integer + 90
                elif numeral_index == 0:
                    integer = integer + 10
                elif s[numeral_index - 1] != "I":
                    integer = integer + 10
            elif s[numeral_index] == "L":
                if numeral_index == 0:
                    integer = integer + 50
                elif numeral_index > 0:
                    if s[numeral_index - 1] != "X":
                        integer = integer + 50
            elif s[numeral_index] == "C":
                if s[numeral_index + 1] == "D":
                    integer = integer + 400
                elif s[numeral_index + 1] == "M":
                    integer = integer + 900
                elif numeral_index == 0:
                    integer = integer + 100
                elif numeral_index > 0:
                    if s[numeral_index - 1] != "X":
                        integer = integer + 100
            elif s[numeral_index] == "D":
                if numeral_index == 0:
                    integer = integer + 500
                elif numeral_index > 0:
                    if s[numeral_index - 1] != "C":
                        integer = integer + 500
            elif s[numeral_index] == "M":
                if numeral_index == 0:
                    integer = integer + 1000
                elif numeral_index > 0:
                    if s[numeral_index - 1] != "C":
                        integer = integer + 1000
        return integer
