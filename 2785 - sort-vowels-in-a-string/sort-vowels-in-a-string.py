class Solution:
    def sortVowels(self, s: str) -> str:
        vowelsDefinition = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

        result = list(s)
        foundVowels = list()

        for char in result:
            if char in vowelsDefinition:
                foundVowels.append(char)
        foundVowels.sort(reverse=True)

        for i in range(len(result)):
            if result[i] in vowelsDefinition:
                result[i] = foundVowels.pop()
        
        return "".join(result)
        