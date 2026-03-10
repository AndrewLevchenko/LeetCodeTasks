class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = s[0:1]
        # abba-like variant
        for i in range(len(s) - 1):
            left_pointer = i
            right_pointer = i + 1
            while (True):
                if s[left_pointer] != s[right_pointer]:
                    break
                elif len(best) < len(s[left_pointer:right_pointer + 1]):
                    best = s[left_pointer:right_pointer + 1]

                if left_pointer == 0 or right_pointer == len(s) - 1:
                    break
                else:
                    left_pointer = left_pointer - 1
                    right_pointer = right_pointer + 1
        # abcba-like variant
        for i in range(len(s) - 2):
            left_pointer = i
            right_pointer = i + 2
            while (True):
                if s[left_pointer] != s[right_pointer]:
                    break
                elif len(best) < len(s[left_pointer:right_pointer + 1]):
                    best = s[left_pointer:right_pointer + 1]

                if left_pointer == 0 or right_pointer == len(s) - 1:
                    break
                else:
                    left_pointer = left_pointer - 1
                    right_pointer = right_pointer + 1

        return best


print(Solution().longestPalindrome("babad"))

print(Solution().longestPalindrome("cbbd"))