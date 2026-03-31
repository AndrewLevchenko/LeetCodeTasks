class Solution:
    d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    def romanToInt(self, s: str) -> int:
        result = 0
        prev = 0
        for i in s[::-1]:
            number = self.d[i]
            if number>=prev:
                result +=number
                prev = number
            else:
                result -=number

        return result
