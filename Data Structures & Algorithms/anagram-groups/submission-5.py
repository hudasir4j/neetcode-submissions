class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}

        for st in strs:
            st_arr = list(st)
            st_arr.sort()

            if (tuple(st_arr) not in tracker):
                tracker[tuple(st_arr)] = [st]
            else:
                tracker[tuple(st_arr)].append(st)
        
        return list(tracker.values())
