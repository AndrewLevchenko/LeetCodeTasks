class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        currentRow = 0
        dR = 1

        rows = list()
        for i in range(numRows):
            rows.append("")

        i = 0
        for char in s:
            rows[i] = rows[i] + char
            i = i + dR
            if i > numRows - 1:
                i = numRows - 2
                dR = -1
            elif i < 0:
                i = 1
                dR = 1

        return "".join(rows)


