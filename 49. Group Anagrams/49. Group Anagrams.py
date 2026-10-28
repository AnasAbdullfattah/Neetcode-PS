class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        my_dictionary = defaultdict(list)
        for s in strs:
            a = "".join(sorted(s))
            my_dictionary[a].append(s)
        return list(my_dictionary.values())