class StringUtility:
    # All the function are to do something to the string according to the lab.
    def __init__(self, string):
        self.string = string
# Returns the strin as is
    def __str__(self):
        return self.string
# Returns number of vowel or too much if >= 5
    def vowels(self):
        count = 0
        for element in self.string:
            if element.lower() in "aeiouAEIOU":
                count += 1
        if count >= 5:
            return "many"
        else:
            return f"{count}"
# retruns the first two and last two parts of a string
    def bothEnds(self):
        if len(self.string) <= 2:
            return ""
        else:
            return f"{self.string[:2]}" + f"{self.string[-2:]}"
# returns every letter that is the same as the first letter after the first letter as "*"
    def fixStart(self):
        strfix = ""
        if len(self.string) < 2:
            return self.string
        else:
            strfix = self.string[1:]
            strfix = strfix.replace(self.string[0], "*")
            return self.string[0] + strfix
# returns ascii sum for the characters
    def asciiSum(self):
        strascii = 0
        for element in self.string:
            strascii += ord(element)
        return strascii
# Returns a cryptography shifting the letters by the length of the string
    def cipher(self):
        indexchange = len(self.string)
        while indexchange > 26:
            indexchange -= 26
        strcipher = self.string
        cryptography = []
        for i in range(len(strcipher)):
            newlet = chr(ord(self.string[i]) + indexchange)
            ordvalue = ord(newlet)
            if ord(self.string[i]) == 32:
                cryptography.append(" ")
            elif ordvalue in range(97, 123):
                cryptography.append(newlet)
            elif ordvalue in range(65, 91):
                cryptography.append(newlet)
            else:
                cryptography.append(chr(ord(newlet) - 26))
        listtostring = ''.join(map(str, cryptography))
        return listtostring
