def encryptSimbol(alphabet, symbol, key):
    if symbol.upper() not in alphabet:
        return symbol
    if symbol.islower():
        return alphabet[(alphabet.index(symbol.upper()) + key) % len(alphabet)].lower()
    else:
        return alphabet[(alphabet.index(symbol.upper()) + key) % len(alphabet)]


def encryptString(string, key, alphabets):
    Output = []
    for symbol in string:
        currentAlphabet = alphabets[0]
        for alph in alphabets:
            if symbol.upper() in alph:
                currentAlphabet = alph
                break
        Output.append(encryptSimbol(currentAlphabet, symbol, key))

    return "".join(Output)


alphabets = [
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
     'X', 'Y', 'Z'],
    ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц',
     'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']]

defaultFileName = "inputTextFile.txt"
print("Enter file name")
fileName = input()
if fileName == "":
    fileName = defaultFileName

inputFile = open(fileName, "r", encoding="utf-8")
InputString = inputFile.read()

defaultMode = 2
print("Enter mode number\n"
      "1 - decrypt\n"
      "2 - encrypt\n"
      "3 - breaking\n")

mode = input()
if mode == "":
    mode = defaultMode
else:
    mode = int(mode)

if mode == 1 or mode == 2:
    print("Enter key")
    key = int(input())
    if mode == 1:
        key = -key
    print(encryptString(InputString, key, alphabets))
elif mode == 3:
    for i in range(0, 40):
        print(encryptString(InputString, i, alphabets))
