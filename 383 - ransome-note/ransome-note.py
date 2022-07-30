def canConstruct(self, ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    countCharsInNote = {}
    for char in ransomNote:
        countCharsInNote[char] = countCharsInNote.get(char, 0) + 1                 
            
    for char in magazine:            
        if countCharsInNote.get(char, False):
            countCharsInNote[char] -= 1
            if countCharsInNote[char] == 0:
                del countCharsInNote[char]
        if not countCharsInNote:
            return True
    return False
             
        

if __name__ == "__main__":
    print(canConstruct("aaaaaaaasdsdfas", "asdinasaaaaaaaaaaaaaadsfg"))