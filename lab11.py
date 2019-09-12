# Python3.6 version file
def findPlaceInCanada():
    canadaPostalCode = {
        "a": "Newfoundland",
        "b": "Nova Scotia",
        "c": "Prince Edward Island",
        "e": "New Brunswick",
        "g": "Quebec",
        "h": "Quebec",
        "j": "Quebec",
        "k": "Ontario",
        "l": "Ontario",
        "m": "Ontario",
        "n": "Ontario",
        "p": "Ontario",
        "r": "Manitoba",
        "s": "Saskatchewan",
        "t": "Alberta",
        "v": "British Columbia",
        "x": "Nunavut or Northwest Territories",
        "y": "Yukon"
    }
    userRawInput = input("Please enter Canada postal code and press enter: ")
    userRawInputLowercase = userRawInput.lower()
    userInput = userRawInputLowercase.replace(" ","")
    province = userInput[0]
    cityStyle = ""

    def checkErrorOfStr():
        if len(userInput) == 6:
            if userInput[::2].isalpha() is True:
            # Returns True if all characters in the string are alphabetic and there is at least one character. Returns False otherwise.
                if userInput[1::2].isdecimal() is True:
                # Returns True if all characters in the string are decimal characters and there is at least one character. Returns False otherwise.
                    return True
                else:
                    print("Sorry, you put wrong numbers in the postal code, try again.\n")
            else:
                print("Sorry, you put wrong characters in the postal code, try again.\n")
        else:
            print("You put too many/few characters, please text again.\n")

    if checkErrorOfStr() == True:
        if userInput[1] == "0":
            cityStyle = "a rural"
        else:
            cityStyle = "an urban"
        print(f"The Canada postal code is {userInput.upper()}.")
        print(f"The Canada postal code is for {cityStyle} address in {canadaPostalCode[province]}.\n")
    findPlaceInCanada()
findPlaceInCanada()