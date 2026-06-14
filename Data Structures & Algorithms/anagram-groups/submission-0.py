class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [(''.join(sorted(s)), s) for s in strs]
        print(sorted_strs)
        groupings = {}
        for sorted_str, unsorted_s in sorted_strs:
            print(sorted_str)
            if sorted_str in groupings:
                groupings[sorted_str].append(unsorted_s)
            else:
                groupings[sorted_str] = [unsorted_s]

        return [value for key, value in groupings.items()]