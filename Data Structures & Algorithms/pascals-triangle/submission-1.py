class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            sublist = [1]
            for k in range(1, i+1):
                s = int(sublist[k-1] * (i - k + 1) / k)

                if s != 0:
                    sublist.append(s)
            result.append(sublist)

        return result