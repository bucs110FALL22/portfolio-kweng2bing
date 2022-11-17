class StringUtility:
    # All the function are to do something to the string according to the lab.
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def vowels(self):
        count = 0
        for element in self.string:
            if element.lower() in "aeiouAEIOU":
                count += 1
        if count >= 5:
            return "many"
        else:
            return f"{count}"

    def bothEnds(self):
        if len(self.string) <= 2:
            return ""
        else:
            return f"{self.string[:2]}" + f"{self.string[-2:]}"

    def fixStart(self):
        strfix = ""
        if len(self.string) < 2:
            return self.string
        else:
            strfix = self.string[1:]
            strfix = strfix.replace(self.string[0], "*")
            return self.string[0] + strfix

    def asciiSum(self):
        strascii = 0
        for element in self.string:
            strascii += ord(element)
        return strascii

    def cipher(self):
        indexchange = len(self.string)
        while len(self.string) > 26:
            indexchange -= 26
        strcipher = self.string
        cryptography = []
        for i in range(len(strcipher)):
            newlet = chr(ord(self.string[i]) + indexchange)
            ordvalue = ord(newlet)
            if ordvalue == 32:
                cryptography.append(" ")
            elif ordvalue in range(97, 123):
                cryptography.append(newlet)
            elif ordvalue in range(65, 91):
                cryptography.append(newlet)
            else:
                cryptography.append(chr(ord(newlet) - 26))

        listtostring = ''.join(map(str, cryptography))
        return listtostring
