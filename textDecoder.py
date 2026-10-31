
DECODING = {
    "%20": " ", 
    "%25": "%", 
    "%7C": "|",
    "%26": "&", 
    "#21": "!"
}

def main():
    print("please input an encoded string for me to decode")
    encodedString = input()
    
    characterNumber = 0
    characterList = []
    encodedVariableList = []

    translatedString = ""

    
    for char in encodedString:
        substringListNumber = 0
        characterNumber += 1
        characterList.append(char)
  
        #print(characterList)
        #nuts%20%26%20bolts
        if char == "%":
            #slice the string from the encoding char until you get to a character that isn't enumerable
            for char in encodedString[len(characterList):]:
                
                if char.isdigit():
                    substringListNumber += 1
                    continue
                else:
                    testVariable = encodedString[len(characterList)-1:len(characterList)+substringListNumber]
                    encodedVariableList.append(str(testVariable))
                    
                print(encodedVariableList)
                break
        print(translatedString)
    for String in encodedVariableList:
        encodedString = encodedString.replace(String,DECODING[String])
        print(encodedString)
main()
