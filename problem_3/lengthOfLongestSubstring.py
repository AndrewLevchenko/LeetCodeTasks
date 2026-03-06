class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        best_len = 1
        left_pointer = 0

        letters = dict()

        for ind, letter in enumerate(s):

            if letter not in letters:
                letters[letter] = ind
                right_pointer = ind

                if best_len < right_pointer - left_pointer + 1:
                    best_len = right_pointer - left_pointer + 1
            else:
                new_left_pointer = letters[letter] + 1
                for j in range(left_pointer, new_left_pointer):
                    letters.pop(s[j])
                letters[letter] = ind
                left_pointer = new_left_pointer

        return best_len

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))