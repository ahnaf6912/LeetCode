class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        index = 0
        for index in range(len(strs[0])):
            target = strs[0][index]
            if all(index < len(word) and word[index] == target for word in strs):
                common_prefix = common_prefix + target
            else:
                break
        return common_prefix
