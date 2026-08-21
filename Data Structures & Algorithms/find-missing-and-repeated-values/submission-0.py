class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        my_set = set(range(1, n*n +1))
        my_list = []

        for i in range(n):
            for j in range(n):
                if grid[i][j] in my_set:
                    my_set.remove(grid[i][j])
                else:
                    my_list.append(grid[i][j])
        
        my_list.extend(my_set)
        
        return my_list