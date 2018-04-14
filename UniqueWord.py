class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dic = {} 
        for word in dictionary:
            abb = word if len(word) <= 2 else word[0] + str(len(word) - 2) + word[-1]
            self.dic[abb] = word if abb not in self.dic else "" if self.dic[abb] != word else self.dic[abb]


    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abb = word if len(word) <= 2 else word[0] + str(len(word) - 2) + word[-1]
        return abb is not in self.dic or self.dic[abb] == word



# Your ValidWordAbbr object will be instantiated and called as such:
dictionary = ["door", "doct", "dead", "dear"]
vwa = ValidWordAbbr(dictionary)
print(vwa.dic)
print(vwa.isUnique("word"))
# vwa.isUnique("anotherWord")