class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_nums = n*n

        hashmap = {}
        needed = list(range(1, len(grid)**2 + 1))
        result = []

        for r in grid:
            for c in r:
                hashmap[c] = hashmap.get(c, 0) + 1
        
        repeated = -1
        missing = -1

        print(hashmap)

        for i in range(1, total_nums + 1):
            hashmap[i] = hashmap.get(i, 0)
            if (hashmap[i] == 0):
                missing = i
            elif(hashmap[i] == 2):
                repeated = i

        result.append(repeated)
        result.append(missing)
        return result