Numbers1 = [13, 26, 14, 25, 15, 24, 16, 23, 17, 22, 18, 21, 19, 20, 13, 1, 11, 2, 10, 3, 9, 4, 8, 5, 6, 7]
Combined_Letters = ["ML", "LK", "KJ", "JI", "IH", "HG", "GF", "FE", "ED", "DC", "CB", "BA", "AN", "NO", "OP", "PQ", "QR", "RS", "ST", "TU","UV","VW", "WX", "XY", "YZ", "ZA"]
Numbers2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52] and ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W" "X", "Y", "Z", " ", "'"]

while(True):
    def unbreakable (input):
        return Numbers1[Alphabet.index(input)]
    def breakable (input):
        return Alphabet[Numbers1.index(input)]


    text = str.upper(input("Type in your text"))
    question = input("Encrypt or Decrypt?")
    if(question == "Encrypt"):
        for letter in text:
            print(unbreakable(letter), end="")
    if(question == "Decrypt"):
        for letter in text.split(" "):
            print(breakable(int(letter)), end="")
    else:
        break
