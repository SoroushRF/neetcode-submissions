class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            sortedword = "".join(sorted(word))
            if sortedword not in hashmap:
                hashmap[sortedword] = [word]
            else:
                hashmap[sortedword].append(word)

        return list(hashmap.values())