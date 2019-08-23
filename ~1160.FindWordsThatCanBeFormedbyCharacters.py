class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        ans = 0
        chars_hash = self.helper(chars)
        for word in words:
            word_hash = self.helper(word)
            flag = 0
            for char in word_hash:
                if char not in chars_hash or word_hash[char] > chars_hash[char]:
                    flag = 1
                    break
            if flag == 0:
                ans += len(word)
        return ans


    def helper(self, word):
        ans = {}
        for char in word:
            ans[char] = ans.get(char, 0) +1
        return ans
