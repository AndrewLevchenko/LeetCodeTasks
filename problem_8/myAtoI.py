class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0

        digits = '0123456789'

        pos_sign = True
        if s[0] == '-':
            pos_sign = False
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        s = s.lstrip('0')
        digits_list = []
        for digit in s:
            if digit in digits:
                digits_list.append(digits.index(digit))
                print(digits.index(digit))
            else:
                break
        i = 0
        number_length = len(digits_list)
        result = 0
        for digit in digits_list:
            result += digit * (10 ** (number_length - i - 1))
            i += 1

        if pos_sign == False:
            return -result if result < 2 ** 31 else -2 ** 31
        return result if result <= 2 ** 31 - 1 else 2 ** 31 - 1